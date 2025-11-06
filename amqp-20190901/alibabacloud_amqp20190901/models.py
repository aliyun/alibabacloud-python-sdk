# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class BindRequest(TeaModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: int = None,
        console_session_id: str = None,
        dst_name: str = None,
        instance_id: str = None,
        src_name: str = None,
        vhost_name: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        # This parameter is required.
        self.binding_type = binding_type
        self.console_session_id = console_session_id
        # This parameter is required.
        self.dst_name = dst_name
        self.instance_id = instance_id
        # This parameter is required.
        self.src_name = src_name
        # This parameter is required.
        self.vhost_name = vhost_name

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
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.dst_name is not None:
            result['DstName'] = self.dst_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.src_name is not None:
            result['SrcName'] = self.src_name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('DstName') is not None:
            self.dst_name = m.get('DstName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SrcName') is not None:
            self.src_name = m.get('SrcName')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class BindResponseBody(TeaModel):
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


class BindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelUserSettingRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CancelUserSettingResponseBody(TeaModel):
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


class CancelUserSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelUserSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CancelUserSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigureUserSettingRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        console_session_id: str = None,
        instance_id: str = None,
        logstore: str = None,
        project_name: str = None,
        put_type: str = None,
    ):
        self.bucket_name = bucket_name
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.logstore = logstore
        self.project_name = project_name
        # This parameter is required.
        self.put_type = put_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.put_type is not None:
            result['PutType'] = self.put_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('PutType') is not None:
            self.put_type = m.get('PutType')
        return self


class ConfigureUserSettingResponseBody(TeaModel):
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


class ConfigureUserSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigureUserSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfigureUserSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConsoleClearPretendStatusRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        # This parameter is required.
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class ConsoleClearPretendStatusResponseBody(TeaModel):
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


class ConsoleClearPretendStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConsoleClearPretendStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConsoleClearPretendStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConsoleSavePretendStatusRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        key: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.console_session_id = console_session_id
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.key is not None:
            result['Key'] = self.key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ConsoleSavePretendStatusResponseBody(TeaModel):
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


class ConsoleSavePretendStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConsoleSavePretendStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConsoleSavePretendStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCloudMonitorSLRRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class CreateCloudMonitorSLRResponseBody(TeaModel):
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


class CreateCloudMonitorSLRResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCloudMonitorSLRResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateCloudMonitorSLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateExchangeRequest(TeaModel):
    def __init__(
        self,
        alternate_exchange: str = None,
        auto_delete: bool = None,
        console_session_id: str = None,
        exchange_name: str = None,
        exchange_type: int = None,
        instance_id: str = None,
        internal: bool = None,
        vhost_name: str = None,
        xdelayed_type: str = None,
        xhash_header: str = None,
    ):
        self.alternate_exchange = alternate_exchange
        self.auto_delete = auto_delete
        self.console_session_id = console_session_id
        # This parameter is required.
        self.exchange_name = exchange_name
        # This parameter is required.
        self.exchange_type = exchange_type
        self.instance_id = instance_id
        self.internal = internal
        # This parameter is required.
        self.vhost_name = vhost_name
        self.xdelayed_type = xdelayed_type
        self.xhash_header = xhash_header

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alternate_exchange is not None:
            result['AlternateExchange'] = self.alternate_exchange
        if self.auto_delete is not None:
            result['AutoDelete'] = self.auto_delete
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.internal is not None:
            result['Internal'] = self.internal
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        if self.xdelayed_type is not None:
            result['XDelayedType'] = self.xdelayed_type
        if self.xhash_header is not None:
            result['XHashHeader'] = self.xhash_header
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlternateExchange') is not None:
            self.alternate_exchange = m.get('AlternateExchange')
        if m.get('AutoDelete') is not None:
            self.auto_delete = m.get('AutoDelete')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Internal') is not None:
            self.internal = m.get('Internal')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        if m.get('XDelayedType') is not None:
            self.xdelayed_type = m.get('XDelayedType')
        if m.get('XHashHeader') is not None:
            self.xhash_header = m.get('XHashHeader')
        return self


class CreateExchangeResponseBody(TeaModel):
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


class CreateLogDeliverySLRRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class CreateLogDeliverySLRResponseBody(TeaModel):
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


class CreateLogDeliverySLRResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLogDeliverySLRResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateLogDeliverySLRResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateQueueRequest(TeaModel):
    def __init__(
        self,
        auto_delete: bool = None,
        auto_expire: int = None,
        console_session_id: str = None,
        dead_letter_exchange: str = None,
        dead_letter_routing_key: str = None,
        exclusive: bool = None,
        instance_id: str = None,
        max_length: int = None,
        maximun_prioty: int = None,
        message_ttl: int = None,
        ordered: bool = None,
        queue_name: str = None,
        retry_inherit: bool = None,
        retry_interval: int = None,
        retry_times: int = None,
        single_active_consumer: bool = None,
        vhost_name: str = None,
    ):
        self.auto_delete = auto_delete
        self.auto_expire = auto_expire
        self.console_session_id = console_session_id
        self.dead_letter_exchange = dead_letter_exchange
        self.dead_letter_routing_key = dead_letter_routing_key
        self.exclusive = exclusive
        self.instance_id = instance_id
        self.max_length = max_length
        self.maximun_prioty = maximun_prioty
        self.message_ttl = message_ttl
        self.ordered = ordered
        # This parameter is required.
        self.queue_name = queue_name
        self.retry_inherit = retry_inherit
        self.retry_interval = retry_interval
        self.retry_times = retry_times
        self.single_active_consumer = single_active_consumer
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete is not None:
            result['AutoDelete'] = self.auto_delete
        if self.auto_expire is not None:
            result['AutoExpire'] = self.auto_expire
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.dead_letter_exchange is not None:
            result['DeadLetterExchange'] = self.dead_letter_exchange
        if self.dead_letter_routing_key is not None:
            result['DeadLetterRoutingKey'] = self.dead_letter_routing_key
        if self.exclusive is not None:
            result['Exclusive'] = self.exclusive
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_length is not None:
            result['MaxLength'] = self.max_length
        if self.maximun_prioty is not None:
            result['MaximunPrioty'] = self.maximun_prioty
        if self.message_ttl is not None:
            result['MessageTTL'] = self.message_ttl
        if self.ordered is not None:
            result['Ordered'] = self.ordered
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.retry_inherit is not None:
            result['RetryInherit'] = self.retry_inherit
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times
        if self.single_active_consumer is not None:
            result['SingleActiveConsumer'] = self.single_active_consumer
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDelete') is not None:
            self.auto_delete = m.get('AutoDelete')
        if m.get('AutoExpire') is not None:
            self.auto_expire = m.get('AutoExpire')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('DeadLetterExchange') is not None:
            self.dead_letter_exchange = m.get('DeadLetterExchange')
        if m.get('DeadLetterRoutingKey') is not None:
            self.dead_letter_routing_key = m.get('DeadLetterRoutingKey')
        if m.get('Exclusive') is not None:
            self.exclusive = m.get('Exclusive')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')
        if m.get('MaximunPrioty') is not None:
            self.maximun_prioty = m.get('MaximunPrioty')
        if m.get('MessageTTL') is not None:
            self.message_ttl = m.get('MessageTTL')
        if m.get('Ordered') is not None:
            self.ordered = m.get('Ordered')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RetryInherit') is not None:
            self.retry_inherit = m.get('RetryInherit')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')
        if m.get('SingleActiveConsumer') is not None:
            self.single_active_consumer = m.get('SingleActiveConsumer')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class CreateQueueResponseBody(TeaModel):
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


class CreateVhostRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class CreateVhostResponseBody(TeaModel):
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


class CreateVhostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVhostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateVhostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DashboardCheckServiceStatusRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class DashboardCheckServiceStatusResponseBody(TeaModel):
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


class DashboardCheckServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DashboardCheckServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DashboardCheckServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DashboardListRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        dashboard_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.dashboard_name = dashboard_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.dashboard_name is not None:
            result['DashboardName'] = self.dashboard_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('DashboardName') is not None:
            self.dashboard_name = m.get('DashboardName')
        return self


class DashboardListResponseBody(TeaModel):
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


class DashboardListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DashboardListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DashboardListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteExchangeRequest(TeaModel):
    def __init__(
        self,
        collina: str = None,
        console_session_id: str = None,
        exchange_name: str = None,
        exchange_names: Dict[str, Any] = None,
        instance_id: str = None,
        umid_token: str = None,
        vhost_name: str = None,
    ):
        self.collina = collina
        self.console_session_id = console_session_id
        self.exchange_name = exchange_name
        self.exchange_names = exchange_names
        self.instance_id = instance_id
        self.umid_token = umid_token
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collina is not None:
            result['Collina'] = self.collina
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.exchange_names is not None:
            result['ExchangeNames'] = self.exchange_names
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collina') is not None:
            self.collina = m.get('Collina')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('ExchangeNames') is not None:
            self.exchange_names = m.get('ExchangeNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class DeleteExchangeShrinkRequest(TeaModel):
    def __init__(
        self,
        collina: str = None,
        console_session_id: str = None,
        exchange_name: str = None,
        exchange_names_shrink: str = None,
        instance_id: str = None,
        umid_token: str = None,
        vhost_name: str = None,
    ):
        self.collina = collina
        self.console_session_id = console_session_id
        self.exchange_name = exchange_name
        self.exchange_names_shrink = exchange_names_shrink
        self.instance_id = instance_id
        self.umid_token = umid_token
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collina is not None:
            result['Collina'] = self.collina
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.exchange_names_shrink is not None:
            result['ExchangeNames'] = self.exchange_names_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collina') is not None:
            self.collina = m.get('Collina')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('ExchangeNames') is not None:
            self.exchange_names_shrink = m.get('ExchangeNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class DeleteExchangeResponseBody(TeaModel):
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


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteInstanceResponseBody(TeaModel):
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


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQueueRequest(TeaModel):
    def __init__(
        self,
        collina: str = None,
        console_session_id: str = None,
        instance_id: str = None,
        queue_name: str = None,
        queue_names: Dict[str, Any] = None,
        umid_token: str = None,
        vhost_name: str = None,
    ):
        self.collina = collina
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.queue_names = queue_names
        self.umid_token = umid_token
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collina is not None:
            result['Collina'] = self.collina
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.queue_names is not None:
            result['QueueNames'] = self.queue_names
        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collina') is not None:
            self.collina = m.get('Collina')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('QueueNames') is not None:
            self.queue_names = m.get('QueueNames')
        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class DeleteQueueShrinkRequest(TeaModel):
    def __init__(
        self,
        collina: str = None,
        console_session_id: str = None,
        instance_id: str = None,
        queue_name: str = None,
        queue_names_shrink: str = None,
        umid_token: str = None,
        vhost_name: str = None,
    ):
        self.collina = collina
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.queue_names_shrink = queue_names_shrink
        self.umid_token = umid_token
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collina is not None:
            result['Collina'] = self.collina
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.queue_names_shrink is not None:
            result['QueueNames'] = self.queue_names_shrink
        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collina') is not None:
            self.collina = m.get('Collina')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('QueueNames') is not None:
            self.queue_names_shrink = m.get('QueueNames')
        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class DeleteQueueResponseBody(TeaModel):
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


class DeleteStaticAccountRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        create_time_stamp: int = None,
        instance_id: str = None,
        user_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.create_time_stamp = create_time_stamp
        self.instance_id = instance_id
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteStaticAccountResponseBody(TeaModel):
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


class DeleteStaticAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStaticAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteStaticAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVhostRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_name: str = None,
        vhost_names: Dict[str, Any] = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.vhost_name = vhost_name
        self.vhost_names = vhost_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        if self.vhost_names is not None:
            result['VhostNames'] = self.vhost_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        if m.get('VhostNames') is not None:
            self.vhost_names = m.get('VhostNames')
        return self


class DeleteVhostShrinkRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_name: str = None,
        vhost_names_shrink: str = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.vhost_name = vhost_name
        self.vhost_names_shrink = vhost_names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        if self.vhost_names_shrink is not None:
            result['VhostNames'] = self.vhost_names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        if m.get('VhostNames') is not None:
            self.vhost_names_shrink = m.get('VhostNames')
        return self


class DeleteVhostResponseBody(TeaModel):
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


class DeleteVhostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVhostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteVhostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class DescribeRegionsResponseBodyDataRegions(TeaModel):
    def __init__(
        self,
        region_cn_name: str = None,
        region_id: str = None,
        region_name: str = None,
    ):
        self.region_cn_name = region_cn_name
        self.region_id = region_id
        self.region_name = region_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_cn_name is not None:
            result['RegionCnName'] = self.region_cn_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCnName') is not None:
            self.region_cn_name = m.get('RegionCnName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class DescribeRegionsResponseBodyData(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyDataRegions] = None,
    ):
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyDataRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: DescribeRegionsResponseBodyData = None,
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
            temp_model = DescribeRegionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        export_type: int = None,
        instance_id: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.export_type = export_type
        # This parameter is required.
        self.instance_id = instance_id
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ExportResponseBody(TeaModel):
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


class ExportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchStaticAccountRequest(TeaModel):
    def __init__(
        self,
        account_access_key: str = None,
        console_session_id: str = None,
        create_time_stamp: int = None,
        instance_id: str = None,
        remark: str = None,
        skey: str = None,
        secret_sign: str = None,
        user_name: str = None,
    ):
        # This parameter is required.
        self.account_access_key = account_access_key
        self.console_session_id = console_session_id
        # This parameter is required.
        self.create_time_stamp = create_time_stamp
        # This parameter is required.
        self.instance_id = instance_id
        self.remark = remark
        # This parameter is required.
        self.skey = skey
        # This parameter is required.
        self.secret_sign = secret_sign
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_access_key is not None:
            result['AccountAccessKey'] = self.account_access_key
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.skey is not None:
            result['SKey'] = self.skey
        if self.secret_sign is not None:
            result['SecretSign'] = self.secret_sign
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountAccessKey') is not None:
            self.account_access_key = m.get('AccountAccessKey')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SKey') is not None:
            self.skey = m.get('SKey')
        if m.get('SecretSign') is not None:
            self.secret_sign = m.get('SecretSign')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class FetchStaticAccountResponseBodyData(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        create_time_stamp: int = None,
        instance_id: str = None,
        master_uid: int = None,
        password: str = None,
        remark: str = None,
        user_name: str = None,
    ):
        self.access_key = access_key
        self.create_time_stamp = create_time_stamp
        self.instance_id = instance_id
        self.master_uid = master_uid
        self.password = password
        self.remark = remark
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
        if self.remark is not None:
            result['Remark'] = self.remark
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
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class FetchStaticAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: FetchStaticAccountResponseBodyData = None,
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
            temp_model = FetchStaticAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FetchStaticAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchStaticAccountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = FetchStaticAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAckInfoByIntervalRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        console_session_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        interval_sec: int = None,
        page_size: int = None,
        queue_name: str = None,
        start_time: int = None,
        vhost_name: str = None,
    ):
        self.client_token = client_token
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.interval_sec = interval_sec
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.interval_sec is not None:
            result['IntervalSec'] = self.interval_sec
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IntervalSec') is not None:
            self.interval_sec = m.get('IntervalSec')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetAckInfoByIntervalResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        action: str = None,
        channel_id: str = None,
        connection_id: str = None,
        delivery_tag: int = None,
        queue_name: str = None,
        rocket_mq_msg_id: str = None,
        rt: int = None,
        time_stamp: str = None,
    ):
        self.action = action
        self.channel_id = channel_id
        self.connection_id = connection_id
        self.delivery_tag = delivery_tag
        self.queue_name = queue_name
        self.rocket_mq_msg_id = rocket_mq_msg_id
        self.rt = rt
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.delivery_tag is not None:
            result['DeliveryTag'] = self.delivery_tag
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.rocket_mq_msg_id is not None:
            result['RocketMqMsgId'] = self.rocket_mq_msg_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('DeliveryTag') is not None:
            self.delivery_tag = m.get('DeliveryTag')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('RocketMqMsgId') is not None:
            self.rocket_mq_msg_id = m.get('RocketMqMsgId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class GetAckInfoByIntervalResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: List[GetAckInfoByIntervalResponseBodyDataVoList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            for k in self.vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VoList'] = []
        if self.vo_list is not None:
            for k in self.vo_list:
                result['VoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vo_list = []
        if m.get('VoList') is not None:
            for k in m.get('VoList'):
                temp_model = GetAckInfoByIntervalResponseBodyDataVoList()
                self.vo_list.append(temp_model.from_map(k))
        return self


class GetAckInfoByIntervalResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetAckInfoByIntervalResponseBodyData = None,
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
            temp_model = GetAckInfoByIntervalResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAckInfoByIntervalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAckInfoByIntervalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetAckInfoByIntervalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAckInfoOfMessageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        console_session_id: str = None,
        consume_status: str = None,
        delivery_tag: str = None,
        end_time: int = None,
        instance_id: str = None,
        msg_id: str = None,
        queue_name: str = None,
        start_time: int = None,
        time_stamp: str = None,
        vhost_name: str = None,
    ):
        self.client_token = client_token
        self.console_session_id = console_session_id
        # This parameter is required.
        self.consume_status = consume_status
        # This parameter is required.
        self.delivery_tag = delivery_tag
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.msg_id = msg_id
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.time_stamp = time_stamp
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.consume_status is not None:
            result['ConsumeStatus'] = self.consume_status
        if self.delivery_tag is not None:
            result['DeliveryTag'] = self.delivery_tag
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ConsumeStatus') is not None:
            self.consume_status = m.get('ConsumeStatus')
        if m.get('DeliveryTag') is not None:
            self.delivery_tag = m.get('DeliveryTag')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetAckInfoOfMessageResponseBodyData(TeaModel):
    def __init__(
        self,
        ack_error_info: str = None,
        ack_result: str = None,
        action: str = None,
        code: str = None,
        property: Dict[str, Any] = None,
        time_stamp: str = None,
    ):
        self.ack_error_info = ack_error_info
        self.ack_result = ack_result
        self.action = action
        self.code = code
        self.property = property
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ack_error_info is not None:
            result['AckErrorInfo'] = self.ack_error_info
        if self.ack_result is not None:
            result['AckResult'] = self.ack_result
        if self.action is not None:
            result['Action'] = self.action
        if self.code is not None:
            result['Code'] = self.code
        if self.property is not None:
            result['Property'] = self.property
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckErrorInfo') is not None:
            self.ack_error_info = m.get('AckErrorInfo')
        if m.get('AckResult') is not None:
            self.ack_result = m.get('AckResult')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Property') is not None:
            self.property = m.get('Property')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class GetAckInfoOfMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetAckInfoOfMessageResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAckInfoOfMessageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAckInfoOfMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAckInfoOfMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetAckInfoOfMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBindingCountRequest(TeaModel):
    def __init__(
        self,
        binding_type: int = None,
        console_session_id: str = None,
        instance_id: str = None,
        resource_name: str = None,
        upstream: bool = None,
        vhost_name: str = None,
    ):
        # This parameter is required.
        self.binding_type = binding_type
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        # This parameter is required.
        self.resource_name = resource_name
        # This parameter is required.
        self.upstream = upstream
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.upstream is not None:
            result['Upstream'] = self.upstream
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Upstream') is not None:
            self.upstream = m.get('Upstream')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetBindingCountResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: int = None,
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


class GetBindingCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBindingCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetBindingCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBindingErrorByTaskIdRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        page_size: int = None,
        task_id: int = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetBindingErrorByTaskIdResponseBodyDataVoListBindingErrorDO(TeaModel):
    def __init__(
        self,
        destination: str = None,
        destination_type: str = None,
        error_message: str = None,
        routing_key: str = None,
        src: str = None,
        task_id: int = None,
        vhost_name: str = None,
    ):
        self.destination = destination
        self.destination_type = destination_type
        self.error_message = error_message
        self.routing_key = routing_key
        self.src = src
        self.task_id = task_id
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key
        if self.src is not None:
            result['Src'] = self.src
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')
        if m.get('Src') is not None:
            self.src = m.get('Src')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetBindingErrorByTaskIdResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        binding_error_do: List[GetBindingErrorByTaskIdResponseBodyDataVoListBindingErrorDO] = None,
    ):
        self.binding_error_do = binding_error_do

    def validate(self):
        if self.binding_error_do:
            for k in self.binding_error_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindingErrorDO'] = []
        if self.binding_error_do is not None:
            for k in self.binding_error_do:
                result['BindingErrorDO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.binding_error_do = []
        if m.get('BindingErrorDO') is not None:
            for k in m.get('BindingErrorDO'):
                temp_model = GetBindingErrorByTaskIdResponseBodyDataVoListBindingErrorDO()
                self.binding_error_do.append(temp_model.from_map(k))
        return self


class GetBindingErrorByTaskIdResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: GetBindingErrorByTaskIdResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = GetBindingErrorByTaskIdResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class GetBindingErrorByTaskIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetBindingErrorByTaskIdResponseBodyData = None,
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
            temp_model = GetBindingErrorByTaskIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetBindingErrorByTaskIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBindingErrorByTaskIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetBindingErrorByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommonBuyUrlRequest(TeaModel):
    def __init__(
        self,
        action_type: str = None,
        console_session_id: str = None,
        instance_id: str = None,
    ):
        # This parameter is required.
        self.action_type = action_type
        self.console_session_id = console_session_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetCommonBuyUrlResponseBody(TeaModel):
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


class GetCommonBuyUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCommonBuyUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetCommonBuyUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConsumeTraceByQueueAndRocketMqMsgIdRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        console_session_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        msg_id: str = None,
        queue_name: str = None,
        start_time: int = None,
        vhost_name: str = None,
    ):
        self.client_token = client_token
        self.console_session_id = console_session_id
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.msg_id = msg_id
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetConsumeTraceByQueueAndRocketMqMsgIdResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_ack_tag: str = None,
        client_address: str = None,
        code: str = None,
        consume_type: str = None,
        consumer_tag: str = None,
        current_status: str = None,
        delivery_error_info: str = None,
        delivery_tag: str = None,
        dlq_queue_msg_id_map: Dict[str, Any] = None,
        reason: str = None,
        show_ack_icon: bool = None,
        time_stamp: str = None,
        user_id: str = None,
    ):
        self.auto_ack_tag = auto_ack_tag
        self.client_address = client_address
        self.code = code
        self.consume_type = consume_type
        self.consumer_tag = consumer_tag
        self.current_status = current_status
        self.delivery_error_info = delivery_error_info
        self.delivery_tag = delivery_tag
        self.dlq_queue_msg_id_map = dlq_queue_msg_id_map
        self.reason = reason
        self.show_ack_icon = show_ack_icon
        self.time_stamp = time_stamp
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_ack_tag is not None:
            result['AutoAckTag'] = self.auto_ack_tag
        if self.client_address is not None:
            result['ClientAddress'] = self.client_address
        if self.code is not None:
            result['Code'] = self.code
        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type
        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status
        if self.delivery_error_info is not None:
            result['DeliveryErrorInfo'] = self.delivery_error_info
        if self.delivery_tag is not None:
            result['DeliveryTag'] = self.delivery_tag
        if self.dlq_queue_msg_id_map is not None:
            result['DlqQueueMsgIdMap'] = self.dlq_queue_msg_id_map
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.show_ack_icon is not None:
            result['ShowAckIcon'] = self.show_ack_icon
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoAckTag') is not None:
            self.auto_ack_tag = m.get('AutoAckTag')
        if m.get('ClientAddress') is not None:
            self.client_address = m.get('ClientAddress')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')
        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')
        if m.get('DeliveryErrorInfo') is not None:
            self.delivery_error_info = m.get('DeliveryErrorInfo')
        if m.get('DeliveryTag') is not None:
            self.delivery_tag = m.get('DeliveryTag')
        if m.get('DlqQueueMsgIdMap') is not None:
            self.dlq_queue_msg_id_map = m.get('DlqQueueMsgIdMap')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ShowAckIcon') is not None:
            self.show_ack_icon = m.get('ShowAckIcon')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetConsumeTraceByQueueAndRocketMqMsgIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetConsumeTraceByQueueAndRocketMqMsgIdResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetConsumeTraceByQueueAndRocketMqMsgIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConsumeTraceByQueueAndRocketMqMsgIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConsumeTraceByQueueAndRocketMqMsgIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetConsumeTraceByQueueAndRocketMqMsgIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExchangeErrorByTaskIdRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        page_size: int = None,
        task_id: int = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetExchangeErrorByTaskIdResponseBodyDataVoListExchangeErrorDO(TeaModel):
    def __init__(
        self,
        error_message: int = None,
        exchange_name: str = None,
        exchange_type: str = None,
        task_id: int = None,
        vhost_name: str = None,
    ):
        self.error_message = error_message
        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.task_id = task_id
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetExchangeErrorByTaskIdResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        exchange_error_do: List[GetExchangeErrorByTaskIdResponseBodyDataVoListExchangeErrorDO] = None,
    ):
        self.exchange_error_do = exchange_error_do

    def validate(self):
        if self.exchange_error_do:
            for k in self.exchange_error_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExchangeErrorDO'] = []
        if self.exchange_error_do is not None:
            for k in self.exchange_error_do:
                result['ExchangeErrorDO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exchange_error_do = []
        if m.get('ExchangeErrorDO') is not None:
            for k in m.get('ExchangeErrorDO'):
                temp_model = GetExchangeErrorByTaskIdResponseBodyDataVoListExchangeErrorDO()
                self.exchange_error_do.append(temp_model.from_map(k))
        return self


class GetExchangeErrorByTaskIdResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: GetExchangeErrorByTaskIdResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = GetExchangeErrorByTaskIdResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class GetExchangeErrorByTaskIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetExchangeErrorByTaskIdResponseBodyData = None,
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
            temp_model = GetExchangeErrorByTaskIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetExchangeErrorByTaskIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExchangeErrorByTaskIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetExchangeErrorByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExchangeRateRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        exchange_names: Dict[str, Any] = None,
        instance_id: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.exchange_names = exchange_names
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.exchange_names is not None:
            result['ExchangeNames'] = self.exchange_names
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ExchangeNames') is not None:
            self.exchange_names = m.get('ExchangeNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetExchangeRateShrinkRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        exchange_names_shrink: str = None,
        instance_id: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.exchange_names_shrink = exchange_names_shrink
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.exchange_names_shrink is not None:
            result['ExchangeNames'] = self.exchange_names_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ExchangeNames') is not None:
            self.exchange_names_shrink = m.get('ExchangeNames')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetExchangeRateResponseBodyDataExchangeQuotaVO(TeaModel):
    def __init__(
        self,
        exchange_name: str = None,
        in_qps: int = None,
        instance_id: str = None,
        out_qps: int = None,
        vhost_name: str = None,
    ):
        self.exchange_name = exchange_name
        self.in_qps = in_qps
        self.instance_id = instance_id
        self.out_qps = out_qps
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.in_qps is not None:
            result['InQps'] = self.in_qps
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.out_qps is not None:
            result['OutQps'] = self.out_qps
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InQps') is not None:
            self.in_qps = m.get('InQps')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OutQps') is not None:
            self.out_qps = m.get('OutQps')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetExchangeRateResponseBodyData(TeaModel):
    def __init__(
        self,
        exchange_quota_vo: List[GetExchangeRateResponseBodyDataExchangeQuotaVO] = None,
    ):
        self.exchange_quota_vo = exchange_quota_vo

    def validate(self):
        if self.exchange_quota_vo:
            for k in self.exchange_quota_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExchangeQuotaVO'] = []
        if self.exchange_quota_vo is not None:
            for k in self.exchange_quota_vo:
                result['ExchangeQuotaVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exchange_quota_vo = []
        if m.get('ExchangeQuotaVO') is not None:
            for k in m.get('ExchangeQuotaVO'):
                temp_model = GetExchangeRateResponseBodyDataExchangeQuotaVO()
                self.exchange_quota_vo.append(temp_model.from_map(k))
        return self


class GetExchangeRateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetExchangeRateResponseBodyData = None,
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
            temp_model = GetExchangeRateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetExchangeRateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExchangeRateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetExchangeRateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMsgIdListByQueueRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        console_session_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        page_size: int = None,
        queue_name: str = None,
        start_time: int = None,
        vhost_name: str = None,
    ):
        self.client_token = client_token
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetMsgIdListByQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: List[str] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            self.vo_list = m.get('VoList')
        return self


class GetMsgIdListByQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetMsgIdListByQueueResponseBodyData = None,
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
            temp_model = GetMsgIdListByQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMsgIdListByQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMsgIdListByQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetMsgIdListByQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueConsumersRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        instance_id: str = None,
        page_size: int = None,
        queue_name: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        self.current_page = current_page
        # This parameter is required.
        self.instance_id = instance_id
        self.page_size = page_size
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetQueueConsumersResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        client_address: str = None,
        consumer_tag: str = None,
        gmt_create: int = None,
    ):
        self.client_address = client_address
        self.consumer_tag = consumer_tag
        self.gmt_create = gmt_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_address is not None:
            result['ClientAddress'] = self.client_address
        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientAddress') is not None:
            self.client_address = m.get('ClientAddress')
        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        return self


class GetQueueConsumersResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        task_id: str = None,
        total_count: int = None,
        vo_list: List[GetQueueConsumersResponseBodyDataVoList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.task_id = task_id
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            for k in self.vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VoList'] = []
        if self.vo_list is not None:
            for k in self.vo_list:
                result['VoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vo_list = []
        if m.get('VoList') is not None:
            for k in m.get('VoList'):
                temp_model = GetQueueConsumersResponseBodyDataVoList()
                self.vo_list.append(temp_model.from_map(k))
        return self


class GetQueueConsumersResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetQueueConsumersResponseBodyData = None,
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
            temp_model = GetQueueConsumersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueueConsumersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueueConsumersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetQueueConsumersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueErrorByTaskIdRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        page_size: int = None,
        task_id: int = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetQueueErrorByTaskIdResponseBodyDataVoListQueueErrorDO(TeaModel):
    def __init__(
        self,
        auto_delete: bool = None,
        durable: bool = None,
        error_message: int = None,
        queue_name: str = None,
        task_id: int = None,
        vhost_name: str = None,
    ):
        self.auto_delete = auto_delete
        self.durable = durable
        self.error_message = error_message
        self.queue_name = queue_name
        self.task_id = task_id
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete is not None:
            result['AutoDelete'] = self.auto_delete
        if self.durable is not None:
            result['Durable'] = self.durable
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoDelete') is not None:
            self.auto_delete = m.get('AutoDelete')
        if m.get('Durable') is not None:
            self.durable = m.get('Durable')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetQueueErrorByTaskIdResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        queue_error_do: List[GetQueueErrorByTaskIdResponseBodyDataVoListQueueErrorDO] = None,
    ):
        self.queue_error_do = queue_error_do

    def validate(self):
        if self.queue_error_do:
            for k in self.queue_error_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueueErrorDO'] = []
        if self.queue_error_do is not None:
            for k in self.queue_error_do:
                result['QueueErrorDO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.queue_error_do = []
        if m.get('QueueErrorDO') is not None:
            for k in m.get('QueueErrorDO'):
                temp_model = GetQueueErrorByTaskIdResponseBodyDataVoListQueueErrorDO()
                self.queue_error_do.append(temp_model.from_map(k))
        return self


class GetQueueErrorByTaskIdResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: GetQueueErrorByTaskIdResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = GetQueueErrorByTaskIdResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class GetQueueErrorByTaskIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetQueueErrorByTaskIdResponseBodyData = None,
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
            temp_model = GetQueueErrorByTaskIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueueErrorByTaskIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueueErrorByTaskIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetQueueErrorByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetQueueRateRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        queue_names: Dict[str, Any] = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.queue_names = queue_names
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_names is not None:
            result['QueueNames'] = self.queue_names
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueNames') is not None:
            self.queue_names = m.get('QueueNames')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetQueueRateShrinkRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        queue_names_shrink: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.queue_names_shrink = queue_names_shrink
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_names_shrink is not None:
            result['QueueNames'] = self.queue_names_shrink
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueNames') is not None:
            self.queue_names_shrink = m.get('QueueNames')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetQueueRateResponseBodyData(TeaModel):
    def __init__(
        self,
        in_qps: int = None,
        instance_id: str = None,
        out_qps: int = None,
        queue_name: str = None,
        vhost_name: str = None,
    ):
        self.in_qps = in_qps
        self.instance_id = instance_id
        self.out_qps = out_qps
        self.queue_name = queue_name
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_qps is not None:
            result['InQps'] = self.in_qps
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.out_qps is not None:
            result['OutQps'] = self.out_qps
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InQps') is not None:
            self.in_qps = m.get('InQps')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OutQps') is not None:
            self.out_qps = m.get('OutQps')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetQueueRateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetQueueRateResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetQueueRateResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetQueueRateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetQueueRateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetQueueRateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSendTraceByConnectionAndChannelAndDeliveryTagRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        client_token: str = None,
        connection_id: str = None,
        console_session_id: str = None,
        delivery_tag: int = None,
        end_time: int = None,
        instance_id: str = None,
        start_time: int = None,
        vhost_name: str = None,
    ):
        # This parameter is required.
        self.channel_id = channel_id
        self.client_token = client_token
        # This parameter is required.
        self.connection_id = connection_id
        self.console_session_id = console_session_id
        # This parameter is required.
        self.delivery_tag = delivery_tag
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.delivery_tag is not None:
            result['DeliveryTag'] = self.delivery_tag
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('DeliveryTag') is not None:
            self.delivery_tag = m.get('DeliveryTag')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        delay: str = None,
        exchange: str = None,
        expiration: str = None,
        message_id: str = None,
        queue_msg_id_map: Dict[str, Any] = None,
        remote_address: str = None,
        routing_key: str = None,
        send_error_info: str = None,
        time_stamp: str = None,
        user_id: str = None,
        vhost: str = None,
        xdelay: str = None,
    ):
        self.code = code
        self.delay = delay
        self.exchange = exchange
        self.expiration = expiration
        self.message_id = message_id
        self.queue_msg_id_map = queue_msg_id_map
        self.remote_address = remote_address
        self.routing_key = routing_key
        self.send_error_info = send_error_info
        self.time_stamp = time_stamp
        self.user_id = user_id
        self.vhost = vhost
        self.xdelay = xdelay

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.delay is not None:
            result['Delay'] = self.delay
        if self.exchange is not None:
            result['Exchange'] = self.exchange
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.queue_msg_id_map is not None:
            result['QueueMsgIdMap'] = self.queue_msg_id_map
        if self.remote_address is not None:
            result['RemoteAddress'] = self.remote_address
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key
        if self.send_error_info is not None:
            result['SendErrorInfo'] = self.send_error_info
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vhost is not None:
            result['Vhost'] = self.vhost
        if self.xdelay is not None:
            result['XDelay'] = self.xdelay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Delay') is not None:
            self.delay = m.get('Delay')
        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('QueueMsgIdMap') is not None:
            self.queue_msg_id_map = m.get('QueueMsgIdMap')
        if m.get('RemoteAddress') is not None:
            self.remote_address = m.get('RemoteAddress')
        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')
        if m.get('SendErrorInfo') is not None:
            self.send_error_info = m.get('SendErrorInfo')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')
        if m.get('XDelay') is not None:
            self.xdelay = m.get('XDelay')
        return self


class GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBodyData = None,
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
            temp_model = GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSendTraceByConnectionAndChannelAndDeliveryTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSendTraceByMsgIdRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        console_session_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        msg_id: str = None,
        page_size: int = None,
        queue_name: str = None,
        start_time: int = None,
        vhost_name: str = None,
    ):
        self.client_token = client_token
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.msg_id = msg_id
        # This parameter is required.
        self.page_size = page_size
        self.queue_name = queue_name
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetSendTraceByMsgIdResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        code: str = None,
        exchange: str = None,
        instance_id: str = None,
        message_body_length: str = None,
        message_properties_map: Dict[str, Any] = None,
        queue_msg_id_map: Dict[str, Any] = None,
        remote_address: str = None,
        routing_key: str = None,
        send_error_info: str = None,
        time_stamp: str = None,
        user_id: str = None,
        vhost: str = None,
    ):
        self.code = code
        self.exchange = exchange
        self.instance_id = instance_id
        self.message_body_length = message_body_length
        self.message_properties_map = message_properties_map
        self.queue_msg_id_map = queue_msg_id_map
        self.remote_address = remote_address
        self.routing_key = routing_key
        self.send_error_info = send_error_info
        self.time_stamp = time_stamp
        self.user_id = user_id
        self.vhost = vhost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.exchange is not None:
            result['Exchange'] = self.exchange
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_body_length is not None:
            result['MessageBodyLength'] = self.message_body_length
        if self.message_properties_map is not None:
            result['MessagePropertiesMap'] = self.message_properties_map
        if self.queue_msg_id_map is not None:
            result['QueueMsgIdMap'] = self.queue_msg_id_map
        if self.remote_address is not None:
            result['RemoteAddress'] = self.remote_address
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key
        if self.send_error_info is not None:
            result['SendErrorInfo'] = self.send_error_info
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vhost is not None:
            result['Vhost'] = self.vhost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageBodyLength') is not None:
            self.message_body_length = m.get('MessageBodyLength')
        if m.get('MessagePropertiesMap') is not None:
            self.message_properties_map = m.get('MessagePropertiesMap')
        if m.get('QueueMsgIdMap') is not None:
            self.queue_msg_id_map = m.get('QueueMsgIdMap')
        if m.get('RemoteAddress') is not None:
            self.remote_address = m.get('RemoteAddress')
        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')
        if m.get('SendErrorInfo') is not None:
            self.send_error_info = m.get('SendErrorInfo')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')
        return self


class GetSendTraceByMsgIdResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: List[GetSendTraceByMsgIdResponseBodyDataVoList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            for k in self.vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VoList'] = []
        if self.vo_list is not None:
            for k in self.vo_list:
                result['VoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vo_list = []
        if m.get('VoList') is not None:
            for k in m.get('VoList'):
                temp_model = GetSendTraceByMsgIdResponseBodyDataVoList()
                self.vo_list.append(temp_model.from_map(k))
        return self


class GetSendTraceByMsgIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetSendTraceByMsgIdResponseBodyData = None,
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
            temp_model = GetSendTraceByMsgIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSendTraceByMsgIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSendTraceByMsgIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetSendTraceByMsgIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSendTraceByQueueRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        console_session_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        page_size: int = None,
        queue_name: str = None,
        start_time: int = None,
        vhost_name: str = None,
    ):
        self.client_token = client_token
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetSendTraceByQueueResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        code: str = None,
        exchange: str = None,
        message_body_length: str = None,
        message_id: str = None,
        message_properties_map: Dict[str, Any] = None,
        queue_msg_id_map: Dict[str, Any] = None,
        remote_address: str = None,
        routing_key: str = None,
        send_error_info: str = None,
        time_stamp: str = None,
        user_id: str = None,
        vhost: str = None,
    ):
        self.code = code
        self.exchange = exchange
        self.message_body_length = message_body_length
        self.message_id = message_id
        self.message_properties_map = message_properties_map
        self.queue_msg_id_map = queue_msg_id_map
        self.remote_address = remote_address
        self.routing_key = routing_key
        self.send_error_info = send_error_info
        self.time_stamp = time_stamp
        self.user_id = user_id
        self.vhost = vhost

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.exchange is not None:
            result['Exchange'] = self.exchange
        if self.message_body_length is not None:
            result['MessageBodyLength'] = self.message_body_length
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.message_properties_map is not None:
            result['MessagePropertiesMap'] = self.message_properties_map
        if self.queue_msg_id_map is not None:
            result['QueueMsgIdMap'] = self.queue_msg_id_map
        if self.remote_address is not None:
            result['RemoteAddress'] = self.remote_address
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key
        if self.send_error_info is not None:
            result['SendErrorInfo'] = self.send_error_info
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vhost is not None:
            result['Vhost'] = self.vhost
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')
        if m.get('MessageBodyLength') is not None:
            self.message_body_length = m.get('MessageBodyLength')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('MessagePropertiesMap') is not None:
            self.message_properties_map = m.get('MessagePropertiesMap')
        if m.get('QueueMsgIdMap') is not None:
            self.queue_msg_id_map = m.get('QueueMsgIdMap')
        if m.get('RemoteAddress') is not None:
            self.remote_address = m.get('RemoteAddress')
        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')
        if m.get('SendErrorInfo') is not None:
            self.send_error_info = m.get('SendErrorInfo')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')
        return self


class GetSendTraceByQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: List[GetSendTraceByQueueResponseBodyDataVoList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            for k in self.vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VoList'] = []
        if self.vo_list is not None:
            for k in self.vo_list:
                result['VoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vo_list = []
        if m.get('VoList') is not None:
            for k in m.get('VoList'):
                temp_model = GetSendTraceByQueueResponseBodyDataVoList()
                self.vo_list.append(temp_model.from_map(k))
        return self


class GetSendTraceByQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetSendTraceByQueueResponseBodyData = None,
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
            temp_model = GetSendTraceByQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSendTraceByQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSendTraceByQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetSendTraceByQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStatisticsByVhostRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsListChannelStatistics(TeaModel):
    def __init__(
        self,
        ack_qps: float = None,
        confirm_qps: float = None,
        deliver_qps: float = None,
        get_qps: float = None,
        prefetch: int = None,
        publish_qps: float = None,
        state: int = None,
        unacked: int = None,
        unconfirmed: int = None,
    ):
        self.ack_qps = ack_qps
        self.confirm_qps = confirm_qps
        self.deliver_qps = deliver_qps
        self.get_qps = get_qps
        self.prefetch = prefetch
        self.publish_qps = publish_qps
        self.state = state
        self.unacked = unacked
        self.unconfirmed = unconfirmed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ack_qps is not None:
            result['AckQps'] = self.ack_qps
        if self.confirm_qps is not None:
            result['ConfirmQps'] = self.confirm_qps
        if self.deliver_qps is not None:
            result['DeliverQps'] = self.deliver_qps
        if self.get_qps is not None:
            result['GetQps'] = self.get_qps
        if self.prefetch is not None:
            result['Prefetch'] = self.prefetch
        if self.publish_qps is not None:
            result['PublishQps'] = self.publish_qps
        if self.state is not None:
            result['State'] = self.state
        if self.unacked is not None:
            result['Unacked'] = self.unacked
        if self.unconfirmed is not None:
            result['Unconfirmed'] = self.unconfirmed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckQps') is not None:
            self.ack_qps = m.get('AckQps')
        if m.get('ConfirmQps') is not None:
            self.confirm_qps = m.get('ConfirmQps')
        if m.get('DeliverQps') is not None:
            self.deliver_qps = m.get('DeliverQps')
        if m.get('GetQps') is not None:
            self.get_qps = m.get('GetQps')
        if m.get('Prefetch') is not None:
            self.prefetch = m.get('Prefetch')
        if m.get('PublishQps') is not None:
            self.publish_qps = m.get('PublishQps')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Unacked') is not None:
            self.unacked = m.get('Unacked')
        if m.get('Unconfirmed') is not None:
            self.unconfirmed = m.get('Unconfirmed')
        return self


class GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsList(TeaModel):
    def __init__(
        self,
        channel_statistics: List[GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsListChannelStatistics] = None,
    ):
        self.channel_statistics = channel_statistics

    def validate(self):
        if self.channel_statistics:
            for k in self.channel_statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChannelStatistics'] = []
        if self.channel_statistics is not None:
            for k in self.channel_statistics:
                result['ChannelStatistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channel_statistics = []
        if m.get('ChannelStatistics') is not None:
            for k in m.get('ChannelStatistics'):
                temp_model = GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsListChannelStatistics()
                self.channel_statistics.append(temp_model.from_map(k))
        return self


class GetStatisticsByVhostResponseBodyDataConnectionStatistics(TeaModel):
    def __init__(
        self,
        access_key: str = None,
        channel_num: int = None,
        channel_statistics_list: GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsList = None,
        connection_name: str = None,
        deliver_qps: float = None,
        protocol: str = None,
        publish_qps: float = None,
        remote_address: str = None,
        security_transport: bool = None,
        state: int = None,
    ):
        self.access_key = access_key
        self.channel_num = channel_num
        self.channel_statistics_list = channel_statistics_list
        self.connection_name = connection_name
        self.deliver_qps = deliver_qps
        self.protocol = protocol
        self.publish_qps = publish_qps
        self.remote_address = remote_address
        self.security_transport = security_transport
        self.state = state

    def validate(self):
        if self.channel_statistics_list:
            self.channel_statistics_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.channel_statistics_list is not None:
            result['ChannelStatisticsList'] = self.channel_statistics_list.to_map()
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name
        if self.deliver_qps is not None:
            result['DeliverQps'] = self.deliver_qps
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.publish_qps is not None:
            result['PublishQps'] = self.publish_qps
        if self.remote_address is not None:
            result['RemoteAddress'] = self.remote_address
        if self.security_transport is not None:
            result['SecurityTransport'] = self.security_transport
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('ChannelStatisticsList') is not None:
            temp_model = GetStatisticsByVhostResponseBodyDataConnectionStatisticsChannelStatisticsList()
            self.channel_statistics_list = temp_model.from_map(m['ChannelStatisticsList'])
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')
        if m.get('DeliverQps') is not None:
            self.deliver_qps = m.get('DeliverQps')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('PublishQps') is not None:
            self.publish_qps = m.get('PublishQps')
        if m.get('RemoteAddress') is not None:
            self.remote_address = m.get('RemoteAddress')
        if m.get('SecurityTransport') is not None:
            self.security_transport = m.get('SecurityTransport')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class GetStatisticsByVhostResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_statistics: List[GetStatisticsByVhostResponseBodyDataConnectionStatistics] = None,
    ):
        self.connection_statistics = connection_statistics

    def validate(self):
        if self.connection_statistics:
            for k in self.connection_statistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionStatistics'] = []
        if self.connection_statistics is not None:
            for k in self.connection_statistics:
                result['ConnectionStatistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_statistics = []
        if m.get('ConnectionStatistics') is not None:
            for k in m.get('ConnectionStatistics'):
                temp_model = GetStatisticsByVhostResponseBodyDataConnectionStatistics()
                self.connection_statistics.append(temp_model.from_map(k))
        return self


class GetStatisticsByVhostResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetStatisticsByVhostResponseBodyData = None,
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
            temp_model = GetStatisticsByVhostResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetStatisticsByVhostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStatisticsByVhostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetStatisticsByVhostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskByUidRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetTaskByUidResponseBodyDataVoListImportDefinitionTaskDO(TeaModel):
    def __init__(
        self,
        binding_num: int = None,
        exchange_num: int = None,
        gmt_create: str = None,
        id: int = None,
        import_type: int = None,
        instance_id: str = None,
        instance_name: str = None,
        queue_num: int = None,
        status: int = None,
        user_id: int = None,
        vhost_name: str = None,
        vhost_num: int = None,
    ):
        self.binding_num = binding_num
        self.exchange_num = exchange_num
        self.gmt_create = gmt_create
        self.id = id
        self.import_type = import_type
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.queue_num = queue_num
        self.status = status
        self.user_id = user_id
        self.vhost_name = vhost_name
        self.vhost_num = vhost_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binding_num is not None:
            result['BindingNum'] = self.binding_num
        if self.exchange_num is not None:
            result['ExchangeNum'] = self.exchange_num
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.import_type is not None:
            result['ImportType'] = self.import_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.queue_num is not None:
            result['QueueNum'] = self.queue_num
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        if self.vhost_num is not None:
            result['VhostNum'] = self.vhost_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingNum') is not None:
            self.binding_num = m.get('BindingNum')
        if m.get('ExchangeNum') is not None:
            self.exchange_num = m.get('ExchangeNum')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('QueueNum') is not None:
            self.queue_num = m.get('QueueNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        if m.get('VhostNum') is not None:
            self.vhost_num = m.get('VhostNum')
        return self


class GetTaskByUidResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        import_definition_task_do: List[GetTaskByUidResponseBodyDataVoListImportDefinitionTaskDO] = None,
    ):
        self.import_definition_task_do = import_definition_task_do

    def validate(self):
        if self.import_definition_task_do:
            for k in self.import_definition_task_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImportDefinitionTaskDO'] = []
        if self.import_definition_task_do is not None:
            for k in self.import_definition_task_do:
                result['ImportDefinitionTaskDO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_definition_task_do = []
        if m.get('ImportDefinitionTaskDO') is not None:
            for k in m.get('ImportDefinitionTaskDO'):
                temp_model = GetTaskByUidResponseBodyDataVoListImportDefinitionTaskDO()
                self.import_definition_task_do.append(temp_model.from_map(k))
        return self


class GetTaskByUidResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: GetTaskByUidResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = GetTaskByUidResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class GetTaskByUidResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTaskByUidResponseBodyData = None,
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
            temp_model = GetTaskByUidResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTaskByUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskByUidResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetTaskByUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTpsByTimeRequest(TeaModel):
    def __init__(
        self,
        api: str = None,
        client_token: str = None,
        console_session_id: str = None,
        end_time: int = None,
        instance_id: str = None,
        queue_name: str = None,
        start_time: int = None,
        vhost_name: str = None,
    ):
        self.api = api
        self.client_token = client_token
        self.console_session_id = console_session_id
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        self.queue_name = queue_name
        # This parameter is required.
        self.start_time = start_time
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api is not None:
            result['Api'] = self.api
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Api') is not None:
            self.api = m.get('Api')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetTpsByTimeResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_tps: int = None,
        start_time: int = None,
        tps_list: List[int] = None,
    ):
        self.end_time = end_time
        self.max_tps = max_tps
        self.start_time = start_time
        self.tps_list = tps_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tps_list is not None:
            result['tpsList'] = self.tps_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('tpsList') is not None:
            self.tps_list = m.get('tpsList')
        return self


class GetTpsByTimeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetTpsByTimeResponseBodyData = None,
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
            temp_model = GetTpsByTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTpsByTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTpsByTimeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetTpsByTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserSettingRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetUserSettingResponseBodyData(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        region_id: str = None,
        user_id: int = None,
    ):
        self.logstore = logstore
        self.region_id = region_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetUserSettingResponseBodyData = None,
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
            temp_model = GetUserSettingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetUserSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVhostErrorByTaskIdRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        page_size: int = None,
        task_id: int = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetVhostErrorByTaskIdResponseBodyDataVoListVhostErrorDO(TeaModel):
    def __init__(
        self,
        error_message: int = None,
        task_id: int = None,
        vhost_name: str = None,
    ):
        self.error_message = error_message
        self.task_id = task_id
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetVhostErrorByTaskIdResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        vhost_error_do: List[GetVhostErrorByTaskIdResponseBodyDataVoListVhostErrorDO] = None,
    ):
        self.vhost_error_do = vhost_error_do

    def validate(self):
        if self.vhost_error_do:
            for k in self.vhost_error_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['VhostErrorDO'] = []
        if self.vhost_error_do is not None:
            for k in self.vhost_error_do:
                result['VhostErrorDO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vhost_error_do = []
        if m.get('VhostErrorDO') is not None:
            for k in m.get('VhostErrorDO'):
                temp_model = GetVhostErrorByTaskIdResponseBodyDataVoListVhostErrorDO()
                self.vhost_error_do.append(temp_model.from_map(k))
        return self


class GetVhostErrorByTaskIdResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: GetVhostErrorByTaskIdResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = GetVhostErrorByTaskIdResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class GetVhostErrorByTaskIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetVhostErrorByTaskIdResponseBodyData = None,
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
            temp_model = GetVhostErrorByTaskIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVhostErrorByTaskIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVhostErrorByTaskIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetVhostErrorByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVhostRateRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_names: Dict[str, Any] = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.vhost_names = vhost_names

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_names is not None:
            result['VhostNames'] = self.vhost_names
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostNames') is not None:
            self.vhost_names = m.get('VhostNames')
        return self


class GetVhostRateShrinkRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_names_shrink: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.vhost_names_shrink = vhost_names_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_names_shrink is not None:
            result['VhostNames'] = self.vhost_names_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostNames') is not None:
            self.vhost_names_shrink = m.get('VhostNames')
        return self


class GetVhostRateResponseBodyData(TeaModel):
    def __init__(
        self,
        channel_num: int = None,
        connection_num: int = None,
        in_qps: int = None,
        out_qps: int = None,
        vhost_name: str = None,
    ):
        self.channel_num = channel_num
        self.connection_num = connection_num
        self.in_qps = in_qps
        self.out_qps = out_qps
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.connection_num is not None:
            result['ConnectionNum'] = self.connection_num
        if self.in_qps is not None:
            result['InQps'] = self.in_qps
        if self.out_qps is not None:
            result['OutQps'] = self.out_qps
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('ConnectionNum') is not None:
            self.connection_num = m.get('ConnectionNum')
        if m.get('InQps') is not None:
            self.in_qps = m.get('InQps')
        if m.get('OutQps') is not None:
            self.out_qps = m.get('OutQps')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class GetVhostRateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[GetVhostRateResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetVhostRateResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVhostRateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVhostRateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetVhostRateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportDefinitionAsynchronousRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        import_type: int = None,
        instance_id: str = None,
        instance_name: str = None,
        oss_url: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.import_type = import_type
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.oss_url = oss_url
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.import_type is not None:
            result['ImportType'] = self.import_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ImportDefinitionAsynchronousResponseBodyData(TeaModel):
    def __init__(
        self,
        result: bool = None,
    ):
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ImportDefinitionAsynchronousResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ImportDefinitionAsynchronousResponseBodyData = None,
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
            temp_model = ImportDefinitionAsynchronousResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportDefinitionAsynchronousResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportDefinitionAsynchronousResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ImportDefinitionAsynchronousResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstancePreivewRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        tags: str = None,
    ):
        self.console_session_id = console_session_id
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class InstancePreivewResponseBodyDataInstancesInstancesVOTagsTagsVO(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class InstancePreivewResponseBodyDataInstancesInstancesVOTags(TeaModel):
    def __init__(
        self,
        tags_vo: List[InstancePreivewResponseBodyDataInstancesInstancesVOTagsTagsVO] = None,
    ):
        self.tags_vo = tags_vo

    def validate(self):
        if self.tags_vo:
            for k in self.tags_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagsVO'] = []
        if self.tags_vo is not None:
            for k in self.tags_vo:
                result['TagsVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags_vo = []
        if m.get('TagsVO') is not None:
            for k in m.get('TagsVO'):
                temp_model = InstancePreivewResponseBodyDataInstancesInstancesVOTagsTagsVO()
                self.tags_vo.append(temp_model.from_map(k))
        return self


class InstancePreivewResponseBodyDataInstancesInstancesVO(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        cease_status: bool = None,
        classic_endpoint: str = None,
        enable_dlq_ttl: bool = None,
        encrypted: bool = None,
        expire: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        invisible_time: int = None,
        kms_key_id: str = None,
        max_binding_count: int = None,
        max_connection_channel_count: int = None,
        max_connection_count: int = None,
        max_consume_retry_time: int = None,
        max_eiptps: int = None,
        max_exchange_count: int = None,
        max_msg_body_byte: int = None,
        max_msg_delay_hour: int = None,
        max_msg_trace_time: int = None,
        max_queue: int = None,
        max_queue_consumer_count: int = None,
        max_retry_interval: int = None,
        max_retry_times: int = None,
        max_tps: int = None,
        max_vhost: int = None,
        order_create: int = None,
        order_type: str = None,
        private_endpoint: str = None,
        public_endpoint: str = None,
        resource_group_id: str = None,
        serverless_rate: float = None,
        serverless_switch: bool = None,
        status: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        support_msg_trace: bool = None,
        support_open_source_auth: bool = None,
        tags: InstancePreivewResponseBodyDataInstancesInstancesVOTags = None,
        used_queue: int = None,
        used_vhost: int = None,
        version: int = None,
    ):
        self.auto_renew = auto_renew
        self.cease_status = cease_status
        self.classic_endpoint = classic_endpoint
        self.enable_dlq_ttl = enable_dlq_ttl
        self.encrypted = encrypted
        self.expire = expire
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.invisible_time = invisible_time
        self.kms_key_id = kms_key_id
        self.max_binding_count = max_binding_count
        self.max_connection_channel_count = max_connection_channel_count
        self.max_connection_count = max_connection_count
        self.max_consume_retry_time = max_consume_retry_time
        self.max_eiptps = max_eiptps
        self.max_exchange_count = max_exchange_count
        self.max_msg_body_byte = max_msg_body_byte
        self.max_msg_delay_hour = max_msg_delay_hour
        self.max_msg_trace_time = max_msg_trace_time
        self.max_queue = max_queue
        self.max_queue_consumer_count = max_queue_consumer_count
        self.max_retry_interval = max_retry_interval
        self.max_retry_times = max_retry_times
        self.max_tps = max_tps
        self.max_vhost = max_vhost
        self.order_create = order_create
        self.order_type = order_type
        self.private_endpoint = private_endpoint
        self.public_endpoint = public_endpoint
        self.resource_group_id = resource_group_id
        self.serverless_rate = serverless_rate
        self.serverless_switch = serverless_switch
        self.status = status
        self.storage_size = storage_size
        self.support_eip = support_eip
        self.support_msg_trace = support_msg_trace
        self.support_open_source_auth = support_open_source_auth
        self.tags = tags
        self.used_queue = used_queue
        self.used_vhost = used_vhost
        self.version = version

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cease_status is not None:
            result['CeaseStatus'] = self.cease_status
        if self.classic_endpoint is not None:
            result['ClassicEndpoint'] = self.classic_endpoint
        if self.enable_dlq_ttl is not None:
            result['EnableDlqTtl'] = self.enable_dlq_ttl
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.invisible_time is not None:
            result['InvisibleTime'] = self.invisible_time
        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id
        if self.max_binding_count is not None:
            result['MaxBindingCount'] = self.max_binding_count
        if self.max_connection_channel_count is not None:
            result['MaxConnectionChannelCount'] = self.max_connection_channel_count
        if self.max_connection_count is not None:
            result['MaxConnectionCount'] = self.max_connection_count
        if self.max_consume_retry_time is not None:
            result['MaxConsumeRetryTime'] = self.max_consume_retry_time
        if self.max_eiptps is not None:
            result['MaxEIPTPS'] = self.max_eiptps
        if self.max_exchange_count is not None:
            result['MaxExchangeCount'] = self.max_exchange_count
        if self.max_msg_body_byte is not None:
            result['MaxMsgBodyByte'] = self.max_msg_body_byte
        if self.max_msg_delay_hour is not None:
            result['MaxMsgDelayHour'] = self.max_msg_delay_hour
        if self.max_msg_trace_time is not None:
            result['MaxMsgTraceTime'] = self.max_msg_trace_time
        if self.max_queue is not None:
            result['MaxQueue'] = self.max_queue
        if self.max_queue_consumer_count is not None:
            result['MaxQueueConsumerCount'] = self.max_queue_consumer_count
        if self.max_retry_interval is not None:
            result['MaxRetryInterval'] = self.max_retry_interval
        if self.max_retry_times is not None:
            result['MaxRetryTimes'] = self.max_retry_times
        if self.max_tps is not None:
            result['MaxTPS'] = self.max_tps
        if self.max_vhost is not None:
            result['MaxVhost'] = self.max_vhost
        if self.order_create is not None:
            result['OrderCreate'] = self.order_create
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.private_endpoint is not None:
            result['PrivateEndpoint'] = self.private_endpoint
        if self.public_endpoint is not None:
            result['PublicEndpoint'] = self.public_endpoint
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.serverless_rate is not None:
            result['ServerlessRate'] = self.serverless_rate
        if self.serverless_switch is not None:
            result['ServerlessSwitch'] = self.serverless_switch
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.support_eip is not None:
            result['SupportEIP'] = self.support_eip
        if self.support_msg_trace is not None:
            result['SupportMsgTrace'] = self.support_msg_trace
        if self.support_open_source_auth is not None:
            result['SupportOpenSourceAuth'] = self.support_open_source_auth
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.used_queue is not None:
            result['UsedQueue'] = self.used_queue
        if self.used_vhost is not None:
            result['UsedVhost'] = self.used_vhost
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('CeaseStatus') is not None:
            self.cease_status = m.get('CeaseStatus')
        if m.get('ClassicEndpoint') is not None:
            self.classic_endpoint = m.get('ClassicEndpoint')
        if m.get('EnableDlqTtl') is not None:
            self.enable_dlq_ttl = m.get('EnableDlqTtl')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InvisibleTime') is not None:
            self.invisible_time = m.get('InvisibleTime')
        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')
        if m.get('MaxBindingCount') is not None:
            self.max_binding_count = m.get('MaxBindingCount')
        if m.get('MaxConnectionChannelCount') is not None:
            self.max_connection_channel_count = m.get('MaxConnectionChannelCount')
        if m.get('MaxConnectionCount') is not None:
            self.max_connection_count = m.get('MaxConnectionCount')
        if m.get('MaxConsumeRetryTime') is not None:
            self.max_consume_retry_time = m.get('MaxConsumeRetryTime')
        if m.get('MaxEIPTPS') is not None:
            self.max_eiptps = m.get('MaxEIPTPS')
        if m.get('MaxExchangeCount') is not None:
            self.max_exchange_count = m.get('MaxExchangeCount')
        if m.get('MaxMsgBodyByte') is not None:
            self.max_msg_body_byte = m.get('MaxMsgBodyByte')
        if m.get('MaxMsgDelayHour') is not None:
            self.max_msg_delay_hour = m.get('MaxMsgDelayHour')
        if m.get('MaxMsgTraceTime') is not None:
            self.max_msg_trace_time = m.get('MaxMsgTraceTime')
        if m.get('MaxQueue') is not None:
            self.max_queue = m.get('MaxQueue')
        if m.get('MaxQueueConsumerCount') is not None:
            self.max_queue_consumer_count = m.get('MaxQueueConsumerCount')
        if m.get('MaxRetryInterval') is not None:
            self.max_retry_interval = m.get('MaxRetryInterval')
        if m.get('MaxRetryTimes') is not None:
            self.max_retry_times = m.get('MaxRetryTimes')
        if m.get('MaxTPS') is not None:
            self.max_tps = m.get('MaxTPS')
        if m.get('MaxVhost') is not None:
            self.max_vhost = m.get('MaxVhost')
        if m.get('OrderCreate') is not None:
            self.order_create = m.get('OrderCreate')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PrivateEndpoint') is not None:
            self.private_endpoint = m.get('PrivateEndpoint')
        if m.get('PublicEndpoint') is not None:
            self.public_endpoint = m.get('PublicEndpoint')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServerlessRate') is not None:
            self.serverless_rate = m.get('ServerlessRate')
        if m.get('ServerlessSwitch') is not None:
            self.serverless_switch = m.get('ServerlessSwitch')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('SupportEIP') is not None:
            self.support_eip = m.get('SupportEIP')
        if m.get('SupportMsgTrace') is not None:
            self.support_msg_trace = m.get('SupportMsgTrace')
        if m.get('SupportOpenSourceAuth') is not None:
            self.support_open_source_auth = m.get('SupportOpenSourceAuth')
        if m.get('Tags') is not None:
            temp_model = InstancePreivewResponseBodyDataInstancesInstancesVOTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UsedQueue') is not None:
            self.used_queue = m.get('UsedQueue')
        if m.get('UsedVhost') is not None:
            self.used_vhost = m.get('UsedVhost')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class InstancePreivewResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        instances_vo: List[InstancePreivewResponseBodyDataInstancesInstancesVO] = None,
    ):
        self.instances_vo = instances_vo

    def validate(self):
        if self.instances_vo:
            for k in self.instances_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstancesVO'] = []
        if self.instances_vo is not None:
            for k in self.instances_vo:
                result['InstancesVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances_vo = []
        if m.get('InstancesVO') is not None:
            for k in m.get('InstancesVO'):
                temp_model = InstancePreivewResponseBodyDataInstancesInstancesVO()
                self.instances_vo.append(temp_model.from_map(k))
        return self


class InstancePreivewResponseBodyData(TeaModel):
    def __init__(
        self,
        exchange_num: int = None,
        instance_num: int = None,
        instances: InstancePreivewResponseBodyDataInstances = None,
        queue_num: int = None,
        vhost_num: int = None,
    ):
        self.exchange_num = exchange_num
        self.instance_num = instance_num
        self.instances = instances
        self.queue_num = queue_num
        self.vhost_num = vhost_num

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exchange_num is not None:
            result['ExchangeNum'] = self.exchange_num
        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.queue_num is not None:
            result['QueueNum'] = self.queue_num
        if self.vhost_num is not None:
            result['VhostNum'] = self.vhost_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExchangeNum') is not None:
            self.exchange_num = m.get('ExchangeNum')
        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')
        if m.get('Instances') is not None:
            temp_model = InstancePreivewResponseBodyDataInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('QueueNum') is not None:
            self.queue_num = m.get('QueueNum')
        if m.get('VhostNum') is not None:
            self.vhost_num = m.get('VhostNum')
        return self


class InstancePreivewResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: InstancePreivewResponseBodyData = None,
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
            temp_model = InstancePreivewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InstancePreivewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstancePreivewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = InstancePreivewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangeRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        exchange_name_prefix: str = None,
        instance_id: str = None,
        page_size: int = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        self.exchange_name_prefix = exchange_name_prefix
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.exchange_name_prefix is not None:
            result['ExchangeNamePrefix'] = self.exchange_name_prefix
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ExchangeNamePrefix') is not None:
            self.exchange_name_prefix = m.get('ExchangeNamePrefix')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ListExchangeResponseBodyDataVoListExchangVO(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        auto_delete: bool = None,
        can_delete: bool = None,
        create_time: int = None,
        exchange_type: int = None,
        internal: bool = None,
        name: str = None,
        vhost_name: str = None,
    ):
        self.attributes = attributes
        self.auto_delete = auto_delete
        self.can_delete = can_delete
        self.create_time = create_time
        self.exchange_type = exchange_type
        self.internal = internal
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
        if self.auto_delete is not None:
            result['AutoDelete'] = self.auto_delete
        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.exchange_type is not None:
            result['ExchangeType'] = self.exchange_type
        if self.internal is not None:
            result['Internal'] = self.internal
        if self.name is not None:
            result['Name'] = self.name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('AutoDelete') is not None:
            self.auto_delete = m.get('AutoDelete')
        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExchangeType') is not None:
            self.exchange_type = m.get('ExchangeType')
        if m.get('Internal') is not None:
            self.internal = m.get('Internal')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ListExchangeResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        exchang_vo: List[ListExchangeResponseBodyDataVoListExchangVO] = None,
    ):
        self.exchang_vo = exchang_vo

    def validate(self):
        if self.exchang_vo:
            for k in self.exchang_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExchangVO'] = []
        if self.exchang_vo is not None:
            for k in self.exchang_vo:
                result['ExchangVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exchang_vo = []
        if m.get('ExchangVO') is not None:
            for k in m.get('ExchangVO'):
                temp_model = ListExchangeResponseBodyDataVoListExchangVO()
                self.exchang_vo.append(temp_model.from_map(k))
        return self


class ListExchangeResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: ListExchangeResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = ListExchangeResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class ListExchangeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListExchangeResponseBodyData = None,
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
            temp_model = ListExchangeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListExchangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExchangeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListExchangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangeDownstreamBindingsRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        exchange_name: str = None,
        instance_id: str = None,
        page_size: int = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.exchange_name = exchange_name
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ListExchangeDownstreamBindingsResponseBodyDataVoListBindingVO(TeaModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: int = None,
        dst_name: str = None,
        src_name: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.dst_name = dst_name
        self.src_name = src_name

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
        if self.dst_name is not None:
            result['DstName'] = self.dst_name
        if self.src_name is not None:
            result['SrcName'] = self.src_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DstName') is not None:
            self.dst_name = m.get('DstName')
        if m.get('SrcName') is not None:
            self.src_name = m.get('SrcName')
        return self


class ListExchangeDownstreamBindingsResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        binding_vo: List[ListExchangeDownstreamBindingsResponseBodyDataVoListBindingVO] = None,
    ):
        self.binding_vo = binding_vo

    def validate(self):
        if self.binding_vo:
            for k in self.binding_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindingVO'] = []
        if self.binding_vo is not None:
            for k in self.binding_vo:
                result['BindingVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.binding_vo = []
        if m.get('BindingVO') is not None:
            for k in m.get('BindingVO'):
                temp_model = ListExchangeDownstreamBindingsResponseBodyDataVoListBindingVO()
                self.binding_vo.append(temp_model.from_map(k))
        return self


class ListExchangeDownstreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        vo_list: ListExchangeDownstreamBindingsResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VoList') is not None:
            temp_model = ListExchangeDownstreamBindingsResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class ListExchangeDownstreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListExchangeDownstreamBindingsResponseBodyData = None,
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
            temp_model = ListExchangeDownstreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListExchangeDownstreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExchangeDownstreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListExchangeDownstreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExchangeUpstreamBindingsRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        exchange_name: str = None,
        instance_id: str = None,
        page_size: int = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.exchange_name = exchange_name
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ListExchangeUpstreamBindingsResponseBodyDataVoListBindingVO(TeaModel):
    def __init__(
        self,
        argument: str = None,
        bind_type: int = None,
        binding_key: str = None,
        dst_name: str = None,
        src_name: str = None,
    ):
        self.argument = argument
        self.bind_type = bind_type
        self.binding_key = binding_key
        self.dst_name = dst_name
        self.src_name = src_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.argument is not None:
            result['Argument'] = self.argument
        if self.bind_type is not None:
            result['BindType'] = self.bind_type
        if self.binding_key is not None:
            result['BindingKey'] = self.binding_key
        if self.dst_name is not None:
            result['DstName'] = self.dst_name
        if self.src_name is not None:
            result['SrcName'] = self.src_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindType') is not None:
            self.bind_type = m.get('BindType')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('DstName') is not None:
            self.dst_name = m.get('DstName')
        if m.get('SrcName') is not None:
            self.src_name = m.get('SrcName')
        return self


class ListExchangeUpstreamBindingsResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        binding_vo: List[ListExchangeUpstreamBindingsResponseBodyDataVoListBindingVO] = None,
    ):
        self.binding_vo = binding_vo

    def validate(self):
        if self.binding_vo:
            for k in self.binding_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindingVO'] = []
        if self.binding_vo is not None:
            for k in self.binding_vo:
                result['BindingVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.binding_vo = []
        if m.get('BindingVO') is not None:
            for k in m.get('BindingVO'):
                temp_model = ListExchangeUpstreamBindingsResponseBodyDataVoListBindingVO()
                self.binding_vo.append(temp_model.from_map(k))
        return self


class ListExchangeUpstreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        vo_list: ListExchangeUpstreamBindingsResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VoList') is not None:
            temp_model = ListExchangeUpstreamBindingsResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class ListExchangeUpstreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListExchangeUpstreamBindingsResponseBodyData = None,
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
            temp_model = ListExchangeUpstreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListExchangeUpstreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExchangeUpstreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListExchangeUpstreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class ListInstanceResponseBodyDataInstancesTagsTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListInstanceResponseBodyDataInstancesTags(TeaModel):
    def __init__(
        self,
        tags: List[ListInstanceResponseBodyDataInstancesTagsTags] = None,
    ):
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListInstanceResponseBodyDataInstancesTagsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListInstanceResponseBodyDataInstances(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        classic_endpoint: str = None,
        expire: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_type: str = None,
        max_eiptps: int = None,
        max_queue: int = None,
        max_tps: int = None,
        max_vhost: int = None,
        order_create: int = None,
        order_type: str = None,
        private_endpoint: str = None,
        public_endpoint: str = None,
        status: str = None,
        storage_size: int = None,
        support_eip: bool = None,
        tags: ListInstanceResponseBodyDataInstancesTags = None,
    ):
        self.auto_renew = auto_renew
        self.classic_endpoint = classic_endpoint
        self.expire = expire
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.max_eiptps = max_eiptps
        self.max_queue = max_queue
        self.max_tps = max_tps
        self.max_vhost = max_vhost
        self.order_create = order_create
        self.order_type = order_type
        self.private_endpoint = private_endpoint
        self.public_endpoint = public_endpoint
        self.status = status
        self.storage_size = storage_size
        self.support_eip = support_eip
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.classic_endpoint is not None:
            result['ClassicEndpoint'] = self.classic_endpoint
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_eiptps is not None:
            result['MaxEIPTPS'] = self.max_eiptps
        if self.max_queue is not None:
            result['MaxQueue'] = self.max_queue
        if self.max_tps is not None:
            result['MaxTPS'] = self.max_tps
        if self.max_vhost is not None:
            result['MaxVhost'] = self.max_vhost
        if self.order_create is not None:
            result['OrderCreate'] = self.order_create
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
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClassicEndpoint') is not None:
            self.classic_endpoint = m.get('ClassicEndpoint')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxEIPTPS') is not None:
            self.max_eiptps = m.get('MaxEIPTPS')
        if m.get('MaxQueue') is not None:
            self.max_queue = m.get('MaxQueue')
        if m.get('MaxTPS') is not None:
            self.max_tps = m.get('MaxTPS')
        if m.get('MaxVhost') is not None:
            self.max_vhost = m.get('MaxVhost')
        if m.get('OrderCreate') is not None:
            self.order_create = m.get('OrderCreate')
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
        if m.get('Tags') is not None:
            temp_model = ListInstanceResponseBodyDataInstancesTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class ListInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        instances: List[ListInstanceResponseBodyDataInstances] = None,
    ):
        self.instances = instances

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListInstanceResponseBodyData = None,
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
            temp_model = ListInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceAlarmRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetailsAlarmDetail(TeaModel):
    def __init__(
        self,
        alert_state: str = None,
        comparison_operator: str = None,
        contact_groups: str = None,
        dimensions: str = None,
        effective_interval: str = None,
        enable_state: bool = None,
        group_id: str = None,
        group_name: str = None,
        mail_subject: str = None,
        metric_name: str = None,
        namespace: str = None,
        no_effective_interval: str = None,
        period: str = None,
        resources: str = None,
        rule_id: str = None,
        rule_name: str = None,
        silence_time: str = None,
        statistics: str = None,
        threshold: str = None,
        times: str = None,
        webhook: str = None,
    ):
        self.alert_state = alert_state
        self.comparison_operator = comparison_operator
        self.contact_groups = contact_groups
        self.dimensions = dimensions
        self.effective_interval = effective_interval
        self.enable_state = enable_state
        self.group_id = group_id
        self.group_name = group_name
        self.mail_subject = mail_subject
        self.metric_name = metric_name
        self.namespace = namespace
        self.no_effective_interval = no_effective_interval
        self.period = period
        self.resources = resources
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.silence_time = silence_time
        self.statistics = statistics
        self.threshold = threshold
        self.times = times
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_state is not None:
            result['AlertState'] = self.alert_state
        if self.comparison_operator is not None:
            result['ComparisonOperator'] = self.comparison_operator
        if self.contact_groups is not None:
            result['ContactGroups'] = self.contact_groups
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.effective_interval is not None:
            result['EffectiveInterval'] = self.effective_interval
        if self.enable_state is not None:
            result['EnableState'] = self.enable_state
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.mail_subject is not None:
            result['MailSubject'] = self.mail_subject
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.no_effective_interval is not None:
            result['NoEffectiveInterval'] = self.no_effective_interval
        if self.period is not None:
            result['Period'] = self.period
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.silence_time is not None:
            result['SilenceTime'] = self.silence_time
        if self.statistics is not None:
            result['Statistics'] = self.statistics
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.times is not None:
            result['Times'] = self.times
        if self.webhook is not None:
            result['Webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertState') is not None:
            self.alert_state = m.get('AlertState')
        if m.get('ComparisonOperator') is not None:
            self.comparison_operator = m.get('ComparisonOperator')
        if m.get('ContactGroups') is not None:
            self.contact_groups = m.get('ContactGroups')
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EffectiveInterval') is not None:
            self.effective_interval = m.get('EffectiveInterval')
        if m.get('EnableState') is not None:
            self.enable_state = m.get('EnableState')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('MailSubject') is not None:
            self.mail_subject = m.get('MailSubject')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('NoEffectiveInterval') is not None:
            self.no_effective_interval = m.get('NoEffectiveInterval')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('SilenceTime') is not None:
            self.silence_time = m.get('SilenceTime')
        if m.get('Statistics') is not None:
            self.statistics = m.get('Statistics')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        if m.get('Webhook') is not None:
            self.webhook = m.get('Webhook')
        return self


class ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetails(TeaModel):
    def __init__(
        self,
        alarm_detail: List[ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetailsAlarmDetail] = None,
    ):
        self.alarm_detail = alarm_detail

    def validate(self):
        if self.alarm_detail:
            for k in self.alarm_detail:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmDetail'] = []
        if self.alarm_detail is not None:
            for k in self.alarm_detail:
                result['AlarmDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_detail = []
        if m.get('AlarmDetail') is not None:
            for k in m.get('AlarmDetail'):
                temp_model = ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetailsAlarmDetail()
                self.alarm_detail.append(temp_model.from_map(k))
        return self


class ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVO(TeaModel):
    def __init__(
        self,
        alarm_count: int = None,
        alarm_details: ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetails = None,
        has_config_alarm: bool = None,
    ):
        self.alarm_count = alarm_count
        self.alarm_details = alarm_details
        self.has_config_alarm = has_config_alarm

    def validate(self):
        if self.alarm_details:
            self.alarm_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count
        if self.alarm_details is not None:
            result['AlarmDetails'] = self.alarm_details.to_map()
        if self.has_config_alarm is not None:
            result['HasConfigAlarm'] = self.has_config_alarm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')
        if m.get('AlarmDetails') is not None:
            temp_model = ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVOAlarmDetails()
            self.alarm_details = temp_model.from_map(m['AlarmDetails'])
        if m.get('HasConfigAlarm') is not None:
            self.has_config_alarm = m.get('HasConfigAlarm')
        return self


class ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVO(TeaModel):
    def __init__(
        self,
        alarm_vo: ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVO = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.alarm_vo = alarm_vo
        self.instance_id = instance_id
        self.instance_name = instance_name

    def validate(self):
        if self.alarm_vo:
            self.alarm_vo.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_vo is not None:
            result['AlarmVO'] = self.alarm_vo.to_map()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmVO') is not None:
            temp_model = ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVOAlarmVO()
            self.alarm_vo = temp_model.from_map(m['AlarmVO'])
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class ListInstanceAlarmResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        commodity_instance_alarm_vo: List[ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVO] = None,
    ):
        self.commodity_instance_alarm_vo = commodity_instance_alarm_vo

    def validate(self):
        if self.commodity_instance_alarm_vo:
            for k in self.commodity_instance_alarm_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CommodityInstanceAlarmVO'] = []
        if self.commodity_instance_alarm_vo is not None:
            for k in self.commodity_instance_alarm_vo:
                result['CommodityInstanceAlarmVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodity_instance_alarm_vo = []
        if m.get('CommodityInstanceAlarmVO') is not None:
            for k in m.get('CommodityInstanceAlarmVO'):
                temp_model = ListInstanceAlarmResponseBodyDataVoListCommodityInstanceAlarmVO()
                self.commodity_instance_alarm_vo.append(temp_model.from_map(k))
        return self


class ListInstanceAlarmResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: ListInstanceAlarmResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = ListInstanceAlarmResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class ListInstanceAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListInstanceAlarmResponseBodyData = None,
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
            temp_model = ListInstanceAlarmResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstanceAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceAlarmResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListInstanceAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogstoreRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        project_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        return self


class ListLogstoreResponseBodyData(TeaModel):
    def __init__(
        self,
        logstores: List[str] = None,
    ):
        self.logstores = logstores

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstores is not None:
            result['Logstores'] = self.logstores
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstores') is not None:
            self.logstores = m.get('Logstores')
        return self


class ListLogstoreResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListLogstoreResponseBodyData = None,
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
            temp_model = ListLogstoreResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListLogstoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogstoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListLogstoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class ListProjectResponseBodyData(TeaModel):
    def __init__(
        self,
        projects: List[str] = None,
    ):
        self.projects = projects

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.projects is not None:
            result['Projects'] = self.projects
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Projects') is not None:
            self.projects = m.get('Projects')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListProjectResponseBodyData = None,
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
            temp_model = ListProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        instance_id: str = None,
        page_size: int = None,
        queue_name_prefix: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        self.queue_name_prefix = queue_name_prefix
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name_prefix is not None:
            result['QueueNamePrefix'] = self.queue_name_prefix
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueNamePrefix') is not None:
            self.queue_name_prefix = m.get('QueueNamePrefix')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ListQueueResponseBodyDataVoListQueueVO(TeaModel):
    def __init__(
        self,
        accumulation_count: int = None,
        attributes: Dict[str, Any] = None,
        auto_delete: bool = None,
        can_delete: bool = None,
        create_time: int = None,
        durable: bool = None,
        exclusive: bool = None,
        last_consume_time: int = None,
        name: str = None,
        vhost_name: str = None,
    ):
        self.accumulation_count = accumulation_count
        self.attributes = attributes
        self.auto_delete = auto_delete
        self.can_delete = can_delete
        self.create_time = create_time
        self.durable = durable
        self.exclusive = exclusive
        self.last_consume_time = last_consume_time
        self.name = name
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accumulation_count is not None:
            result['AccumulationCount'] = self.accumulation_count
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.auto_delete is not None:
            result['AutoDelete'] = self.auto_delete
        if self.can_delete is not None:
            result['CanDelete'] = self.can_delete
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.durable is not None:
            result['Durable'] = self.durable
        if self.exclusive is not None:
            result['Exclusive'] = self.exclusive
        if self.last_consume_time is not None:
            result['LastConsumeTime'] = self.last_consume_time
        if self.name is not None:
            result['Name'] = self.name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccumulationCount') is not None:
            self.accumulation_count = m.get('AccumulationCount')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('AutoDelete') is not None:
            self.auto_delete = m.get('AutoDelete')
        if m.get('CanDelete') is not None:
            self.can_delete = m.get('CanDelete')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Durable') is not None:
            self.durable = m.get('Durable')
        if m.get('Exclusive') is not None:
            self.exclusive = m.get('Exclusive')
        if m.get('LastConsumeTime') is not None:
            self.last_consume_time = m.get('LastConsumeTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ListQueueResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        queue_vo: List[ListQueueResponseBodyDataVoListQueueVO] = None,
    ):
        self.queue_vo = queue_vo

    def validate(self):
        if self.queue_vo:
            for k in self.queue_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['QueueVO'] = []
        if self.queue_vo is not None:
            for k in self.queue_vo:
                result['QueueVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.queue_vo = []
        if m.get('QueueVO') is not None:
            for k in m.get('QueueVO'):
                temp_model = ListQueueResponseBodyDataVoListQueueVO()
                self.queue_vo.append(temp_model.from_map(k))
        return self


class ListQueueResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: ListQueueResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = ListQueueResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class ListQueueResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListQueueResponseBodyData = None,
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
            temp_model = ListQueueResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQueueUpstreamBindingsRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        current_page: int = None,
        instance_id: str = None,
        page_size: int = None,
        queue_name: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class ListQueueUpstreamBindingsResponseBodyDataVoListBindingVO(TeaModel):
    def __init__(
        self,
        argument: str = None,
        binding_key: str = None,
        binding_type: int = None,
        dst_name: str = None,
        src_name: str = None,
    ):
        self.argument = argument
        self.binding_key = binding_key
        self.binding_type = binding_type
        self.dst_name = dst_name
        self.src_name = src_name

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
        if self.dst_name is not None:
            result['DstName'] = self.dst_name
        if self.src_name is not None:
            result['SrcName'] = self.src_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Argument') is not None:
            self.argument = m.get('Argument')
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('DstName') is not None:
            self.dst_name = m.get('DstName')
        if m.get('SrcName') is not None:
            self.src_name = m.get('SrcName')
        return self


class ListQueueUpstreamBindingsResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        binding_vo: List[ListQueueUpstreamBindingsResponseBodyDataVoListBindingVO] = None,
    ):
        self.binding_vo = binding_vo

    def validate(self):
        if self.binding_vo:
            for k in self.binding_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BindingVO'] = []
        if self.binding_vo is not None:
            for k in self.binding_vo:
                result['BindingVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.binding_vo = []
        if m.get('BindingVO') is not None:
            for k in m.get('BindingVO'):
                temp_model = ListQueueUpstreamBindingsResponseBodyDataVoListBindingVO()
                self.binding_vo.append(temp_model.from_map(k))
        return self


class ListQueueUpstreamBindingsResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        vo_list: ListQueueUpstreamBindingsResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('VoList') is not None:
            temp_model = ListQueueUpstreamBindingsResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class ListQueueUpstreamBindingsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListQueueUpstreamBindingsResponseBodyData = None,
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
            temp_model = ListQueueUpstreamBindingsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListQueueUpstreamBindingsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListQueueUpstreamBindingsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListQueueUpstreamBindingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListStaticAccountsRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListStaticAccountsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Dict[str, Any] = None,
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


class ListStaticAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListStaticAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListStaticAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVhostRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        vhost_name_prefix: str = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.vhost_name_prefix = vhost_name_prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vhost_name_prefix is not None:
            result['VhostNamePrefix'] = self.vhost_name_prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VhostNamePrefix') is not None:
            self.vhost_name_prefix = m.get('VhostNamePrefix')
        return self


class ListVhostResponseBodyDataVhosts(TeaModel):
    def __init__(
        self,
        channel_num: int = None,
        connection_num: int = None,
        name: str = None,
    ):
        self.channel_num = channel_num
        self.connection_num = connection_num
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_num is not None:
            result['ChannelNum'] = self.channel_num
        if self.connection_num is not None:
            result['ConnectionNum'] = self.connection_num
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelNum') is not None:
            self.channel_num = m.get('ChannelNum')
        if m.get('ConnectionNum') is not None:
            self.connection_num = m.get('ConnectionNum')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListVhostResponseBodyData(TeaModel):
    def __init__(
        self,
        vhosts: List[ListVhostResponseBodyDataVhosts] = None,
    ):
        self.vhosts = vhosts

    def validate(self):
        if self.vhosts:
            for k in self.vhosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Vhosts'] = []
        if self.vhosts is not None:
            for k in self.vhosts:
                result['Vhosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vhosts = []
        if m.get('Vhosts') is not None:
            for k in m.get('Vhosts'):
                temp_model = ListVhostResponseBodyDataVhosts()
                self.vhosts.append(temp_model.from_map(k))
        return self


class ListVhostResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: ListVhostResponseBodyData = None,
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
            temp_model = ListVhostResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListVhostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVhostResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListVhostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MetadataRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
    ):
        self.console_session_id = console_session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        return self


class MetadataResponseBodyData(TeaModel):
    def __init__(
        self,
        endpoint: str = None,
        has_pretend_permission: bool = None,
        internal_endpoint: str = None,
        pretend_user_id: str = None,
        user_status: int = None,
    ):
        self.endpoint = endpoint
        self.has_pretend_permission = has_pretend_permission
        self.internal_endpoint = internal_endpoint
        self.pretend_user_id = pretend_user_id
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.has_pretend_permission is not None:
            result['HasPretendPermission'] = self.has_pretend_permission
        if self.internal_endpoint is not None:
            result['InternalEndpoint'] = self.internal_endpoint
        if self.pretend_user_id is not None:
            result['PretendUserId'] = self.pretend_user_id
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('HasPretendPermission') is not None:
            self.has_pretend_permission = m.get('HasPretendPermission')
        if m.get('InternalEndpoint') is not None:
            self.internal_endpoint = m.get('InternalEndpoint')
        if m.get('PretendUserId') is not None:
            self.pretend_user_id = m.get('PretendUserId')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        return self


class MetadataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: MetadataResponseBodyData = None,
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
            temp_model = MetadataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MetadataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = MetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurgeQueueRequest(TeaModel):
    def __init__(
        self,
        collina: str = None,
        console_session_id: str = None,
        instance_id: str = None,
        queue_name: str = None,
        queue_names: Dict[str, Any] = None,
        umid_token: str = None,
        vhost_name: str = None,
    ):
        self.collina = collina
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.queue_names = queue_names
        self.umid_token = umid_token
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collina is not None:
            result['Collina'] = self.collina
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.queue_names is not None:
            result['QueueNames'] = self.queue_names
        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collina') is not None:
            self.collina = m.get('Collina')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('QueueNames') is not None:
            self.queue_names = m.get('QueueNames')
        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class PurgeQueueShrinkRequest(TeaModel):
    def __init__(
        self,
        collina: str = None,
        console_session_id: str = None,
        instance_id: str = None,
        queue_name: str = None,
        queue_names_shrink: str = None,
        umid_token: str = None,
        vhost_name: str = None,
    ):
        self.collina = collina
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.queue_name = queue_name
        self.queue_names_shrink = queue_names_shrink
        self.umid_token = umid_token
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.collina is not None:
            result['Collina'] = self.collina
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.queue_names_shrink is not None:
            result['QueueNames'] = self.queue_names_shrink
        if self.umid_token is not None:
            result['UmidToken'] = self.umid_token
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collina') is not None:
            self.collina = m.get('Collina')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('QueueNames') is not None:
            self.queue_names_shrink = m.get('QueueNames')
        if m.get('UmidToken') is not None:
            self.umid_token = m.get('UmidToken')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class PurgeQueueResponseBody(TeaModel):
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


class PurgeQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PurgeQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = PurgeQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageByMessageIdRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        console_session_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        message_id: str = None,
        page_size: int = None,
        queue_name: str = None,
        vhost_name: str = None,
    ):
        self.begin_time = begin_time
        self.console_session_id = console_session_id
        self.current_page = current_page
        self.end_time = end_time
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.message_id = message_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class QueryMessageByMessageIdResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        body: str = None,
        cluster_id: str = None,
        content_encoding: str = None,
        content_type: str = None,
        correlation_id: str = None,
        delivery_mode: int = None,
        exchange_name: str = None,
        expiration: str = None,
        headers: str = None,
        immediate: bool = None,
        mandatory: bool = None,
        message_id: str = None,
        priority: int = None,
        process_token: str = None,
        reconsume_times: int = None,
        reply_to: str = None,
        routing_key: str = None,
        store_timestamp: int = None,
        timestamp: int = None,
        type: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.body = body
        self.cluster_id = cluster_id
        self.content_encoding = content_encoding
        self.content_type = content_type
        self.correlation_id = correlation_id
        self.delivery_mode = delivery_mode
        self.exchange_name = exchange_name
        self.expiration = expiration
        self.headers = headers
        self.immediate = immediate
        self.mandatory = mandatory
        self.message_id = message_id
        self.priority = priority
        self.process_token = process_token
        self.reconsume_times = reconsume_times
        self.reply_to = reply_to
        self.routing_key = routing_key
        self.store_timestamp = store_timestamp
        self.timestamp = timestamp
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.body is not None:
            result['Body'] = self.body
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.correlation_id is not None:
            result['CorrelationId'] = self.correlation_id
        if self.delivery_mode is not None:
            result['DeliveryMode'] = self.delivery_mode
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.immediate is not None:
            result['Immediate'] = self.immediate
        if self.mandatory is not None:
            result['Mandatory'] = self.mandatory
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.process_token is not None:
            result['ProcessToken'] = self.process_token
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.reply_to is not None:
            result['ReplyTo'] = self.reply_to
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CorrelationId') is not None:
            self.correlation_id = m.get('CorrelationId')
        if m.get('DeliveryMode') is not None:
            self.delivery_mode = m.get('DeliveryMode')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Immediate') is not None:
            self.immediate = m.get('Immediate')
        if m.get('Mandatory') is not None:
            self.mandatory = m.get('Mandatory')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ProcessToken') is not None:
            self.process_token = m.get('ProcessToken')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('ReplyTo') is not None:
            self.reply_to = m.get('ReplyTo')
        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryMessageByMessageIdResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        task_id: str = None,
        total_count: int = None,
        vo_list: List[QueryMessageByMessageIdResponseBodyDataVoList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.task_id = task_id
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            for k in self.vo_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VoList'] = []
        if self.vo_list is not None:
            for k in self.vo_list:
                result['VoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vo_list = []
        if m.get('VoList') is not None:
            for k in m.get('VoList'):
                temp_model = QueryMessageByMessageIdResponseBodyDataVoList()
                self.vo_list.append(temp_model.from_map(k))
        return self


class QueryMessageByMessageIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryMessageByMessageIdResponseBodyData = None,
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
            temp_model = QueryMessageByMessageIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMessageByMessageIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMessageByMessageIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryMessageByMessageIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageByQueueNameRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        console_session_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        page_size: int = None,
        queue_name: str = None,
        task_id: str = None,
        vhost_name: str = None,
    ):
        # This parameter is required.
        self.begin_time = begin_time
        self.console_session_id = console_session_id
        # This parameter is required.
        self.current_page = current_page
        # This parameter is required.
        self.end_time = end_time
        self.instance_id = instance_id
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.queue_name = queue_name
        self.task_id = task_id
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class QueryMessageByQueueNameResponseBodyDataVoListAmqpMessageVO(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        body: str = None,
        cluster_id: str = None,
        content_encoding: str = None,
        content_type: str = None,
        correlation_id: str = None,
        delivery_mode: int = None,
        exchange_name: str = None,
        expiration: str = None,
        headers: str = None,
        immediate: bool = None,
        mandatory: bool = None,
        message_id: str = None,
        priority: int = None,
        process_token: str = None,
        reconsume_times: int = None,
        reply_to: str = None,
        routing_key: str = None,
        store_timestamp: int = None,
        timestamp: int = None,
        type: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.body = body
        self.cluster_id = cluster_id
        self.content_encoding = content_encoding
        self.content_type = content_type
        self.correlation_id = correlation_id
        self.delivery_mode = delivery_mode
        self.exchange_name = exchange_name
        self.expiration = expiration
        self.headers = headers
        self.immediate = immediate
        self.mandatory = mandatory
        self.message_id = message_id
        self.priority = priority
        self.process_token = process_token
        self.reconsume_times = reconsume_times
        self.reply_to = reply_to
        self.routing_key = routing_key
        self.store_timestamp = store_timestamp
        self.timestamp = timestamp
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.body is not None:
            result['Body'] = self.body
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.correlation_id is not None:
            result['CorrelationId'] = self.correlation_id
        if self.delivery_mode is not None:
            result['DeliveryMode'] = self.delivery_mode
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.headers is not None:
            result['Headers'] = self.headers
        if self.immediate is not None:
            result['Immediate'] = self.immediate
        if self.mandatory is not None:
            result['Mandatory'] = self.mandatory
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.process_token is not None:
            result['ProcessToken'] = self.process_token
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.reply_to is not None:
            result['ReplyTo'] = self.reply_to
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CorrelationId') is not None:
            self.correlation_id = m.get('CorrelationId')
        if m.get('DeliveryMode') is not None:
            self.delivery_mode = m.get('DeliveryMode')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('Headers') is not None:
            self.headers = m.get('Headers')
        if m.get('Immediate') is not None:
            self.immediate = m.get('Immediate')
        if m.get('Mandatory') is not None:
            self.mandatory = m.get('Mandatory')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ProcessToken') is not None:
            self.process_token = m.get('ProcessToken')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('ReplyTo') is not None:
            self.reply_to = m.get('ReplyTo')
        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryMessageByQueueNameResponseBodyDataVoList(TeaModel):
    def __init__(
        self,
        amqp_message_vo: List[QueryMessageByQueueNameResponseBodyDataVoListAmqpMessageVO] = None,
    ):
        self.amqp_message_vo = amqp_message_vo

    def validate(self):
        if self.amqp_message_vo:
            for k in self.amqp_message_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AmqpMessageVO'] = []
        if self.amqp_message_vo is not None:
            for k in self.amqp_message_vo:
                result['AmqpMessageVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.amqp_message_vo = []
        if m.get('AmqpMessageVO') is not None:
            for k in m.get('AmqpMessageVO'):
                temp_model = QueryMessageByQueueNameResponseBodyDataVoListAmqpMessageVO()
                self.amqp_message_vo.append(temp_model.from_map(k))
        return self


class QueryMessageByQueueNameResponseBodyData(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        task_id: str = None,
        total_count: int = None,
        vo_list: QueryMessageByQueueNameResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.task_id = task_id
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('VoList') is not None:
            temp_model = QueryMessageByQueueNameResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m['VoList'])
        return self


class QueryMessageByQueueNameResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: QueryMessageByQueueNameResponseBodyData = None,
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
            temp_model = QueryMessageByQueueNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMessageByQueueNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMessageByQueueNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = QueryMessageByQueueNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseInstanceRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ReleaseInstanceResponseBody(TeaModel):
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


class ReleaseInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReleaseInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ReleaseInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        console_session_id: str = None,
        exchange_name: str = None,
        instance_id: str = None,
        message_id: str = None,
        props: str = None,
        routing_key: str = None,
        vhost_name: str = None,
    ):
        # This parameter is required.
        self.body = body
        self.console_session_id = console_session_id
        # This parameter is required.
        self.exchange_name = exchange_name
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.message_id = message_id
        self.props = props
        # This parameter is required.
        self.routing_key = routing_key
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.props is not None:
            result['Props'] = self.props
        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Props') is not None:
            self.props = m.get('Props')
        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class SendMessageResponseBody(TeaModel):
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
        # Id of the request
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


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageCopyRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        process_token: str = None,
        queue_name: str = None,
        vhost_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.process_token = process_token
        # This parameter is required.
        self.queue_name = queue_name
        # This parameter is required.
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.process_token is not None:
            result['ProcessToken'] = self.process_token
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProcessToken') is not None:
            self.process_token = m.get('ProcessToken')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class SendMessageCopyResponseBody(TeaModel):
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


class SendMessageCopyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageCopyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SendMessageCopyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindRequest(TeaModel):
    def __init__(
        self,
        binding_key: str = None,
        binding_type: int = None,
        console_session_id: str = None,
        dst_name: str = None,
        instance_id: str = None,
        src_name: str = None,
        vhost_name: str = None,
    ):
        self.binding_key = binding_key
        # This parameter is required.
        self.binding_type = binding_type
        self.console_session_id = console_session_id
        # This parameter is required.
        self.dst_name = dst_name
        self.instance_id = instance_id
        # This parameter is required.
        self.src_name = src_name
        # This parameter is required.
        self.vhost_name = vhost_name

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
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.dst_name is not None:
            result['DstName'] = self.dst_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.src_name is not None:
            result['SrcName'] = self.src_name
        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingKey') is not None:
            self.binding_key = m.get('BindingKey')
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('DstName') is not None:
            self.dst_name = m.get('DstName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SrcName') is not None:
            self.src_name = m.get('SrcName')
        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')
        return self


class UnbindResponseBody(TeaModel):
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


class UnbindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UnbindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class UpdateInstanceResponseBody(TeaModel):
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


class UpdateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRetryStrategyRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        retry_interval: int = None,
        retry_times: int = None,
    ):
        self.console_session_id = console_session_id
        self.instance_id = instance_id
        self.retry_interval = retry_interval
        self.retry_times = retry_times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval
        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')
        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')
        return self


class UpdateInstanceRetryStrategyResponseBody(TeaModel):
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


class UpdateInstanceRetryStrategyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateInstanceRetryStrategyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateInstanceRetryStrategyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServerlessSwitchRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
        serverless_switch: bool = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.serverless_switch = serverless_switch

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.serverless_switch is not None:
            result['ServerlessSwitch'] = self.serverless_switch
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ServerlessSwitch') is not None:
            self.serverless_switch = m.get('ServerlessSwitch')
        return self


class UpdateServerlessSwitchResponseBody(TeaModel):
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


class UpdateServerlessSwitchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServerlessSwitchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateServerlessSwitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeLimitsRequest(TeaModel):
    def __init__(
        self,
        console_session_id: str = None,
        instance_id: str = None,
    ):
        self.console_session_id = console_session_id
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.console_session_id is not None:
            result['ConsoleSessionId'] = self.console_session_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsoleSessionId') is not None:
            self.console_session_id = m.get('ConsoleSessionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpgradeLimitsResponseBody(TeaModel):
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


class UpgradeLimitsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeLimitsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpgradeLimitsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


