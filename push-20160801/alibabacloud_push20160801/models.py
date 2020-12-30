# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class BindAliasRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
        alias_name: str = None,
    ):
        self.app_key = app_key
        self.device_id = device_id
        self.alias_name = alias_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
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
        body: BindAliasResponseBody = None,
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
        self.app_key = app_key
        self.device_id = device_id
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
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
        body: BindPhoneResponseBody = None,
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
        self.app_key = app_key
        self.client_key = client_key
        self.key_type = key_type
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
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
        body: BindTagResponseBody = None,
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
            temp_model = BindTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelPushRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        message_id: int = None,
    ):
        self.app_key = app_key
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
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
        body: CancelPushResponseBody = None,
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
            temp_model = CancelPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDeviceRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
    ):
        self.app_key = app_key
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
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
        request_id: str = None,
        available: bool = None,
    ):
        self.request_id = request_id
        self.available = available

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available is not None:
            result['Available'] = self.available
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Available') is not None:
            self.available = m.get('Available')
        return self


class CheckDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckDeviceResponseBody = None,
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
            temp_model = CheckDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckDevicesRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_ids: str = None,
    ):
        self.app_key = app_key
        self.device_ids = device_ids

    def validate(self):
        pass

    def to_map(self):
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
        device_id: str = None,
        available: bool = None,
    ):
        self.device_id = device_id
        self.available = available

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.available is not None:
            result['Available'] = self.available
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Available') is not None:
            self.available = m.get('Available')
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
        request_id: str = None,
        device_check_infos: CheckDevicesResponseBodyDeviceCheckInfos = None,
    ):
        self.request_id = request_id
        self.device_check_infos = device_check_infos

    def validate(self):
        if self.device_check_infos:
            self.device_check_infos.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_check_infos is not None:
            result['DeviceCheckInfos'] = self.device_check_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceCheckInfos') is not None:
            temp_model = CheckDevicesResponseBodyDeviceCheckInfos()
            self.device_check_infos = temp_model.from_map(m['DeviceCheckInfos'])
        return self


class CheckDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckDevicesResponseBody = None,
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
            temp_model = CheckDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteContinuouslyPushRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        message_id: str = None,
    ):
        self.app_key = app_key
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
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
        request_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class CompleteContinuouslyPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CompleteContinuouslyPushResponseBody = None,
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
        self.app_key = app_key
        self.message_id = message_id
        self.target = target
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
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
        request_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class ContinuouslyPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ContinuouslyPushResponseBody = None,
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
            temp_model = ContinuouslyPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSummaryAppsResponseBodySummaryAppInfosSummaryAppInfo(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_key: int = None,
    ):
        self.app_name = app_name
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
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
        body: ListSummaryAppsResponseBody = None,
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
            temp_model = ListSummaryAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
    ):
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
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
        tag_infos: ListTagsResponseBodyTagInfos = None,
        request_id: str = None,
    ):
        self.tag_infos = tag_infos
        self.request_id = request_id

    def validate(self):
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        result = dict()
        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagInfos') is not None:
            temp_model = ListTagsResponseBodyTagInfos()
            self.tag_infos = temp_model.from_map(m['TagInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagsResponseBody = None,
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
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MassPushRequestPushTask(TeaModel):
    def __init__(
        self,
        job_key: str = None,
        i_osnotification_collapse_id: str = None,
        i_ossilent_notification: bool = None,
        store_offline: bool = None,
        i_osnotification_category: str = None,
        i_ossubtitle: str = None,
        android_notification_channel: str = None,
        android_notification_huawei_channel: str = None,
        i_osapns_env: str = None,
        i_osbadge_auto_increment: bool = None,
        android_xiao_mi_notify_title: str = None,
        android_notification_xiaomi_channel: str = None,
        android_xiao_mi_activity: str = None,
        android_popup_title: str = None,
        i_osremind_body: str = None,
        android_activity: str = None,
        android_notify_type: str = None,
        i_osmutable_content: bool = None,
        target: str = None,
        android_open_url: str = None,
        android_notification_notify_id: int = None,
        expire_time: str = None,
        android_notification_vivo_channel: str = None,
        android_open_type: str = None,
        device_type: str = None,
        android_popup_activity: str = None,
        android_remind: bool = None,
        android_popup_body: str = None,
        android_ext_parameters: str = None,
        i_osext_parameters: str = None,
        android_xiao_mi_notify_body: str = None,
        body: str = None,
        android_notification_bar_type: int = None,
        android_notification_bar_priority: int = None,
        target_value: str = None,
        i_osmusic: str = None,
        i_osremind: bool = None,
        push_type: str = None,
        i_osbadge: int = None,
        send_speed: int = None,
        title: str = None,
        push_time: str = None,
        android_music: str = None,
    ):
        self.job_key = job_key
        self.i_osnotification_collapse_id = i_osnotification_collapse_id
        self.i_ossilent_notification = i_ossilent_notification
        self.store_offline = store_offline
        self.i_osnotification_category = i_osnotification_category
        self.i_ossubtitle = i_ossubtitle
        self.android_notification_channel = android_notification_channel
        self.android_notification_huawei_channel = android_notification_huawei_channel
        self.i_osapns_env = i_osapns_env
        self.i_osbadge_auto_increment = i_osbadge_auto_increment
        self.android_xiao_mi_notify_title = android_xiao_mi_notify_title
        self.android_notification_xiaomi_channel = android_notification_xiaomi_channel
        self.android_xiao_mi_activity = android_xiao_mi_activity
        self.android_popup_title = android_popup_title
        self.i_osremind_body = i_osremind_body
        self.android_activity = android_activity
        self.android_notify_type = android_notify_type
        self.i_osmutable_content = i_osmutable_content
        self.target = target
        self.android_open_url = android_open_url
        self.android_notification_notify_id = android_notification_notify_id
        self.expire_time = expire_time
        self.android_notification_vivo_channel = android_notification_vivo_channel
        self.android_open_type = android_open_type
        self.device_type = device_type
        self.android_popup_activity = android_popup_activity
        self.android_remind = android_remind
        self.android_popup_body = android_popup_body
        self.android_ext_parameters = android_ext_parameters
        self.i_osext_parameters = i_osext_parameters
        self.android_xiao_mi_notify_body = android_xiao_mi_notify_body
        self.body = body
        self.android_notification_bar_type = android_notification_bar_type
        self.android_notification_bar_priority = android_notification_bar_priority
        self.target_value = target_value
        self.i_osmusic = i_osmusic
        self.i_osremind = i_osremind
        self.push_type = push_type
        self.i_osbadge = i_osbadge
        self.send_speed = send_speed
        self.title = title
        self.push_time = push_time
        self.android_music = android_music

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.i_osnotification_collapse_id is not None:
            result['iOSNotificationCollapseId'] = self.i_osnotification_collapse_id
        if self.i_ossilent_notification is not None:
            result['iOSSilentNotification'] = self.i_ossilent_notification
        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline
        if self.i_osnotification_category is not None:
            result['iOSNotificationCategory'] = self.i_osnotification_category
        if self.i_ossubtitle is not None:
            result['iOSSubtitle'] = self.i_ossubtitle
        if self.android_notification_channel is not None:
            result['AndroidNotificationChannel'] = self.android_notification_channel
        if self.android_notification_huawei_channel is not None:
            result['AndroidNotificationHuaweiChannel'] = self.android_notification_huawei_channel
        if self.i_osapns_env is not None:
            result['iOSApnsEnv'] = self.i_osapns_env
        if self.i_osbadge_auto_increment is not None:
            result['iOSBadgeAutoIncrement'] = self.i_osbadge_auto_increment
        if self.android_xiao_mi_notify_title is not None:
            result['AndroidXiaoMiNotifyTitle'] = self.android_xiao_mi_notify_title
        if self.android_notification_xiaomi_channel is not None:
            result['AndroidNotificationXiaomiChannel'] = self.android_notification_xiaomi_channel
        if self.android_xiao_mi_activity is not None:
            result['AndroidXiaoMiActivity'] = self.android_xiao_mi_activity
        if self.android_popup_title is not None:
            result['AndroidPopupTitle'] = self.android_popup_title
        if self.i_osremind_body is not None:
            result['iOSRemindBody'] = self.i_osremind_body
        if self.android_activity is not None:
            result['AndroidActivity'] = self.android_activity
        if self.android_notify_type is not None:
            result['AndroidNotifyType'] = self.android_notify_type
        if self.i_osmutable_content is not None:
            result['iOSMutableContent'] = self.i_osmutable_content
        if self.target is not None:
            result['Target'] = self.target
        if self.android_open_url is not None:
            result['AndroidOpenUrl'] = self.android_open_url
        if self.android_notification_notify_id is not None:
            result['AndroidNotificationNotifyId'] = self.android_notification_notify_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.android_notification_vivo_channel is not None:
            result['AndroidNotificationVivoChannel'] = self.android_notification_vivo_channel
        if self.android_open_type is not None:
            result['AndroidOpenType'] = self.android_open_type
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.android_popup_activity is not None:
            result['AndroidPopupActivity'] = self.android_popup_activity
        if self.android_remind is not None:
            result['AndroidRemind'] = self.android_remind
        if self.android_popup_body is not None:
            result['AndroidPopupBody'] = self.android_popup_body
        if self.android_ext_parameters is not None:
            result['AndroidExtParameters'] = self.android_ext_parameters
        if self.i_osext_parameters is not None:
            result['iOSExtParameters'] = self.i_osext_parameters
        if self.android_xiao_mi_notify_body is not None:
            result['AndroidXiaoMiNotifyBody'] = self.android_xiao_mi_notify_body
        if self.body is not None:
            result['Body'] = self.body
        if self.android_notification_bar_type is not None:
            result['AndroidNotificationBarType'] = self.android_notification_bar_type
        if self.android_notification_bar_priority is not None:
            result['AndroidNotificationBarPriority'] = self.android_notification_bar_priority
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.i_osmusic is not None:
            result['iOSMusic'] = self.i_osmusic
        if self.i_osremind is not None:
            result['iOSRemind'] = self.i_osremind
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.i_osbadge is not None:
            result['iOSBadge'] = self.i_osbadge
        if self.send_speed is not None:
            result['SendSpeed'] = self.send_speed
        if self.title is not None:
            result['Title'] = self.title
        if self.push_time is not None:
            result['PushTime'] = self.push_time
        if self.android_music is not None:
            result['AndroidMusic'] = self.android_music
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('iOSNotificationCollapseId') is not None:
            self.i_osnotification_collapse_id = m.get('iOSNotificationCollapseId')
        if m.get('iOSSilentNotification') is not None:
            self.i_ossilent_notification = m.get('iOSSilentNotification')
        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')
        if m.get('iOSNotificationCategory') is not None:
            self.i_osnotification_category = m.get('iOSNotificationCategory')
        if m.get('iOSSubtitle') is not None:
            self.i_ossubtitle = m.get('iOSSubtitle')
        if m.get('AndroidNotificationChannel') is not None:
            self.android_notification_channel = m.get('AndroidNotificationChannel')
        if m.get('AndroidNotificationHuaweiChannel') is not None:
            self.android_notification_huawei_channel = m.get('AndroidNotificationHuaweiChannel')
        if m.get('iOSApnsEnv') is not None:
            self.i_osapns_env = m.get('iOSApnsEnv')
        if m.get('iOSBadgeAutoIncrement') is not None:
            self.i_osbadge_auto_increment = m.get('iOSBadgeAutoIncrement')
        if m.get('AndroidXiaoMiNotifyTitle') is not None:
            self.android_xiao_mi_notify_title = m.get('AndroidXiaoMiNotifyTitle')
        if m.get('AndroidNotificationXiaomiChannel') is not None:
            self.android_notification_xiaomi_channel = m.get('AndroidNotificationXiaomiChannel')
        if m.get('AndroidXiaoMiActivity') is not None:
            self.android_xiao_mi_activity = m.get('AndroidXiaoMiActivity')
        if m.get('AndroidPopupTitle') is not None:
            self.android_popup_title = m.get('AndroidPopupTitle')
        if m.get('iOSRemindBody') is not None:
            self.i_osremind_body = m.get('iOSRemindBody')
        if m.get('AndroidActivity') is not None:
            self.android_activity = m.get('AndroidActivity')
        if m.get('AndroidNotifyType') is not None:
            self.android_notify_type = m.get('AndroidNotifyType')
        if m.get('iOSMutableContent') is not None:
            self.i_osmutable_content = m.get('iOSMutableContent')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('AndroidOpenUrl') is not None:
            self.android_open_url = m.get('AndroidOpenUrl')
        if m.get('AndroidNotificationNotifyId') is not None:
            self.android_notification_notify_id = m.get('AndroidNotificationNotifyId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('AndroidNotificationVivoChannel') is not None:
            self.android_notification_vivo_channel = m.get('AndroidNotificationVivoChannel')
        if m.get('AndroidOpenType') is not None:
            self.android_open_type = m.get('AndroidOpenType')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('AndroidPopupActivity') is not None:
            self.android_popup_activity = m.get('AndroidPopupActivity')
        if m.get('AndroidRemind') is not None:
            self.android_remind = m.get('AndroidRemind')
        if m.get('AndroidPopupBody') is not None:
            self.android_popup_body = m.get('AndroidPopupBody')
        if m.get('AndroidExtParameters') is not None:
            self.android_ext_parameters = m.get('AndroidExtParameters')
        if m.get('iOSExtParameters') is not None:
            self.i_osext_parameters = m.get('iOSExtParameters')
        if m.get('AndroidXiaoMiNotifyBody') is not None:
            self.android_xiao_mi_notify_body = m.get('AndroidXiaoMiNotifyBody')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('AndroidNotificationBarType') is not None:
            self.android_notification_bar_type = m.get('AndroidNotificationBarType')
        if m.get('AndroidNotificationBarPriority') is not None:
            self.android_notification_bar_priority = m.get('AndroidNotificationBarPriority')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('iOSMusic') is not None:
            self.i_osmusic = m.get('iOSMusic')
        if m.get('iOSRemind') is not None:
            self.i_osremind = m.get('iOSRemind')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('iOSBadge') is not None:
            self.i_osbadge = m.get('iOSBadge')
        if m.get('SendSpeed') is not None:
            self.send_speed = m.get('SendSpeed')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')
        if m.get('AndroidMusic') is not None:
            self.android_music = m.get('AndroidMusic')
        return self


class MassPushRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        push_task: List[MassPushRequestPushTask] = None,
    ):
        self.app_key = app_key
        self.push_task = push_task

    def validate(self):
        if self.push_task:
            for k in self.push_task:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        result['PushTask'] = []
        if self.push_task is not None:
            for k in self.push_task:
                result['PushTask'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
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
        request_id: str = None,
        message_ids: MassPushResponseBodyMessageIds = None,
    ):
        self.request_id = request_id
        self.message_ids = message_ids

    def validate(self):
        if self.message_ids:
            self.message_ids.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_ids is not None:
            result['MessageIds'] = self.message_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageIds') is not None:
            temp_model = MassPushResponseBodyMessageIds()
            self.message_ids = temp_model.from_map(m['MessageIds'])
        return self


class MassPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MassPushResponseBody = None,
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
            temp_model = MassPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        push_type: str = None,
        device_type: str = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
        body: str = None,
        job_key: str = None,
        send_speed: int = None,
        store_offline: bool = None,
        push_time: str = None,
        expire_time: str = None,
        i_osapns_env: str = None,
        i_osremind: bool = None,
        i_osremind_body: str = None,
        i_osbadge: int = None,
        i_osbadge_auto_increment: bool = None,
        i_ossilent_notification: bool = None,
        i_osmusic: str = None,
        i_ossubtitle: str = None,
        i_osnotification_category: str = None,
        i_osmutable_content: bool = None,
        i_osext_parameters: str = None,
        android_notify_type: str = None,
        android_open_type: str = None,
        android_activity: str = None,
        android_music: str = None,
        android_open_url: str = None,
        android_xiao_mi_activity: str = None,
        android_xiao_mi_notify_title: str = None,
        android_xiao_mi_notify_body: str = None,
        android_popup_activity: str = None,
        android_popup_title: str = None,
        android_popup_body: str = None,
        android_notification_bar_type: int = None,
        android_notification_bar_priority: int = None,
        android_ext_parameters: str = None,
        android_remind: bool = None,
        android_notification_channel: str = None,
        android_notification_xiaomi_channel: str = None,
        sms_template_name: str = None,
        sms_sign_name: str = None,
        sms_params: str = None,
        sms_delay_secs: int = None,
        sms_send_policy: int = None,
        android_notification_vivo_channel: str = None,
        android_notification_huawei_channel: str = None,
        android_notification_notify_id: int = None,
        i_osnotification_collapse_id: str = None,
    ):
        self.app_key = app_key
        self.push_type = push_type
        self.device_type = device_type
        self.target = target
        self.target_value = target_value
        self.title = title
        self.body = body
        self.job_key = job_key
        self.send_speed = send_speed
        self.store_offline = store_offline
        self.push_time = push_time
        self.expire_time = expire_time
        self.i_osapns_env = i_osapns_env
        self.i_osremind = i_osremind
        self.i_osremind_body = i_osremind_body
        self.i_osbadge = i_osbadge
        self.i_osbadge_auto_increment = i_osbadge_auto_increment
        self.i_ossilent_notification = i_ossilent_notification
        self.i_osmusic = i_osmusic
        self.i_ossubtitle = i_ossubtitle
        self.i_osnotification_category = i_osnotification_category
        self.i_osmutable_content = i_osmutable_content
        self.i_osext_parameters = i_osext_parameters
        self.android_notify_type = android_notify_type
        self.android_open_type = android_open_type
        self.android_activity = android_activity
        self.android_music = android_music
        self.android_open_url = android_open_url
        self.android_xiao_mi_activity = android_xiao_mi_activity
        self.android_xiao_mi_notify_title = android_xiao_mi_notify_title
        self.android_xiao_mi_notify_body = android_xiao_mi_notify_body
        self.android_popup_activity = android_popup_activity
        self.android_popup_title = android_popup_title
        self.android_popup_body = android_popup_body
        self.android_notification_bar_type = android_notification_bar_type
        self.android_notification_bar_priority = android_notification_bar_priority
        self.android_ext_parameters = android_ext_parameters
        self.android_remind = android_remind
        self.android_notification_channel = android_notification_channel
        self.android_notification_xiaomi_channel = android_notification_xiaomi_channel
        self.sms_template_name = sms_template_name
        self.sms_sign_name = sms_sign_name
        self.sms_params = sms_params
        self.sms_delay_secs = sms_delay_secs
        self.sms_send_policy = sms_send_policy
        self.android_notification_vivo_channel = android_notification_vivo_channel
        self.android_notification_huawei_channel = android_notification_huawei_channel
        self.android_notification_notify_id = android_notification_notify_id
        self.i_osnotification_collapse_id = i_osnotification_collapse_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        if self.body is not None:
            result['Body'] = self.body
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.send_speed is not None:
            result['SendSpeed'] = self.send_speed
        if self.store_offline is not None:
            result['StoreOffline'] = self.store_offline
        if self.push_time is not None:
            result['PushTime'] = self.push_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.i_osapns_env is not None:
            result['iOSApnsEnv'] = self.i_osapns_env
        if self.i_osremind is not None:
            result['iOSRemind'] = self.i_osremind
        if self.i_osremind_body is not None:
            result['iOSRemindBody'] = self.i_osremind_body
        if self.i_osbadge is not None:
            result['iOSBadge'] = self.i_osbadge
        if self.i_osbadge_auto_increment is not None:
            result['iOSBadgeAutoIncrement'] = self.i_osbadge_auto_increment
        if self.i_ossilent_notification is not None:
            result['iOSSilentNotification'] = self.i_ossilent_notification
        if self.i_osmusic is not None:
            result['iOSMusic'] = self.i_osmusic
        if self.i_ossubtitle is not None:
            result['iOSSubtitle'] = self.i_ossubtitle
        if self.i_osnotification_category is not None:
            result['iOSNotificationCategory'] = self.i_osnotification_category
        if self.i_osmutable_content is not None:
            result['iOSMutableContent'] = self.i_osmutable_content
        if self.i_osext_parameters is not None:
            result['iOSExtParameters'] = self.i_osext_parameters
        if self.android_notify_type is not None:
            result['AndroidNotifyType'] = self.android_notify_type
        if self.android_open_type is not None:
            result['AndroidOpenType'] = self.android_open_type
        if self.android_activity is not None:
            result['AndroidActivity'] = self.android_activity
        if self.android_music is not None:
            result['AndroidMusic'] = self.android_music
        if self.android_open_url is not None:
            result['AndroidOpenUrl'] = self.android_open_url
        if self.android_xiao_mi_activity is not None:
            result['AndroidXiaoMiActivity'] = self.android_xiao_mi_activity
        if self.android_xiao_mi_notify_title is not None:
            result['AndroidXiaoMiNotifyTitle'] = self.android_xiao_mi_notify_title
        if self.android_xiao_mi_notify_body is not None:
            result['AndroidXiaoMiNotifyBody'] = self.android_xiao_mi_notify_body
        if self.android_popup_activity is not None:
            result['AndroidPopupActivity'] = self.android_popup_activity
        if self.android_popup_title is not None:
            result['AndroidPopupTitle'] = self.android_popup_title
        if self.android_popup_body is not None:
            result['AndroidPopupBody'] = self.android_popup_body
        if self.android_notification_bar_type is not None:
            result['AndroidNotificationBarType'] = self.android_notification_bar_type
        if self.android_notification_bar_priority is not None:
            result['AndroidNotificationBarPriority'] = self.android_notification_bar_priority
        if self.android_ext_parameters is not None:
            result['AndroidExtParameters'] = self.android_ext_parameters
        if self.android_remind is not None:
            result['AndroidRemind'] = self.android_remind
        if self.android_notification_channel is not None:
            result['AndroidNotificationChannel'] = self.android_notification_channel
        if self.android_notification_xiaomi_channel is not None:
            result['AndroidNotificationXiaomiChannel'] = self.android_notification_xiaomi_channel
        if self.sms_template_name is not None:
            result['SmsTemplateName'] = self.sms_template_name
        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name
        if self.sms_params is not None:
            result['SmsParams'] = self.sms_params
        if self.sms_delay_secs is not None:
            result['SmsDelaySecs'] = self.sms_delay_secs
        if self.sms_send_policy is not None:
            result['SmsSendPolicy'] = self.sms_send_policy
        if self.android_notification_vivo_channel is not None:
            result['AndroidNotificationVivoChannel'] = self.android_notification_vivo_channel
        if self.android_notification_huawei_channel is not None:
            result['AndroidNotificationHuaweiChannel'] = self.android_notification_huawei_channel
        if self.android_notification_notify_id is not None:
            result['AndroidNotificationNotifyId'] = self.android_notification_notify_id
        if self.i_osnotification_collapse_id is not None:
            result['iOSNotificationCollapseId'] = self.i_osnotification_collapse_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('SendSpeed') is not None:
            self.send_speed = m.get('SendSpeed')
        if m.get('StoreOffline') is not None:
            self.store_offline = m.get('StoreOffline')
        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('iOSApnsEnv') is not None:
            self.i_osapns_env = m.get('iOSApnsEnv')
        if m.get('iOSRemind') is not None:
            self.i_osremind = m.get('iOSRemind')
        if m.get('iOSRemindBody') is not None:
            self.i_osremind_body = m.get('iOSRemindBody')
        if m.get('iOSBadge') is not None:
            self.i_osbadge = m.get('iOSBadge')
        if m.get('iOSBadgeAutoIncrement') is not None:
            self.i_osbadge_auto_increment = m.get('iOSBadgeAutoIncrement')
        if m.get('iOSSilentNotification') is not None:
            self.i_ossilent_notification = m.get('iOSSilentNotification')
        if m.get('iOSMusic') is not None:
            self.i_osmusic = m.get('iOSMusic')
        if m.get('iOSSubtitle') is not None:
            self.i_ossubtitle = m.get('iOSSubtitle')
        if m.get('iOSNotificationCategory') is not None:
            self.i_osnotification_category = m.get('iOSNotificationCategory')
        if m.get('iOSMutableContent') is not None:
            self.i_osmutable_content = m.get('iOSMutableContent')
        if m.get('iOSExtParameters') is not None:
            self.i_osext_parameters = m.get('iOSExtParameters')
        if m.get('AndroidNotifyType') is not None:
            self.android_notify_type = m.get('AndroidNotifyType')
        if m.get('AndroidOpenType') is not None:
            self.android_open_type = m.get('AndroidOpenType')
        if m.get('AndroidActivity') is not None:
            self.android_activity = m.get('AndroidActivity')
        if m.get('AndroidMusic') is not None:
            self.android_music = m.get('AndroidMusic')
        if m.get('AndroidOpenUrl') is not None:
            self.android_open_url = m.get('AndroidOpenUrl')
        if m.get('AndroidXiaoMiActivity') is not None:
            self.android_xiao_mi_activity = m.get('AndroidXiaoMiActivity')
        if m.get('AndroidXiaoMiNotifyTitle') is not None:
            self.android_xiao_mi_notify_title = m.get('AndroidXiaoMiNotifyTitle')
        if m.get('AndroidXiaoMiNotifyBody') is not None:
            self.android_xiao_mi_notify_body = m.get('AndroidXiaoMiNotifyBody')
        if m.get('AndroidPopupActivity') is not None:
            self.android_popup_activity = m.get('AndroidPopupActivity')
        if m.get('AndroidPopupTitle') is not None:
            self.android_popup_title = m.get('AndroidPopupTitle')
        if m.get('AndroidPopupBody') is not None:
            self.android_popup_body = m.get('AndroidPopupBody')
        if m.get('AndroidNotificationBarType') is not None:
            self.android_notification_bar_type = m.get('AndroidNotificationBarType')
        if m.get('AndroidNotificationBarPriority') is not None:
            self.android_notification_bar_priority = m.get('AndroidNotificationBarPriority')
        if m.get('AndroidExtParameters') is not None:
            self.android_ext_parameters = m.get('AndroidExtParameters')
        if m.get('AndroidRemind') is not None:
            self.android_remind = m.get('AndroidRemind')
        if m.get('AndroidNotificationChannel') is not None:
            self.android_notification_channel = m.get('AndroidNotificationChannel')
        if m.get('AndroidNotificationXiaomiChannel') is not None:
            self.android_notification_xiaomi_channel = m.get('AndroidNotificationXiaomiChannel')
        if m.get('SmsTemplateName') is not None:
            self.sms_template_name = m.get('SmsTemplateName')
        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')
        if m.get('SmsParams') is not None:
            self.sms_params = m.get('SmsParams')
        if m.get('SmsDelaySecs') is not None:
            self.sms_delay_secs = m.get('SmsDelaySecs')
        if m.get('SmsSendPolicy') is not None:
            self.sms_send_policy = m.get('SmsSendPolicy')
        if m.get('AndroidNotificationVivoChannel') is not None:
            self.android_notification_vivo_channel = m.get('AndroidNotificationVivoChannel')
        if m.get('AndroidNotificationHuaweiChannel') is not None:
            self.android_notification_huawei_channel = m.get('AndroidNotificationHuaweiChannel')
        if m.get('AndroidNotificationNotifyId') is not None:
            self.android_notification_notify_id = m.get('AndroidNotificationNotifyId')
        if m.get('iOSNotificationCollapseId') is not None:
            self.i_osnotification_collapse_id = m.get('iOSNotificationCollapseId')
        return self


class PushResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class PushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushResponseBody = None,
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
            temp_model = PushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushMessageToAndroidRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
        body: str = None,
        job_key: str = None,
    ):
        self.app_key = app_key
        self.target = target
        self.target_value = target_value
        self.title = title
        self.body = body
        self.job_key = job_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        if self.body is not None:
            result['Body'] = self.body
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        return self


class PushMessageToAndroidResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class PushMessageToAndroidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushMessageToAndroidResponseBody = None,
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
            temp_model = PushMessageToAndroidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushMessageToiOSRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
        body: str = None,
        job_key: str = None,
    ):
        self.app_key = app_key
        self.target = target
        self.target_value = target_value
        self.title = title
        self.body = body
        self.job_key = job_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        if self.body is not None:
            result['Body'] = self.body
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        return self


class PushMessageToiOSResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class PushMessageToiOSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushMessageToiOSResponseBody = None,
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
            temp_model = PushMessageToiOSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushNoticeToAndroidRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        target: str = None,
        target_value: str = None,
        title: str = None,
        body: str = None,
        job_key: str = None,
        ext_parameters: str = None,
    ):
        self.app_key = app_key
        self.target = target
        self.target_value = target_value
        self.title = title
        self.body = body
        self.job_key = job_key
        self.ext_parameters = ext_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.title is not None:
            result['Title'] = self.title
        if self.body is not None:
            result['Body'] = self.body
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')
        return self


class PushNoticeToAndroidResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class PushNoticeToAndroidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushNoticeToAndroidResponseBody = None,
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
            temp_model = PushNoticeToAndroidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushNoticeToiOSRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        target: str = None,
        target_value: str = None,
        apns_env: str = None,
        title: str = None,
        body: str = None,
        job_key: str = None,
        ext_parameters: str = None,
    ):
        self.app_key = app_key
        self.target = target
        self.target_value = target_value
        self.apns_env = apns_env
        self.title = title
        self.body = body
        self.job_key = job_key
        self.ext_parameters = ext_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        if self.apns_env is not None:
            result['ApnsEnv'] = self.apns_env
        if self.title is not None:
            result['Title'] = self.title
        if self.body is not None:
            result['Body'] = self.body
        if self.job_key is not None:
            result['JobKey'] = self.job_key
        if self.ext_parameters is not None:
            result['ExtParameters'] = self.ext_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        if m.get('ApnsEnv') is not None:
            self.apns_env = m.get('ApnsEnv')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('JobKey') is not None:
            self.job_key = m.get('JobKey')
        if m.get('ExtParameters') is not None:
            self.ext_parameters = m.get('ExtParameters')
        return self


class PushNoticeToiOSResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message_id: str = None,
    ):
        self.request_id = request_id
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class PushNoticeToiOSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PushNoticeToiOSResponseBody = None,
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
            temp_model = PushNoticeToiOSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAliasesRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
    ):
        self.app_key = app_key
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
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
        request_id: str = None,
        alias_infos: QueryAliasesResponseBodyAliasInfos = None,
    ):
        self.request_id = request_id
        self.alias_infos = alias_infos

    def validate(self):
        if self.alias_infos:
            self.alias_infos.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.alias_infos is not None:
            result['AliasInfos'] = self.alias_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AliasInfos') is not None:
            temp_model = QueryAliasesResponseBodyAliasInfos()
            self.alias_infos = temp_model.from_map(m['AliasInfos'])
        return self


class QueryAliasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAliasesResponseBody = None,
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
            temp_model = QueryAliasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceCountRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        target: str = None,
        target_value: str = None,
    ):
        self.app_key = app_key
        self.target = target
        self.target_value = target_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.target is not None:
            result['Target'] = self.target
        if self.target_value is not None:
            result['TargetValue'] = self.target_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('TargetValue') is not None:
            self.target_value = m.get('TargetValue')
        return self


class QueryDeviceCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_count: int = None,
    ):
        self.request_id = request_id
        self.device_count = device_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_count is not None:
            result['DeviceCount'] = self.device_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')
        return self


class QueryDeviceCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceCountResponseBody = None,
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
            temp_model = QueryDeviceCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
    ):
        self.app_key = app_key
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
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
        last_online_time: str = None,
        phone_number: str = None,
        push_enabled: bool = None,
        device_type: str = None,
        device_id: str = None,
        online: bool = None,
        tags: str = None,
        device_token: str = None,
        alias: str = None,
    ):
        self.account = account
        self.last_online_time = last_online_time
        self.phone_number = phone_number
        self.push_enabled = push_enabled
        self.device_type = device_type
        self.device_id = device_id
        self.online = online
        self.tags = tags
        self.device_token = device_token
        self.alias = alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.last_online_time is not None:
            result['LastOnlineTime'] = self.last_online_time
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.push_enabled is not None:
            result['PushEnabled'] = self.push_enabled
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.online is not None:
            result['Online'] = self.online
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.device_token is not None:
            result['DeviceToken'] = self.device_token
        if self.alias is not None:
            result['Alias'] = self.alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('LastOnlineTime') is not None:
            self.last_online_time = m.get('LastOnlineTime')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PushEnabled') is not None:
            self.push_enabled = m.get('PushEnabled')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('DeviceToken') is not None:
            self.device_token = m.get('DeviceToken')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        return self


class QueryDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        device_info: QueryDeviceInfoResponseBodyDeviceInfo = None,
    ):
        self.request_id = request_id
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceInfo') is not None:
            temp_model = QueryDeviceInfoResponseBodyDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class QueryDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceInfoResponseBody = None,
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
            temp_model = QueryDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicesByAccountRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        account: str = None,
    ):
        self.app_key = app_key
        self.account = account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.account is not None:
            result['Account'] = self.account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Account') is not None:
            self.account = m.get('Account')
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
        body: QueryDevicesByAccountResponseBody = None,
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
            temp_model = QueryDevicesByAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicesByAliasRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        alias: str = None,
    ):
        self.app_key = app_key
        self.alias = alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.alias is not None:
            result['Alias'] = self.alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
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
        body: QueryDevicesByAliasResponseBody = None,
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
            temp_model = QueryDevicesByAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceStatRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        start_time: str = None,
        end_time: str = None,
        device_type: str = None,
        query_type: str = None,
    ):
        self.app_key = app_key
        self.start_time = start_time
        self.end_time = end_time
        self.device_type = device_type
        self.query_type = query_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.query_type is not None:
            result['QueryType'] = self.query_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')
        return self


