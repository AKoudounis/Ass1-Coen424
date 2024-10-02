# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from generated import count_laureates_by_keyword_pb2 as count__laureates__by__keyword__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in count_laureates_by_keyword_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PrizeKeywordServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CountLaureatesByKeyword = channel.unary_unary(
                '/prize.PrizeKeywordService/CountLaureatesByKeyword',
                request_serializer=count__laureates__by__keyword__pb2.CountLaureatesByKeywordRequest.SerializeToString,
                response_deserializer=count__laureates__by__keyword__pb2.CountLaureatesByKeywordResponse.FromString,
                _registered_method=True)


class PrizeKeywordServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CountLaureatesByKeyword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PrizeKeywordServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CountLaureatesByKeyword': grpc.unary_unary_rpc_method_handler(
                    servicer.CountLaureatesByKeyword,
                    request_deserializer=count__laureates__by__keyword__pb2.CountLaureatesByKeywordRequest.FromString,
                    response_serializer=count__laureates__by__keyword__pb2.CountLaureatesByKeywordResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prize.PrizeKeywordService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('prize.PrizeKeywordService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class PrizeKeywordService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CountLaureatesByKeyword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/prize.PrizeKeywordService/CountLaureatesByKeyword',
            count__laureates__by__keyword__pb2.CountLaureatesByKeywordRequest.SerializeToString,
            count__laureates__by__keyword__pb2.CountLaureatesByKeywordResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
