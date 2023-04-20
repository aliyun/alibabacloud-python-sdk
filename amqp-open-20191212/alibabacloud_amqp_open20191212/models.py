# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class DataValue(TeaModel):
    def __init__(
        self,
        master_uid: int = None,
        c_instance_id: str = None,
        access_key: str = None,
        user_name: str = None,
        password: str = None,
        deleted: int = None,
        create_timestamp: int = None,
    ):
        self.master_uid = master_uid
        self.c_instance_id = c_instance_id
        self.access_key = access_key
        self.user_name = user_name
        self.password = password
        self.deleted = deleted
        self.create_timestamp = create_timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.master_uid is not None:
            result['masterUid'] = self.master_uid
        if self.c_instance_id is not None:
            result['cInstanceId'] = self.c_instance_id
        if self.access_key is not None:
            result['accessKey'] = self.access_key
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.password is not None:
            result['password'] = self.password
        if self.deleted is not None:
            result['deleted'] = self.deleted
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('masterUid') is not None:
            self.master_uid = m.get('masterUid')
        if m.get('cInstanceId') is not None:
            self.c_instance_id = m.get('cInstanceId')
        if m.get('accessKey') is not None:
            self.access_key = m.get('accessKey')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        return self


class CreateAccountRequest(TeaModel):
    def __init__(
        self,
        account_access_key: str = None,
        create_timestamp: int = None,
        instance_id: str = None,
        secret_sign: str = None,
        signature: str = None,
        user_name: str = None,
    ):
        self.account_access_key = account_access_key
        self.create_timestamp = create_timestamp
        self.instance_id = instance_id
        self.secret_sign = secret_sign
        self.signature = signature
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_access_key is not None:
            result['accountAccessKey'] = self.account_access_key
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.secret_sign is not None:
            result['secretSign'] = self.secret_sign
        if self.signature is not None:
            result['signature'] = self.signature
        if self.user_name is not None:
            result['userName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountAccessKey') is not None:
            self.account_access_key = m.get('accountAccessKey')
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('secretSign') is not None:
            self.secret_sign = m.get('secretSign')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        return self


class CreateAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        create_time_stamp: int = None,
        instance_id: str = None,
        master_uid: int = None,
        password: str = None,
        user_name: str = None,
    ):
        # AccessKey ID。
        self.access_key = access_key
        self.create_time_stamp = create_time_stamp
        self.instance_id = instance_id
        self.master_uid = master_uid
        self.password = password
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.master_uid is not None:
            result['MasterUId'] = self.master_uid
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MasterUId') is not None:
            self.master_uid = m.get('MasterUId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateAccountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBindingRequest(TeaModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        instance_id: str = None,
        source_exchange: str = None,
        virtual_host: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.destination_name = destination_name
        self.instance_id = instance_id
        self.source_exchange = source_exchange
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExchangeRequest(TeaModel):
    def __init__(
        self,
        alternate_exchange: str = None,
        auto_delete_state: bool = None,
        exchange_name: str = None,
        exchange_type: str = None,
        instance_id: str = None,
        internal: bool = None,
        virtual_host: str = None,
    ):
        self.alternate_exchange = alternate_exchange
        self.auto_delete_state = auto_delete_state
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.instance_id = instance_id
        self.internal = internal
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alternate_exchange is not None:
            result['AlternateExchange'] = self.alternate_exchange
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internal is not None:
            result['Internal'] = self.internal
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlternateExchange') is not None:
            self.alternate_exchange = m.get('AlternateExchange')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Internal') is not None:
            self.internal = m.get('Internal')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateExchangeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateExchangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueueRequest(TeaModel):
    def __init__(
        self,
        auto_delete_state: bool = None,
        auto_expire_state: int = None,
        dead_letter_exchange: str = None,
        dead_letter_routing_key: str = None,
        exclusive_state: bool = None,
        instance_id: str = None,
        max_length: int = None,
        maximum_priority: int = None,
        message_ttl: int = None,
        queue_name: str = None,
        virtual_host: str = None,
    ):
        self.auto_delete_state = auto_delete_state
        self.auto_expire_state = auto_expire_state
        self.dead_letter_exchange = dead_letter_exchange
        self.dead_letter_routing_key = dead_letter_routing_key
        self.exclusive_state = exclusive_state
        self.instance_id = instance_id
        self.max_length = max_length
        self.maximum_priority = maximum_priority
        self.message_ttl = message_ttl
        self.queue_name = queue_name
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.auto_expire_state is not None:
            result['AutoExpireState'] = self.auto_expire_state
        if self.dead_letter_exchange is not None:
            result['DeadLetterExchange'] = self.dead_letter_exchange
        if self.dead_letter_routing_key is not None:
            result['DeadLetterRoutingKey'] = self.dead_letter_routing_key
        if self.exclusive_state is not None:
            result['ExclusiveState'] = self.exclusive_state
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.maximum_priority is not None:
            result['MaximumPriority'] = self.maximum_priority
        if self.message_ttl is not None:
            result['MessageTTL'] = self.message_ttl
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('AutoExpireState') is not None:
            self.auto_expire_state = m.get('AutoExpireState')
        if m.get('DeadLetterExchange') is not None:
            self.dead_letter_exchange = m.get('DeadLetterExchange')
        if m.get('DeadLetterRoutingKey') is not None:
            self.dead_letter_routing_key = m.get('DeadLetterRoutingKey')
        if m.get('ExclusiveState') is not None:
            self.exclusive_state = m.get('ExclusiveState')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaximumPriority') is not None:
            self.maximum_priority = m.get('MaximumPriority')
        if m.get('MessageTTL') is not None:
            self.message_ttl = m.get('MessageTTL')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: CreateVirtualHostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVirtualHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccountRequest(TeaModel):
    def __init__(
        self,
        create_timestamp: int = None,
        user_name: str = None,
    ):
        self.create_timestamp = create_timestamp
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBindingRequest(TeaModel):
    def __init__(
        self,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        instance_id: str = None,
        source_exchange: str = None,
        virtual_host: str = None,
    ):
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.destination_name = destination_name
        self.instance_id = instance_id
        self.source_exchange = source_exchange
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteBindingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteBindingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExchangeRequest(TeaModel):
    def __init__(
        self,
        exchange_name: str = None,
        instance_id: str = None,
        virtual_host: str = None,
    ):
        self.exchange_name = exchange_name
        self.instance_id = instance_id
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteExchangeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: DeleteVirtualHostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        current_exchanges: int = None,
        current_queues: int = None,
        current_virtual_hosts: int = None,
        max_exchanges: int = None,
        max_queues: int = None,
        max_virtual_hosts: int = None,
    ):
        self.current_exchanges = current_exchanges
        self.current_queues = current_queues
        self.current_virtual_hosts = current_virtual_hosts
        self.max_exchanges = max_exchanges
        self.max_queues = max_queues
        self.max_virtual_hosts = max_virtual_hosts

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_exchanges is not None:
            result['CurrentExchanges'] = self.current_exchanges
        if self.current_queues is not None:
            result['CurrentQueues'] = self.current_queues
        if self.current_virtual_hosts is not None:
            result['CurrentVirtualHosts'] = self.current_virtual_hosts
        if self.max_exchanges is not None:
            result['MaxExchanges'] = self.max_exchanges
        if self.max_queues is not None:
            result['MaxQueues'] = self.max_queues
        if self.max_virtual_hosts is not None:
            result['MaxVirtualHosts'] = self.max_virtual_hosts
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentExchanges') is not None:
            self.current_exchanges = m.get('CurrentExchanges')
        if m.get('CurrentQueues') is not None:
            self.current_queues = m.get('CurrentQueues')
        if m.get('CurrentVirtualHosts') is not None:
            self.current_virtual_hosts = m.get('CurrentVirtualHosts')
        if m.get('MaxExchanges') is not None:
            self.max_exchanges = m.get('MaxExchanges')
        if m.get('MaxQueues') is not None:
            self.max_queues = m.get('MaxQueues')
        if m.get('MaxVirtualHosts') is not None:
            self.max_virtual_hosts = m.get('MaxVirtualHosts')
        return self