class QueryDeviceStatResponseBodyAppDeviceStatsAppDeviceStat(TeaModel):
    def __init__(
        self,
        time: str = None,
        device_type: str = None,
        count: int = None,
    ):
        self.time = time
        self.device_type = device_type
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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
        request_id: str = None,
        app_device_stats: QueryDeviceStatResponseBodyAppDeviceStats = None,
    ):
        self.request_id = request_id
        self.app_device_stats = app_device_stats

    def validate(self):
        if self.app_device_stats:
            self.app_device_stats.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_device_stats is not None:
            result['AppDeviceStats'] = self.app_device_stats.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppDeviceStats') is not None:
            temp_model = QueryDeviceStatResponseBodyAppDeviceStats()
            self.app_device_stats = temp_model.from_map(m['AppDeviceStats'])
        return self


class QueryDeviceStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDeviceStatResponseBody = None,
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
            temp_model = QueryDeviceStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushRecordsRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        start_time: str = None,
        end_time: str = None,
        push_type: str = None,
        target: str = None,
        source: str = None,
        keyword: str = None,
        next_token: str = None,
        page_size: int = None,
        page: int = None,
    ):
        self.app_key = app_key
        self.start_time = start_time
        self.end_time = end_time
        self.push_type = push_type
        self.target = target
        self.source = source
        self.keyword = keyword
        self.next_token = next_token
        self.page_size = page_size
        self.page = page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.target is not None:
            result['Target'] = self.target
        if self.source is not None:
            result['Source'] = self.source
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryPushRecordsResponseBodyPushInfosPushInfo(TeaModel):
    def __init__(
        self,
        status: str = None,
        message_id: str = None,
        app_key: int = None,
        device_type: str = None,
        push_type: str = None,
        body: str = None,
        title: str = None,
        source: str = None,
        push_time: str = None,
        target: str = None,
    ):
        self.status = status
        self.message_id = message_id
        self.app_key = app_key
        self.device_type = device_type
        self.push_type = push_type
        self.body = body
        self.title = title
        self.source = source
        self.push_time = push_time
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.body is not None:
            result['Body'] = self.body
        if self.title is not None:
            result['Title'] = self.title
        if self.source is not None:
            result['Source'] = self.source
        if self.push_time is not None:
            result['PushTime'] = self.push_time
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('PushTime') is not None:
            self.push_time = m.get('PushTime')
        if m.get('Target') is not None:
            self.target = m.get('Target')
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
        push_infos: QueryPushRecordsResponseBodyPushInfos = None,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
        page: int = None,
    ):
        self.push_infos = push_infos
        self.next_token = next_token
        self.page_size = page_size
        self.request_id = request_id
        self.total = total
        self.page = page

    def validate(self):
        if self.push_infos:
            self.push_infos.validate()

    def to_map(self):
        result = dict()
        if self.push_infos is not None:
            result['PushInfos'] = self.push_infos.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        if self.page is not None:
            result['Page'] = self.page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PushInfos') is not None:
            temp_model = QueryPushRecordsResponseBodyPushInfos()
            self.push_infos = temp_model.from_map(m['PushInfos'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        return self


class QueryPushRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPushRecordsResponseBody = None,
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
            temp_model = QueryPushRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushStatByAppRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        start_time: str = None,
        end_time: str = None,
        granularity: str = None,
    ):
        self.app_key = app_key
        self.start_time = start_time
        self.end_time = end_time
        self.granularity = granularity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        return self


class QueryPushStatByAppResponseBodyAppPushStatsAppPushStat(TeaModel):
    def __init__(
        self,
        time: str = None,
        deleted_count: int = None,
        opened_count: int = None,
        sms_receive_success_count: int = None,
        sms_skip_count: int = None,
        sms_receive_failed_count: int = None,
        sms_failed_count: int = None,
        received_count: int = None,
        sent_count: int = None,
        sms_sent_count: int = None,
        accept_count: int = None,
    ):
        self.time = time
        self.deleted_count = deleted_count
        self.opened_count = opened_count
        self.sms_receive_success_count = sms_receive_success_count
        self.sms_skip_count = sms_skip_count
        self.sms_receive_failed_count = sms_receive_failed_count
        self.sms_failed_count = sms_failed_count
        self.received_count = received_count
        self.sent_count = sent_count
        self.sms_sent_count = sms_sent_count
        self.accept_count = accept_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count
        if self.opened_count is not None:
            result['OpenedCount'] = self.opened_count
        if self.sms_receive_success_count is not None:
            result['SmsReceiveSuccessCount'] = self.sms_receive_success_count
        if self.sms_skip_count is not None:
            result['SmsSkipCount'] = self.sms_skip_count
        if self.sms_receive_failed_count is not None:
            result['SmsReceiveFailedCount'] = self.sms_receive_failed_count
        if self.sms_failed_count is not None:
            result['SmsFailedCount'] = self.sms_failed_count
        if self.received_count is not None:
            result['ReceivedCount'] = self.received_count
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.sms_sent_count is not None:
            result['SmsSentCount'] = self.sms_sent_count
        if self.accept_count is not None:
            result['AcceptCount'] = self.accept_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')
        if m.get('OpenedCount') is not None:
            self.opened_count = m.get('OpenedCount')
        if m.get('SmsReceiveSuccessCount') is not None:
            self.sms_receive_success_count = m.get('SmsReceiveSuccessCount')
        if m.get('SmsSkipCount') is not None:
            self.sms_skip_count = m.get('SmsSkipCount')
        if m.get('SmsReceiveFailedCount') is not None:
            self.sms_receive_failed_count = m.get('SmsReceiveFailedCount')
        if m.get('SmsFailedCount') is not None:
            self.sms_failed_count = m.get('SmsFailedCount')
        if m.get('ReceivedCount') is not None:
            self.received_count = m.get('ReceivedCount')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('SmsSentCount') is not None:
            self.sms_sent_count = m.get('SmsSentCount')
        if m.get('AcceptCount') is not None:
            self.accept_count = m.get('AcceptCount')
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
        request_id: str = None,
        app_push_stats: QueryPushStatByAppResponseBodyAppPushStats = None,
    ):
        self.request_id = request_id
        self.app_push_stats = app_push_stats

    def validate(self):
        if self.app_push_stats:
            self.app_push_stats.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_push_stats is not None:
            result['AppPushStats'] = self.app_push_stats.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppPushStats') is not None:
            temp_model = QueryPushStatByAppResponseBodyAppPushStats()
            self.app_push_stats = temp_model.from_map(m['AppPushStats'])
        return self


class QueryPushStatByAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPushStatByAppResponseBody = None,
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
            temp_model = QueryPushStatByAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPushStatByMsgRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        message_id: int = None,
    ):
        self.app_key = app_key
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
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
        message_id: str = None,
        deleted_count: int = None,
        opened_count: int = None,
        sms_receive_success_count: int = None,
        sms_skip_count: int = None,
        sms_receive_failed_count: int = None,
        sms_failed_count: int = None,
        received_count: int = None,
        sent_count: int = None,
        sms_sent_count: int = None,
        accept_count: int = None,
    ):
        self.message_id = message_id
        self.deleted_count = deleted_count
        self.opened_count = opened_count
        self.sms_receive_success_count = sms_receive_success_count
        self.sms_skip_count = sms_skip_count
        self.sms_receive_failed_count = sms_receive_failed_count
        self.sms_failed_count = sms_failed_count
        self.received_count = received_count
        self.sent_count = sent_count
        self.sms_sent_count = sms_sent_count
        self.accept_count = accept_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count
        if self.opened_count is not None:
            result['OpenedCount'] = self.opened_count
        if self.sms_receive_success_count is not None:
            result['SmsReceiveSuccessCount'] = self.sms_receive_success_count
        if self.sms_skip_count is not None:
            result['SmsSkipCount'] = self.sms_skip_count
        if self.sms_receive_failed_count is not None:
            result['SmsReceiveFailedCount'] = self.sms_receive_failed_count
        if self.sms_failed_count is not None:
            result['SmsFailedCount'] = self.sms_failed_count
        if self.received_count is not None:
            result['ReceivedCount'] = self.received_count
        if self.sent_count is not None:
            result['SentCount'] = self.sent_count
        if self.sms_sent_count is not None:
            result['SmsSentCount'] = self.sms_sent_count
        if self.accept_count is not None:
            result['AcceptCount'] = self.accept_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')
        if m.get('OpenedCount') is not None:
            self.opened_count = m.get('OpenedCount')
        if m.get('SmsReceiveSuccessCount') is not None:
            self.sms_receive_success_count = m.get('SmsReceiveSuccessCount')
        if m.get('SmsSkipCount') is not None:
            self.sms_skip_count = m.get('SmsSkipCount')
        if m.get('SmsReceiveFailedCount') is not None:
            self.sms_receive_failed_count = m.get('SmsReceiveFailedCount')
        if m.get('SmsFailedCount') is not None:
            self.sms_failed_count = m.get('SmsFailedCount')
        if m.get('ReceivedCount') is not None:
            self.received_count = m.get('ReceivedCount')
        if m.get('SentCount') is not None:
            self.sent_count = m.get('SentCount')
        if m.get('SmsSentCount') is not None:
            self.sms_sent_count = m.get('SmsSentCount')
        if m.get('AcceptCount') is not None:
            self.accept_count = m.get('AcceptCount')
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
        request_id: str = None,
        push_stats: QueryPushStatByMsgResponseBodyPushStats = None,
    ):
        self.request_id = request_id
        self.push_stats = push_stats

    def validate(self):
        if self.push_stats:
            self.push_stats.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.push_stats is not None:
            result['PushStats'] = self.push_stats.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PushStats') is not None:
            temp_model = QueryPushStatByMsgResponseBodyPushStats()
            self.push_stats = temp_model.from_map(m['PushStats'])
        return self


class QueryPushStatByMsgResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPushStatByMsgResponseBody = None,
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
        self.app_key = app_key
        self.client_key = client_key
        self.key_type = key_type

    def validate(self):
        pass

    def to_map(self):
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
        tag_infos: QueryTagsResponseBodyTagInfos = None,
        request_id: str = None,
    ):
        self.tag_infos = tag_infos
        self.request_id = request_id

    def validate(self):
        if self.tag_infos:
            self.tag_infos.validate()

    def to_map(self):
        result = dict()
        if self.tag_infos is not None:
            result['TagInfos'] = self.tag_infos.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagInfos') is not None:
            temp_model = QueryTagsResponseBodyTagInfos()
            self.tag_infos = temp_model.from_map(m['TagInfos'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryTagsResponseBody = None,
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
            temp_model = QueryTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUniqueDeviceStatRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        start_time: str = None,
        end_time: str = None,
        granularity: str = None,
    ):
        self.app_key = app_key
        self.start_time = start_time
        self.end_time = end_time
        self.granularity = granularity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        return self


class QueryUniqueDeviceStatResponseBodyAppDeviceStatsAppDeviceStat(TeaModel):
    def __init__(
        self,
        time: str = None,
        count: int = None,
    ):
        self.time = time
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Count') is not None:
            self.count = m.get('Count')
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
        request_id: str = None,
        app_device_stats: QueryUniqueDeviceStatResponseBodyAppDeviceStats = None,
    ):
        self.request_id = request_id
        self.app_device_stats = app_device_stats

    def validate(self):
        if self.app_device_stats:
            self.app_device_stats.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.app_device_stats is not None:
            result['AppDeviceStats'] = self.app_device_stats.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AppDeviceStats') is not None:
            temp_model = QueryUniqueDeviceStatResponseBodyAppDeviceStats()
            self.app_device_stats = temp_model.from_map(m['AppDeviceStats'])
        return self


class QueryUniqueDeviceStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUniqueDeviceStatResponseBody = None,
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
            temp_model = QueryUniqueDeviceStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveTagRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        tag_name: str = None,
    ):
        self.app_key = app_key
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
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
        body: RemoveTagResponseBody = None,
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
            temp_model = RemoveTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAliasRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
        alias_name: str = None,
        unbind_all: bool = None,
    ):
        self.app_key = app_key
        self.device_id = device_id
        self.alias_name = alias_name
        self.unbind_all = unbind_all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.unbind_all is not None:
            result['UnbindAll'] = self.unbind_all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
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
        body: UnbindAliasResponseBody = None,
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
            temp_model = UnbindAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindPhoneRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        device_id: str = None,
    ):
        self.app_key = app_key
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
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
        body: UnbindPhoneResponseBody = None,
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
        self.app_key = app_key
        self.client_key = client_key
        self.key_type = key_type
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
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
        body: UnbindTagResponseBody = None,
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
            temp_model = UnbindTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


