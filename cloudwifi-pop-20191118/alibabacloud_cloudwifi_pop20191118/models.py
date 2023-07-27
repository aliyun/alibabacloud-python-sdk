# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddApListToApgroupRequest(TeaModel):
    def __init__(
        self,
        ap_group_id: str = None,
        ap_mac_list: Dict[str, Any] = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_group_id = ap_group_id
        self.ap_mac_list = ap_mac_list
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_id is not None:
            result['ApGroupId'] = self.ap_group_id
        if self.ap_mac_list is not None:
            result['ApMacList'] = self.ap_mac_list
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupId') is not None:
            self.ap_group_id = m.get('ApGroupId')
        if m.get('ApMacList') is not None:
            self.ap_mac_list = m.get('ApMacList')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class AddApListToApgroupShrinkRequest(TeaModel):
    def __init__(
        self,
        ap_group_id: str = None,
        ap_mac_list_shrink: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_group_id = ap_group_id
        self.ap_mac_list_shrink = ap_mac_list_shrink
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_id is not None:
            result['ApGroupId'] = self.ap_group_id
        if self.ap_mac_list_shrink is not None:
            result['ApMacList'] = self.ap_mac_list_shrink
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupId') is not None:
            self.ap_group_id = m.get('ApGroupId')
        if m.get('ApMacList') is not None:
            self.ap_mac_list_shrink = m.get('ApMacList')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class AddApListToApgroupResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class AddApListToApgroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddApListToApgroupResponseBody = None,
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
            temp_model = AddApListToApgroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelApThirdAppRequest(TeaModel):
    def __init__(
        self,
        ap_asset_id: int = None,
        app_code: str = None,
        app_name: str = None,
        id: int = None,
        mac: str = None,
    ):
        self.ap_asset_id = ap_asset_id
        self.app_code = app_code
        self.app_name = app_name
        self.id = id
        self.mac = mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_asset_id is not None:
            result['ApAssetId'] = self.ap_asset_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.id is not None:
            result['Id'] = self.id
        if self.mac is not None:
            result['Mac'] = self.mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApAssetId') is not None:
            self.ap_asset_id = m.get('ApAssetId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        return self


class DelApThirdAppResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DelApThirdAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DelApThirdAppResponseBody = None,
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
            temp_model = DelApThirdAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApSsidConfigRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        radio_index: str = None,
        ssid: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name
        self.radio_index = radio_index
        self.ssid = ssid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.radio_index is not None:
            result['RadioIndex'] = self.radio_index
        if self.ssid is not None:
            result['Ssid'] = self.ssid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RadioIndex') is not None:
            self.radio_index = m.get('RadioIndex')
        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')
        return self


class DeleteApSsidConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class DeleteApSsidConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApSsidConfigResponseBody = None,
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
            temp_model = DeleteApSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApgroupConfigRequest(TeaModel):
    def __init__(
        self,
        ap_group_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_group_uuid = ap_group_uuid
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class DeleteApgroupConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class DeleteApgroupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApgroupConfigResponseBody = None,
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
            temp_model = DeleteApgroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApgroupSsidConfigRequest(TeaModel):
    def __init__(
        self,
        apgroup_id: int = None,
        app_code: str = None,
        app_name: str = None,
        id: int = None,
    ):
        self.apgroup_id = apgroup_id
        self.app_code = app_code
        self.app_name = app_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteApgroupSsidConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        task_id: str = None,
    ):
        self.id = id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteApgroupSsidConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteApgroupSsidConfigResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteApgroupSsidConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApgroupSsidConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApgroupSsidConfigResponseBody = None,
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
            temp_model = DeleteApgroupSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApgroupThirdAppRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        id: int = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteApgroupThirdAppResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApgroupThirdAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApgroupThirdAppResponseBody = None,
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
            temp_model = DeleteApgroupThirdAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        ids: str = None,
        request_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.ids = ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNetDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNetDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNetDeviceInfoResponseBody = None,
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
            temp_model = DeleteNetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditApgroupThirdAppRequest(TeaModel):
    def __init__(
        self,
        apgroup_id: int = None,
        app_code: str = None,
        app_data: str = None,
        app_name: str = None,
        apply_to_sub_group: int = None,
        category: int = None,
        config_type: str = None,
        id: int = None,
        inherit_parent_group: int = None,
        third_app_name: str = None,
    ):
        self.apgroup_id = apgroup_id
        self.app_code = app_code
        self.app_data = app_data
        self.app_name = app_name
        self.apply_to_sub_group = apply_to_sub_group
        self.category = category
        self.config_type = config_type
        self.id = id
        self.inherit_parent_group = inherit_parent_group
        self.third_app_name = third_app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_data is not None:
            result['AppData'] = self.app_data
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.apply_to_sub_group is not None:
            result['ApplyToSubGroup'] = self.apply_to_sub_group
        if self.category is not None:
            result['Category'] = self.category
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.id is not None:
            result['Id'] = self.id
        if self.inherit_parent_group is not None:
            result['InheritParentGroup'] = self.inherit_parent_group
        if self.third_app_name is not None:
            result['ThirdAppName'] = self.third_app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppData') is not None:
            self.app_data = m.get('AppData')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ApplyToSubGroup') is not None:
            self.apply_to_sub_group = m.get('ApplyToSubGroup')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InheritParentGroup') is not None:
            self.inherit_parent_group = m.get('InheritParentGroup')
        if m.get('ThirdAppName') is not None:
            self.third_app_name = m.get('ThirdAppName')
        return self


class EditApgroupThirdAppResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditApgroupThirdAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditApgroupThirdAppResponseBody = None,
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
            temp_model = EditApgroupThirdAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EffectApConfigRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class EffectApConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class EffectApConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EffectApConfigResponseBody = None,
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
            temp_model = EffectApConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EffectApgroupConfigRequest(TeaModel):
    def __init__(
        self,
        ap_group_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_group_uuid = ap_group_uuid
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class EffectApgroupConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class EffectApgroupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EffectApgroupConfigResponseBody = None,
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
            temp_model = EffectApgroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApAddressByMacRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        language: str = None,
        mac: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.language = language
        self.mac = mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.language is not None:
            result['Language'] = self.language
        if self.mac is not None:
            result['Mac'] = self.mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        return self


class GetApAddressByMacResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApAddressByMacResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApAddressByMacResponseBody = None,
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
            temp_model = GetApAddressByMacResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApAssetRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApAssetResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApAssetResponseBody = None,
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
            temp_model = GetApAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApDetailStatusRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        mac: str = None,
        need_apgroup_info: bool = None,
        need_radio_status: bool = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.mac = mac
        self.need_apgroup_info = need_apgroup_info
        self.need_radio_status = need_radio_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.need_apgroup_info is not None:
            result['NeedApgroupInfo'] = self.need_apgroup_info
        if self.need_radio_status is not None:
            result['NeedRadioStatus'] = self.need_radio_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('NeedApgroupInfo') is not None:
            self.need_apgroup_info = m.get('NeedApgroupInfo')
        if m.get('NeedRadioStatus') is not None:
            self.need_radio_status = m.get('NeedRadioStatus')
        return self


class GetApDetailStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApDetailStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApDetailStatusResponseBody = None,
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
            temp_model = GetApDetailStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApDetailedConfigRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApDetailedConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApDetailedConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApDetailedConfigResponseBody = None,
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
            temp_model = GetApDetailedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApInfoFromPoolRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApInfoFromPoolResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApInfoFromPoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApInfoFromPoolResponseBody = None,
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
            temp_model = GetApInfoFromPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApRunHistoryTimeSerRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        end: int = None,
        start: int = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetApRunHistoryTimeSerResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApRunHistoryTimeSerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApRunHistoryTimeSerResponseBody = None,
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
            temp_model = GetApRunHistoryTimeSerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApStatusByGroupIdRequest(TeaModel):
    def __init__(
        self,
        apgroup_id: str = None,
        app_code: str = None,
        app_name: str = None,
        cursor: int = None,
        page_size: int = None,
    ):
        self.apgroup_id = apgroup_id
        self.app_code = app_code
        self.app_name = app_name
        self.cursor = cursor
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetApStatusByGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApStatusByGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApStatusByGroupIdResponseBody = None,
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
            temp_model = GetApStatusByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApgroupConfigByIdentityRequest(TeaModel):
    def __init__(
        self,
        apgroup_id: int = None,
        apgroup_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.apgroup_id = apgroup_id
        self.apgroup_uuid = apgroup_uuid
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApgroupConfigByIdentityResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApgroupConfigByIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApgroupConfigByIdentityResponseBody = None,
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
            temp_model = GetApgroupConfigByIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApgroupDetailedConfigRequest(TeaModel):
    def __init__(
        self,
        apgroup_id: int = None,
        apgroup_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.apgroup_id = apgroup_id
        self.apgroup_uuid = apgroup_uuid
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApgroupDetailedConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApgroupDetailedConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApgroupDetailedConfigResponseBody = None,
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
            temp_model = GetApgroupDetailedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApgroupIdRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApgroupIdResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApgroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApgroupIdResponseBody = None,
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
            temp_model = GetApgroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApgroupSsidConfigRequest(TeaModel):
    def __init__(
        self,
        ap_group_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_group_uuid = ap_group_uuid
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApgroupSsidConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApgroupSsidConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetApgroupSsidConfigResponseBody = None,
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
            temp_model = GetApgroupSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBatchTaskProgressRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        task_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetBatchTaskProgressResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBatchTaskProgressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBatchTaskProgressResponseBody = None,
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
            temp_model = GetBatchTaskProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupMiscAggTimeSerRequest(TeaModel):
    def __init__(
        self,
        apgroup_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
        end: int = None,
        start: int = None,
    ):
        self.apgroup_uuid = apgroup_uuid
        self.app_code = app_code
        self.app_name = app_name
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetGroupMiscAggTimeSerResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupMiscAggTimeSerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGroupMiscAggTimeSerResponseBody = None,
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
            temp_model = GetGroupMiscAggTimeSerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        cursor: int = None,
        host_name: str = None,
        id: int = None,
        idc: str = None,
        logic_net_pod: str = None,
        manufacturer: str = None,
        mgn_ip: str = None,
        model: str = None,
        net_pod: str = None,
        page_size: int = None,
        password: str = None,
        request_id: str = None,
        role: str = None,
        service_tag: str = None,
        username: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.cursor = cursor
        self.host_name = host_name
        self.id = id
        self.idc = idc
        self.logic_net_pod = logic_net_pod
        self.manufacturer = manufacturer
        self.mgn_ip = mgn_ip
        self.model = model
        self.net_pod = net_pod
        self.page_size = page_size
        self.password = password
        self.request_id = request_id
        self.role = role
        self.service_tag = service_tag
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip
        if self.model is not None:
            result['Model'] = self.model
        if self.net_pod is not None:
            result['NetPod'] = self.net_pod
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.password is not None:
            result['Password'] = self.password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role
        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetNetDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNetDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNetDeviceInfoResponseBody = None,
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
            temp_model = GetNetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetDeviceInfoWithSizeRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        cursor: int = None,
        host_name: str = None,
        id: int = None,
        idc: str = None,
        logic_net_pod: str = None,
        manufacturer: str = None,
        mgn_ip: str = None,
        model: str = None,
        net_pod: str = None,
        page_size: int = None,
        password: str = None,
        request_id: str = None,
        role: str = None,
        service_tag: str = None,
        username: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.cursor = cursor
        self.host_name = host_name
        self.id = id
        self.idc = idc
        self.logic_net_pod = logic_net_pod
        self.manufacturer = manufacturer
        self.mgn_ip = mgn_ip
        self.model = model
        self.net_pod = net_pod
        self.page_size = page_size
        self.password = password
        self.request_id = request_id
        self.role = role
        self.service_tag = service_tag
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip
        if self.model is not None:
            result['Model'] = self.model
        if self.net_pod is not None:
            result['NetPod'] = self.net_pod
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.password is not None:
            result['Password'] = self.password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role
        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetNetDeviceInfoWithSizeResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        data: List[Dict[str, Any]] = None,
    ):
        self.count = count
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetNetDeviceInfoWithSizeResponseBody(TeaModel):
    def __init__(
        self,
        data: GetNetDeviceInfoWithSizeResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetNetDeviceInfoWithSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNetDeviceInfoWithSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNetDeviceInfoWithSizeResponseBody = None,
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
            temp_model = GetNetDeviceInfoWithSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPageVisitDataRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        end_time: str = None,
        pid: str = None,
        start_time: str = None,
    ):
        # appCode
        self.app_code = app_code
        # appName
        self.app_name = app_name
        # endTime
        self.end_time = end_time
        # pId
        self.pid = pid
        # startTime
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pid is not None:
            result['PId'] = self.pid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PId') is not None:
            self.pid = m.get('PId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetPageVisitDataResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPageVisitDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPageVisitDataResponseBody = None,
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
            temp_model = GetPageVisitDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRadioRunHistoryTimeSerRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        end: int = None,
        start: int = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetRadioRunHistoryTimeSerResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRadioRunHistoryTimeSerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRadioRunHistoryTimeSerResponseBody = None,
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
            temp_model = GetRadioRunHistoryTimeSerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStaDetailedStatusByMacRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        sta_mac: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.sta_mac = sta_mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.sta_mac is not None:
            result['StaMac'] = self.sta_mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StaMac') is not None:
            self.sta_mac = m.get('StaMac')
        return self


class GetStaDetailedStatusByMacResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetStaDetailedStatusByMacResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStaDetailedStatusByMacResponseBody = None,
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
            temp_model = GetStaDetailedStatusByMacResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStaStatusListByApRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        cursor: int = None,
        page_size: int = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name
        self.cursor = cursor
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetStaStatusListByApResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetStaStatusListByApResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStaStatusListByApResponseBody = None,
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
            temp_model = GetStaStatusListByApResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JudgeXingTianBusinessRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        realm_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.realm_id = realm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.realm_id is not None:
            result['RealmId'] = self.realm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RealmId') is not None:
            self.realm_id = m.get('RealmId')
        return self


class JudgeXingTianBusinessResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JudgeXingTianBusinessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: JudgeXingTianBusinessResponseBody = None,
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
            temp_model = JudgeXingTianBusinessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KickStaRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        sta_mac: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.sta_mac = sta_mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.sta_mac is not None:
            result['StaMac'] = self.sta_mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StaMac') is not None:
            self.sta_mac = m.get('StaMac')
        return self


class KickStaResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class KickStaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KickStaResponseBody = None,
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
            temp_model = KickStaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApgroupDescendantRequest(TeaModel):
    def __init__(
        self,
        apgroup_id: int = None,
        apgroup_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
        cursor: int = None,
        level: int = None,
        page_size: int = None,
    ):
        self.apgroup_id = apgroup_id
        self.apgroup_uuid = apgroup_uuid
        self.app_code = app_code
        self.app_name = app_name
        self.cursor = cursor
        self.level = level
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.level is not None:
            result['Level'] = self.level
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListApgroupDescendantResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApgroupDescendantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListApgroupDescendantResponseBody = None,
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
            temp_model = ListApgroupDescendantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobOrdersRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        changing_type: str = None,
        client_system: str = None,
        client_unique_id: str = None,
        cursor: int = None,
        end_time: str = None,
        handler: str = None,
        id: str = None,
        order_status: str = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        title: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.changing_type = changing_type
        self.client_system = client_system
        self.client_unique_id = client_unique_id
        self.cursor = cursor
        self.end_time = end_time
        self.handler = handler
        self.id = id
        self.order_status = order_status
        self.page_size = page_size
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.changing_type is not None:
            result['ChangingType'] = self.changing_type
        if self.client_system is not None:
            result['ClientSystem'] = self.client_system
        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.handler is not None:
            result['Handler'] = self.handler
        if self.id is not None:
            result['Id'] = self.id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ChangingType') is not None:
            self.changing_type = m.get('ChangingType')
        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')
        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Handler') is not None:
            self.handler = m.get('Handler')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListJobOrdersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListJobOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobOrdersResponseBody = None,
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
            temp_model = ListJobOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobOrdersWithSizeRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        changing_type: str = None,
        client_system: str = None,
        client_unique_id: str = None,
        cursor: int = None,
        end_time: str = None,
        handler: str = None,
        id: str = None,
        order_status: str = None,
        page_size: int = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
        title: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.changing_type = changing_type
        self.client_system = client_system
        self.client_unique_id = client_unique_id
        self.cursor = cursor
        self.end_time = end_time
        self.handler = handler
        self.id = id
        self.order_status = order_status
        self.page_size = page_size
        self.request_id = request_id
        self.start_time = start_time
        self.status = status
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.changing_type is not None:
            result['ChangingType'] = self.changing_type
        if self.client_system is not None:
            result['ClientSystem'] = self.client_system
        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.handler is not None:
            result['Handler'] = self.handler
        if self.id is not None:
            result['Id'] = self.id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ChangingType') is not None:
            self.changing_type = m.get('ChangingType')
        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')
        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Handler') is not None:
            self.handler = m.get('Handler')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListJobOrdersWithSizeResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        data: List[Dict[str, Any]] = None,
    ):
        self.count = count
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListJobOrdersWithSizeResponseBody(TeaModel):
    def __init__(
        self,
        data: ListJobOrdersWithSizeResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListJobOrdersWithSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListJobOrdersWithSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobOrdersWithSizeResponseBody = None,
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
            temp_model = ListJobOrdersWithSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NewApgroupConfigRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        name: str = None,
        parent_apgroup_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.name = name
        self.parent_apgroup_id = parent_apgroup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_apgroup_id is not None:
            result['ParentApgroupId'] = self.parent_apgroup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentApgroupId') is not None:
            self.parent_apgroup_id = m.get('ParentApgroupId')
        return self


class NewApgroupConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class NewApgroupConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NewApgroupConfigResponseBody = None,
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
            temp_model = NewApgroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NewJobOrderRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        callback_url: str = None,
        change_type: str = None,
        client_system: str = None,
        client_unique_id: str = None,
        creator: str = None,
        params: Dict[str, Any] = None,
        refer_url: str = None,
        request_id: str = None,
        title: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.callback_url = callback_url
        self.change_type = change_type
        self.client_system = client_system
        self.client_unique_id = client_unique_id
        self.creator = creator
        self.params = params
        self.refer_url = refer_url
        self.request_id = request_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.change_type is not None:
            result['ChangeType'] = self.change_type
        if self.client_system is not None:
            result['ClientSystem'] = self.client_system
        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.params is not None:
            result['Params'] = self.params
        if self.refer_url is not None:
            result['ReferUrl'] = self.refer_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')
        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')
        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ReferUrl') is not None:
            self.refer_url = m.get('ReferUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class NewJobOrderShrinkRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        callback_url: str = None,
        change_type: str = None,
        client_system: str = None,
        client_unique_id: str = None,
        creator: str = None,
        params_shrink: str = None,
        refer_url: str = None,
        request_id: str = None,
        title: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.callback_url = callback_url
        self.change_type = change_type
        self.client_system = client_system
        self.client_unique_id = client_unique_id
        self.creator = creator
        self.params_shrink = params_shrink
        self.refer_url = refer_url
        self.request_id = request_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.change_type is not None:
            result['ChangeType'] = self.change_type
        if self.client_system is not None:
            result['ClientSystem'] = self.client_system
        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.params_shrink is not None:
            result['Params'] = self.params_shrink
        if self.refer_url is not None:
            result['ReferUrl'] = self.refer_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')
        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')
        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Params') is not None:
            self.params_shrink = m.get('Params')
        if m.get('ReferUrl') is not None:
            self.refer_url = m.get('ReferUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class NewJobOrderResponseBodyData(TeaModel):
    def __init__(
        self,
        order_id: int = None,
    ):
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class NewJobOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: NewJobOrderResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = NewJobOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NewJobOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NewJobOrderResponseBody = None,
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
            temp_model = NewJobOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NewNetDeviceInfoRequestDevices(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        idc: str = None,
        logic_net_pod: str = None,
        manufacturer: str = None,
        mgn_ip: str = None,
        model: str = None,
        net_pod: str = None,
        password: str = None,
        role: str = None,
        service_tag: str = None,
        username: str = None,
    ):
        self.host_name = host_name
        self.idc = idc
        self.logic_net_pod = logic_net_pod
        self.manufacturer = manufacturer
        self.mgn_ip = mgn_ip
        self.model = model
        self.net_pod = net_pod
        self.password = password
        self.role = role
        self.service_tag = service_tag
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip
        if self.model is not None:
            result['Model'] = self.model
        if self.net_pod is not None:
            result['NetPod'] = self.net_pod
        if self.password is not None:
            result['Password'] = self.password
        if self.role is not None:
            result['Role'] = self.role
        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class NewNetDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        devices: List[NewNetDeviceInfoRequestDevices] = None,
        request_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.devices = devices
        self.request_id = request_id

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = NewNetDeviceInfoRequestDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NewNetDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NewNetDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: NewNetDeviceInfoResponseBody = None,
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
            temp_model = NewNetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutAppConfigAndSaveRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        configure_type: str = None,
        current_time: int = None,
        data: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name
        self.configure_type = configure_type
        self.current_time = current_time
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.configure_type is not None:
            result['ConfigureType'] = self.configure_type
        if self.current_time is not None:
            result['CurrentTime'] = self.current_time
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ConfigureType') is not None:
            self.configure_type = m.get('ConfigureType')
        if m.get('CurrentTime') is not None:
            self.current_time = m.get('CurrentTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class PutAppConfigAndSaveResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutAppConfigAndSaveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutAppConfigAndSaveResponseBody = None,
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
            temp_model = PutAppConfigAndSaveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryJobOrderRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryJobOrderResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryJobOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryJobOrderResponseBody = None,
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
            temp_model = QueryJobOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootApRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class RebootApResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootApResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootApResponseBody = None,
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
            temp_model = RebootApResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterApAssetRequest(TeaModel):
    def __init__(
        self,
        ap_group_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
        id: int = None,
        mac: str = None,
        serial_no: str = None,
    ):
        self.ap_group_uuid = ap_group_uuid
        self.app_code = app_code
        self.app_name = app_name
        self.id = id
        self.mac = mac
        self.serial_no = serial_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.id is not None:
            result['Id'] = self.id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class RegisterApAssetResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterApAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterApAssetResponseBody = None,
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
            temp_model = RegisterApAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RepairApRadioRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        radio_index: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name
        self.radio_index = radio_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.radio_index is not None:
            result['RadioIndex'] = self.radio_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RadioIndex') is not None:
            self.radio_index = m.get('RadioIndex')
        return self


class RepairApRadioResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: bool = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RepairApRadioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RepairApRadioResponseBody = None,
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
            temp_model = RepairApRadioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApBasicConfigRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        country: str = None,
        dai: str = None,
        description: str = None,
        echo_int: int = None,
        failover: int = None,
        id: int = None,
        insecure_allowed: int = None,
        lan_ip: str = None,
        lan_mask: str = None,
        lan_status: int = None,
        log_ip: str = None,
        log_level: int = None,
        name: str = None,
        passwd: str = None,
        protocol: str = None,
        route: str = None,
        scan: int = None,
        token_server: str = None,
        vpn: str = None,
        work_mode: int = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.country = country
        self.dai = dai
        self.description = description
        self.echo_int = echo_int
        self.failover = failover
        self.id = id
        self.insecure_allowed = insecure_allowed
        self.lan_ip = lan_ip
        self.lan_mask = lan_mask
        self.lan_status = lan_status
        self.log_ip = log_ip
        self.log_level = log_level
        self.name = name
        self.passwd = passwd
        self.protocol = protocol
        self.route = route
        self.scan = scan
        self.token_server = token_server
        self.vpn = vpn
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.country is not None:
            result['Country'] = self.country
        if self.dai is not None:
            result['Dai'] = self.dai
        if self.description is not None:
            result['Description'] = self.description
        if self.echo_int is not None:
            result['EchoInt'] = self.echo_int
        if self.failover is not None:
            result['Failover'] = self.failover
        if self.id is not None:
            result['Id'] = self.id
        if self.insecure_allowed is not None:
            result['InsecureAllowed'] = self.insecure_allowed
        if self.lan_ip is not None:
            result['LanIp'] = self.lan_ip
        if self.lan_mask is not None:
            result['LanMask'] = self.lan_mask
        if self.lan_status is not None:
            result['LanStatus'] = self.lan_status
        if self.log_ip is not None:
            result['LogIp'] = self.log_ip
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.name is not None:
            result['Name'] = self.name
        if self.passwd is not None:
            result['Passwd'] = self.passwd
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.route is not None:
            result['Route'] = self.route
        if self.scan is not None:
            result['Scan'] = self.scan
        if self.token_server is not None:
            result['TokenServer'] = self.token_server
        if self.vpn is not None:
            result['Vpn'] = self.vpn
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Dai') is not None:
            self.dai = m.get('Dai')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EchoInt') is not None:
            self.echo_int = m.get('EchoInt')
        if m.get('Failover') is not None:
            self.failover = m.get('Failover')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsecureAllowed') is not None:
            self.insecure_allowed = m.get('InsecureAllowed')
        if m.get('LanIp') is not None:
            self.lan_ip = m.get('LanIp')
        if m.get('LanMask') is not None:
            self.lan_mask = m.get('LanMask')
        if m.get('LanStatus') is not None:
            self.lan_status = m.get('LanStatus')
        if m.get('LogIp') is not None:
            self.log_ip = m.get('LogIp')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Passwd') is not None:
            self.passwd = m.get('Passwd')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('Scan') is not None:
            self.scan = m.get('Scan')
        if m.get('TokenServer') is not None:
            self.token_server = m.get('TokenServer')
        if m.get('Vpn') is not None:
            self.vpn = m.get('Vpn')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        return self


class SaveApBasicConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApBasicConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApBasicConfigResponseBody = None,
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
            temp_model = SaveApBasicConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApPortalConfigRequest(TeaModel):
    def __init__(
        self,
        ap_config_id: int = None,
        app_auth_url: str = None,
        app_code: str = None,
        app_name: str = None,
        auth_key: str = None,
        auth_secret: str = None,
        check_url: str = None,
        client_download: int = None,
        client_upload: int = None,
        countdown: int = None,
        network: int = None,
        portal_types: List[str] = None,
        portal_url: str = None,
        time_stamp: int = None,
        total_download: int = None,
        total_upload: int = None,
        web_auth_url: str = None,
        whitelist: str = None,
    ):
        self.ap_config_id = ap_config_id
        self.app_auth_url = app_auth_url
        self.app_code = app_code
        self.app_name = app_name
        self.auth_key = auth_key
        self.auth_secret = auth_secret
        self.check_url = check_url
        self.client_download = client_download
        self.client_upload = client_upload
        self.countdown = countdown
        self.network = network
        self.portal_types = portal_types
        self.portal_url = portal_url
        self.time_stamp = time_stamp
        self.total_download = total_download
        self.total_upload = total_upload
        self.web_auth_url = web_auth_url
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_config_id is not None:
            result['ApConfigId'] = self.ap_config_id
        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.client_download is not None:
            result['ClientDownload'] = self.client_download
        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload
        if self.countdown is not None:
            result['Countdown'] = self.countdown
        if self.network is not None:
            result['Network'] = self.network
        if self.portal_types is not None:
            result['PortalTypes'] = self.portal_types
        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApConfigId') is not None:
            self.ap_config_id = m.get('ApConfigId')
        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')
        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')
        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PortalTypes') is not None:
            self.portal_types = m.get('PortalTypes')
        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class SaveApPortalConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        ap_config_id: int = None,
        app_auth_url: str = None,
        app_code: str = None,
        app_name: str = None,
        auth_key: str = None,
        auth_secret: str = None,
        check_url: str = None,
        client_download: int = None,
        client_upload: int = None,
        countdown: int = None,
        network: int = None,
        portal_types_shrink: str = None,
        portal_url: str = None,
        time_stamp: int = None,
        total_download: int = None,
        total_upload: int = None,
        web_auth_url: str = None,
        whitelist: str = None,
    ):
        self.ap_config_id = ap_config_id
        self.app_auth_url = app_auth_url
        self.app_code = app_code
        self.app_name = app_name
        self.auth_key = auth_key
        self.auth_secret = auth_secret
        self.check_url = check_url
        self.client_download = client_download
        self.client_upload = client_upload
        self.countdown = countdown
        self.network = network
        self.portal_types_shrink = portal_types_shrink
        self.portal_url = portal_url
        self.time_stamp = time_stamp
        self.total_download = total_download
        self.total_upload = total_upload
        self.web_auth_url = web_auth_url
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_config_id is not None:
            result['ApConfigId'] = self.ap_config_id
        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.client_download is not None:
            result['ClientDownload'] = self.client_download
        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload
        if self.countdown is not None:
            result['Countdown'] = self.countdown
        if self.network is not None:
            result['Network'] = self.network
        if self.portal_types_shrink is not None:
            result['PortalTypes'] = self.portal_types_shrink
        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApConfigId') is not None:
            self.ap_config_id = m.get('ApConfigId')
        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')
        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')
        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PortalTypes') is not None:
            self.portal_types_shrink = m.get('PortalTypes')
        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class SaveApPortalConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApPortalConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApPortalConfigResponseBody = None,
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
            temp_model = SaveApPortalConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApRadioConfigRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        bcast_rate: int = None,
        beacon_int: int = None,
        channel: str = None,
        disabled: str = None,
        frag: int = None,
        htmode: str = None,
        hwmode: str = None,
        id: int = None,
        mcast_rate: int = None,
        mgmt_rate: int = None,
        minrate: int = None,
        noscan: str = None,
        probereq: str = None,
        require_mode: str = None,
        rts: int = None,
        shortgi: str = None,
        txpower: str = None,
        uapsd: int = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.bcast_rate = bcast_rate
        self.beacon_int = beacon_int
        self.channel = channel
        self.disabled = disabled
        self.frag = frag
        self.htmode = htmode
        self.hwmode = hwmode
        self.id = id
        self.mcast_rate = mcast_rate
        self.mgmt_rate = mgmt_rate
        self.minrate = minrate
        self.noscan = noscan
        self.probereq = probereq
        self.require_mode = require_mode
        self.rts = rts
        self.shortgi = shortgi
        self.txpower = txpower
        self.uapsd = uapsd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.bcast_rate is not None:
            result['BcastRate'] = self.bcast_rate
        if self.beacon_int is not None:
            result['BeaconInt'] = self.beacon_int
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.frag is not None:
            result['Frag'] = self.frag
        if self.htmode is not None:
            result['Htmode'] = self.htmode
        if self.hwmode is not None:
            result['Hwmode'] = self.hwmode
        if self.id is not None:
            result['Id'] = self.id
        if self.mcast_rate is not None:
            result['McastRate'] = self.mcast_rate
        if self.mgmt_rate is not None:
            result['MgmtRate'] = self.mgmt_rate
        if self.minrate is not None:
            result['Minrate'] = self.minrate
        if self.noscan is not None:
            result['Noscan'] = self.noscan
        if self.probereq is not None:
            result['Probereq'] = self.probereq
        if self.require_mode is not None:
            result['RequireMode'] = self.require_mode
        if self.rts is not None:
            result['Rts'] = self.rts
        if self.shortgi is not None:
            result['Shortgi'] = self.shortgi
        if self.txpower is not None:
            result['Txpower'] = self.txpower
        if self.uapsd is not None:
            result['Uapsd'] = self.uapsd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BcastRate') is not None:
            self.bcast_rate = m.get('BcastRate')
        if m.get('BeaconInt') is not None:
            self.beacon_int = m.get('BeaconInt')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Frag') is not None:
            self.frag = m.get('Frag')
        if m.get('Htmode') is not None:
            self.htmode = m.get('Htmode')
        if m.get('Hwmode') is not None:
            self.hwmode = m.get('Hwmode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('McastRate') is not None:
            self.mcast_rate = m.get('McastRate')
        if m.get('MgmtRate') is not None:
            self.mgmt_rate = m.get('MgmtRate')
        if m.get('Minrate') is not None:
            self.minrate = m.get('Minrate')
        if m.get('Noscan') is not None:
            self.noscan = m.get('Noscan')
        if m.get('Probereq') is not None:
            self.probereq = m.get('Probereq')
        if m.get('RequireMode') is not None:
            self.require_mode = m.get('RequireMode')
        if m.get('Rts') is not None:
            self.rts = m.get('Rts')
        if m.get('Shortgi') is not None:
            self.shortgi = m.get('Shortgi')
        if m.get('Txpower') is not None:
            self.txpower = m.get('Txpower')
        if m.get('Uapsd') is not None:
            self.uapsd = m.get('Uapsd')
        return self


class SaveApRadioConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApRadioConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApRadioConfigResponseBody = None,
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
            temp_model = SaveApRadioConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApSsidConfigRequest(TeaModel):
    def __init__(
        self,
        acct_port: int = None,
        acct_secret: str = None,
        acct_server: str = None,
        acct_status_server_work: int = None,
        ap_asset_id: int = None,
        app_code: str = None,
        app_name: str = None,
        arp_proxy_enable: int = None,
        auth_cache: str = None,
        auth_port: int = None,
        auth_secret: str = None,
        auth_server: str = None,
        auth_status_server_work: int = None,
        cir: int = None,
        cir_step: int = None,
        cir_type: int = None,
        cir_ul: int = None,
        dae_client: str = None,
        dae_port: int = None,
        dae_secret: str = None,
        disabled: str = None,
        disassoc_low_ack: str = None,
        disassoc_weak_rssi: int = None,
        dynamic_vlan: int = None,
        enc_key: str = None,
        encryption: str = None,
        fourth_auth_port: int = None,
        fourth_auth_secret: str = None,
        fourth_auth_server: str = None,
        ft_over_ds: int = None,
        hidden: str = None,
        id: int = None,
        ieee_80211r: int = None,
        ieee_80211w: str = None,
        ignore_weak_probe: int = None,
        isolate: str = None,
        lite_effect: bool = None,
        mac: str = None,
        max_inactivity: int = None,
        maxassoc: int = None,
        mobility_domain: str = None,
        multicast_forward: int = None,
        nasid: str = None,
        nd_proxy_work: int = None,
        network: int = None,
        ownip: str = None,
        radio_index: str = None,
        secondary_acct_port: int = None,
        secondary_acct_secret: str = None,
        secondary_acct_server: str = None,
        secondary_auth_port: int = None,
        secondary_auth_secret: str = None,
        secondary_auth_server: str = None,
        send_config_to_ap: bool = None,
        short_preamble: str = None,
        ssid: str = None,
        ssid_lb: int = None,
        third_auth_port: int = None,
        third_auth_secret: str = None,
        third_auth_server: str = None,
        type: int = None,
        vlan_dhcp: int = None,
        wmm: str = None,
    ):
        self.acct_port = acct_port
        self.acct_secret = acct_secret
        self.acct_server = acct_server
        self.acct_status_server_work = acct_status_server_work
        self.ap_asset_id = ap_asset_id
        self.app_code = app_code
        self.app_name = app_name
        self.arp_proxy_enable = arp_proxy_enable
        self.auth_cache = auth_cache
        self.auth_port = auth_port
        self.auth_secret = auth_secret
        self.auth_server = auth_server
        self.auth_status_server_work = auth_status_server_work
        self.cir = cir
        self.cir_step = cir_step
        self.cir_type = cir_type
        self.cir_ul = cir_ul
        self.dae_client = dae_client
        self.dae_port = dae_port
        self.dae_secret = dae_secret
        self.disabled = disabled
        self.disassoc_low_ack = disassoc_low_ack
        self.disassoc_weak_rssi = disassoc_weak_rssi
        self.dynamic_vlan = dynamic_vlan
        self.enc_key = enc_key
        self.encryption = encryption
        self.fourth_auth_port = fourth_auth_port
        self.fourth_auth_secret = fourth_auth_secret
        self.fourth_auth_server = fourth_auth_server
        self.ft_over_ds = ft_over_ds
        self.hidden = hidden
        self.id = id
        self.ieee_80211r = ieee_80211r
        self.ieee_80211w = ieee_80211w
        self.ignore_weak_probe = ignore_weak_probe
        self.isolate = isolate
        self.lite_effect = lite_effect
        self.mac = mac
        self.max_inactivity = max_inactivity
        self.maxassoc = maxassoc
        self.mobility_domain = mobility_domain
        self.multicast_forward = multicast_forward
        self.nasid = nasid
        self.nd_proxy_work = nd_proxy_work
        self.network = network
        self.ownip = ownip
        self.radio_index = radio_index
        self.secondary_acct_port = secondary_acct_port
        self.secondary_acct_secret = secondary_acct_secret
        self.secondary_acct_server = secondary_acct_server
        self.secondary_auth_port = secondary_auth_port
        self.secondary_auth_secret = secondary_auth_secret
        self.secondary_auth_server = secondary_auth_server
        self.send_config_to_ap = send_config_to_ap
        self.short_preamble = short_preamble
        self.ssid = ssid
        self.ssid_lb = ssid_lb
        self.third_auth_port = third_auth_port
        self.third_auth_secret = third_auth_secret
        self.third_auth_server = third_auth_server
        self.type = type
        self.vlan_dhcp = vlan_dhcp
        self.wmm = wmm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acct_port is not None:
            result['AcctPort'] = self.acct_port
        if self.acct_secret is not None:
            result['AcctSecret'] = self.acct_secret
        if self.acct_server is not None:
            result['AcctServer'] = self.acct_server
        if self.acct_status_server_work is not None:
            result['AcctStatusServerWork'] = self.acct_status_server_work
        if self.ap_asset_id is not None:
            result['ApAssetId'] = self.ap_asset_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.arp_proxy_enable is not None:
            result['ArpProxyEnable'] = self.arp_proxy_enable
        if self.auth_cache is not None:
            result['AuthCache'] = self.auth_cache
        if self.auth_port is not None:
            result['AuthPort'] = self.auth_port
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.auth_server is not None:
            result['AuthServer'] = self.auth_server
        if self.auth_status_server_work is not None:
            result['AuthStatusServerWork'] = self.auth_status_server_work
        if self.cir is not None:
            result['Cir'] = self.cir
        if self.cir_step is not None:
            result['CirStep'] = self.cir_step
        if self.cir_type is not None:
            result['CirType'] = self.cir_type
        if self.cir_ul is not None:
            result['CirUl'] = self.cir_ul
        if self.dae_client is not None:
            result['DaeClient'] = self.dae_client
        if self.dae_port is not None:
            result['DaePort'] = self.dae_port
        if self.dae_secret is not None:
            result['DaeSecret'] = self.dae_secret
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.disassoc_low_ack is not None:
            result['DisassocLowAck'] = self.disassoc_low_ack
        if self.disassoc_weak_rssi is not None:
            result['DisassocWeakRssi'] = self.disassoc_weak_rssi
        if self.dynamic_vlan is not None:
            result['DynamicVlan'] = self.dynamic_vlan
        if self.enc_key is not None:
            result['EncKey'] = self.enc_key
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.fourth_auth_port is not None:
            result['FourthAuthPort'] = self.fourth_auth_port
        if self.fourth_auth_secret is not None:
            result['FourthAuthSecret'] = self.fourth_auth_secret
        if self.fourth_auth_server is not None:
            result['FourthAuthServer'] = self.fourth_auth_server
        if self.ft_over_ds is not None:
            result['FtOverDs'] = self.ft_over_ds
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.id is not None:
            result['Id'] = self.id
        if self.ieee_80211r is not None:
            result['Ieee80211r'] = self.ieee_80211r
        if self.ieee_80211w is not None:
            result['Ieee80211w'] = self.ieee_80211w
        if self.ignore_weak_probe is not None:
            result['IgnoreWeakProbe'] = self.ignore_weak_probe
        if self.isolate is not None:
            result['Isolate'] = self.isolate
        if self.lite_effect is not None:
            result['LiteEffect'] = self.lite_effect
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.max_inactivity is not None:
            result['MaxInactivity'] = self.max_inactivity
        if self.maxassoc is not None:
            result['Maxassoc'] = self.maxassoc
        if self.mobility_domain is not None:
            result['MobilityDomain'] = self.mobility_domain
        if self.multicast_forward is not None:
            result['MulticastForward'] = self.multicast_forward
        if self.nasid is not None:
            result['Nasid'] = self.nasid
        if self.nd_proxy_work is not None:
            result['NdProxyWork'] = self.nd_proxy_work
        if self.network is not None:
            result['Network'] = self.network
        if self.ownip is not None:
            result['Ownip'] = self.ownip
        if self.radio_index is not None:
            result['RadioIndex'] = self.radio_index
        if self.secondary_acct_port is not None:
            result['SecondaryAcctPort'] = self.secondary_acct_port
        if self.secondary_acct_secret is not None:
            result['SecondaryAcctSecret'] = self.secondary_acct_secret
        if self.secondary_acct_server is not None:
            result['SecondaryAcctServer'] = self.secondary_acct_server
        if self.secondary_auth_port is not None:
            result['SecondaryAuthPort'] = self.secondary_auth_port
        if self.secondary_auth_secret is not None:
            result['SecondaryAuthSecret'] = self.secondary_auth_secret
        if self.secondary_auth_server is not None:
            result['SecondaryAuthServer'] = self.secondary_auth_server
        if self.send_config_to_ap is not None:
            result['SendConfigToAp'] = self.send_config_to_ap
        if self.short_preamble is not None:
            result['ShortPreamble'] = self.short_preamble
        if self.ssid is not None:
            result['Ssid'] = self.ssid
        if self.ssid_lb is not None:
            result['SsidLb'] = self.ssid_lb
        if self.third_auth_port is not None:
            result['ThirdAuthPort'] = self.third_auth_port
        if self.third_auth_secret is not None:
            result['ThirdAuthSecret'] = self.third_auth_secret
        if self.third_auth_server is not None:
            result['ThirdAuthServer'] = self.third_auth_server
        if self.type is not None:
            result['Type'] = self.type
        if self.vlan_dhcp is not None:
            result['VlanDhcp'] = self.vlan_dhcp
        if self.wmm is not None:
            result['Wmm'] = self.wmm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcctPort') is not None:
            self.acct_port = m.get('AcctPort')
        if m.get('AcctSecret') is not None:
            self.acct_secret = m.get('AcctSecret')
        if m.get('AcctServer') is not None:
            self.acct_server = m.get('AcctServer')
        if m.get('AcctStatusServerWork') is not None:
            self.acct_status_server_work = m.get('AcctStatusServerWork')
        if m.get('ApAssetId') is not None:
            self.ap_asset_id = m.get('ApAssetId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ArpProxyEnable') is not None:
            self.arp_proxy_enable = m.get('ArpProxyEnable')
        if m.get('AuthCache') is not None:
            self.auth_cache = m.get('AuthCache')
        if m.get('AuthPort') is not None:
            self.auth_port = m.get('AuthPort')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('AuthServer') is not None:
            self.auth_server = m.get('AuthServer')
        if m.get('AuthStatusServerWork') is not None:
            self.auth_status_server_work = m.get('AuthStatusServerWork')
        if m.get('Cir') is not None:
            self.cir = m.get('Cir')
        if m.get('CirStep') is not None:
            self.cir_step = m.get('CirStep')
        if m.get('CirType') is not None:
            self.cir_type = m.get('CirType')
        if m.get('CirUl') is not None:
            self.cir_ul = m.get('CirUl')
        if m.get('DaeClient') is not None:
            self.dae_client = m.get('DaeClient')
        if m.get('DaePort') is not None:
            self.dae_port = m.get('DaePort')
        if m.get('DaeSecret') is not None:
            self.dae_secret = m.get('DaeSecret')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DisassocLowAck') is not None:
            self.disassoc_low_ack = m.get('DisassocLowAck')
        if m.get('DisassocWeakRssi') is not None:
            self.disassoc_weak_rssi = m.get('DisassocWeakRssi')
        if m.get('DynamicVlan') is not None:
            self.dynamic_vlan = m.get('DynamicVlan')
        if m.get('EncKey') is not None:
            self.enc_key = m.get('EncKey')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('FourthAuthPort') is not None:
            self.fourth_auth_port = m.get('FourthAuthPort')
        if m.get('FourthAuthSecret') is not None:
            self.fourth_auth_secret = m.get('FourthAuthSecret')
        if m.get('FourthAuthServer') is not None:
            self.fourth_auth_server = m.get('FourthAuthServer')
        if m.get('FtOverDs') is not None:
            self.ft_over_ds = m.get('FtOverDs')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ieee80211r') is not None:
            self.ieee_80211r = m.get('Ieee80211r')
        if m.get('Ieee80211w') is not None:
            self.ieee_80211w = m.get('Ieee80211w')
        if m.get('IgnoreWeakProbe') is not None:
            self.ignore_weak_probe = m.get('IgnoreWeakProbe')
        if m.get('Isolate') is not None:
            self.isolate = m.get('Isolate')
        if m.get('LiteEffect') is not None:
            self.lite_effect = m.get('LiteEffect')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('MaxInactivity') is not None:
            self.max_inactivity = m.get('MaxInactivity')
        if m.get('Maxassoc') is not None:
            self.maxassoc = m.get('Maxassoc')
        if m.get('MobilityDomain') is not None:
            self.mobility_domain = m.get('MobilityDomain')
        if m.get('MulticastForward') is not None:
            self.multicast_forward = m.get('MulticastForward')
        if m.get('Nasid') is not None:
            self.nasid = m.get('Nasid')
        if m.get('NdProxyWork') is not None:
            self.nd_proxy_work = m.get('NdProxyWork')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('Ownip') is not None:
            self.ownip = m.get('Ownip')
        if m.get('RadioIndex') is not None:
            self.radio_index = m.get('RadioIndex')
        if m.get('SecondaryAcctPort') is not None:
            self.secondary_acct_port = m.get('SecondaryAcctPort')
        if m.get('SecondaryAcctSecret') is not None:
            self.secondary_acct_secret = m.get('SecondaryAcctSecret')
        if m.get('SecondaryAcctServer') is not None:
            self.secondary_acct_server = m.get('SecondaryAcctServer')
        if m.get('SecondaryAuthPort') is not None:
            self.secondary_auth_port = m.get('SecondaryAuthPort')
        if m.get('SecondaryAuthSecret') is not None:
            self.secondary_auth_secret = m.get('SecondaryAuthSecret')
        if m.get('SecondaryAuthServer') is not None:
            self.secondary_auth_server = m.get('SecondaryAuthServer')
        if m.get('SendConfigToAp') is not None:
            self.send_config_to_ap = m.get('SendConfigToAp')
        if m.get('ShortPreamble') is not None:
            self.short_preamble = m.get('ShortPreamble')
        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')
        if m.get('SsidLb') is not None:
            self.ssid_lb = m.get('SsidLb')
        if m.get('ThirdAuthPort') is not None:
            self.third_auth_port = m.get('ThirdAuthPort')
        if m.get('ThirdAuthSecret') is not None:
            self.third_auth_secret = m.get('ThirdAuthSecret')
        if m.get('ThirdAuthServer') is not None:
            self.third_auth_server = m.get('ThirdAuthServer')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VlanDhcp') is not None:
            self.vlan_dhcp = m.get('VlanDhcp')
        if m.get('Wmm') is not None:
            self.wmm = m.get('Wmm')
        return self


class SaveApSsidConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class SaveApSsidConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApSsidConfigResponseBody = None,
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
            temp_model = SaveApSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApThirdAppRequest(TeaModel):
    def __init__(
        self,
        add_style: int = None,
        ap_asset_id: int = None,
        app_code: str = None,
        app_data: str = None,
        app_name: str = None,
        category: int = None,
        id: int = None,
        mac: str = None,
        third_app_name: str = None,
        version: str = None,
    ):
        self.add_style = add_style
        self.ap_asset_id = ap_asset_id
        self.app_code = app_code
        self.app_data = app_data
        self.app_name = app_name
        self.category = category
        self.id = id
        self.mac = mac
        self.third_app_name = third_app_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_style is not None:
            result['AddStyle'] = self.add_style
        if self.ap_asset_id is not None:
            result['ApAssetId'] = self.ap_asset_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_data is not None:
            result['AppData'] = self.app_data
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.third_app_name is not None:
            result['ThirdAppName'] = self.third_app_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddStyle') is not None:
            self.add_style = m.get('AddStyle')
        if m.get('ApAssetId') is not None:
            self.ap_asset_id = m.get('ApAssetId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppData') is not None:
            self.app_data = m.get('AppData')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('ThirdAppName') is not None:
            self.third_app_name = m.get('ThirdAppName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class SaveApThirdAppResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApThirdAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApThirdAppResponseBody = None,
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
            temp_model = SaveApThirdAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApgroupBasicConfigRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        country: str = None,
        dai: str = None,
        description: str = None,
        echo_int: int = None,
        failover: int = None,
        id: int = None,
        insecure_allowed: int = None,
        is_config_strong_consistency: bool = None,
        lan_ip: str = None,
        lan_mask: str = None,
        lan_status: int = None,
        log_ip: str = None,
        log_level: int = None,
        name: str = None,
        parent_apgroup_id: int = None,
        passwd: str = None,
        protocol: str = None,
        route: str = None,
        scan: int = None,
        token_server: str = None,
        vpn: str = None,
        work_mode: int = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.country = country
        self.dai = dai
        self.description = description
        self.echo_int = echo_int
        self.failover = failover
        self.id = id
        self.insecure_allowed = insecure_allowed
        self.is_config_strong_consistency = is_config_strong_consistency
        self.lan_ip = lan_ip
        self.lan_mask = lan_mask
        self.lan_status = lan_status
        self.log_ip = log_ip
        self.log_level = log_level
        self.name = name
        self.parent_apgroup_id = parent_apgroup_id
        self.passwd = passwd
        self.protocol = protocol
        self.route = route
        self.scan = scan
        self.token_server = token_server
        self.vpn = vpn
        self.work_mode = work_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.country is not None:
            result['Country'] = self.country
        if self.dai is not None:
            result['Dai'] = self.dai
        if self.description is not None:
            result['Description'] = self.description
        if self.echo_int is not None:
            result['EchoInt'] = self.echo_int
        if self.failover is not None:
            result['Failover'] = self.failover
        if self.id is not None:
            result['Id'] = self.id
        if self.insecure_allowed is not None:
            result['InsecureAllowed'] = self.insecure_allowed
        if self.is_config_strong_consistency is not None:
            result['IsConfigStrongConsistency'] = self.is_config_strong_consistency
        if self.lan_ip is not None:
            result['LanIp'] = self.lan_ip
        if self.lan_mask is not None:
            result['LanMask'] = self.lan_mask
        if self.lan_status is not None:
            result['LanStatus'] = self.lan_status
        if self.log_ip is not None:
            result['LogIp'] = self.log_ip
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_apgroup_id is not None:
            result['ParentApgroupId'] = self.parent_apgroup_id
        if self.passwd is not None:
            result['Passwd'] = self.passwd
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.route is not None:
            result['Route'] = self.route
        if self.scan is not None:
            result['Scan'] = self.scan
        if self.token_server is not None:
            result['TokenServer'] = self.token_server
        if self.vpn is not None:
            result['Vpn'] = self.vpn
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Dai') is not None:
            self.dai = m.get('Dai')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EchoInt') is not None:
            self.echo_int = m.get('EchoInt')
        if m.get('Failover') is not None:
            self.failover = m.get('Failover')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsecureAllowed') is not None:
            self.insecure_allowed = m.get('InsecureAllowed')
        if m.get('IsConfigStrongConsistency') is not None:
            self.is_config_strong_consistency = m.get('IsConfigStrongConsistency')
        if m.get('LanIp') is not None:
            self.lan_ip = m.get('LanIp')
        if m.get('LanMask') is not None:
            self.lan_mask = m.get('LanMask')
        if m.get('LanStatus') is not None:
            self.lan_status = m.get('LanStatus')
        if m.get('LogIp') is not None:
            self.log_ip = m.get('LogIp')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentApgroupId') is not None:
            self.parent_apgroup_id = m.get('ParentApgroupId')
        if m.get('Passwd') is not None:
            self.passwd = m.get('Passwd')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('Scan') is not None:
            self.scan = m.get('Scan')
        if m.get('TokenServer') is not None:
            self.token_server = m.get('TokenServer')
        if m.get('Vpn') is not None:
            self.vpn = m.get('Vpn')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        return self


class SaveApgroupBasicConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        task_id: str = None,
    ):
        self.id = id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SaveApgroupBasicConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: SaveApgroupBasicConfigResponseBodyData = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SaveApgroupBasicConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApgroupBasicConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApgroupBasicConfigResponseBody = None,
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
            temp_model = SaveApgroupBasicConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApgroupPortalConfigRequest(TeaModel):
    def __init__(
        self,
        apgroup_id: int = None,
        app_auth_url: str = None,
        app_code: str = None,
        app_name: str = None,
        auth_key: str = None,
        auth_secret: str = None,
        check_url: str = None,
        client_download: int = None,
        client_upload: int = None,
        countdown: int = None,
        network: int = None,
        portal_types: List[str] = None,
        portal_url: str = None,
        time_stamp: int = None,
        total_download: int = None,
        total_upload: int = None,
        web_auth_url: str = None,
        whitelist: str = None,
    ):
        self.apgroup_id = apgroup_id
        self.app_auth_url = app_auth_url
        self.app_code = app_code
        self.app_name = app_name
        self.auth_key = auth_key
        self.auth_secret = auth_secret
        self.check_url = check_url
        self.client_download = client_download
        self.client_upload = client_upload
        self.countdown = countdown
        self.network = network
        self.portal_types = portal_types
        self.portal_url = portal_url
        self.time_stamp = time_stamp
        self.total_download = total_download
        self.total_upload = total_upload
        self.web_auth_url = web_auth_url
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.client_download is not None:
            result['ClientDownload'] = self.client_download
        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload
        if self.countdown is not None:
            result['Countdown'] = self.countdown
        if self.network is not None:
            result['Network'] = self.network
        if self.portal_types is not None:
            result['PortalTypes'] = self.portal_types
        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')
        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')
        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PortalTypes') is not None:
            self.portal_types = m.get('PortalTypes')
        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class SaveApgroupPortalConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        apgroup_id: int = None,
        app_auth_url: str = None,
        app_code: str = None,
        app_name: str = None,
        auth_key: str = None,
        auth_secret: str = None,
        check_url: str = None,
        client_download: int = None,
        client_upload: int = None,
        countdown: int = None,
        network: int = None,
        portal_types_shrink: str = None,
        portal_url: str = None,
        time_stamp: int = None,
        total_download: int = None,
        total_upload: int = None,
        web_auth_url: str = None,
        whitelist: str = None,
    ):
        self.apgroup_id = apgroup_id
        self.app_auth_url = app_auth_url
        self.app_code = app_code
        self.app_name = app_name
        self.auth_key = auth_key
        self.auth_secret = auth_secret
        self.check_url = check_url
        self.client_download = client_download
        self.client_upload = client_upload
        self.countdown = countdown
        self.network = network
        self.portal_types_shrink = portal_types_shrink
        self.portal_url = portal_url
        self.time_stamp = time_stamp
        self.total_download = total_download
        self.total_upload = total_upload
        self.web_auth_url = web_auth_url
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.client_download is not None:
            result['ClientDownload'] = self.client_download
        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload
        if self.countdown is not None:
            result['Countdown'] = self.countdown
        if self.network is not None:
            result['Network'] = self.network
        if self.portal_types_shrink is not None:
            result['PortalTypes'] = self.portal_types_shrink
        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')
        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')
        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PortalTypes') is not None:
            self.portal_types_shrink = m.get('PortalTypes')
        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class SaveApgroupPortalConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApgroupPortalConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApgroupPortalConfigResponseBody = None,
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
            temp_model = SaveApgroupPortalConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApgroupSsidConfigRequest(TeaModel):
    def __init__(
        self,
        acct_port: int = None,
        acct_secret: str = None,
        acct_server: str = None,
        apgroup_id: str = None,
        app_code: str = None,
        app_name: str = None,
        auth_cache: str = None,
        auth_port: int = None,
        auth_secret: str = None,
        auth_server: str = None,
        binding: str = None,
        cir: int = None,
        dae_client: str = None,
        dae_port: int = None,
        dae_secret: str = None,
        disabled: str = None,
        disassoc_low_ack: str = None,
        disassoc_weak_rssi: int = None,
        dynamic_vlan: int = None,
        effect: bool = None,
        enc_key: str = None,
        encryption: str = None,
        hidden: str = None,
        id: int = None,
        ieee_80211w: str = None,
        ignore_weak_probe: int = None,
        isolate: str = None,
        lite_effect: bool = None,
        max_inactivity: int = None,
        maxassoc: str = None,
        multicast_forward: int = None,
        nasid: str = None,
        network: int = None,
        new_ssid: str = None,
        ownip: str = None,
        secondary_acct_port: int = None,
        secondary_acct_secret: str = None,
        secondary_acct_server: str = None,
        secondary_auth_port: int = None,
        secondary_auth_secret: str = None,
        secondary_auth_server: str = None,
        short_preamble: str = None,
        ssid: str = None,
        ssid_lb: int = None,
        type: int = None,
        vlan_dhcp: int = None,
        wmm: str = None,
    ):
        self.acct_port = acct_port
        self.acct_secret = acct_secret
        self.acct_server = acct_server
        self.apgroup_id = apgroup_id
        self.app_code = app_code
        self.app_name = app_name
        self.auth_cache = auth_cache
        self.auth_port = auth_port
        self.auth_secret = auth_secret
        self.auth_server = auth_server
        self.binding = binding
        self.cir = cir
        self.dae_client = dae_client
        self.dae_port = dae_port
        self.dae_secret = dae_secret
        self.disabled = disabled
        self.disassoc_low_ack = disassoc_low_ack
        self.disassoc_weak_rssi = disassoc_weak_rssi
        self.dynamic_vlan = dynamic_vlan
        self.effect = effect
        self.enc_key = enc_key
        self.encryption = encryption
        self.hidden = hidden
        self.id = id
        self.ieee_80211w = ieee_80211w
        self.ignore_weak_probe = ignore_weak_probe
        self.isolate = isolate
        self.lite_effect = lite_effect
        self.max_inactivity = max_inactivity
        self.maxassoc = maxassoc
        self.multicast_forward = multicast_forward
        self.nasid = nasid
        self.network = network
        self.new_ssid = new_ssid
        self.ownip = ownip
        self.secondary_acct_port = secondary_acct_port
        self.secondary_acct_secret = secondary_acct_secret
        self.secondary_acct_server = secondary_acct_server
        self.secondary_auth_port = secondary_auth_port
        self.secondary_auth_secret = secondary_auth_secret
        self.secondary_auth_server = secondary_auth_server
        self.short_preamble = short_preamble
        self.ssid = ssid
        self.ssid_lb = ssid_lb
        self.type = type
        self.vlan_dhcp = vlan_dhcp
        self.wmm = wmm

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acct_port is not None:
            result['AcctPort'] = self.acct_port
        if self.acct_secret is not None:
            result['AcctSecret'] = self.acct_secret
        if self.acct_server is not None:
            result['AcctServer'] = self.acct_server
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_cache is not None:
            result['AuthCache'] = self.auth_cache
        if self.auth_port is not None:
            result['AuthPort'] = self.auth_port
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.auth_server is not None:
            result['AuthServer'] = self.auth_server
        if self.binding is not None:
            result['Binding'] = self.binding
        if self.cir is not None:
            result['Cir'] = self.cir
        if self.dae_client is not None:
            result['DaeClient'] = self.dae_client
        if self.dae_port is not None:
            result['DaePort'] = self.dae_port
        if self.dae_secret is not None:
            result['DaeSecret'] = self.dae_secret
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.disassoc_low_ack is not None:
            result['DisassocLowAck'] = self.disassoc_low_ack
        if self.disassoc_weak_rssi is not None:
            result['DisassocWeakRssi'] = self.disassoc_weak_rssi
        if self.dynamic_vlan is not None:
            result['DynamicVlan'] = self.dynamic_vlan
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.enc_key is not None:
            result['EncKey'] = self.enc_key
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.id is not None:
            result['Id'] = self.id
        if self.ieee_80211w is not None:
            result['Ieee80211w'] = self.ieee_80211w
        if self.ignore_weak_probe is not None:
            result['IgnoreWeakProbe'] = self.ignore_weak_probe
        if self.isolate is not None:
            result['Isolate'] = self.isolate
        if self.lite_effect is not None:
            result['LiteEffect'] = self.lite_effect
        if self.max_inactivity is not None:
            result['MaxInactivity'] = self.max_inactivity
        if self.maxassoc is not None:
            result['Maxassoc'] = self.maxassoc
        if self.multicast_forward is not None:
            result['MulticastForward'] = self.multicast_forward
        if self.nasid is not None:
            result['Nasid'] = self.nasid
        if self.network is not None:
            result['Network'] = self.network
        if self.new_ssid is not None:
            result['NewSsid'] = self.new_ssid
        if self.ownip is not None:
            result['Ownip'] = self.ownip
        if self.secondary_acct_port is not None:
            result['SecondaryAcctPort'] = self.secondary_acct_port
        if self.secondary_acct_secret is not None:
            result['SecondaryAcctSecret'] = self.secondary_acct_secret
        if self.secondary_acct_server is not None:
            result['SecondaryAcctServer'] = self.secondary_acct_server
        if self.secondary_auth_port is not None:
            result['SecondaryAuthPort'] = self.secondary_auth_port
        if self.secondary_auth_secret is not None:
            result['SecondaryAuthSecret'] = self.secondary_auth_secret
        if self.secondary_auth_server is not None:
            result['SecondaryAuthServer'] = self.secondary_auth_server
        if self.short_preamble is not None:
            result['ShortPreamble'] = self.short_preamble
        if self.ssid is not None:
            result['Ssid'] = self.ssid
        if self.ssid_lb is not None:
            result['SsidLb'] = self.ssid_lb
        if self.type is not None:
            result['Type'] = self.type
        if self.vlan_dhcp is not None:
            result['VlanDhcp'] = self.vlan_dhcp
        if self.wmm is not None:
            result['Wmm'] = self.wmm
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcctPort') is not None:
            self.acct_port = m.get('AcctPort')
        if m.get('AcctSecret') is not None:
            self.acct_secret = m.get('AcctSecret')
        if m.get('AcctServer') is not None:
            self.acct_server = m.get('AcctServer')
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthCache') is not None:
            self.auth_cache = m.get('AuthCache')
        if m.get('AuthPort') is not None:
            self.auth_port = m.get('AuthPort')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('AuthServer') is not None:
            self.auth_server = m.get('AuthServer')
        if m.get('Binding') is not None:
            self.binding = m.get('Binding')
        if m.get('Cir') is not None:
            self.cir = m.get('Cir')
        if m.get('DaeClient') is not None:
            self.dae_client = m.get('DaeClient')
        if m.get('DaePort') is not None:
            self.dae_port = m.get('DaePort')
        if m.get('DaeSecret') is not None:
            self.dae_secret = m.get('DaeSecret')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DisassocLowAck') is not None:
            self.disassoc_low_ack = m.get('DisassocLowAck')
        if m.get('DisassocWeakRssi') is not None:
            self.disassoc_weak_rssi = m.get('DisassocWeakRssi')
        if m.get('DynamicVlan') is not None:
            self.dynamic_vlan = m.get('DynamicVlan')
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('EncKey') is not None:
            self.enc_key = m.get('EncKey')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ieee80211w') is not None:
            self.ieee_80211w = m.get('Ieee80211w')
        if m.get('IgnoreWeakProbe') is not None:
            self.ignore_weak_probe = m.get('IgnoreWeakProbe')
        if m.get('Isolate') is not None:
            self.isolate = m.get('Isolate')
        if m.get('LiteEffect') is not None:
            self.lite_effect = m.get('LiteEffect')
        if m.get('MaxInactivity') is not None:
            self.max_inactivity = m.get('MaxInactivity')
        if m.get('Maxassoc') is not None:
            self.maxassoc = m.get('Maxassoc')
        if m.get('MulticastForward') is not None:
            self.multicast_forward = m.get('MulticastForward')
        if m.get('Nasid') is not None:
            self.nasid = m.get('Nasid')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NewSsid') is not None:
            self.new_ssid = m.get('NewSsid')
        if m.get('Ownip') is not None:
            self.ownip = m.get('Ownip')
        if m.get('SecondaryAcctPort') is not None:
            self.secondary_acct_port = m.get('SecondaryAcctPort')
        if m.get('SecondaryAcctSecret') is not None:
            self.secondary_acct_secret = m.get('SecondaryAcctSecret')
        if m.get('SecondaryAcctServer') is not None:
            self.secondary_acct_server = m.get('SecondaryAcctServer')
        if m.get('SecondaryAuthPort') is not None:
            self.secondary_auth_port = m.get('SecondaryAuthPort')
        if m.get('SecondaryAuthSecret') is not None:
            self.secondary_auth_secret = m.get('SecondaryAuthSecret')
        if m.get('SecondaryAuthServer') is not None:
            self.secondary_auth_server = m.get('SecondaryAuthServer')
        if m.get('ShortPreamble') is not None:
            self.short_preamble = m.get('ShortPreamble')
        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')
        if m.get('SsidLb') is not None:
            self.ssid_lb = m.get('SsidLb')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VlanDhcp') is not None:
            self.vlan_dhcp = m.get('VlanDhcp')
        if m.get('Wmm') is not None:
            self.wmm = m.get('Wmm')
        return self


class SaveApgroupSsidConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class SaveApgroupSsidConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveApgroupSsidConfigResponseBody = None,
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
            temp_model = SaveApgroupSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApAddressRequest(TeaModel):
    def __init__(
        self,
        ap_area_name: str = None,
        ap_building_name: str = None,
        ap_campus_name: str = None,
        ap_city_name: str = None,
        ap_floor: str = None,
        ap_group: str = None,
        ap_name: str = None,
        ap_nation_name: str = None,
        ap_province_name: str = None,
        ap_unit_id: int = None,
        ap_unit_name: str = None,
        app_code: str = None,
        app_name: str = None,
        direction: str = None,
        language: str = None,
        lat: str = None,
        lng: str = None,
        mac: str = None,
    ):
        self.ap_area_name = ap_area_name
        self.ap_building_name = ap_building_name
        self.ap_campus_name = ap_campus_name
        self.ap_city_name = ap_city_name
        self.ap_floor = ap_floor
        self.ap_group = ap_group
        self.ap_name = ap_name
        self.ap_nation_name = ap_nation_name
        self.ap_province_name = ap_province_name
        self.ap_unit_id = ap_unit_id
        self.ap_unit_name = ap_unit_name
        self.app_code = app_code
        self.app_name = app_name
        self.direction = direction
        self.language = language
        self.lat = lat
        self.lng = lng
        self.mac = mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_area_name is not None:
            result['ApAreaName'] = self.ap_area_name
        if self.ap_building_name is not None:
            result['ApBuildingName'] = self.ap_building_name
        if self.ap_campus_name is not None:
            result['ApCampusName'] = self.ap_campus_name
        if self.ap_city_name is not None:
            result['ApCityName'] = self.ap_city_name
        if self.ap_floor is not None:
            result['ApFloor'] = self.ap_floor
        if self.ap_group is not None:
            result['ApGroup'] = self.ap_group
        if self.ap_name is not None:
            result['ApName'] = self.ap_name
        if self.ap_nation_name is not None:
            result['ApNationName'] = self.ap_nation_name
        if self.ap_province_name is not None:
            result['ApProvinceName'] = self.ap_province_name
        if self.ap_unit_id is not None:
            result['ApUnitId'] = self.ap_unit_id
        if self.ap_unit_name is not None:
            result['ApUnitName'] = self.ap_unit_name
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.language is not None:
            result['Language'] = self.language
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lng is not None:
            result['Lng'] = self.lng
        if self.mac is not None:
            result['Mac'] = self.mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApAreaName') is not None:
            self.ap_area_name = m.get('ApAreaName')
        if m.get('ApBuildingName') is not None:
            self.ap_building_name = m.get('ApBuildingName')
        if m.get('ApCampusName') is not None:
            self.ap_campus_name = m.get('ApCampusName')
        if m.get('ApCityName') is not None:
            self.ap_city_name = m.get('ApCityName')
        if m.get('ApFloor') is not None:
            self.ap_floor = m.get('ApFloor')
        if m.get('ApGroup') is not None:
            self.ap_group = m.get('ApGroup')
        if m.get('ApName') is not None:
            self.ap_name = m.get('ApName')
        if m.get('ApNationName') is not None:
            self.ap_nation_name = m.get('ApNationName')
        if m.get('ApProvinceName') is not None:
            self.ap_province_name = m.get('ApProvinceName')
        if m.get('ApUnitId') is not None:
            self.ap_unit_id = m.get('ApUnitId')
        if m.get('ApUnitName') is not None:
            self.ap_unit_name = m.get('ApUnitName')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lng') is not None:
            self.lng = m.get('Lng')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        return self


class SetApAddressResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class SetApAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetApAddressResponseBody = None,
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
            temp_model = SetApAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApNameRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        app_code: str = None,
        app_name: str = None,
        name: str = None,
    ):
        self.ap_mac = ap_mac
        self.app_code = app_code
        self.app_name = app_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetApNameResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class SetApNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetApNameResponseBody = None,
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
            temp_model = SetApNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnRegisterApAssetRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        asset_apgroup_id: int = None,
        category: int = None,
        id: int = None,
        mac: str = None,
        serial_no: str = None,
        use_for: int = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.asset_apgroup_id = asset_apgroup_id
        self.category = category
        self.id = id
        self.mac = mac
        self.serial_no = serial_no
        self.use_for = use_for

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.asset_apgroup_id is not None:
            result['AssetApgroupId'] = self.asset_apgroup_id
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.use_for is not None:
            result['UseFor'] = self.use_for
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AssetApgroupId') is not None:
            self.asset_apgroup_id = m.get('AssetApgroupId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('UseFor') is not None:
            self.use_for = m.get('UseFor')
        return self


class UnRegisterApAssetResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnRegisterApAssetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnRegisterApAssetResponseBody = None,
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
            temp_model = UnRegisterApAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNetDeviceInfoRequestDevices(TeaModel):
    def __init__(
        self,
        host_name: str = None,
        id: int = None,
        idc: str = None,
        logic_net_pod: str = None,
        manufacturer: str = None,
        mgn_ip: str = None,
        model: str = None,
        net_pod: str = None,
        password: str = None,
        role: str = None,
        service_tag: str = None,
        username: str = None,
    ):
        self.host_name = host_name
        self.id = id
        self.idc = idc
        self.logic_net_pod = logic_net_pod
        self.manufacturer = manufacturer
        self.mgn_ip = mgn_ip
        self.model = model
        self.net_pod = net_pod
        self.password = password
        self.role = role
        self.service_tag = service_tag
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip
        if self.model is not None:
            result['Model'] = self.model
        if self.net_pod is not None:
            result['NetPod'] = self.net_pod
        if self.password is not None:
            result['Password'] = self.password
        if self.role is not None:
            result['Role'] = self.role
        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateNetDeviceInfoRequest(TeaModel):
    def __init__(
        self,
        app_code: str = None,
        app_name: str = None,
        devices: List[UpdateNetDeviceInfoRequestDevices] = None,
        request_id: str = None,
    ):
        self.app_code = app_code
        self.app_name = app_name
        self.devices = devices
        self.request_id = request_id

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = UpdateNetDeviceInfoRequestDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNetDeviceInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: List[int] = None,
        error_code: int = None,
        error_message: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNetDeviceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNetDeviceInfoResponseBody = None,
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
            temp_model = UpdateNetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


