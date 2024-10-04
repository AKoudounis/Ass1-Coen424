import grpc
from concurrent import futures
import redis
import json
import time
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Import the generated classes
from generated import count_laureates_by_category_pb2
from generated import count_laureates_by_category_pb2_grpc
from generated import count_laureates_by_keyword_pb2
from generated import count_laureates_by_keyword_pb2_grpc
from generated import find_laureate_by_name_pb2
from generated import find_laureate_by_name_pb2_grpc

# Set up logging
logging.basicConfig(level=logging.INFO)

# Redis connection details from environment variables
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')  # Default Redis port
REDIS_USERNAME = os.getenv('REDIS_USERNAME')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

class PrizeService(
    count_laureates_by_category_pb2_grpc.PrizeCategoryServiceServicer,
    count_laureates_by_keyword_pb2_grpc.PrizeKeywordServiceServicer,
    find_laureate_by_name_pb2_grpc.FindLaureateByNameServiceServicer,
):
    def __init__(self):
        self.redis_client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            username=REDIS_USERNAME,
            password=REDIS_PASSWORD,
            decode_responses=True
        )

    def CountLaureatesByCategory(self, request, context):
        logging.info(f"Received request to count laureates in category: '{request.category}' from {request.start_year} to {request.end_year}")
        try:
            query = f"@category:{request.category} @year:[{request.start_year} {request.end_year}]"
            logging.info(f"Executing Redis query: {query}")

            result = self.redis_client.execute_command("FT.SEARCH", "idx:prizes", query, "RETURN", 1, "laureates", "LIMIT", 0, 10000)
            unique_laureate_ids = set()

            for i in range(1, len(result), 2):
                laureate_data = result[i]
                laureate_info = self.redis_client.hgetall(laureate_data)
                motivations = json.loads(laureate_info.get('laureates', '[]'))

                for motivation in motivations:
                    unique_laureate_ids.add(motivation['id'])

            return count_laureates_by_category_pb2.CountLaureatesByCategoryResponse(total_laureates=len(unique_laureate_ids))
        
        except Exception as e:
            logging.error(f"Error executing query: {str(e)}")
            context.set_details(f"Error executing query: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return count_laureates_by_category_pb2.CountLaureatesByCategoryResponse(total_laureates=0)

    def CountLaureatesByKeyword(self, request, context):
        query = f"@laureates:*{request.keyword}*"  # Use wildcards to match the keyword
        logging.info(f"Executing Redis query: {query}")
        
        try:
            result = self.redis_client.execute_command("FT.SEARCH", "idx:prizes", query, "RETURN", 1, "laureates", "LIMIT", 0, 10000)
            unique_laureate_ids = set()
            
            for i in range(1, len(result), 2):
                laureate_data = result[i]
                laureate_info = self.redis_client.hgetall(laureate_data)
                motivations = json.loads(laureate_info.get('laureates', '[]'))

                for motivation in motivations:
                    unique_laureate_ids.add(motivation['id'])

            total_laureates = len(unique_laureate_ids)
            logging.info(f"Total unique laureates found for keyword '{request.keyword}': {total_laureates}")
            
            return count_laureates_by_keyword_pb2.CountLaureatesByKeywordResponse(total_laureates=total_laureates)
        
        except Exception as e:
            logging.error(f"Error executing keyword query: {str(e)}")
            context.set_details(f"Error executing keyword query: {str(e)}")
            context.set_code(grpc.StatusCode.INTERNAL)
            return count_laureates_by_keyword_pb2.CountLaureatesByKeywordResponse(total_laureates=0)
            
    def FindLaureate(self, request, context):
        query = f"@laureates:*{request.firstname}* @laureates:*{request.lastname}*"
        result = self.redis_client.execute_command("FT.SEARCH", "idx:prizes", query, "RETURN", 3, "year", "category", "laureates")
        
        laureates_info = []
        for i in range(1, len(result), 2):
            laureate_key = result[i]
            laureate_data = self.redis_client.hgetall(laureate_key)
            motivations = json.loads(laureate_data.get('laureates', '[]'))
            matching_motivations = [m['motivation'].strip('"') for m in motivations if m['surname'].lower() == request.lastname.lower()]
            laureates_info.append(find_laureate_by_name_pb2.LaureateInfo(
                year=int(laureate_data.get('year')),
                category=laureate_data.get('category'),
                motivations=matching_motivations
            ))
        
        return find_laureate_by_name_pb2.FindLaureateByNameResponse(laureates=laureates_info)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prize_service = PrizeService()

    # Register the services
    count_laureates_by_category_pb2_grpc.add_PrizeCategoryServiceServicer_to_server(prize_service, server)
    count_laureates_by_keyword_pb2_grpc.add_PrizeKeywordServiceServicer_to_server(prize_service, server)
    find_laureate_by_name_pb2_grpc.add_FindLaureateByNameServiceServicer_to_server(prize_service, server)
    
    # Use dynamic port assignment
    server.add_secure_port(f'[::]:{os.getenv("PORT", 50051)})
    server.start()
    logging.info("Server is running...")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
