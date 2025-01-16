# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BindAliasRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        app_key: int = None,
        device_id: str = None,
    ):
        # This parameter is required.
        self.alias_name = alias_name
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class BindAliasResponseBody(TeaModel):
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


class BindAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindAliasResponseBody = None,
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
            temp_model = BindAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindPhoneRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
        phone_number: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class BindPhoneResponseBody(TeaModel):
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


class BindPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindPhoneResponseBody = None,
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
            temp_model = BindPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindTagRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        client_key: str = None,
        key_type: str = None,
        tag_name: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.client_key = client_key
        # This parameter is required.
        self.key_type = key_type
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.client_key is not None:
            result['ClientKey'] = self.client_key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ClientKey') is not None:
            self.client_key = m.get('ClientKey')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class BindTagResponseBody(TeaModel):
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


class BindTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindTagResponseBody = None,
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
            temp_model = BindTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPushRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        message_id: int = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class CancelPushResponseBody(TeaModel):
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


class CancelPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelPushResponseBody = None,
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
            temp_model = CancelPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckCertificateRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
    ):
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class CheckCertificateResponseBodyDevelopmentCertInfo(TeaModel):
    def __init__(
        self,
        exipre_time: int = None,
        status: str = None,
    ):
        self.exipre_time = exipre_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exipre_time is not None:
            result['ExipreTime'] = self.exipre_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExipreTime') is not None:
            self.exipre_time = m.get('ExipreTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckCertificateResponseBodyProductionCertInfo(TeaModel):
    def __init__(
        self,
        exipre_time: int = None,
        status: str = None,
    ):
        self.exipre_time = exipre_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exipre_time is not None:
            result['ExipreTime'] = self.exipre_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExipreTime') is not None:
            self.exipre_time = m.get('ExipreTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CheckCertificateResponseBody(TeaModel):
    def __init__(
        self,
        android: bool = None,
        development_cert_info: CheckCertificateResponseBodyDevelopmentCertInfo = None,
        ios: bool = None,
        production_cert_info: CheckCertificateResponseBodyProductionCertInfo = None,
        request_id: str = None,
    ):
        self.android = android
        self.development_cert_info = development_cert_info
        self.ios = ios
        self.production_cert_info = production_cert_info
        self.request_id = request_id

    def validate(self):
        if self.development_cert_info:
            self.development_cert_info.validate()
        if self.production_cert_info:
            self.production_cert_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android is not None:
            result['Android'] = self.android
        if self.development_cert_info is not None:
            result['DevelopmentCertInfo'] = self.development_cert_info.to_map()
        if self.ios is not None:
            result['IOS'] = self.ios
        if self.production_cert_info is not None:
            result['ProductionCertInfo'] = self.production_cert_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Android') is not None:
            self.android = m.get('Android')
        if m.get('DevelopmentCertInfo') is not None:
            temp_model = CheckCertificateResponseBodyDevelopmentCertInfo()
            self.development_cert_info = temp_model.from_map(m['DevelopmentCertInfo'])
        if m.get('IOS') is not None:
            self.ios = m.get('IOS')
        if m.get('ProductionCertInfo') is not None:
            temp_model = CheckCertificateResponseBodyProductionCertInfo()
            self.production_cert_info = temp_model.from_map(m['ProductionCertInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckCertificateResponseBody = None,
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
            temp_model = CheckCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDeviceRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class CheckDeviceResponseBody(TeaModel):
    def __init__(
        self,
        available: bool = None,
        request_id: str = None,
    ):
        self.available = available
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDeviceResponseBody = None,
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
            temp_model = CheckDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDevicesRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_ids: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_ids = device_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceIds') is not None:
            self.device_ids = m.get('DeviceIds')
        return self


class CheckDevicesResponseBodyDeviceCheckInfosDeviceCheckInfo(TeaModel):
    def __init__(
        self,
        available: bool = None,
        device_id: str = None,
    ):
        self.available = available
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available is not None:
            result['Available'] = self.available
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class CheckDevicesResponseBodyDeviceCheckInfos(TeaModel):
    def __init__(
        self,
        device_check_info: List[CheckDevicesResponseBodyDeviceCheckInfosDeviceCheckInfo] = None,
    ):
        self.device_check_info = device_check_info

    def validate(self):
        if self.device_check_info:
            for k in self.device_check_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceCheckInfo'] = []
        if self.device_check_info is not None:
            for k in self.device_check_info:
                result['DeviceCheckInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_check_info = []
        if m.get('DeviceCheckInfo') is not None:
            for k in m.get('DeviceCheckInfo'):
                temp_model = CheckDevicesResponseBodyDeviceCheckInfosDeviceCheckInfo()
                self.device_check_info.append(temp_model.from_map(k))
        return self


class CheckDevicesResponseBody(TeaModel):
    def __init__(
        self,
        device_check_infos: CheckDevicesResponseBodyDeviceCheckInfos = None,
        request_id: str = None,
    ):
        self.device_check_infos = device_check_infos
        self.request_id = request_id

    def validate(self):
        if self.device_check_infos:
            self.device_check_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_check_infos is not None:
            result['DeviceCheckInfos'] = self.device_check_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCheckInfos') is not None:
            temp_model = CheckDevicesResponseBodyDeviceCheckInfos()
            self.device_check_infos = temp_model.from_map(m['DeviceCheckInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckDevicesResponseBody = None,
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
            temp_model = CheckDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteContinuouslyPushRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        message_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class CompleteContinuouslyPushResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CompleteContinuouslyPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CompleteContinuouslyPushResponseBody = None,
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
            temp_model = CompleteContinuouslyPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinuouslyPushRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        message_id: str = None,
        target: str = None,
        target_value: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.message_id = message_id
        # This parameter is required.
        self.target = target
        # This parameter is required.
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        return self


class ContinuouslyPushResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ContinuouslyPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContinuouslyPushResponseBody = None,
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
            temp_model = ContinuouslyPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSummaryAppsResponseBodySummaryAppInfosSummaryAppInfo(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        app_name: str = None,
    ):
        self.app_key = app_key
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ListSummaryAppsResponseBodySummaryAppInfos(TeaModel):
    def __init__(
        self,
        summary_app_info: List[ListSummaryAppsResponseBodySummaryAppInfosSummaryAppInfo] = None,
    ):
        self.summary_app_info = summary_app_info

    def validate(self):
        if self.summary_app_info:
            for k in self.summary_app_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SummaryAppInfo'] = []
        if self.summary_app_info is not None:
            for k in self.summary_app_info:
                result['SummaryAppInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summary_app_info = []
        if m.get('SummaryAppInfo') is not None:
            for k in m.get('SummaryAppInfo'):
                temp_model = ListSummaryAppsResponseBodySummaryAppInfosSummaryAppInfo()
                self.summary_app_info.append(temp_model.from_map(k))
        return self


class ListSummaryAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        summary_app_infos: ListSummaryAppsResponseBodySummaryAppInfos = None,
    ):
        self.request_id = request_id
        self.summary_app_infos = summary_app_infos

    def validate(self):
        if self.summary_app_infos:
            self.summary_app_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.summary_app_infos is not None:
            result['SummaryAppInfos'] = self.summary_app_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SummaryAppInfos') is not None:
            temp_model = ListSummaryAppsResponseBodySummaryAppInfos()
            self.summary_app_infos = temp_model.from_map(m['SummaryAppInfos'])
        return self


class ListSummaryAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSummaryAppsResponseBody = None,
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
            temp_model = ListSummaryAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
    ):
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ListTagsResponseBodyTagInfosTagInfo(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
    ):
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class ListTagsResponseBodyTagInfos(TeaModel):
    def __init__(
        self,
        tag_info: List[ListTagsResponseBodyTagInfosTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = ListTagsResponseBodyTagInfosTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_infos: ListTagsResponseBodyTagInfos = None,
    ):
        self.request_id = request_id
        self.tag_infos = tag_infos

    def validate(self):
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagInfos') is not None:
            temp_model = ListTagsResponseBodyTagInfos()
            self.tag_infos = temp_model.from_map(m['TagInfos'])
        return self


class ListTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagsResponseBody = None,
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
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MassPushRequestPushTask(TeaModel):
    def __init__(
        self,
        android_activity: str = None,
        android_badge_add_num: int = None,
        android_badge_class: str = None,
        android_badge_set_num: int = None,
        android_big_body: str = None,
        android_big_picture_url: str = None,
        android_big_title: str = None,
        android_ext_parameters: str = None,
        android_honor_target_user_type: int = None,
        android_huawei_receipt_id: str = None,
        android_huawei_target_user_type: int = None,
        android_image_url: str = None,
        android_inbox_body: str = None,
        android_message_huawei_category: str = None,
        android_message_huawei_urgency: str = None,
        android_message_oppo_category: str = None,
        android_message_oppo_notify_level: int = None,
        android_message_vivo_category: str = None,
        android_music: str = None,
        android_notification_bar_priority: int = None,
        android_notification_bar_type: int = None,
        android_notification_channel: str = None,
        android_notification_group: str = None,
        android_notification_honor_channel: str = None,
        android_notification_huawei_channel: str = None,
        android_notification_notify_id: int = None,
        android_notification_thread_id: str = None,
        android_notification_vivo_channel: str = None,
        android_notification_xiaomi_channel: str = None,
        android_notify_type: str = None,
        android_open_type: str = None,
        android_open_url: str = None,
        android_popup_activity: str = None,
        android_popup_body: str = None,
        android_popup_title: str = None,
        android_remind: bool = None,
        android_render_style: str = None,
        android_target_user_type: int = None,
        android_vivo_push_mode: int = None,
        android_vivo_receipt_id: str = None,
        android_xiao_mi_activity: str = None,
        android_xiao_mi_notify_body: str = None,
        android_xiao_mi_notify_title: str = None,
        android_xiaomi_big_picture_url: str = None,
        android_xiaomi_image_url: str = None,
        body: str = None,
        device_type: str = None,
        expire_time: str = None,
        harmony_action: str = None,
        harmony_action_type: str = None,
        harmony_badge_add_num: int = None,
        harmony_badge_set_num: int = None,
        harmony_category: str = None,
        harmony_ext_parameters: str = None,
        harmony_extension_extra_data: str = None,
        harmony_extension_push: bool = None,
        harmony_image_url: str = None,
        harmony_inbox_content: str = None,
        harmony_notification_slot_type: str = None,
        harmony_notify_id: int = None,
        harmony_receipt_id: str = None,
        harmony_remind: bool = None,
        harmony_remind_body: str = None,
        harmony_remind_title: str = None,
        harmony_render_style: str = None,
        harmony_test_message: bool = None,
        harmony_uri: str = None,
        job_key: str = None,
        push_time: str = None,
        push_type: str = None,
        send_channels: str = None,
        send_speed: int = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
        trim: bool = None,
        i_osapns_env: str = None,
        i_osbadge: int = None,
        i_osbadge_auto_increment: bool = None,
        i_osext_parameters: str = None,
        i_osinterruption_level: str = None,
        i_osmusic: str = None,
        i_osmutable_content: bool = None,
        i_osnotification_category: str = None,
        i_osnotification_collapse_id: str = None,
        i_osnotification_thread_id: str = None,
        i_osrelevance_score: float = None,
        i_osremind: bool = None,
        i_osremind_body: str = None,
        i_ossilent_notification: bool = None,
        i_ossubtitle: str = None,
    ):
        self.android_activity = android_activity
        self.android_badge_add_num = android_badge_add_num
        self.android_badge_class = android_badge_class
        self.android_badge_set_num = android_badge_set_num
        self.android_big_body = android_big_body
        self.android_big_picture_url = android_big_picture_url
        self.android_big_title = android_big_title
        self.android_ext_parameters = android_ext_parameters
        self.android_honor_target_user_type = android_honor_target_user_type
        self.android_huawei_receipt_id = android_huawei_receipt_id
        self.android_huawei_target_user_type = android_huawei_target_user_type
        self.android_image_url = android_image_url
        self.android_inbox_body = android_inbox_body
        self.android_message_huawei_category = android_message_huawei_category
        self.android_message_huawei_urgency = android_message_huawei_urgency
        self.android_message_oppo_category = android_message_oppo_category
        self.android_message_oppo_notify_level = android_message_oppo_notify_level
        self.android_message_vivo_category = android_message_vivo_category
        self.android_music = android_music
        self.android_notification_bar_priority = android_notification_bar_priority
        self.android_notification_bar_type = android_notification_bar_type
        self.android_notification_channel = android_notification_channel
        self.android_notification_group = android_notification_group
        self.android_notification_honor_channel = android_notification_honor_channel
        self.android_notification_huawei_channel = android_notification_huawei_channel
        self.android_notification_notify_id = android_notification_notify_id
        self.android_notification_thread_id = android_notification_thread_id
        self.android_notification_vivo_channel = android_notification_vivo_channel
        self.android_notification_xiaomi_channel = android_notification_xiaomi_channel
        self.android_notify_type = android_notify_type
        self.android_open_type = android_open_type
        self.android_open_url = android_open_url
        self.android_popup_activity = android_popup_activity
        self.android_popup_body = android_popup_body
        self.android_popup_title = android_popup_title
        self.android_remind = android_remind
        self.android_render_style = android_render_style
        self.android_target_user_type = android_target_user_type
        self.android_vivo_push_mode = android_vivo_push_mode
        self.android_vivo_receipt_id = android_vivo_receipt_id
        self.android_xiao_mi_activity = android_xiao_mi_activity
        self.android_xiao_mi_notify_body = android_xiao_mi_notify_body
        self.android_xiao_mi_notify_title = android_xiao_mi_notify_title
        self.android_xiaomi_big_picture_url = android_xiaomi_big_picture_url
        self.android_xiaomi_image_url = android_xiaomi_image_url
        # This parameter is required.
        self.body = body
        # This parameter is required.
        self.device_type = device_type
        self.expire_time = expire_time
        self.harmony_action = harmony_action
        self.harmony_action_type = harmony_action_type
        self.harmony_badge_add_num = harmony_badge_add_num
        self.harmony_badge_set_num = harmony_badge_set_num
        self.harmony_category = harmony_category
        self.harmony_ext_parameters = harmony_ext_parameters
        self.harmony_extension_extra_data = harmony_extension_extra_data
        self.harmony_extension_push = harmony_extension_push
        self.harmony_image_url = harmony_image_url
        self.harmony_inbox_content = harmony_inbox_content
        self.harmony_notification_slot_type = harmony_notification_slot_type
        self.harmony_notify_id = harmony_notify_id
        self.harmony_receipt_id = harmony_receipt_id
        self.harmony_remind = harmony_remind
        self.harmony_remind_body = harmony_remind_body
        self.harmony_remind_title = harmony_remind_title
        self.harmony_render_style = harmony_render_style
        self.harmony_test_message = harmony_test_message
        self.harmony_uri = harmony_uri
        self.job_key = job_key
        self.push_time = push_time
        # This parameter is required.
        self.push_type = push_type
        self.send_channels = send_channels
        self.send_speed = send_speed
        self.store_offline = store_offline
        # This parameter is required.
        self.target = target
        # This parameter is required.
        self.target_value = target_value
        self.title = title
        self.trim = trim
        self.i_osapns_env = i_osapns_env
        self.i_osbadge = i_osbadge
        self.i_osbadge_auto_increment = i_osbadge_auto_increment
        self.i_osext_parameters = i_osext_parameters
        self.i_osinterruption_level = i_osinterruption_level
        self.i_osmusic = i_osmusic
        self.i_osmutable_content = i_osmutable_content
        self.i_osnotification_category = i_osnotification_category
        self.i_osnotification_collapse_id = i_osnotification_collapse_id
        self.i_osnotification_thread_id = i_osnotification_thread_id
        self.i_osrelevance_score = i_osrelevance_score
        self.i_osremind = i_osremind
        self.i_osremind_body = i_osremind_body
        self.i_ossilent_notification = i_ossilent_notification
        self.i_ossubtitle = i_ossubtitle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_activity is not None:
            result['AndroidActivity'] = self.android_activity
        if self.android_badge_add_num is not None:
            result['AndroidBadgeAddNum'] = self.android_badge_add_num
        if self.android_badge_class is not None:
            result['AndroidBadgeClass'] = self.android_badge_class
        if self.android_badge_set_num is not None:
            result['AndroidBadgeSetNum'] = self.android_badge_set_num
        if self.android_big_body is not None:
            result['AndroidBigBody'] = self.android_big_body
        if self.android_big_picture_url is not None:
            result['AndroidBigPictureUrl'] = self.android_big_picture_url
        if self.android_big_title is not None:
            result['AndroidBigTitle'] = self.android_big_title
        if self.android_ext_parameters is not None:
            result['AndroidExtParameters'] = self.android_ext_parameters
        if self.android_honor_target_user_type is not None:
            result['AndroidHonorTargetUserType'] = self.android_honor_target_user_type
        if self.android_huawei_receipt_id is not None:
            result['AndroidHuaweiReceiptId'] = self.android_huawei_receipt_id
        if self.android_huawei_target_user_type is not None:
            result['AndroidHuaweiTargetUserType'] = self.android_huawei_target_user_type
        if self.android_image_url is not None:
            result['AndroidImageUrl'] = self.android_image_url
        if self.android_inbox_body is not None:
            result['AndroidInboxBody'] = self.android_inbox_body
        if self.android_message_huawei_category is not None:
            result['AndroidMessageHuaweiCategory'] = self.android_message_huawei_category
        if self.android_message_huawei_urgency is not None:
            result['AndroidMessageHuaweiUrgency'] = self.android_message_huawei_urgency
        if self.android_message_oppo_category is not None:
            result['AndroidMessageOppoCategory'] = self.android_message_oppo_category
        if self.android_message_oppo_notify_level is not None:
            result['AndroidMessageOppoNotifyLevel'] = self.android_message_oppo_notify_level
        if self.android_message_vivo_category is not None:
            result['AndroidMessageVivoCategory'] = self.android_message_vivo_category
        if self.android_music is not None:
            result['AndroidMusic'] = self.android_music
        if self.android_notification_bar_priority is not None:
            result['AndroidNotificationBarPriority'] = self.android_notification_bar_priority
        if self.android_notification_bar_type is not None:
            result['AndroidNotificationBarType'] = self.android_notification_bar_type
        if self.android_notification_channel is not None:
            result['AndroidNotificationChannel'] = self.android_notification_channel
        if self.android_notification_group is not None:
            result['AndroidNotificationGroup'] = self.android_notification_group
        if self.android_notification_honor_channel is not None:
            result['AndroidNotificationHonorChannel'] = self.android_notification_honor_channel
        if self.android_notification_huawei_channel is not None:
            result['AndroidNotificationHuaweiChannel'] = self.android_notification_huawei_channel
        if self.android_notification_notify_id is not None:
            result['AndroidNotificationNotifyId'] = self.android_notification_notify_id
        if self.android_notification_thread_id is not None:
            result['AndroidNotificationThreadId'] = self.android_notification_thread_id
        if self.android_notification_vivo_channel is not None:
            result['AndroidNotificationVivoChannel'] = self.android_notification_vivo_channel
        if self.android_notification_xiaomi_channel is not None:
            result['AndroidNotificationXiaomiChannel'] = self.android_notification_xiaomi_channel
        if self.android_notify_type is not None:
            result['AndroidNotifyType'] = self.android_notify_type
        if self.android_open_type is not None:
            result['AndroidOpenType'] = self.android_open_type
        if self.android_open_url is not None:
            result['AndroidOpenUrl'] = self.android_open_url
        if self.android_popup_activity is not None:
            result['AndroidPopupActivity'] = self.android_popup_activity
        if self.android_popup_body is not None:
            result['AndroidPopupBody'] = self.android_popup_body
        if self.android_popup_title is not None:
            result['AndroidPopupTitle'] = self.android_popup_title
        if self.android_remind is not None:
            result['AndroidRemind'] = self.android_remind
        if self.android_render_style is not None:
            result['AndroidRenderStyle'] = self.android_render_style
        if self.android_target_user_type is not None:
            result['AndroidTargetUserType'] = self.android_target_user_type
        if self.android_vivo_push_mode is not None:
            result['AndroidVivoPushMode'] = self.android_vivo_push_mode
        if self.android_vivo_receipt_id is not None:
            result['AndroidVivoReceiptId'] = self.android_vivo_receipt_id
        if self.android_xiao_mi_activity is not None:
            result['AndroidXiaoMiActivity'] = self.android_xiao_mi_activity
        if self.android_xiao_mi_notify_body is not None:
            result['AndroidXiaoMiNotifyBody'] = self.android_xiao_mi_notify_body
        if self.android_xiao_mi_notify_title is not None:
            result['AndroidXiaoMiNotifyTitle'] = self.android_xiao_mi_notify_title
        if self.android_xiaomi_big_picture_url is not None:
            result['AndroidXiaomiBigPictureUrl'] = self.android_xiaomi_big_picture_url
        if self.android_xiaomi_image_url is not None:
            result['AndroidXiaomiImageUrl'] = self.android_xiaomi_image_url
        if self.body is not None:
            result['Body'] = self.body
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.harmony_action is not None:
            result['HarmonyAction'] = self.harmony_action
        if self.harmony_action_type is not None:
            result['HarmonyActionType'] = self.harmony_action_type
        if self.harmony_badge_add_num is not None:
            result['HarmonyBadgeAddNum'] = self.harmony_badge_add_num
        if self.harmony_badge_set_num is not None:
            result['HarmonyBadgeSetNum'] = self.harmony_badge_set_num
        if self.harmony_category is not None:
            result['HarmonyCategory'] = self.harmony_category
        if self.harmony_ext_parameters is not None:
            result['HarmonyExtParameters'] = self.harmony_ext_parameters
        if self.harmony_extension_extra_data is not None:
            result['HarmonyExtensionExtraData'] = self.harmony_extension_extra_data
        if self.harmony_extension_push is not None:
            result['HarmonyExtensionPush'] = self.harmony_extension_push
        if self.harmony_image_url is not None:
            result['HarmonyImageUrl'] = self.harmony_image_url
        if self.harmony_inbox_content is not None:
            result['HarmonyInboxContent'] = self.harmony_inbox_content
        if self.harmony_notification_slot_type is not None:
            result['HarmonyNotificationSlotType'] = self.harmony_notification_slot_type
        if self.harmony_notify_id is not None:
            result['HarmonyNotifyId'] = self.harmony_notify_id
        if self.harmony_receipt_id is not None:
            result['HarmonyReceiptId'] = self.harmony_receipt_id
        if self.harmony_remind is not None:
            result['HarmonyRemind'] = self.harmony_remind
        if self.harmony_remind_body is not None:
            result['HarmonyRemindBody'] = self.harmony_remind_body
        if self.harmony_remind_title is not None:
            result['HarmonyRemindTitle'] = self.harmony_remind_title
        if self.harmony_render_style is not None:
            result['HarmonyRenderStyle'] = self.harmony_render_style
        if self.harmony_test_message is not None:
            result['HarmonyTestMessage'] = self.harmony_test_message
        if self.harmony_uri is not None:
            result['HarmonyUri'] = self.harmony_uri
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.push_time is not None:
            result['PushTime'] = self.push_time
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.send_channels is not None:
            result['SendChannels'] = self.send_channels
        if self.send_speed is not None:
            result['SendSpeed'] = self.send_speed
        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        if self.trim is not None:
            result['Trim'] = self.trim
        if self.i_osapns_env is not None:
            result['iOSApnsEnv'] = self.i_osapns_env
        if self.i_osbadge is not None:
            result['iOSBadge'] = self.i_osbadge
        if self.i_osbadge_auto_increment is not None:
            result['iOSBadgeAutoIncrement'] = self.i_osbadge_auto_increment
        if self.i_osext_parameters is not None:
            result['iOSExtParameters'] = self.i_osext_parameters
        if self.i_osinterruption_level is not None:
            result['iOSInterruptionLevel'] = self.i_osinterruption_level
        if self.i_osmusic is not None:
            result['iOSMusic'] = self.i_osmusic
        if self.i_osmutable_content is not None:
            result['iOSMutableContent'] = self.i_osmutable_content
        if self.i_osnotification_category is not None:
            result['iOSNotificationCategory'] = self.i_osnotification_category
        if self.i_osnotification_collapse_id is not None:
            result['iOSNotificationCollapseId'] = self.i_osnotification_collapse_id
        if self.i_osnotification_thread_id is not None:
            result['iOSNotificationThreadId'] = self.i_osnotification_thread_id
        if self.i_osrelevance_score is not None:
            result['iOSRelevanceScore'] = self.i_osrelevance_score
        if self.i_osremind is not None:
            result['iOSRemind'] = self.i_osremind
        if self.i_osremind_body is not None:
            result['iOSRemindBody'] = self.i_osremind_body
        if self.i_ossilent_notification is not None:
            result['iOSSilentNotification'] = self.i_ossilent_notification
        if self.i_ossubtitle is not None:
            result['iOSSubtitle'] = self.i_ossubtitle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidActivity') is not None:
            self.android_activity = m.get('AndroidActivity')
        if m.get('AndroidBadgeAddNum') is not None:
            self.android_badge_add_num = m.get('AndroidBadgeAddNum')
        if m.get('AndroidBadgeClass') is not None:
            self.android_badge_class = m.get('AndroidBadgeClass')
        if m.get('AndroidBadgeSetNum') is not None:
            self.android_badge_set_num = m.get('AndroidBadgeSetNum')
        if m.get('AndroidBigBody') is not None:
            self.android_big_body = m.get('AndroidBigBody')
        if m.get('AndroidBigPictureUrl') is not None:
            self.android_big_picture_url = m.get('AndroidBigPictureUrl')
        if m.get('AndroidBigTitle') is not None:
            self.android_big_title = m.get('AndroidBigTitle')
        if m.get('AndroidExtParameters') is not None:
            self.android_ext_parameters = m.get('AndroidExtParameters')
        if m.get('AndroidHonorTargetUserType') is not None:
            self.android_honor_target_user_type = m.get('AndroidHonorTargetUserType')
        if m.get('AndroidHuaweiReceiptId') is not None:
            self.android_huawei_receipt_id = m.get('AndroidHuaweiReceiptId')
        if m.get('AndroidHuaweiTargetUserType') is not None:
            self.android_huawei_target_user_type = m.get('AndroidHuaweiTargetUserType')
        if m.get('AndroidImageUrl') is not None:
            self.android_image_url = m.get('AndroidImageUrl')
        if m.get('AndroidInboxBody') is not None:
            self.android_inbox_body = m.get('AndroidInboxBody')
        if m.get('AndroidMessageHuaweiCategory') is not None:
            self.android_message_huawei_category = m.get('AndroidMessageHuaweiCategory')
        if m.get('AndroidMessageHuaweiUrgency') is not None:
            self.android_message_huawei_urgency = m.get('AndroidMessageHuaweiUrgency')
        if m.get('AndroidMessageOppoCategory') is not None:
            self.android_message_oppo_category = m.get('AndroidMessageOppoCategory')
        if m.get('AndroidMessageOppoNotifyLevel') is not None:
            self.android_message_oppo_notify_level = m.get('AndroidMessageOppoNotifyLevel')
        if m.get('AndroidMessageVivoCategory') is not None:
            self.android_message_vivo_category = m.get('AndroidMessageVivoCategory')
        if m.get('AndroidMusic') is not None:
            self.android_music = m.get('AndroidMusic')
        if m.get('AndroidNotificationBarPriority') is not None:
            self.android_notification_bar_priority = m.get('AndroidNotificationBarPriority')
        if m.get('AndroidNotificationBarType') is not None:
            self.android_notification_bar_type = m.get('AndroidNotificationBarType')
        if m.get('AndroidNotificationChannel') is not None:
            self.android_notification_channel = m.get('AndroidNotificationChannel')
        if m.get('AndroidNotificationGroup') is not None:
            self.android_notification_group = m.get('AndroidNotificationGroup')
        if m.get('AndroidNotificationHonorChannel') is not None:
            self.android_notification_honor_channel = m.get('AndroidNotificationHonorChannel')
        if m.get('AndroidNotificationHuaweiChannel') is not None:
            self.android_notification_huawei_channel = m.get('AndroidNotificationHuaweiChannel')
        if m.get('AndroidNotificationNotifyId') is not None:
            self.android_notification_notify_id = m.get('AndroidNotificationNotifyId')
        if m.get('AndroidNotificationThreadId') is not None:
            self.android_notification_thread_id = m.get('AndroidNotificationThreadId')
        if m.get('AndroidNotificationVivoChannel') is not None:
            self.android_notification_vivo_channel = m.get('AndroidNotificationVivoChannel')
        if m.get('AndroidNotificationXiaomiChannel') is not None:
            self.android_notification_xiaomi_channel = m.get('AndroidNotificationXiaomiChannel')
        if m.get('AndroidNotifyType') is not None:
            self.android_notify_type = m.get('AndroidNotifyType')
        if m.get('AndroidOpenType') is not None:
            self.android_open_type = m.get('AndroidOpenType')
        if m.get('AndroidOpenUrl') is not None:
            self.android_open_url = m.get('AndroidOpenUrl')
        if m.get('AndroidPopupActivity') is not None:
            self.android_popup_activity = m.get('AndroidPopupActivity')
        if m.get('AndroidPopupBody') is not None:
            self.android_popup_body = m.get('AndroidPopupBody')
        if m.get('AndroidPopupTitle') is not None:
            self.android_popup_title = m.get('AndroidPopupTitle')
        if m.get('AndroidRemind') is not None:
            self.android_remind = m.get('AndroidRemind')
        if m.get('AndroidRenderStyle') is not None:
            self.android_render_style = m.get('AndroidRenderStyle')
        if m.get('AndroidTargetUserType') is not None:
            self.android_target_user_type = m.get('AndroidTargetUserType')
        if m.get('AndroidVivoPushMode') is not None:
            self.android_vivo_push_mode = m.get('AndroidVivoPushMode')
        if m.get('AndroidVivoReceiptId') is not None:
            self.android_vivo_receipt_id = m.get('AndroidVivoReceiptId')
        if m.get('AndroidXiaoMiActivity') is not None:
            self.android_xiao_mi_activity = m.get('AndroidXiaoMiActivity')
        if m.get('AndroidXiaoMiNotifyBody') is not None:
            self.android_xiao_mi_notify_body = m.get('AndroidXiaoMiNotifyBody')
        if m.get('AndroidXiaoMiNotifyTitle') is not None:
            self.android_xiao_mi_notify_title = m.get('AndroidXiaoMiNotifyTitle')
        if m.get('AndroidXiaomiBigPictureUrl') is not None:
            self.android_xiaomi_big_picture_url = m.get('AndroidXiaomiBigPictureUrl')
        if m.get('AndroidXiaomiImageUrl') is not None:
            self.android_xiaomi_image_url = m.get('AndroidXiaomiImageUrl')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HarmonyAction') is not None:
            self.harmony_action = m.get('HarmonyAction')
        if m.get('HarmonyActionType') is not None:
            self.harmony_action_type = m.get('HarmonyActionType')
        if m.get('HarmonyBadgeAddNum') is not None:
            self.harmony_badge_add_num = m.get('HarmonyBadgeAddNum')
        if m.get('HarmonyBadgeSetNum') is not None:
            self.harmony_badge_set_num = m.get('HarmonyBadgeSetNum')
        if m.get('HarmonyCategory') is not None:
            self.harmony_category = m.get('HarmonyCategory')
        if m.get('HarmonyExtParameters') is not None:
            self.harmony_ext_parameters = m.get('HarmonyExtParameters')
        if m.get('HarmonyExtensionExtraData') is not None:
            self.harmony_extension_extra_data = m.get('HarmonyExtensionExtraData')
        if m.get('HarmonyExtensionPush') is not None:
            self.harmony_extension_push = m.get('HarmonyExtensionPush')
        if m.get('HarmonyImageUrl') is not None:
            self.harmony_image_url = m.get('HarmonyImageUrl')
        if m.get('HarmonyInboxContent') is not None:
            self.harmony_inbox_content = m.get('HarmonyInboxContent')
        if m.get('HarmonyNotificationSlotType') is not None:
            self.harmony_notification_slot_type = m.get('HarmonyNotificationSlotType')
        if m.get('HarmonyNotifyId') is not None:
            self.harmony_notify_id = m.get('HarmonyNotifyId')
        if m.get('HarmonyReceiptId') is not None:
            self.harmony_receipt_id = m.get('HarmonyReceiptId')
        if m.get('HarmonyRemind') is not None:
            self.harmony_remind = m.get('HarmonyRemind')
        if m.get('HarmonyRemindBody') is not None:
            self.harmony_remind_body = m.get('HarmonyRemindBody')
        if m.get('HarmonyRemindTitle') is not None:
            self.harmony_remind_title = m.get('HarmonyRemindTitle')
        if m.get('HarmonyRenderStyle') is not None:
            self.harmony_render_style = m.get('HarmonyRenderStyle')
        if m.get('HarmonyTestMessage') is not None:
            self.harmony_test_message = m.get('HarmonyTestMessage')
        if m.get('HarmonyUri') is not None:
            self.harmony_uri = m.get('HarmonyUri')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('SendChannels') is not None:
            self.send_channels = m.get('SendChannels')
        if m.get('SendSpeed') is not None:
            self.send_speed = m.get('SendSpeed')
        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Trim') is not None:
            self.trim = m.get('Trim')
        if m.get('iOSApnsEnv') is not None:
            self.i_osapns_env = m.get('iOSApnsEnv')
        if m.get('iOSBadge') is not None:
            self.i_osbadge = m.get('iOSBadge')
        if m.get('iOSBadgeAutoIncrement') is not None:
            self.i_osbadge_auto_increment = m.get('iOSBadgeAutoIncrement')
        if m.get('iOSExtParameters') is not None:
            self.i_osext_parameters = m.get('iOSExtParameters')
        if m.get('iOSInterruptionLevel') is not None:
            self.i_osinterruption_level = m.get('iOSInterruptionLevel')
        if m.get('iOSMusic') is not None:
            self.i_osmusic = m.get('iOSMusic')
        if m.get('iOSMutableContent') is not None:
            self.i_osmutable_content = m.get('iOSMutableContent')
        if m.get('iOSNotificationCategory') is not None:
            self.i_osnotification_category = m.get('iOSNotificationCategory')
        if m.get('iOSNotificationCollapseId') is not None:
            self.i_osnotification_collapse_id = m.get('iOSNotificationCollapseId')
        if m.get('iOSNotificationThreadId') is not None:
            self.i_osnotification_thread_id = m.get('iOSNotificationThreadId')
        if m.get('iOSRelevanceScore') is not None:
            self.i_osrelevance_score = m.get('iOSRelevanceScore')
        if m.get('iOSRemind') is not None:
            self.i_osremind = m.get('iOSRemind')
        if m.get('iOSRemindBody') is not None:
            self.i_osremind_body = m.get('iOSRemindBody')
        if m.get('iOSSilentNotification') is not None:
            self.i_ossilent_notification = m.get('iOSSilentNotification')
        if m.get('iOSSubtitle') is not None:
            self.i_ossubtitle = m.get('iOSSubtitle')
        return self


class MassPushRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        idempotent_token: str = None,
        push_task: List[MassPushRequestPushTask] = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.idempotent_token = idempotent_token
        # This parameter is required.
        self.push_task = push_task

    def validate(self):
        if self.push_task:
            for k in self.push_task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.idempotent_token is not None:
            result['IdempotentToken'] = self.idempotent_token
        result['PushTask'] = []
        if self.push_task is not None:
            for k in self.push_task:
                result['PushTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')
        self.push_task = []
        if m.get('PushTask') is not None:
            for k in m.get('PushTask'):
                temp_model = MassPushRequestPushTask()
                self.push_task.append(temp_model.from_map(k))
        return self


class MassPushResponseBodyMessageIds(TeaModel):
    def __init__(
        self,
        message_id: List[str] = None,
    ):
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class MassPushResponseBody(TeaModel):
    def __init__(
        self,
        message_ids: MassPushResponseBodyMessageIds = None,
        request_id: str = None,
    ):
        self.message_ids = message_ids
        self.request_id = request_id

    def validate(self):
        if self.message_ids:
            self.message_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_ids is not None:
            result['MessageIds'] = self.message_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageIds') is not None:
            temp_model = MassPushResponseBodyMessageIds()
            self.message_ids = temp_model.from_map(m['MessageIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MassPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MassPushResponseBody = None,
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
            temp_model = MassPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushRequest(TeaModel):
    def __init__(
        self,
        android_activity: str = None,
        android_badge_add_num: int = None,
        android_badge_class: str = None,
        android_badge_set_num: int = None,
        android_big_body: str = None,
        android_big_picture_url: str = None,
        android_big_title: str = None,
        android_ext_parameters: str = None,
        android_honor_target_user_type: int = None,
        android_huawei_receipt_id: str = None,
        android_huawei_target_user_type: int = None,
        android_image_url: str = None,
        android_inbox_body: str = None,
        android_message_huawei_category: str = None,
        android_message_huawei_urgency: str = None,
        android_message_oppo_category: str = None,
        android_message_oppo_notify_level: int = None,
        android_message_vivo_category: str = None,
        android_music: str = None,
        android_notification_bar_priority: int = None,
        android_notification_bar_type: int = None,
        android_notification_channel: str = None,
        android_notification_group: str = None,
        android_notification_honor_channel: str = None,
        android_notification_huawei_channel: str = None,
        android_notification_notify_id: int = None,
        android_notification_thread_id: str = None,
        android_notification_vivo_channel: str = None,
        android_notification_xiaomi_channel: str = None,
        android_notify_type: str = None,
        android_open_type: str = None,
        android_open_url: str = None,
        android_popup_activity: str = None,
        android_popup_body: str = None,
        android_popup_title: str = None,
        android_remind: bool = None,
        android_render_style: int = None,
        android_target_user_type: int = None,
        android_vivo_push_mode: int = None,
        android_vivo_receipt_id: str = None,
        android_xiao_mi_activity: str = None,
        android_xiao_mi_notify_body: str = None,
        android_xiao_mi_notify_title: str = None,
        android_xiaomi_big_picture_url: str = None,
        android_xiaomi_image_url: str = None,
        app_key: int = None,
        body: str = None,
        device_type: str = None,
        expire_time: str = None,
        harmony_action: str = None,
        harmony_action_type: str = None,
        harmony_badge_add_num: int = None,
        harmony_badge_set_num: int = None,
        harmony_category: str = None,
        harmony_ext_parameters: str = None,
        harmony_extension_extra_data: str = None,
        harmony_extension_push: bool = None,
        harmony_image_url: str = None,
        harmony_inbox_content: str = None,
        harmony_notification_slot_type: str = None,
        harmony_notify_id: int = None,
        harmony_receipt_id: str = None,
        harmony_remind: bool = None,
        harmony_remind_body: str = None,
        harmony_remind_title: str = None,
        harmony_render_style: str = None,
        harmony_test_message: bool = None,
        harmony_uri: str = None,
        idempotent_token: str = None,
        job_key: str = None,
        push_time: str = None,
        push_type: str = None,
        send_channels: str = None,
        send_speed: int = None,
        sms_delay_secs: int = None,
        sms_params: str = None,
        sms_send_policy: int = None,
        sms_sign_name: str = None,
        sms_template_name: str = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
        trim: bool = None,
        i_osapns_env: str = None,
        i_osbadge: int = None,
        i_osbadge_auto_increment: bool = None,
        i_osext_parameters: str = None,
        i_osinterruption_level: str = None,
        i_osmusic: str = None,
        i_osmutable_content: bool = None,
        i_osnotification_category: str = None,
        i_osnotification_collapse_id: str = None,
        i_osnotification_thread_id: str = None,
        i_osrelevance_score: float = None,
        i_osremind: bool = None,
        i_osremind_body: str = None,
        i_ossilent_notification: bool = None,
        i_ossubtitle: str = None,
    ):
        self.android_activity = android_activity
        self.android_badge_add_num = android_badge_add_num
        self.android_badge_class = android_badge_class
        self.android_badge_set_num = android_badge_set_num
        self.android_big_body = android_big_body
        self.android_big_picture_url = android_big_picture_url
        self.android_big_title = android_big_title
        self.android_ext_parameters = android_ext_parameters
        self.android_honor_target_user_type = android_honor_target_user_type
        self.android_huawei_receipt_id = android_huawei_receipt_id
        self.android_huawei_target_user_type = android_huawei_target_user_type
        self.android_image_url = android_image_url
        self.android_inbox_body = android_inbox_body
        self.android_message_huawei_category = android_message_huawei_category
        self.android_message_huawei_urgency = android_message_huawei_urgency
        self.android_message_oppo_category = android_message_oppo_category
        self.android_message_oppo_notify_level = android_message_oppo_notify_level
        self.android_message_vivo_category = android_message_vivo_category
        self.android_music = android_music
        self.android_notification_bar_priority = android_notification_bar_priority
        self.android_notification_bar_type = android_notification_bar_type
        self.android_notification_channel = android_notification_channel
        self.android_notification_group = android_notification_group
        self.android_notification_honor_channel = android_notification_honor_channel
        self.android_notification_huawei_channel = android_notification_huawei_channel
        self.android_notification_notify_id = android_notification_notify_id
        self.android_notification_thread_id = android_notification_thread_id
        self.android_notification_vivo_channel = android_notification_vivo_channel
        self.android_notification_xiaomi_channel = android_notification_xiaomi_channel
        self.android_notify_type = android_notify_type
        self.android_open_type = android_open_type
        self.android_open_url = android_open_url
        self.android_popup_activity = android_popup_activity
        self.android_popup_body = android_popup_body
        self.android_popup_title = android_popup_title
        self.android_remind = android_remind
        self.android_render_style = android_render_style
        self.android_target_user_type = android_target_user_type
        self.android_vivo_push_mode = android_vivo_push_mode
        self.android_vivo_receipt_id = android_vivo_receipt_id
        self.android_xiao_mi_activity = android_xiao_mi_activity
        self.android_xiao_mi_notify_body = android_xiao_mi_notify_body
        self.android_xiao_mi_notify_title = android_xiao_mi_notify_title
        self.android_xiaomi_big_picture_url = android_xiaomi_big_picture_url
        self.android_xiaomi_image_url = android_xiaomi_image_url
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.body = body
        # This parameter is required.
        self.device_type = device_type
        self.expire_time = expire_time
        self.harmony_action = harmony_action
        self.harmony_action_type = harmony_action_type
        self.harmony_badge_add_num = harmony_badge_add_num
        self.harmony_badge_set_num = harmony_badge_set_num
        self.harmony_category = harmony_category
        self.harmony_ext_parameters = harmony_ext_parameters
        self.harmony_extension_extra_data = harmony_extension_extra_data
        self.harmony_extension_push = harmony_extension_push
        self.harmony_image_url = harmony_image_url
        self.harmony_inbox_content = harmony_inbox_content
        self.harmony_notification_slot_type = harmony_notification_slot_type
        self.harmony_notify_id = harmony_notify_id
        self.harmony_receipt_id = harmony_receipt_id
        self.harmony_remind = harmony_remind
        self.harmony_remind_body = harmony_remind_body
        self.harmony_remind_title = harmony_remind_title
        self.harmony_render_style = harmony_render_style
        self.harmony_test_message = harmony_test_message
        self.harmony_uri = harmony_uri
        self.idempotent_token = idempotent_token
        self.job_key = job_key
        self.push_time = push_time
        # This parameter is required.
        self.push_type = push_type
        self.send_channels = send_channels
        self.send_speed = send_speed
        self.sms_delay_secs = sms_delay_secs
        self.sms_params = sms_params
        self.sms_send_policy = sms_send_policy
        self.sms_sign_name = sms_sign_name
        self.sms_template_name = sms_template_name
        self.store_offline = store_offline
        # This parameter is required.
        self.target = target
        # This parameter is required.
        self.target_value = target_value
        self.title = title
        self.trim = trim
        self.i_osapns_env = i_osapns_env
        self.i_osbadge = i_osbadge
        self.i_osbadge_auto_increment = i_osbadge_auto_increment
        self.i_osext_parameters = i_osext_parameters
        self.i_osinterruption_level = i_osinterruption_level
        self.i_osmusic = i_osmusic
        self.i_osmutable_content = i_osmutable_content
        self.i_osnotification_category = i_osnotification_category
        self.i_osnotification_collapse_id = i_osnotification_collapse_id
        self.i_osnotification_thread_id = i_osnotification_thread_id
        self.i_osrelevance_score = i_osrelevance_score
        self.i_osremind = i_osremind
        self.i_osremind_body = i_osremind_body
        self.i_ossilent_notification = i_ossilent_notification
        self.i_ossubtitle = i_ossubtitle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.android_activity is not None:
            result['AndroidActivity'] = self.android_activity
        if self.android_badge_add_num is not None:
            result['AndroidBadgeAddNum'] = self.android_badge_add_num
        if self.android_badge_class is not None:
            result['AndroidBadgeClass'] = self.android_badge_class
        if self.android_badge_set_num is not None:
            result['AndroidBadgeSetNum'] = self.android_badge_set_num
        if self.android_big_body is not None:
            result['AndroidBigBody'] = self.android_big_body
        if self.android_big_picture_url is not None:
            result['AndroidBigPictureUrl'] = self.android_big_picture_url
        if self.android_big_title is not None:
            result['AndroidBigTitle'] = self.android_big_title
        if self.android_ext_parameters is not None:
            result['AndroidExtParameters'] = self.android_ext_parameters
        if self.android_honor_target_user_type is not None:
            result['AndroidHonorTargetUserType'] = self.android_honor_target_user_type
        if self.android_huawei_receipt_id is not None:
            result['AndroidHuaweiReceiptId'] = self.android_huawei_receipt_id
        if self.android_huawei_target_user_type is not None:
            result['AndroidHuaweiTargetUserType'] = self.android_huawei_target_user_type
        if self.android_image_url is not None:
            result['AndroidImageUrl'] = self.android_image_url
        if self.android_inbox_body is not None:
            result['AndroidInboxBody'] = self.android_inbox_body
        if self.android_message_huawei_category is not None:
            result['AndroidMessageHuaweiCategory'] = self.android_message_huawei_category
        if self.android_message_huawei_urgency is not None:
            result['AndroidMessageHuaweiUrgency'] = self.android_message_huawei_urgency
        if self.android_message_oppo_category is not None:
            result['AndroidMessageOppoCategory'] = self.android_message_oppo_category
        if self.android_message_oppo_notify_level is not None:
            result['AndroidMessageOppoNotifyLevel'] = self.android_message_oppo_notify_level
        if self.android_message_vivo_category is not None:
            result['AndroidMessageVivoCategory'] = self.android_message_vivo_category
        if self.android_music is not None:
            result['AndroidMusic'] = self.android_music
        if self.android_notification_bar_priority is not None:
            result['AndroidNotificationBarPriority'] = self.android_notification_bar_priority
        if self.android_notification_bar_type is not None:
            result['AndroidNotificationBarType'] = self.android_notification_bar_type
        if self.android_notification_channel is not None:
            result['AndroidNotificationChannel'] = self.android_notification_channel
        if self.android_notification_group is not None:
            result['AndroidNotificationGroup'] = self.android_notification_group
        if self.android_notification_honor_channel is not None:
            result['AndroidNotificationHonorChannel'] = self.android_notification_honor_channel
        if self.android_notification_huawei_channel is not None:
            result['AndroidNotificationHuaweiChannel'] = self.android_notification_huawei_channel
        if self.android_notification_notify_id is not None:
            result['AndroidNotificationNotifyId'] = self.android_notification_notify_id
        if self.android_notification_thread_id is not None:
            result['AndroidNotificationThreadId'] = self.android_notification_thread_id
        if self.android_notification_vivo_channel is not None:
            result['AndroidNotificationVivoChannel'] = self.android_notification_vivo_channel
        if self.android_notification_xiaomi_channel is not None:
            result['AndroidNotificationXiaomiChannel'] = self.android_notification_xiaomi_channel
        if self.android_notify_type is not None:
            result['AndroidNotifyType'] = self.android_notify_type
        if self.android_open_type is not None:
            result['AndroidOpenType'] = self.android_open_type
        if self.android_open_url is not None:
            result['AndroidOpenUrl'] = self.android_open_url
        if self.android_popup_activity is not None:
            result['AndroidPopupActivity'] = self.android_popup_activity
        if self.android_popup_body is not None:
            result['AndroidPopupBody'] = self.android_popup_body
        if self.android_popup_title is not None:
            result['AndroidPopupTitle'] = self.android_popup_title
        if self.android_remind is not None:
            result['AndroidRemind'] = self.android_remind
        if self.android_render_style is not None:
            result['AndroidRenderStyle'] = self.android_render_style
        if self.android_target_user_type is not None:
            result['AndroidTargetUserType'] = self.android_target_user_type
        if self.android_vivo_push_mode is not None:
            result['AndroidVivoPushMode'] = self.android_vivo_push_mode
        if self.android_vivo_receipt_id is not None:
            result['AndroidVivoReceiptId'] = self.android_vivo_receipt_id
        if self.android_xiao_mi_activity is not None:
            result['AndroidXiaoMiActivity'] = self.android_xiao_mi_activity
        if self.android_xiao_mi_notify_body is not None:
            result['AndroidXiaoMiNotifyBody'] = self.android_xiao_mi_notify_body
        if self.android_xiao_mi_notify_title is not None:
            result['AndroidXiaoMiNotifyTitle'] = self.android_xiao_mi_notify_title
        if self.android_xiaomi_big_picture_url is not None:
            result['AndroidXiaomiBigPictureUrl'] = self.android_xiaomi_big_picture_url
        if self.android_xiaomi_image_url is not None:
            result['AndroidXiaomiImageUrl'] = self.android_xiaomi_image_url
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.body is not None:
            result['Body'] = self.body
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.harmony_action is not None:
            result['HarmonyAction'] = self.harmony_action
        if self.harmony_action_type is not None:
            result['HarmonyActionType'] = self.harmony_action_type
        if self.harmony_badge_add_num is not None:
            result['HarmonyBadgeAddNum'] = self.harmony_badge_add_num
        if self.harmony_badge_set_num is not None:
            result['HarmonyBadgeSetNum'] = self.harmony_badge_set_num
        if self.harmony_category is not None:
            result['HarmonyCategory'] = self.harmony_category
        if self.harmony_ext_parameters is not None:
            result['HarmonyExtParameters'] = self.harmony_ext_parameters
        if self.harmony_extension_extra_data is not None:
            result['HarmonyExtensionExtraData'] = self.harmony_extension_extra_data
        if self.harmony_extension_push is not None:
            result['HarmonyExtensionPush'] = self.harmony_extension_push
        if self.harmony_image_url is not None:
            result['HarmonyImageUrl'] = self.harmony_image_url
        if self.harmony_inbox_content is not None:
            result['HarmonyInboxContent'] = self.harmony_inbox_content
        if self.harmony_notification_slot_type is not None:
            result['HarmonyNotificationSlotType'] = self.harmony_notification_slot_type
        if self.harmony_notify_id is not None:
            result['HarmonyNotifyId'] = self.harmony_notify_id
        if self.harmony_receipt_id is not None:
            result['HarmonyReceiptId'] = self.harmony_receipt_id
        if self.harmony_remind is not None:
            result['HarmonyRemind'] = self.harmony_remind
        if self.harmony_remind_body is not None:
            result['HarmonyRemindBody'] = self.harmony_remind_body
        if self.harmony_remind_title is not None:
            result['HarmonyRemindTitle'] = self.harmony_remind_title
        if self.harmony_render_style is not None:
            result['HarmonyRenderStyle'] = self.harmony_render_style
        if self.harmony_test_message is not None:
            result['HarmonyTestMessage'] = self.harmony_test_message
        if self.harmony_uri is not None:
            result['HarmonyUri'] = self.harmony_uri
        if self.idempotent_token is not None:
            result['IdempotentToken'] = self.idempotent_token
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.push_time is not None:
            result['PushTime'] = self.push_time
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.send_channels is not None:
            result['SendChannels'] = self.send_channels
        if self.send_speed is not None:
            result['SendSpeed'] = self.send_speed
        if self.sms_delay_secs is not None:
            result['SmsDelaySecs'] = self.sms_delay_secs
        if self.sms_params is not None:
            result['SmsParams'] = self.sms_params
        if self.sms_send_policy is not None:
            result['SmsSendPolicy'] = self.sms_send_policy
        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name
        if self.sms_template_name is not None:
            result['SmsTemplateName'] = self.sms_template_name
        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        if self.trim is not None:
            result['Trim'] = self.trim
        if self.i_osapns_env is not None:
            result['iOSApnsEnv'] = self.i_osapns_env
        if self.i_osbadge is not None:
            result['iOSBadge'] = self.i_osbadge
        if self.i_osbadge_auto_increment is not None:
            result['iOSBadgeAutoIncrement'] = self.i_osbadge_auto_increment
        if self.i_osext_parameters is not None:
            result['iOSExtParameters'] = self.i_osext_parameters
        if self.i_osinterruption_level is not None:
            result['iOSInterruptionLevel'] = self.i_osinterruption_level
        if self.i_osmusic is not None:
            result['iOSMusic'] = self.i_osmusic
        if self.i_osmutable_content is not None:
            result['iOSMutableContent'] = self.i_osmutable_content
        if self.i_osnotification_category is not None:
            result['iOSNotificationCategory'] = self.i_osnotification_category
        if self.i_osnotification_collapse_id is not None:
            result['iOSNotificationCollapseId'] = self.i_osnotification_collapse_id
        if self.i_osnotification_thread_id is not None:
            result['iOSNotificationThreadId'] = self.i_osnotification_thread_id
        if self.i_osrelevance_score is not None:
            result['iOSRelevanceScore'] = self.i_osrelevance_score
        if self.i_osremind is not None:
            result['iOSRemind'] = self.i_osremind
        if self.i_osremind_body is not None:
            result['iOSRemindBody'] = self.i_osremind_body
        if self.i_ossilent_notification is not None:
            result['iOSSilentNotification'] = self.i_ossilent_notification
        if self.i_ossubtitle is not None:
            result['iOSSubtitle'] = self.i_ossubtitle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidActivity') is not None:
            self.android_activity = m.get('AndroidActivity')
        if m.get('AndroidBadgeAddNum') is not None:
            self.android_badge_add_num = m.get('AndroidBadgeAddNum')
        if m.get('AndroidBadgeClass') is not None:
            self.android_badge_class = m.get('AndroidBadgeClass')
        if m.get('AndroidBadgeSetNum') is not None:
            self.android_badge_set_num = m.get('AndroidBadgeSetNum')
        if m.get('AndroidBigBody') is not None:
            self.android_big_body = m.get('AndroidBigBody')
        if m.get('AndroidBigPictureUrl') is not None:
            self.android_big_picture_url = m.get('AndroidBigPictureUrl')
        if m.get('AndroidBigTitle') is not None:
            self.android_big_title = m.get('AndroidBigTitle')
        if m.get('AndroidExtParameters') is not None:
            self.android_ext_parameters = m.get('AndroidExtParameters')
        if m.get('AndroidHonorTargetUserType') is not None:
            self.android_honor_target_user_type = m.get('AndroidHonorTargetUserType')
        if m.get('AndroidHuaweiReceiptId') is not None:
            self.android_huawei_receipt_id = m.get('AndroidHuaweiReceiptId')
        if m.get('AndroidHuaweiTargetUserType') is not None:
            self.android_huawei_target_user_type = m.get('AndroidHuaweiTargetUserType')
        if m.get('AndroidImageUrl') is not None:
            self.android_image_url = m.get('AndroidImageUrl')
        if m.get('AndroidInboxBody') is not None:
            self.android_inbox_body = m.get('AndroidInboxBody')
        if m.get('AndroidMessageHuaweiCategory') is not None:
            self.android_message_huawei_category = m.get('AndroidMessageHuaweiCategory')
        if m.get('AndroidMessageHuaweiUrgency') is not None:
            self.android_message_huawei_urgency = m.get('AndroidMessageHuaweiUrgency')
        if m.get('AndroidMessageOppoCategory') is not None:
            self.android_message_oppo_category = m.get('AndroidMessageOppoCategory')
        if m.get('AndroidMessageOppoNotifyLevel') is not None:
            self.android_message_oppo_notify_level = m.get('AndroidMessageOppoNotifyLevel')
        if m.get('AndroidMessageVivoCategory') is not None:
            self.android_message_vivo_category = m.get('AndroidMessageVivoCategory')
        if m.get('AndroidMusic') is not None:
            self.android_music = m.get('AndroidMusic')
        if m.get('AndroidNotificationBarPriority') is not None:
            self.android_notification_bar_priority = m.get('AndroidNotificationBarPriority')
        if m.get('AndroidNotificationBarType') is not None:
            self.android_notification_bar_type = m.get('AndroidNotificationBarType')
        if m.get('AndroidNotificationChannel') is not None:
            self.android_notification_channel = m.get('AndroidNotificationChannel')
        if m.get('AndroidNotificationGroup') is not None:
            self.android_notification_group = m.get('AndroidNotificationGroup')
        if m.get('AndroidNotificationHonorChannel') is not None:
            self.android_notification_honor_channel = m.get('AndroidNotificationHonorChannel')
        if m.get('AndroidNotificationHuaweiChannel') is not None:
            self.android_notification_huawei_channel = m.get('AndroidNotificationHuaweiChannel')
        if m.get('AndroidNotificationNotifyId') is not None:
            self.android_notification_notify_id = m.get('AndroidNotificationNotifyId')
        if m.get('AndroidNotificationThreadId') is not None:
            self.android_notification_thread_id = m.get('AndroidNotificationThreadId')
        if m.get('AndroidNotificationVivoChannel') is not None:
            self.android_notification_vivo_channel = m.get('AndroidNotificationVivoChannel')
        if m.get('AndroidNotificationXiaomiChannel') is not None:
            self.android_notification_xiaomi_channel = m.get('AndroidNotificationXiaomiChannel')
        if m.get('AndroidNotifyType') is not None:
            self.android_notify_type = m.get('AndroidNotifyType')
        if m.get('AndroidOpenType') is not None:
            self.android_open_type = m.get('AndroidOpenType')
        if m.get('AndroidOpenUrl') is not None:
            self.android_open_url = m.get('AndroidOpenUrl')
        if m.get('AndroidPopupActivity') is not None:
            self.android_popup_activity = m.get('AndroidPopupActivity')
        if m.get('AndroidPopupBody') is not None:
            self.android_popup_body = m.get('AndroidPopupBody')
        if m.get('AndroidPopupTitle') is not None:
            self.android_popup_title = m.get('AndroidPopupTitle')
        if m.get('AndroidRemind') is not None:
            self.android_remind = m.get('AndroidRemind')
        if m.get('AndroidRenderStyle') is not None:
            self.android_render_style = m.get('AndroidRenderStyle')
        if m.get('AndroidTargetUserType') is not None:
            self.android_target_user_type = m.get('AndroidTargetUserType')
        if m.get('AndroidVivoPushMode') is not None:
            self.android_vivo_push_mode = m.get('AndroidVivoPushMode')
        if m.get('AndroidVivoReceiptId') is not None:
            self.android_vivo_receipt_id = m.get('AndroidVivoReceiptId')
        if m.get('AndroidXiaoMiActivity') is not None:
            self.android_xiao_mi_activity = m.get('AndroidXiaoMiActivity')
        if m.get('AndroidXiaoMiNotifyBody') is not None:
            self.android_xiao_mi_notify_body = m.get('AndroidXiaoMiNotifyBody')
        if m.get('AndroidXiaoMiNotifyTitle') is not None:
            self.android_xiao_mi_notify_title = m.get('AndroidXiaoMiNotifyTitle')
        if m.get('AndroidXiaomiBigPictureUrl') is not None:
            self.android_xiaomi_big_picture_url = m.get('AndroidXiaomiBigPictureUrl')
        if m.get('AndroidXiaomiImageUrl') is not None:
            self.android_xiaomi_image_url = m.get('AndroidXiaomiImageUrl')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HarmonyAction') is not None:
            self.harmony_action = m.get('HarmonyAction')
        if m.get('HarmonyActionType') is not None:
            self.harmony_action_type = m.get('HarmonyActionType')
        if m.get('HarmonyBadgeAddNum') is not None:
            self.harmony_badge_add_num = m.get('HarmonyBadgeAddNum')
        if m.get('HarmonyBadgeSetNum') is not None:
            self.harmony_badge_set_num = m.get('HarmonyBadgeSetNum')
        if m.get('HarmonyCategory') is not None:
            self.harmony_category = m.get('HarmonyCategory')
        if m.get('HarmonyExtParameters') is not None:
            self.harmony_ext_parameters = m.get('HarmonyExtParameters')
        if m.get('HarmonyExtensionExtraData') is not None:
            self.harmony_extension_extra_data = m.get('HarmonyExtensionExtraData')
        if m.get('HarmonyExtensionPush') is not None:
            self.harmony_extension_push = m.get('HarmonyExtensionPush')
        if m.get('HarmonyImageUrl') is not None:
            self.harmony_image_url = m.get('HarmonyImageUrl')
        if m.get('HarmonyInboxContent') is not None:
            self.harmony_inbox_content = m.get('HarmonyInboxContent')
        if m.get('HarmonyNotificationSlotType') is not None:
            self.harmony_notification_slot_type = m.get('HarmonyNotificationSlotType')
        if m.get('HarmonyNotifyId') is not None:
            self.harmony_notify_id = m.get('HarmonyNotifyId')
        if m.get('HarmonyReceiptId') is not None:
            self.harmony_receipt_id = m.get('HarmonyReceiptId')
        if m.get('HarmonyRemind') is not None:
            self.harmony_remind = m.get('HarmonyRemind')
        if m.get('HarmonyRemindBody') is not None:
            self.harmony_remind_body = m.get('HarmonyRemindBody')
        if m.get('HarmonyRemindTitle') is not None:
            self.harmony_remind_title = m.get('HarmonyRemindTitle')
        if m.get('HarmonyRenderStyle') is not None:
            self.harmony_render_style = m.get('HarmonyRenderStyle')
        if m.get('HarmonyTestMessage') is not None:
            self.harmony_test_message = m.get('HarmonyTestMessage')
        if m.get('HarmonyUri') is not None:
            self.harmony_uri = m.get('HarmonyUri')
        if m.get('IdempotentToken') is not None:
            self.idempotent_token = m.get('IdempotentToken')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('SendChannels') is not None:
            self.send_channels = m.get('SendChannels')
        if m.get('SendSpeed') is not None:
            self.send_speed = m.get('SendSpeed')
        if m.get('SmsDelaySecs') is not None:
            self.sms_delay_secs = m.get('SmsDelaySecs')
        if m.get('SmsParams') is not None:
            self.sms_params = m.get('SmsParams')
        if m.get('SmsSendPolicy') is not None:
            self.sms_send_policy = m.get('SmsSendPolicy')
        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')
        if m.get('SmsTemplateName') is not None:
            self.sms_template_name = m.get('SmsTemplateName')
        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Trim') is not None:
            self.trim = m.get('Trim')
        if m.get('iOSApnsEnv') is not None:
            self.i_osapns_env = m.get('iOSApnsEnv')
        if m.get('iOSBadge') is not None:
            self.i_osbadge = m.get('iOSBadge')
        if m.get('iOSBadgeAutoIncrement') is not None:
            self.i_osbadge_auto_increment = m.get('iOSBadgeAutoIncrement')
        if m.get('iOSExtParameters') is not None:
            self.i_osext_parameters = m.get('iOSExtParameters')
        if m.get('iOSInterruptionLevel') is not None:
            self.i_osinterruption_level = m.get('iOSInterruptionLevel')
        if m.get('iOSMusic') is not None:
            self.i_osmusic = m.get('iOSMusic')
        if m.get('iOSMutableContent') is not None:
            self.i_osmutable_content = m.get('iOSMutableContent')
        if m.get('iOSNotificationCategory') is not None:
            self.i_osnotification_category = m.get('iOSNotificationCategory')
        if m.get('iOSNotificationCollapseId') is not None:
            self.i_osnotification_collapse_id = m.get('iOSNotificationCollapseId')
        if m.get('iOSNotificationThreadId') is not None:
            self.i_osnotification_thread_id = m.get('iOSNotificationThreadId')
        if m.get('iOSRelevanceScore') is not None:
            self.i_osrelevance_score = m.get('iOSRelevanceScore')
        if m.get('iOSRemind') is not None:
            self.i_osremind = m.get('iOSRemind')
        if m.get('iOSRemindBody') is not None:
            self.i_osremind_body = m.get('iOSRemindBody')
        if m.get('iOSSilentNotification') is not None:
            self.i_ossilent_notification = m.get('iOSSilentNotification')
        if m.get('iOSSubtitle') is not None:
            self.i_ossubtitle = m.get('iOSSubtitle')
        return self


class PushResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushResponseBody = None,
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
            temp_model = PushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushMessageToAndroidRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        body: str = None,
        job_key: str = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.body = body
        self.job_key = job_key
        self.store_offline = store_offline
        # This parameter is required.
        self.target = target
        # This parameter is required.
        self.target_value = target_value
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.body is not None:
            result['Body'] = self.body
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PushMessageToAndroidResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushMessageToAndroidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushMessageToAndroidResponseBody = None,
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
            temp_model = PushMessageToAndroidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushMessageToiOSRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        body: str = None,
        job_key: str = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.body = body
        self.job_key = job_key
        self.store_offline = store_offline
        # This parameter is required.
        self.target = target
        # This parameter is required.
        self.target_value = target_value
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.body is not None:
            result['Body'] = self.body
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PushMessageToiOSResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushMessageToiOSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushMessageToiOSResponseBody = None,
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
            temp_model = PushMessageToiOSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushNoticeToAndroidRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        body: str = None,
        ext_parameters: str = None,
        job_key: str = None,
        store_offline: bool = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.body = body
        self.ext_parameters = ext_parameters
        self.job_key = job_key
        self.store_offline = store_offline
        # This parameter is required.
        self.target = target
        # This parameter is required.
        self.target_value = target_value
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.body is not None:
            result['Body'] = self.body
        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PushNoticeToAndroidResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushNoticeToAndroidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushNoticeToAndroidResponseBody = None,
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
            temp_model = PushNoticeToAndroidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushNoticeToiOSRequest(TeaModel):
    def __init__(
        self,
        apns_env: str = None,
        app_key: int = None,
        body: str = None,
        ext_parameters: str = None,
        job_key: str = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.apns_env = apns_env
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.body = body
        self.ext_parameters = ext_parameters
        self.job_key = job_key
        # This parameter is required.
        self.target = target
        # This parameter is required.
        self.target_value = target_value
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apns_env is not None:
            result['ApnsEnv'] = self.apns_env
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.body is not None:
            result['Body'] = self.body
        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApnsEnv') is not None:
            self.apns_env = m.get('ApnsEnv')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class PushNoticeToiOSResponseBody(TeaModel):
    def __init__(
        self,
        message_id: str = None,
        request_id: str = None,
    ):
        self.message_id = message_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PushNoticeToiOSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushNoticeToiOSResponseBody = None,
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
            temp_model = PushNoticeToiOSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAliasesRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class QueryAliasesResponseBodyAliasInfosAliasInfo(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
    ):
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        return self


class QueryAliasesResponseBodyAliasInfos(TeaModel):
    def __init__(
        self,
        alias_info: List[QueryAliasesResponseBodyAliasInfosAliasInfo] = None,
    ):
        self.alias_info = alias_info

    def validate(self):
        if self.alias_info:
            for k in self.alias_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AliasInfo'] = []
        if self.alias_info is not None:
            for k in self.alias_info:
                result['AliasInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alias_info = []
        if m.get('AliasInfo') is not None:
            for k in m.get('AliasInfo'):
                temp_model = QueryAliasesResponseBodyAliasInfosAliasInfo()
                self.alias_info.append(temp_model.from_map(k))
        return self


class QueryAliasesResponseBody(TeaModel):
    def __init__(
        self,
        alias_infos: QueryAliasesResponseBodyAliasInfos = None,
        request_id: str = None,
    ):
        self.alias_infos = alias_infos
        self.request_id = request_id

    def validate(self):
        if self.alias_infos:
            self.alias_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_infos is not None:
            result['AliasInfos'] = self.alias_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasInfos') is not None:
            temp_model = QueryAliasesResponseBodyAliasInfos()
            self.alias_infos = temp_model.from_map(m['AliasInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAliasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAliasesResponseBody = None,
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
            temp_model = QueryAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class QueryDeviceInfoResponseBodyDeviceInfo(TeaModel):
    def __init__(
        self,
        account: str = None,
        alias: str = None,
        brand: str = None,
        device_id: str = None,
        device_token: str = None,
        device_type: str = None,
        last_online_time: str = None,
        model: str = None,
        online: bool = None,
        phone_number: str = None,
        push_enabled: bool = None,
        tags: str = None,
    ):
        self.account = account
        self.alias = alias
        self.brand = brand
        self.device_id = device_id
        self.device_token = device_token
        self.device_type = device_type
        self.last_online_time = last_online_time
        self.model = model
        self.online = online
        self.phone_number = phone_number
        self.push_enabled = push_enabled
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.last_online_time is not None:
            result['LastOnlineTime'] = self.last_online_time
        if self.model is not None:
            result['Model'] = self.model
        if self.online is not None:
            result['Online'] = self.online
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.push_enabled is not None:
            result['PushEnabled'] = self.push_enabled
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('LastOnlineTime') is not None:
            self.last_online_time = m.get('LastOnlineTime')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PushEnabled') is not None:
            self.push_enabled = m.get('PushEnabled')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class QueryDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        device_info: QueryDeviceInfoResponseBodyDeviceInfo = None,
        request_id: str = None,
    ):
        self.device_info = device_info
        self.request_id = request_id

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = QueryDeviceInfoResponseBodyDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceInfoResponseBody = None,
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
            temp_model = QueryDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceStatRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_type: str = None,
        end_time: str = None,
        query_type: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.device_type = device_type
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.query_type = query_type
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryDeviceStatResponseBodyAppDeviceStatsAppDeviceStat(TeaModel):
    def __init__(
        self,
        count: int = None,
        device_type: str = None,
        time: str = None,
    ):
        self.count = count
        self.device_type = device_type
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryDeviceStatResponseBodyAppDeviceStats(TeaModel):
    def __init__(
        self,
        app_device_stat: List[QueryDeviceStatResponseBodyAppDeviceStatsAppDeviceStat] = None,
    ):
        self.app_device_stat = app_device_stat

    def validate(self):
        if self.app_device_stat:
            for k in self.app_device_stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppDeviceStat'] = []
        if self.app_device_stat is not None:
            for k in self.app_device_stat:
                result['AppDeviceStat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_device_stat = []
        if m.get('AppDeviceStat') is not None:
            for k in m.get('AppDeviceStat'):
                temp_model = QueryDeviceStatResponseBodyAppDeviceStatsAppDeviceStat()
                self.app_device_stat.append(temp_model.from_map(k))
        return self


class QueryDeviceStatResponseBody(TeaModel):
    def __init__(
        self,
        app_device_stats: QueryDeviceStatResponseBodyAppDeviceStats = None,
        request_id: str = None,
    ):
        self.app_device_stats = app_device_stats
        self.request_id = request_id

    def validate(self):
        if self.app_device_stats:
            self.app_device_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_device_stats is not None:
            result['AppDeviceStats'] = self.app_device_stats.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDeviceStats') is not None:
            temp_model = QueryDeviceStatResponseBodyAppDeviceStats()
            self.app_device_stats = temp_model.from_map(m['AppDeviceStats'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDeviceStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceStatResponseBody = None,
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
            temp_model = QueryDeviceStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicesByAccountRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        app_key: int = None,
    ):
        # This parameter is required.
        self.account = account
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class QueryDevicesByAccountResponseBodyDeviceIds(TeaModel):
    def __init__(
        self,
        device_id: List[str] = None,
    ):
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class QueryDevicesByAccountResponseBody(TeaModel):
    def __init__(
        self,
        device_ids: QueryDevicesByAccountResponseBodyDeviceIds = None,
        request_id: str = None,
    ):
        self.device_ids = device_ids
        self.request_id = request_id

    def validate(self):
        if self.device_ids:
            self.device_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            temp_model = QueryDevicesByAccountResponseBodyDeviceIds()
            self.device_ids = temp_model.from_map(m['DeviceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDevicesByAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDevicesByAccountResponseBody = None,
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
            temp_model = QueryDevicesByAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicesByAliasRequest(TeaModel):
    def __init__(
        self,
        alias: str = None,
        app_key: int = None,
    ):
        # This parameter is required.
        self.alias = alias
        # This parameter is required.
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class QueryDevicesByAliasResponseBodyDeviceIds(TeaModel):
    def __init__(
        self,
        device_id: List[str] = None,
    ):
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class QueryDevicesByAliasResponseBody(TeaModel):
    def __init__(
        self,
        device_ids: QueryDevicesByAliasResponseBodyDeviceIds = None,
        request_id: str = None,
    ):
        self.device_ids = device_ids
        self.request_id = request_id

    def validate(self):
        if self.device_ids:
            self.device_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            temp_model = QueryDevicesByAliasResponseBodyDeviceIds()
            self.device_ids = temp_model.from_map(m['DeviceIds'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDevicesByAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDevicesByAliasResponseBody = None,
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
            temp_model = QueryDevicesByAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushRecordsRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        end_time: str = None,
        keyword: str = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        push_type: str = None,
        source: str = None,
        start_time: str = None,
        target: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.end_time = end_time
        self.keyword = keyword
        self.next_token = next_token
        self.page = page
        self.page_size = page_size
        self.push_type = push_type
        self.source = source
        # This parameter is required.
        self.start_time = start_time
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.source is not None:
            result['Source'] = self.source
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class QueryPushRecordsResponseBodyPushInfosPushInfo(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        body: str = None,
        device_type: str = None,
        message_id: str = None,
        push_time: str = None,
        push_type: str = None,
        source: str = None,
        status: str = None,
        target: str = None,
        title: str = None,
    ):
        self.app_key = app_key
        self.body = body
        self.device_type = device_type
        self.message_id = message_id
        self.push_time = push_time
        self.push_type = push_type
        self.source = source
        self.status = status
        self.target = target
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.body is not None:
            result['Body'] = self.body
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.push_time is not None:
            result['PushTime'] = self.push_time
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.target is not None:
            result['Target'] = self.target
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class QueryPushRecordsResponseBodyPushInfos(TeaModel):
    def __init__(
        self,
        push_info: List[QueryPushRecordsResponseBodyPushInfosPushInfo] = None,
    ):
        self.push_info = push_info

    def validate(self):
        if self.push_info:
            for k in self.push_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PushInfo'] = []
        if self.push_info is not None:
            for k in self.push_info:
                result['PushInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_info = []
        if m.get('PushInfo') is not None:
            for k in m.get('PushInfo'):
                temp_model = QueryPushRecordsResponseBodyPushInfosPushInfo()
                self.push_info.append(temp_model.from_map(k))
        return self


class QueryPushRecordsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        push_infos: QueryPushRecordsResponseBodyPushInfos = None,
        request_id: str = None,
        total: int = None,
    ):
        self.next_token = next_token
        self.page = page
        self.page_size = page_size
        self.push_infos = push_infos
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.push_infos:
            self.push_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.push_infos is not None:
            result['PushInfos'] = self.push_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PushInfos') is not None:
            temp_model = QueryPushRecordsResponseBodyPushInfos()
            self.push_infos = temp_model.from_map(m['PushInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPushRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPushRecordsResponseBody = None,
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
            temp_model = QueryPushRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushStatByAppRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        end_time: str = None,
        granularity: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.granularity = granularity
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryPushStatByAppResponseBodyAppPushStatsAppPushStat(TeaModel):
    def __init__(
        self,
        accept_count: int = None,
        deleted_count: int = None,
        opened_count: int = None,
        received_count: int = None,
        sent_count: int = None,
        sms_failed_count: int = None,
        sms_receive_failed_count: int = None,
        sms_receive_success_count: int = None,
        sms_sent_count: int = None,
        sms_skip_count: int = None,
        time: str = None,
    ):
        self.accept_count = accept_count
        self.deleted_count = deleted_count
        self.opened_count = opened_count
        self.received_count = received_count
        self.sent_count = sent_count
        self.sms_failed_count = sms_failed_count
        self.sms_receive_failed_count = sms_receive_failed_count
        self.sms_receive_success_count = sms_receive_success_count
        self.sms_sent_count = sms_sent_count
        self.sms_skip_count = sms_skip_count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_count is not None:
            result['AcceptCount'] = self.accept_count
        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count
        if self.opened_count is not None:
            result['OpenedCount'] = self.opened_count
        if self.received_count is not None:
            result['ReceivedCount'] = self.received_count
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.sms_failed_count is not None:
            result['SmsFailedCount'] = self.sms_failed_count
        if self.sms_receive_failed_count is not None:
            result['SmsReceiveFailedCount'] = self.sms_receive_failed_count
        if self.sms_receive_success_count is not None:
            result['SmsReceiveSuccessCount'] = self.sms_receive_success_count
        if self.sms_sent_count is not None:
            result['SmsSentCount'] = self.sms_sent_count
        if self.sms_skip_count is not None:
            result['SmsSkipCount'] = self.sms_skip_count
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptCount') is not None:
            self.accept_count = m.get('AcceptCount')
        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')
        if m.get('OpenedCount') is not None:
            self.opened_count = m.get('OpenedCount')
        if m.get('ReceivedCount') is not None:
            self.received_count = m.get('ReceivedCount')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('SmsFailedCount') is not None:
            self.sms_failed_count = m.get('SmsFailedCount')
        if m.get('SmsReceiveFailedCount') is not None:
            self.sms_receive_failed_count = m.get('SmsReceiveFailedCount')
        if m.get('SmsReceiveSuccessCount') is not None:
            self.sms_receive_success_count = m.get('SmsReceiveSuccessCount')
        if m.get('SmsSentCount') is not None:
            self.sms_sent_count = m.get('SmsSentCount')
        if m.get('SmsSkipCount') is not None:
            self.sms_skip_count = m.get('SmsSkipCount')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryPushStatByAppResponseBodyAppPushStats(TeaModel):
    def __init__(
        self,
        app_push_stat: List[QueryPushStatByAppResponseBodyAppPushStatsAppPushStat] = None,
    ):
        self.app_push_stat = app_push_stat

    def validate(self):
        if self.app_push_stat:
            for k in self.app_push_stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppPushStat'] = []
        if self.app_push_stat is not None:
            for k in self.app_push_stat:
                result['AppPushStat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_push_stat = []
        if m.get('AppPushStat') is not None:
            for k in m.get('AppPushStat'):
                temp_model = QueryPushStatByAppResponseBodyAppPushStatsAppPushStat()
                self.app_push_stat.append(temp_model.from_map(k))
        return self


class QueryPushStatByAppResponseBody(TeaModel):
    def __init__(
        self,
        app_push_stats: QueryPushStatByAppResponseBodyAppPushStats = None,
        request_id: str = None,
    ):
        self.app_push_stats = app_push_stats
        self.request_id = request_id

    def validate(self):
        if self.app_push_stats:
            self.app_push_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_push_stats is not None:
            result['AppPushStats'] = self.app_push_stats.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppPushStats') is not None:
            temp_model = QueryPushStatByAppResponseBodyAppPushStats()
            self.app_push_stats = temp_model.from_map(m['AppPushStats'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPushStatByAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPushStatByAppResponseBody = None,
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
            temp_model = QueryPushStatByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushStatByMsgRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        message_id: int = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class QueryPushStatByMsgResponseBodyPushStatsPushStat(TeaModel):
    def __init__(
        self,
        accept_count: int = None,
        deleted_count: int = None,
        message_id: str = None,
        opened_count: int = None,
        received_count: int = None,
        sent_count: int = None,
        sms_failed_count: int = None,
        sms_receive_failed_count: int = None,
        sms_receive_success_count: int = None,
        sms_sent_count: int = None,
        sms_skip_count: int = None,
    ):
        self.accept_count = accept_count
        self.deleted_count = deleted_count
        self.message_id = message_id
        self.opened_count = opened_count
        self.received_count = received_count
        self.sent_count = sent_count
        self.sms_failed_count = sms_failed_count
        self.sms_receive_failed_count = sms_receive_failed_count
        self.sms_receive_success_count = sms_receive_success_count
        self.sms_sent_count = sms_sent_count
        self.sms_skip_count = sms_skip_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_count is not None:
            result['AcceptCount'] = self.accept_count
        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.opened_count is not None:
            result['OpenedCount'] = self.opened_count
        if self.received_count is not None:
            result['ReceivedCount'] = self.received_count
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.sms_failed_count is not None:
            result['SmsFailedCount'] = self.sms_failed_count
        if self.sms_receive_failed_count is not None:
            result['SmsReceiveFailedCount'] = self.sms_receive_failed_count
        if self.sms_receive_success_count is not None:
            result['SmsReceiveSuccessCount'] = self.sms_receive_success_count
        if self.sms_sent_count is not None:
            result['SmsSentCount'] = self.sms_sent_count
        if self.sms_skip_count is not None:
            result['SmsSkipCount'] = self.sms_skip_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptCount') is not None:
            self.accept_count = m.get('AcceptCount')
        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('OpenedCount') is not None:
            self.opened_count = m.get('OpenedCount')
        if m.get('ReceivedCount') is not None:
            self.received_count = m.get('ReceivedCount')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('SmsFailedCount') is not None:
            self.sms_failed_count = m.get('SmsFailedCount')
        if m.get('SmsReceiveFailedCount') is not None:
            self.sms_receive_failed_count = m.get('SmsReceiveFailedCount')
        if m.get('SmsReceiveSuccessCount') is not None:
            self.sms_receive_success_count = m.get('SmsReceiveSuccessCount')
        if m.get('SmsSentCount') is not None:
            self.sms_sent_count = m.get('SmsSentCount')
        if m.get('SmsSkipCount') is not None:
            self.sms_skip_count = m.get('SmsSkipCount')
        return self


class QueryPushStatByMsgResponseBodyPushStats(TeaModel):
    def __init__(
        self,
        push_stat: List[QueryPushStatByMsgResponseBodyPushStatsPushStat] = None,
    ):
        self.push_stat = push_stat

    def validate(self):
        if self.push_stat:
            for k in self.push_stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PushStat'] = []
        if self.push_stat is not None:
            for k in self.push_stat:
                result['PushStat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.push_stat = []
        if m.get('PushStat') is not None:
            for k in m.get('PushStat'):
                temp_model = QueryPushStatByMsgResponseBodyPushStatsPushStat()
                self.push_stat.append(temp_model.from_map(k))
        return self


class QueryPushStatByMsgResponseBody(TeaModel):
    def __init__(
        self,
        push_stats: QueryPushStatByMsgResponseBodyPushStats = None,
        request_id: str = None,
    ):
        self.push_stats = push_stats
        self.request_id = request_id

    def validate(self):
        if self.push_stats:
            self.push_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.push_stats is not None:
            result['PushStats'] = self.push_stats.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushStats') is not None:
            temp_model = QueryPushStatByMsgResponseBodyPushStats()
            self.push_stats = temp_model.from_map(m['PushStats'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPushStatByMsgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryPushStatByMsgResponseBody = None,
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
            temp_model = QueryPushStatByMsgResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagsRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        client_key: str = None,
        key_type: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.client_key = client_key
        # This parameter is required.
        self.key_type = key_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.client_key is not None:
            result['ClientKey'] = self.client_key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ClientKey') is not None:
            self.client_key = m.get('ClientKey')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        return self


class QueryTagsResponseBodyTagInfosTagInfo(TeaModel):
    def __init__(
        self,
        tag_name: str = None,
    ):
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class QueryTagsResponseBodyTagInfos(TeaModel):
    def __init__(
        self,
        tag_info: List[QueryTagsResponseBodyTagInfosTagInfo] = None,
    ):
        self.tag_info = tag_info

    def validate(self):
        if self.tag_info:
            for k in self.tag_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagInfo'] = []
        if self.tag_info is not None:
            for k in self.tag_info:
                result['TagInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_info = []
        if m.get('TagInfo') is not None:
            for k in m.get('TagInfo'):
                temp_model = QueryTagsResponseBodyTagInfosTagInfo()
                self.tag_info.append(temp_model.from_map(k))
        return self


class QueryTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tag_infos: QueryTagsResponseBodyTagInfos = None,
    ):
        self.request_id = request_id
        self.tag_infos = tag_infos

    def validate(self):
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagInfos') is not None:
            temp_model = QueryTagsResponseBodyTagInfos()
            self.tag_infos = temp_model.from_map(m['TagInfos'])
        return self


class QueryTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTagsResponseBody = None,
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
            temp_model = QueryTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUniqueDeviceStatRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        end_time: str = None,
        granularity: str = None,
        start_time: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.granularity = granularity
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryUniqueDeviceStatResponseBodyAppDeviceStatsAppDeviceStat(TeaModel):
    def __init__(
        self,
        count: int = None,
        time: str = None,
    ):
        self.count = count
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryUniqueDeviceStatResponseBodyAppDeviceStats(TeaModel):
    def __init__(
        self,
        app_device_stat: List[QueryUniqueDeviceStatResponseBodyAppDeviceStatsAppDeviceStat] = None,
    ):
        self.app_device_stat = app_device_stat

    def validate(self):
        if self.app_device_stat:
            for k in self.app_device_stat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppDeviceStat'] = []
        if self.app_device_stat is not None:
            for k in self.app_device_stat:
                result['AppDeviceStat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_device_stat = []
        if m.get('AppDeviceStat') is not None:
            for k in m.get('AppDeviceStat'):
                temp_model = QueryUniqueDeviceStatResponseBodyAppDeviceStatsAppDeviceStat()
                self.app_device_stat.append(temp_model.from_map(k))
        return self


class QueryUniqueDeviceStatResponseBody(TeaModel):
    def __init__(
        self,
        app_device_stats: QueryUniqueDeviceStatResponseBodyAppDeviceStats = None,
        request_id: str = None,
    ):
        self.app_device_stats = app_device_stats
        self.request_id = request_id

    def validate(self):
        if self.app_device_stats:
            self.app_device_stats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_device_stats is not None:
            result['AppDeviceStats'] = self.app_device_stats.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDeviceStats') is not None:
            temp_model = QueryUniqueDeviceStatResponseBodyAppDeviceStats()
            self.app_device_stats = temp_model.from_map(m['AppDeviceStats'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryUniqueDeviceStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUniqueDeviceStatResponseBody = None,
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
            temp_model = QueryUniqueDeviceStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTagRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        tag_name: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class RemoveTagResponseBody(TeaModel):
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


class RemoveTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveTagResponseBody = None,
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
            temp_model = RemoveTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAliasRequest(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        app_key: int = None,
        device_id: str = None,
        unbind_all: bool = None,
    ):
        self.alias_name = alias_name
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id
        self.unbind_all = unbind_all

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.unbind_all is not None:
            result['UnbindAll'] = self.unbind_all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UnbindAll') is not None:
            self.unbind_all = m.get('UnbindAll')
        return self


class UnbindAliasResponseBody(TeaModel):
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


class UnbindAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindAliasResponseBody = None,
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
            temp_model = UnbindAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindPhoneRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class UnbindPhoneResponseBody(TeaModel):
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


class UnbindPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindPhoneResponseBody = None,
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
            temp_model = UnbindPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindTagRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        client_key: str = None,
        key_type: str = None,
        tag_name: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.client_key = client_key
        # This parameter is required.
        self.key_type = key_type
        # This parameter is required.
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.client_key is not None:
            result['ClientKey'] = self.client_key
        if self.key_type is not None:
            result['KeyType'] = self.key_type
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ClientKey') is not None:
            self.client_key = m.get('ClientKey')
        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class UnbindTagResponseBody(TeaModel):
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


class UnbindTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindTagResponseBody = None,
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
            temp_model = UnbindTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