class GetMetadataAmountResponseBody(TeaModel):
    def __init__(
        self,
        data: GetMetadataAmountResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetMetadataAmountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMetadataAmountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMetadataAmountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMetadataAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccountsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAccountsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, List[DataValue]] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v in self.data.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = {}
        if self.data is not None:
            for k, v in self.data.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['data'][k] = l1
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = {}
        if m.get('Data') is not None:
            for k, v in m.get('Data').items():
                l1 = []
                for k1 in v:
                    temp_model = DataValue()
                    l1.append(temp_model.from_map(k1))
                self.data['k'] = l1
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBindingsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        virtual_host: str = None,
    ):
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListBindingsResponseBodyDataBindings(TeaModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        source_exchange: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.destination_name = destination_name
        self.source_exchange = source_exchange

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        return self


class ListBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        bindings: List[ListBindingsResponseBodyDataBindings] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.bindings = bindings
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListBindingsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListBindingsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDownStreamBindingsRequest(TeaModel):
    def __init__(
        self,
        exchange_name: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        virtual_host: str = None,
    ):
        self.exchange_name = exchange_name
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListDownStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        source_exchange: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.destination_name = destination_name
        self.source_exchange = source_exchange

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        return self


class ListDownStreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        bindings: List[ListDownStreamBindingsResponseBodyDataBindings] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.bindings = bindings
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListDownStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListDownStreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListDownStreamBindingsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListDownStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDownStreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDownStreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDownStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangeUpStreamBindingsRequest(TeaModel):
    def __init__(
        self,
        exchange_name: str = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        virtual_host: str = None,
    ):
        self.exchange_name = exchange_name
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListExchangeUpStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        source_exchange: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.destination_name = destination_name
        self.source_exchange = source_exchange

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        return self


class ListExchangeUpStreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        bindings: List[ListExchangeUpStreamBindingsResponseBodyDataBindings] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.bindings = bindings
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListExchangeUpStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListExchangeUpStreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListExchangeUpStreamBindingsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListExchangeUpStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListExchangeUpStreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExchangeUpStreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExchangeUpStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        virtual_host: str = None,
    ):
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListExchangesResponseBodyDataExchanges(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        auto_delete_state: bool = None,
        create_time: int = None,
        exchange_type: str = None,
        name: str = None,
        vhost_name: str = None,
    ):
        self.attributes = attributes
        self.auto_delete_state = auto_delete_state
        self.create_time = create_time
        self.exchange_type = exchange_type
        self.name = name
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        if self.name is not None:
            result['Name'] = self.name
        if self.vhost_name is not None:
            result['VHostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VHostName') is not None:
            self.vhost_name = m.get('VHostName')
        return self


