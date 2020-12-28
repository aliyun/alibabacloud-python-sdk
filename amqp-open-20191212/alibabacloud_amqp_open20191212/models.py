# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CreateBindingRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        source_exchange: str = None,
        destination_name: str = None,
        binding_key: str = None,
        binding_type: str = None,
        argument: str = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.source_exchange = source_exchange
        self.destination_name = destination_name
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.argument = argument

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.argument is not None:
            result['Argument'] = self.argument
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        return self


class CreateBindingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBindingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExchangeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        exchange_name: str = None,
        exchange_type: str = None,
        auto_delete_state: bool = None,
        internal: bool = None,
        alternate_exchange: str = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.auto_delete_state = auto_delete_state
        self.internal = internal
        self.alternate_exchange = alternate_exchange

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.internal is not None:
            result['Internal'] = self.internal
        if self.alternate_exchange is not None:
            result['AlternateExchange'] = self.alternate_exchange
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('Internal') is not None:
            self.internal = m.get('Internal')
        if m.get('AlternateExchange') is not None:
            self.alternate_exchange = m.get('AlternateExchange')
        return self


class CreateExchangeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateExchangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateExchangeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateExchangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueueRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        queue_name: str = None,
        auto_delete_state: bool = None,
        exclusive_state: bool = None,
        message_ttl: int = None,
        auto_expire_state: int = None,
        max_length: int = None,
        dead_letter_exchange: str = None,
        dead_letter_routing_key: str = None,
        maximum_priority: int = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.queue_name = queue_name
        self.auto_delete_state = auto_delete_state
        self.exclusive_state = exclusive_state
        self.message_ttl = message_ttl
        self.auto_expire_state = auto_expire_state
        self.max_length = max_length
        self.dead_letter_exchange = dead_letter_exchange
        self.dead_letter_routing_key = dead_letter_routing_key
        self.maximum_priority = maximum_priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.exclusive_state is not None:
            result['ExclusiveState'] = self.exclusive_state
        if self.message_ttl is not None:
            result['MessageTTL'] = self.message_ttl
        if self.auto_expire_state is not None:
            result['AutoExpireState'] = self.auto_expire_state
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.dead_letter_exchange is not None:
            result['DeadLetterExchange'] = self.dead_letter_exchange
        if self.dead_letter_routing_key is not None:
            result['DeadLetterRoutingKey'] = self.dead_letter_routing_key
        if self.maximum_priority is not None:
            result['MaximumPriority'] = self.maximum_priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('ExclusiveState') is not None:
            self.exclusive_state = m.get('ExclusiveState')
        if m.get('MessageTTL') is not None:
            self.message_ttl = m.get('MessageTTL')
        if m.get('AutoExpireState') is not None:
            self.auto_expire_state = m.get('AutoExpireState')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('DeadLetterExchange') is not None:
            self.dead_letter_exchange = m.get('DeadLetterExchange')
        if m.get('DeadLetterRoutingKey') is not None:
            self.dead_letter_routing_key = m.get('DeadLetterRoutingKey')
        if m.get('MaximumPriority') is not None:
            self.maximum_priority = m.get('MaximumPriority')
        return self


class CreateQueueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateQueueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualHostRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class CreateVirtualHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVirtualHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVirtualHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateVirtualHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindingRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        source_exchange: str = None,
        destination_name: str = None,
        binding_type: str = None,
        binding_key: str = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.source_exchange = source_exchange
        self.destination_name = destination_name
        self.binding_type = binding_type
        self.binding_key = binding_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        return self


class DeleteBindingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBindingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBindingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExchangeRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        exchange_name: str = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.exchange_name = exchange_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        return self


class DeleteExchangeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteExchangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteExchangeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteExchangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQueueRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        queue_name: str = None,
        virtual_host: str = None,
    ):
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class DeleteQueueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteQueueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVirtualHostRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class DeleteVirtualHostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVirtualHostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteVirtualHostResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteVirtualHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMetadataAmountRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetMetadataAmountResponseBodyData(TeaModel):
    def __init__(
        self,
        max_virtual_hosts: int = None,
        current_virtual_hosts: int = None,
        max_queues: int = None,
        current_exchanges: int = None,
        max_exchanges: int = None,
        current_queues: int = None,
    ):
        self.max_virtual_hosts = max_virtual_hosts
        self.current_virtual_hosts = current_virtual_hosts
        self.max_queues = max_queues
        self.current_exchanges = current_exchanges
        self.max_exchanges = max_exchanges
        self.current_queues = current_queues

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_virtual_hosts is not None:
            result['MaxVirtualHosts'] = self.max_virtual_hosts
        if self.current_virtual_hosts is not None:
            result['CurrentVirtualHosts'] = self.current_virtual_hosts
        if self.max_queues is not None:
            result['MaxQueues'] = self.max_queues
        if self.current_exchanges is not None:
            result['CurrentExchanges'] = self.current_exchanges
        if self.max_exchanges is not None:
            result['MaxExchanges'] = self.max_exchanges
        if self.current_queues is not None:
            result['CurrentQueues'] = self.current_queues
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxVirtualHosts') is not None:
            self.max_virtual_hosts = m.get('MaxVirtualHosts')
        if m.get('CurrentVirtualHosts') is not None:
            self.current_virtual_hosts = m.get('CurrentVirtualHosts')
        if m.get('MaxQueues') is not None:
            self.max_queues = m.get('MaxQueues')
        if m.get('CurrentExchanges') is not None:
            self.current_exchanges = m.get('CurrentExchanges')
        if m.get('MaxExchanges') is not None:
            self.max_exchanges = m.get('MaxExchanges')
        if m.get('CurrentQueues') is not None:
            self.current_queues = m.get('CurrentQueues')
        return self


class GetMetadataAmountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetMetadataAmountResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetMetadataAmountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetMetadataAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMetadataAmountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetMetadataAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListBindingsResponseBodyDataBindings(TeaModel):
    def __init__(
        self,
        source_exchange: str = None,
        binding_key: str = None,
        binding_type: str = None,
        argument: str = None,
        destination_name: str = None,
    ):
        self.source_exchange = source_exchange
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.argument = argument
        self.destination_name = destination_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        return self


class ListBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        bindings: List[ListBindingsResponseBodyDataBindings] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.bindings = bindings

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        return self


class ListBindingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListBindingsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListBindingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDownStreamBindingsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        exchange_name: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.exchange_name = exchange_name
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListDownStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(
        self,
        source_exchange: str = None,
        binding_key: str = None,
        binding_type: str = None,
        argument: str = None,
        destination_name: str = None,
    ):
        self.source_exchange = source_exchange
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.argument = argument
        self.destination_name = destination_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        return self


class ListDownStreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        bindings: List[ListDownStreamBindingsResponseBodyDataBindings] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.bindings = bindings

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListDownStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        return self


class ListDownStreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListDownStreamBindingsResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListDownStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDownStreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDownStreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDownStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListExchangesResponseBodyDataExchanges(TeaModel):
    def __init__(
        self,
        auto_delete_state: bool = None,
        create_time: int = None,
        attributes: Dict[str, Any] = None,
        vhost_name: str = None,
        name: str = None,
        exchange_type: str = None,
    ):
        self.auto_delete_state = auto_delete_state
        self.create_time = create_time
        self.attributes = attributes
        self.vhost_name = vhost_name
        self.name = name
        self.exchange_type = exchange_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.vhost_name is not None:
            result['VHostName'] = self.vhost_name
        if self.name is not None:
            result['Name'] = self.name
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('VHostName') is not None:
            self.vhost_name = m.get('VHostName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        return self


class ListExchangesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        exchanges: List[ListExchangesResponseBodyDataExchanges] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.exchanges = exchanges

    def validate(self):
        if self.exchanges:
            for k in self.exchanges:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Exchanges'] = []
        if self.exchanges is not None:
            for k in self.exchanges:
                result['Exchanges'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.exchanges = []
        if m.get('Exchanges') is not None:
            for k in m.get('Exchanges'):
                temp_model = ListExchangesResponseBodyDataExchanges()
                self.exchanges.append(temp_model.from_map(k))
        return self


class ListExchangesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListExchangesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListExchangesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListExchangesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExchangesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListExchangesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangeUpStreamBindingsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        exchange_name: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.exchange_name = exchange_name
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListExchangeUpStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(
        self,
        source_exchange: str = None,
        binding_key: str = None,
        binding_type: str = None,
        argument: str = None,
        destination_name: str = None,
    ):
        self.source_exchange = source_exchange
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.argument = argument
        self.destination_name = destination_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        return self


class ListExchangeUpStreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        bindings: List[ListExchangeUpStreamBindingsResponseBodyDataBindings] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.bindings = bindings

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListExchangeUpStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        return self


class ListExchangeUpStreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: ListExchangeUpStreamBindingsResponseBodyData = None,
        code: int = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListExchangeUpStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListExchangeUpStreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExchangeUpStreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListExchangeUpStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListInstancesResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        status: str = None,
        support_eip: bool = None,
        auto_renew_instance: bool = None,
        expire_time: int = None,
        order_create_time: int = None,
        instance_name: str = None,
        private_endpoint: str = None,
        order_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        public_endpoint: str = None,
    ):
        self.status = status
        self.support_eip = support_eip
        self.auto_renew_instance = auto_renew_instance
        self.expire_time = expire_time
        self.order_create_time = order_create_time
        self.instance_name = instance_name
        self.private_endpoint = private_endpoint
        self.order_type = order_type
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.public_endpoint = public_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip
        if self.auto_renew_instance is not None:
            result['AutoRenewInstance'] = self.auto_renew_instance
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.order_create_time is not None:
            result['OrderCreateTime'] = self.order_create_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.private_endpoint is not None:
            result['PrivateEndpoint'] = self.private_endpoint
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')
        if m.get('AutoRenewInstance') is not None:
            self.auto_renew_instance = m.get('AutoRenewInstance')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('OrderCreateTime') is not None:
            self.order_create_time = m.get('OrderCreateTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PrivateEndpoint') is not None:
            self.private_endpoint = m.get('PrivateEndpoint')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        instances: List[ListInstancesResponseBodyDataInstances] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListInstancesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueConsumersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        queue: str = None,
        next_token: str = None,
        query_count: int = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.queue = queue
        self.next_token = next_token
        self.query_count = query_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        return self


class ListQueueConsumersResponseBodyDataConsumers(TeaModel):
    def __init__(
        self,
        consumer_tag: str = None,
    ):
        self.consumer_tag = consumer_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')
        return self


class ListQueueConsumersResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        consumers: List[ListQueueConsumersResponseBodyDataConsumers] = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.consumers = consumers
        self.max_results = max_results

    def validate(self):
        if self.consumers:
            for k in self.consumers:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Consumers'] = []
        if self.consumers is not None:
            for k in self.consumers:
                result['Consumers'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.consumers = []
        if m.get('Consumers') is not None:
            for k in m.get('Consumers'):
                temp_model = ListQueueConsumersResponseBodyDataConsumers()
                self.consumers.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListQueueConsumersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListQueueConsumersResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListQueueConsumersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListQueueConsumersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListQueueConsumersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListQueueConsumersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueuesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListQueuesResponseBodyDataQueues(TeaModel):
    def __init__(
        self,
        exclusive_state: bool = None,
        auto_delete_state: bool = None,
        create_time: int = None,
        attributes: Dict[str, Any] = None,
        vhost_name: str = None,
        name: str = None,
        owner_id: str = None,
        last_consume_time: int = None,
    ):
        self.exclusive_state = exclusive_state
        self.auto_delete_state = auto_delete_state
        self.create_time = create_time
        self.attributes = attributes
        self.vhost_name = vhost_name
        self.name = name
        self.owner_id = owner_id
        self.last_consume_time = last_consume_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.exclusive_state is not None:
            result['ExclusiveState'] = self.exclusive_state
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.vhost_name is not None:
            result['VHostName'] = self.vhost_name
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.last_consume_time is not None:
            result['LastConsumeTime'] = self.last_consume_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExclusiveState') is not None:
            self.exclusive_state = m.get('ExclusiveState')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('VHostName') is not None:
            self.vhost_name = m.get('VHostName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('LastConsumeTime') is not None:
            self.last_consume_time = m.get('LastConsumeTime')
        return self


class ListQueuesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        queues: List[ListQueuesResponseBodyDataQueues] = None,
        max_results: int = None,
    ):
        self.next_token = next_token
        self.queues = queues
        self.max_results = max_results

    def validate(self):
        if self.queues:
            for k in self.queues:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Queues'] = []
        if self.queues is not None:
            for k in self.queues:
                result['Queues'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.queues = []
        if m.get('Queues') is not None:
            for k in m.get('Queues'):
                temp_model = ListQueuesResponseBodyDataQueues()
                self.queues.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListQueuesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListQueuesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListQueuesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListQueuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListQueuesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListQueuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueUpStreamBindingsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        virtual_host: str = None,
        queue_name: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.instance_id = instance_id
        self.virtual_host = virtual_host
        self.queue_name = queue_name
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListQueueUpStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(
        self,
        source_exchange: str = None,
        binding_key: str = None,
        binding_type: str = None,
        argument: str = None,
        destination_name: str = None,
    ):
        self.source_exchange = source_exchange
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.argument = argument
        self.destination_name = destination_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        return self


class ListQueueUpStreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: str = None,
        bindings: List[ListQueueUpStreamBindingsResponseBodyDataBindings] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.bindings = bindings

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListQueueUpStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        return self


class ListQueueUpStreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListQueueUpStreamBindingsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListQueueUpStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListQueueUpStreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListQueueUpStreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListQueueUpStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualHostsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        next_token: str = None,
        max_results: int = None,
    ):
        self.instance_id = instance_id
        self.next_token = next_token
        self.max_results = max_results

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class ListVirtualHostsResponseBodyDataVirtualHosts(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListVirtualHostsResponseBodyData(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        max_results: int = None,
        virtual_hosts: List[ListVirtualHostsResponseBodyDataVirtualHosts] = None,
    ):
        self.next_token = next_token
        self.max_results = max_results
        self.virtual_hosts = virtual_hosts

    def validate(self):
        if self.virtual_hosts:
            for k in self.virtual_hosts:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['VirtualHosts'] = []
        if self.virtual_hosts is not None:
            for k in self.virtual_hosts:
                result['VirtualHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.virtual_hosts = []
        if m.get('VirtualHosts') is not None:
            for k in m.get('VirtualHosts'):
                temp_model = ListVirtualHostsResponseBodyDataVirtualHosts()
                self.virtual_hosts.append(temp_model.from_map(k))
        return self


class ListVirtualHostsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListVirtualHostsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListVirtualHostsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListVirtualHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListVirtualHostsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListVirtualHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


