# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import auth_service.authservice_pb2 as authservice__pb2


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.login = channel.unary_unary(
                '/auth_service.AuthService/login',
                request_serializer=authservice__pb2.LoginRequest.SerializeToString,
                response_deserializer=authservice__pb2.LoginResponse.FromString,
                )
        self.get_token_by_uuid = channel.unary_unary(
                '/auth_service.AuthService/get_token_by_uuid',
                request_serializer=authservice__pb2.TokenRequest.SerializeToString,
                response_deserializer=authservice__pb2.TokenResponse.FromString,
                )


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_token_by_uuid(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'login': grpc.unary_unary_rpc_method_handler(
                    servicer.login,
                    request_deserializer=authservice__pb2.LoginRequest.FromString,
                    response_serializer=authservice__pb2.LoginResponse.SerializeToString,
            ),
            'get_token_by_uuid': grpc.unary_unary_rpc_method_handler(
                    servicer.get_token_by_uuid,
                    request_deserializer=authservice__pb2.TokenRequest.FromString,
                    response_serializer=authservice__pb2.TokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth_service.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth_service.AuthService/login',
            authservice__pb2.LoginRequest.SerializeToString,
            authservice__pb2.LoginResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_token_by_uuid(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth_service.AuthService/get_token_by_uuid',
            authservice__pb2.TokenRequest.SerializeToString,
            authservice__pb2.TokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