class ListExchangesResponseBodyData(TeaModel):
    def __init__(
        self,
        exchanges: List[ListExchangesResponseBodyDataExchanges] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # Exchange。
        self.exchanges = exchanges
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.exchanges:
            for k in self.exchanges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Exchanges'] = []
        if self.exchanges is not None:
            for k in self.exchanges:
                result['Exchanges'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exchanges = []
        if m.get('Exchanges') is not None:
            for k in m.get('Exchanges'):
                temp_model = ListExchangesResponseBodyDataExchanges()
                self.exchanges.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListExchangesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListExchangesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListExchangesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExchangesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExchangesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExchangesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListInstancesResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        auto_renew_instance: bool = None,
        classic_endpoint: str = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        max_eip_tps: int = None,
        max_queue: int = None,
        max_tps: int = None,
        max_vhost: int = None,
        order_create_time: int = None,
        order_type: str = None,
        private_endpoint: str = None,
        public_endpoint: str = None,
        status: str = None,
        storage_size: int = None,
        support_eip: bool = None,
    ):
        self.auto_renew_instance = auto_renew_instance
        self.classic_endpoint = classic_endpoint
        self.expire_time = expire_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.max_eip_tps = max_eip_tps
        self.max_queue = max_queue
        self.max_tps = max_tps
        self.max_vhost = max_vhost
        self.order_create_time = order_create_time
        self.order_type = order_type
        self.private_endpoint = private_endpoint
        self.public_endpoint = public_endpoint
        self.status = status
        self.storage_size = storage_size
        self.support_eip = support_eip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew_instance is not None:
            result['AutoRenewInstance'] = self.auto_renew_instance
        if self.classic_endpoint is not None:
            result['ClassicEndpoint'] = self.classic_endpoint
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_eip_tps is not None:
            result['MaxEipTps'] = self.max_eip_tps
        if self.max_queue is not None:
            result['MaxQueue'] = self.max_queue
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.max_vhost is not None:
            result['MaxVhost'] = self.max_vhost
        if self.order_create_time is not None:
            result['OrderCreateTime'] = self.order_create_time
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.private_endpoint is not None:
            result['PrivateEndpoint'] = self.private_endpoint
        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenewInstance') is not None:
            self.auto_renew_instance = m.get('AutoRenewInstance')
        if m.get('ClassicEndpoint') is not None:
            self.classic_endpoint = m.get('ClassicEndpoint')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxEipTps') is not None:
            self.max_eip_tps = m.get('MaxEipTps')
        if m.get('MaxQueue') is not None:
            self.max_queue = m.get('MaxQueue')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('MaxVhost') is not None:
            self.max_vhost = m.get('MaxVhost')
        if m.get('OrderCreateTime') is not None:
            self.order_create_time = m.get('OrderCreateTime')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PrivateEndpoint') is not None:
            self.private_endpoint = m.get('PrivateEndpoint')
        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyDataInstances] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.instances = instances
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListInstancesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueConsumersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        next_token: str = None,
        query_count: int = None,
        queue: str = None,
        virtual_host: str = None,
    ):
        self.instance_id = instance_id
        self.next_token = next_token
        self.query_count = query_count
        self.queue = queue
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.query_count is not None:
            result['QueryCount'] = self.query_count
        if self.queue is not None:
            result['Queue'] = self.queue
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')
        if m.get('Queue') is not None:
            self.queue = m.get('Queue')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        consumers: List[ListQueueConsumersResponseBodyDataConsumers] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.consumers = consumers
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.consumers:
            for k in self.consumers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Consumers'] = []
        if self.consumers is not None:
            for k in self.consumers:
                result['Consumers'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumers = []
        if m.get('Consumers') is not None:
            for k in m.get('Consumers'):
                temp_model = ListQueueConsumersResponseBodyDataConsumers()
                self.consumers.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListQueueConsumersResponseBody(TeaModel):
    def __init__(
        self,
        data: ListQueueConsumersResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListQueueConsumersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQueueConsumersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueueConsumersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueueConsumersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueUpStreamBindingsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        queue_name: str = None,
        virtual_host: str = None,
    ):
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.queue_name = queue_name
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListQueueUpStreamBindingsResponseBodyDataBindings(TeaModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: str = None,
        destination_name: str = None,
        source_exchange: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.destination_name = destination_name
        self.source_exchange = source_exchange

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.destination_name is not None:
            result['DestinationName'] = self.destination_name
        if self.source_exchange is not None:
            result['SourceExchange'] = self.source_exchange
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DestinationName') is not None:
            self.destination_name = m.get('DestinationName')
        if m.get('SourceExchange') is not None:
            self.source_exchange = m.get('SourceExchange')
        return self


class ListQueueUpStreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        bindings: List[ListQueueUpStreamBindingsResponseBodyDataBindings] = None,
        max_results: str = None,
        next_token: str = None,
    ):
        self.bindings = bindings
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        if self.bindings:
            for k in self.bindings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bindings'] = []
        if self.bindings is not None:
            for k in self.bindings:
                result['Bindings'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bindings = []
        if m.get('Bindings') is not None:
            for k in m.get('Bindings'):
                temp_model = ListQueueUpStreamBindingsResponseBodyDataBindings()
                self.bindings.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListQueueUpStreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListQueueUpStreamBindingsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListQueueUpStreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQueueUpStreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueueUpStreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueueUpStreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueuesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        virtual_host: str = None,
    ):
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token
        self.virtual_host = virtual_host

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.virtual_host is not None:
            result['VirtualHost'] = self.virtual_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('VirtualHost') is not None:
            self.virtual_host = m.get('VirtualHost')
        return self


class ListQueuesResponseBodyDataQueues(TeaModel):
    def __init__(
        self,
        attributes: Dict[str, Any] = None,
        auto_delete_state: bool = None,
        create_time: int = None,
        exclusive_state: bool = None,
        last_consume_time: int = None,
        name: str = None,
        owner_id: str = None,
        vhost_name: str = None,
    ):
        self.attributes = attributes
        self.auto_delete_state = auto_delete_state
        self.create_time = create_time
        self.exclusive_state = exclusive_state
        self.last_consume_time = last_consume_time
        self.name = name
        self.owner_id = owner_id
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.auto_delete_state is not None:
            result['AutoDeleteState'] = self.auto_delete_state
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exclusive_state is not None:
            result['ExclusiveState'] = self.exclusive_state
        if self.last_consume_time is not None:
            result['LastConsumeTime'] = self.last_consume_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.vhost_name is not None:
            result['VHostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('AutoDeleteState') is not None:
            self.auto_delete_state = m.get('AutoDeleteState')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExclusiveState') is not None:
            self.exclusive_state = m.get('ExclusiveState')
        if m.get('LastConsumeTime') is not None:
            self.last_consume_time = m.get('LastConsumeTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('VHostName') is not None:
            self.vhost_name = m.get('VHostName')
        return self


class ListQueuesResponseBodyData(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        queues: List[ListQueuesResponseBodyDataQueues] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # Queue。
        self.queues = queues

    def validate(self):
        if self.queues:
            for k in self.queues:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Queues'] = []
        if self.queues is not None:
            for k in self.queues:
                result['Queues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.queues = []
        if m.get('Queues') is not None:
            for k in m.get('Queues'):
                temp_model = ListQueuesResponseBodyDataQueues()
                self.queues.append(temp_model.from_map(k))
        return self


class ListQueuesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListQueuesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListQueuesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListQueuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListQueuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVirtualHostsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.instance_id = instance_id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        max_results: int = None,
        next_token: str = None,
        virtual_hosts: List[ListVirtualHostsResponseBodyDataVirtualHosts] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # Vhost。
        self.virtual_hosts = virtual_hosts

    def validate(self):
        if self.virtual_hosts:
            for k in self.virtual_hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['VirtualHosts'] = []
        if self.virtual_hosts is not None:
            for k in self.virtual_hosts:
                result['VirtualHosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.virtual_hosts = []
        if m.get('VirtualHosts') is not None:
            for k in m.get('VirtualHosts'):
                temp_model = ListVirtualHostsResponseBodyDataVirtualHosts()
                self.virtual_hosts.append(temp_model.from_map(k))
        return self


class ListVirtualHostsResponseBody(TeaModel):
    def __init__(
        self,
        data: ListVirtualHostsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListVirtualHostsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListVirtualHostsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVirtualHostsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVirtualHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceNameRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class UpdateInstanceNameResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


