# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cluster_comm_pb2 as cluster__comm__pb2


class TransferSubmitServiceStub(object):
  """submit transfer job
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.send = channel.unary_unary(
        '/com.webank.ai.eggroll.api.driver.clustercomm.TransferSubmitService/send',
        request_serializer=cluster__comm__pb2.TransferMeta.SerializeToString,
        response_deserializer=cluster__comm__pb2.TransferMeta.FromString,
        )
    self.recv = channel.unary_unary(
        '/com.webank.ai.eggroll.api.driver.clustercomm.TransferSubmitService/recv',
        request_serializer=cluster__comm__pb2.TransferMeta.SerializeToString,
        response_deserializer=cluster__comm__pb2.TransferMeta.FromString,
        )
    self.checkStatusNow = channel.unary_unary(
        '/com.webank.ai.eggroll.api.driver.clustercomm.TransferSubmitService/checkStatusNow',
        request_serializer=cluster__comm__pb2.TransferMeta.SerializeToString,
        response_deserializer=cluster__comm__pb2.TransferMeta.FromString,
        )
    self.checkStatus = channel.unary_unary(
        '/com.webank.ai.eggroll.api.driver.clustercomm.TransferSubmitService/checkStatus',
        request_serializer=cluster__comm__pb2.TransferMeta.SerializeToString,
        response_deserializer=cluster__comm__pb2.TransferMeta.FromString,
        )


class TransferSubmitServiceServicer(object):
  """submit transfer job
  """

  def send(self, request, context):
    """send data
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def recv(self, request, context):
    """receive data, i.e. wait for data to arrive
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def checkStatusNow(self, request, context):
    """check the transfer status, return immediately
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def checkStatus(self, request, context):
    """check the transfer status, block until finished or default timeout
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TransferSubmitServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'send': grpc.unary_unary_rpc_method_handler(
          servicer.send,
          request_deserializer=cluster__comm__pb2.TransferMeta.FromString,
          response_serializer=cluster__comm__pb2.TransferMeta.SerializeToString,
      ),
      'recv': grpc.unary_unary_rpc_method_handler(
          servicer.recv,
          request_deserializer=cluster__comm__pb2.TransferMeta.FromString,
          response_serializer=cluster__comm__pb2.TransferMeta.SerializeToString,
      ),
      'checkStatusNow': grpc.unary_unary_rpc_method_handler(
          servicer.checkStatusNow,
          request_deserializer=cluster__comm__pb2.TransferMeta.FromString,
          response_serializer=cluster__comm__pb2.TransferMeta.SerializeToString,
      ),
      'checkStatus': grpc.unary_unary_rpc_method_handler(
          servicer.checkStatus,
          request_deserializer=cluster__comm__pb2.TransferMeta.FromString,
          response_serializer=cluster__comm__pb2.TransferMeta.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'com.webank.ai.eggroll.api.driver.clustercomm.TransferSubmitService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
