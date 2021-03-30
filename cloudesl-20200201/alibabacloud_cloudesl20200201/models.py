# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActivateApDeviceRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        store_id: str = None,
        extra_params: str = None,
    ):
        self.ap_mac = ap_mac
        self.store_id = store_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class ActivateApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ActivateApDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ActivateApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddApDeviceRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        ap_mac: str = None,
        remark: str = None,
        client_token: str = None,
        extra_params: str = None,
    ):
        self.store_id = store_id
        self.ap_mac = ap_mac
        self.remark = remark
        self.client_token = client_token
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class AddApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddApDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddPlanogramShelfRequest(TeaModel):
    def __init__(
        self,
        shelf_type: str = None,
        store_id: str = None,
        shelf: str = None,
        zone: str = None,
        category: str = None,
        client_token: str = None,
        extra_params: str = None,
    ):
        self.shelf_type = shelf_type
        self.store_id = store_id
        self.shelf = shelf
        self.zone = zone
        self.category = category
        self.client_token = client_token
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shelf_type is not None:
            result['ShelfType'] = self.shelf_type
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.zone is not None:
            result['Zone'] = self.zone
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShelfType') is not None:
            self.shelf_type = m.get('ShelfType')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class AddPlanogramShelfResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddPlanogramShelfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddPlanogramShelfResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddPlanogramShelfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRoleActionsRequest(TeaModel):
    def __init__(
        self,
        access_control_lists: str = None,
        extra_params: str = None,
        role_code: str = None,
        client_token: str = None,
    ):
        self.access_control_lists = access_control_lists
        self.extra_params = extra_params
        self.role_code = role_code
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_lists is not None:
            result['AccessControlLists'] = self.access_control_lists
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlLists') is not None:
            self.access_control_lists = m.get('AccessControlLists')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddRoleActionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRoleActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRoleActionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddRoleActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        client_token: str = None,
        extra_params: str = None,
    ):
        self.user_id = user_id
        self.client_token = client_token
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class AddUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignUserRequest(TeaModel):
    def __init__(
        self,
        stores: str = None,
        user_id: str = None,
        user_type: str = None,
        extra_params: str = None,
    ):
        self.stores = stores
        self.user_id = user_id
        self.user_type = user_type
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class AssignUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssignUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssignUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssignUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociatePlanogramRailRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        layer: int = None,
        shelf: str = None,
        rail_code: str = None,
        extra_params: str = None,
    ):
        self.store_id = store_id
        self.layer = layer
        self.shelf = shelf
        self.rail_code = rail_code
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class AssociatePlanogramRailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssociatePlanogramRailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssociatePlanogramRailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssociatePlanogramRailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchInsertItemsRequestItemInfo(TeaModel):
    def __init__(
        self,
        action_price: int = None,
        item_title: str = None,
        brand_name: str = None,
        price_unit: str = None,
        source_code: str = None,
        forest_first_id: str = None,
        customize_feature_f: str = None,
        customize_feature_a: str = None,
        customize_feature_k: str = None,
        member_price: int = None,
        customize_feature_d: str = None,
        promotion_start: str = None,
        model_number: str = None,
        category_name: str = None,
        customize_feature_e: str = None,
        suggest_price: int = None,
        sale_spec: str = None,
        promotion_text: str = None,
        promotion_reason: str = None,
        rank: str = None,
        customize_feature_g: str = None,
        sales_price: int = None,
        customize_feature_h: str = None,
        original_price: int = None,
        customize_feature_i: str = None,
        production_place: str = None,
        item_short_title: str = None,
        customize_feature_b: str = None,
        customize_feature_n: str = None,
        tax_fee: str = None,
        inventory_status: str = None,
        supplier_name: str = None,
        item_pic_url: str = None,
        customize_feature_l: str = None,
        energy_efficiency: str = None,
        customize_feature_c: str = None,
        item_id: str = None,
        manufacturer: str = None,
        material: str = None,
        customize_feature_o: str = None,
        customize_feature_j: str = None,
        be_promotion: bool = None,
        sku_id: str = None,
        customize_feature_m: str = None,
        be_source_code: bool = None,
        forest_second_id: str = None,
        item_qr_code: str = None,
        item_info_index: int = None,
        promotion_end: str = None,
        item_bar_code: str = None,
    ):
        self.action_price = action_price
        self.item_title = item_title
        self.brand_name = brand_name
        self.price_unit = price_unit
        self.source_code = source_code
        self.forest_first_id = forest_first_id
        self.customize_feature_f = customize_feature_f
        self.customize_feature_a = customize_feature_a
        self.customize_feature_k = customize_feature_k
        self.member_price = member_price
        self.customize_feature_d = customize_feature_d
        self.promotion_start = promotion_start
        self.model_number = model_number
        self.category_name = category_name
        self.customize_feature_e = customize_feature_e
        self.suggest_price = suggest_price
        self.sale_spec = sale_spec
        self.promotion_text = promotion_text
        self.promotion_reason = promotion_reason
        self.rank = rank
        self.customize_feature_g = customize_feature_g
        self.sales_price = sales_price
        self.customize_feature_h = customize_feature_h
        self.original_price = original_price
        self.customize_feature_i = customize_feature_i
        self.production_place = production_place
        self.item_short_title = item_short_title
        self.customize_feature_b = customize_feature_b
        self.customize_feature_n = customize_feature_n
        self.tax_fee = tax_fee
        self.inventory_status = inventory_status
        self.supplier_name = supplier_name
        self.item_pic_url = item_pic_url
        self.customize_feature_l = customize_feature_l
        self.energy_efficiency = energy_efficiency
        self.customize_feature_c = customize_feature_c
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.material = material
        self.customize_feature_o = customize_feature_o
        self.customize_feature_j = customize_feature_j
        self.be_promotion = be_promotion
        self.sku_id = sku_id
        self.customize_feature_m = customize_feature_m
        self.be_source_code = be_source_code
        self.forest_second_id = forest_second_id
        self.item_qr_code = item_qr_code
        self.item_info_index = item_info_index
        self.promotion_end = promotion_end
        self.item_bar_code = item_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.forest_first_id is not None:
            result['ForestFirstId'] = self.forest_first_id
        if self.customize_feature_f is not None:
            result['CustomizeFeatureF'] = self.customize_feature_f
        if self.customize_feature_a is not None:
            result['CustomizeFeatureA'] = self.customize_feature_a
        if self.customize_feature_k is not None:
            result['CustomizeFeatureK'] = self.customize_feature_k
        if self.member_price is not None:
            result['MemberPrice'] = self.member_price
        if self.customize_feature_d is not None:
            result['CustomizeFeatureD'] = self.customize_feature_d
        if self.promotion_start is not None:
            result['PromotionStart'] = self.promotion_start
        if self.model_number is not None:
            result['ModelNumber'] = self.model_number
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.customize_feature_e is not None:
            result['CustomizeFeatureE'] = self.customize_feature_e
        if self.suggest_price is not None:
            result['SuggestPrice'] = self.suggest_price
        if self.sale_spec is not None:
            result['SaleSpec'] = self.sale_spec
        if self.promotion_text is not None:
            result['PromotionText'] = self.promotion_text
        if self.promotion_reason is not None:
            result['PromotionReason'] = self.promotion_reason
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.customize_feature_g is not None:
            result['CustomizeFeatureG'] = self.customize_feature_g
        if self.sales_price is not None:
            result['SalesPrice'] = self.sales_price
        if self.customize_feature_h is not None:
            result['CustomizeFeatureH'] = self.customize_feature_h
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.customize_feature_i is not None:
            result['CustomizeFeatureI'] = self.customize_feature_i
        if self.production_place is not None:
            result['ProductionPlace'] = self.production_place
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.customize_feature_b is not None:
            result['CustomizeFeatureB'] = self.customize_feature_b
        if self.customize_feature_n is not None:
            result['CustomizeFeatureN'] = self.customize_feature_n
        if self.tax_fee is not None:
            result['TaxFee'] = self.tax_fee
        if self.inventory_status is not None:
            result['InventoryStatus'] = self.inventory_status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        if self.customize_feature_l is not None:
            result['CustomizeFeatureL'] = self.customize_feature_l
        if self.energy_efficiency is not None:
            result['EnergyEfficiency'] = self.energy_efficiency
        if self.customize_feature_c is not None:
            result['CustomizeFeatureC'] = self.customize_feature_c
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.material is not None:
            result['Material'] = self.material
        if self.customize_feature_o is not None:
            result['CustomizeFeatureO'] = self.customize_feature_o
        if self.customize_feature_j is not None:
            result['CustomizeFeatureJ'] = self.customize_feature_j
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.customize_feature_m is not None:
            result['CustomizeFeatureM'] = self.customize_feature_m
        if self.be_source_code is not None:
            result['BeSourceCode'] = self.be_source_code
        if self.forest_second_id is not None:
            result['ForestSecondId'] = self.forest_second_id
        if self.item_qr_code is not None:
            result['ItemQrCode'] = self.item_qr_code
        if self.item_info_index is not None:
            result['ItemInfoIndex'] = self.item_info_index
        if self.promotion_end is not None:
            result['PromotionEnd'] = self.promotion_end
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('ForestFirstId') is not None:
            self.forest_first_id = m.get('ForestFirstId')
        if m.get('CustomizeFeatureF') is not None:
            self.customize_feature_f = m.get('CustomizeFeatureF')
        if m.get('CustomizeFeatureA') is not None:
            self.customize_feature_a = m.get('CustomizeFeatureA')
        if m.get('CustomizeFeatureK') is not None:
            self.customize_feature_k = m.get('CustomizeFeatureK')
        if m.get('MemberPrice') is not None:
            self.member_price = m.get('MemberPrice')
        if m.get('CustomizeFeatureD') is not None:
            self.customize_feature_d = m.get('CustomizeFeatureD')
        if m.get('PromotionStart') is not None:
            self.promotion_start = m.get('PromotionStart')
        if m.get('ModelNumber') is not None:
            self.model_number = m.get('ModelNumber')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CustomizeFeatureE') is not None:
            self.customize_feature_e = m.get('CustomizeFeatureE')
        if m.get('SuggestPrice') is not None:
            self.suggest_price = m.get('SuggestPrice')
        if m.get('SaleSpec') is not None:
            self.sale_spec = m.get('SaleSpec')
        if m.get('PromotionText') is not None:
            self.promotion_text = m.get('PromotionText')
        if m.get('PromotionReason') is not None:
            self.promotion_reason = m.get('PromotionReason')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('CustomizeFeatureG') is not None:
            self.customize_feature_g = m.get('CustomizeFeatureG')
        if m.get('SalesPrice') is not None:
            self.sales_price = m.get('SalesPrice')
        if m.get('CustomizeFeatureH') is not None:
            self.customize_feature_h = m.get('CustomizeFeatureH')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('CustomizeFeatureI') is not None:
            self.customize_feature_i = m.get('CustomizeFeatureI')
        if m.get('ProductionPlace') is not None:
            self.production_place = m.get('ProductionPlace')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('CustomizeFeatureB') is not None:
            self.customize_feature_b = m.get('CustomizeFeatureB')
        if m.get('CustomizeFeatureN') is not None:
            self.customize_feature_n = m.get('CustomizeFeatureN')
        if m.get('TaxFee') is not None:
            self.tax_fee = m.get('TaxFee')
        if m.get('InventoryStatus') is not None:
            self.inventory_status = m.get('InventoryStatus')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        if m.get('CustomizeFeatureL') is not None:
            self.customize_feature_l = m.get('CustomizeFeatureL')
        if m.get('EnergyEfficiency') is not None:
            self.energy_efficiency = m.get('EnergyEfficiency')
        if m.get('CustomizeFeatureC') is not None:
            self.customize_feature_c = m.get('CustomizeFeatureC')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('CustomizeFeatureO') is not None:
            self.customize_feature_o = m.get('CustomizeFeatureO')
        if m.get('CustomizeFeatureJ') is not None:
            self.customize_feature_j = m.get('CustomizeFeatureJ')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('CustomizeFeatureM') is not None:
            self.customize_feature_m = m.get('CustomizeFeatureM')
        if m.get('BeSourceCode') is not None:
            self.be_source_code = m.get('BeSourceCode')
        if m.get('ForestSecondId') is not None:
            self.forest_second_id = m.get('ForestSecondId')
        if m.get('ItemQrCode') is not None:
            self.item_qr_code = m.get('ItemQrCode')
        if m.get('ItemInfoIndex') is not None:
            self.item_info_index = m.get('ItemInfoIndex')
        if m.get('PromotionEnd') is not None:
            self.promotion_end = m.get('PromotionEnd')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        return self


class BatchInsertItemsRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        extra_params: str = None,
        item_info: List[BatchInsertItemsRequestItemInfo] = None,
    ):
        self.store_id = store_id
        self.extra_params = extra_params
        self.item_info = item_info

    def validate(self):
        if self.item_info:
            for k in self.item_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        result['ItemInfo'] = []
        if self.item_info is not None:
            for k in self.item_info:
                result['ItemInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        self.item_info = []
        if m.get('ItemInfo') is not None:
            for k in m.get('ItemInfo'):
                temp_model = BatchInsertItemsRequestItemInfo()
                self.item_info.append(temp_model.from_map(k))
        return self


class BatchInsertItemsResponseBodyBatchResults(TeaModel):
    def __init__(
        self,
        index: int = None,
        success: bool = None,
        error_code: str = None,
        message: str = None,
    ):
        self.index = index
        self.success = success
        self.error_code = error_code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.success is not None:
            result['Success'] = self.success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class BatchInsertItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        batch_results: List[BatchInsertItemsResponseBodyBatchResults] = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.batch_results = batch_results
        self.code = code
        self.success = success

    def validate(self):
        if self.batch_results:
            for k in self.batch_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['BatchResults'] = []
        if self.batch_results is not None:
            for k in self.batch_results:
                result['BatchResults'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.batch_results = []
        if m.get('BatchResults') is not None:
            for k in m.get('BatchResults'):
                temp_model = BatchInsertItemsResponseBodyBatchResults()
                self.batch_results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchInsertItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchInsertItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchInsertItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindEslDeviceRequest(TeaModel):
    def __init__(
        self,
        item_bar_code: str = None,
        esl_bar_code: str = None,
        store_id: str = None,
        shelf: str = None,
        layer: int = None,
        column: str = None,
        extra_params: str = None,
    ):
        self.item_bar_code = item_bar_code
        self.esl_bar_code = esl_bar_code
        self.store_id = store_id
        self.shelf = shelf
        self.layer = layer
        self.column = column
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.column is not None:
            result['Column'] = self.column
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class BindEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindEslDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ComposePlanogramPositionsRequestShelfPositionInfo(TeaModel):
    def __init__(
        self,
        depth: float = None,
        facing: int = None,
        offset_to: float = None,
        offset_from: float = None,
        column: str = None,
        item_bar_code: str = None,
    ):
        self.depth = depth
        self.facing = facing
        self.offset_to = offset_to
        self.offset_from = offset_from
        self.column = column
        self.item_bar_code = item_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.facing is not None:
            result['Facing'] = self.facing
        if self.offset_to is not None:
            result['OffsetTo'] = self.offset_to
        if self.offset_from is not None:
            result['OffsetFrom'] = self.offset_from
        if self.column is not None:
            result['Column'] = self.column
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('Facing') is not None:
            self.facing = m.get('Facing')
        if m.get('OffsetTo') is not None:
            self.offset_to = m.get('OffsetTo')
        if m.get('OffsetFrom') is not None:
            self.offset_from = m.get('OffsetFrom')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        return self


class ComposePlanogramPositionsRequest(TeaModel):
    def __init__(
        self,
        be_auto_refresh: bool = None,
        layer_origin: str = None,
        layer: int = None,
        action_type: str = None,
        shelf: str = None,
        store_id: str = None,
        extra_params: str = None,
        shelf_position_info: List[ComposePlanogramPositionsRequestShelfPositionInfo] = None,
    ):
        self.be_auto_refresh = be_auto_refresh
        self.layer_origin = layer_origin
        self.layer = layer
        self.action_type = action_type
        self.shelf = shelf
        self.store_id = store_id
        self.extra_params = extra_params
        self.shelf_position_info = shelf_position_info

    def validate(self):
        if self.shelf_position_info:
            for k in self.shelf_position_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.be_auto_refresh is not None:
            result['BeAutoRefresh'] = self.be_auto_refresh
        if self.layer_origin is not None:
            result['LayerOrigin'] = self.layer_origin
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        result['ShelfPositionInfo'] = []
        if self.shelf_position_info is not None:
            for k in self.shelf_position_info:
                result['ShelfPositionInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeAutoRefresh') is not None:
            self.be_auto_refresh = m.get('BeAutoRefresh')
        if m.get('LayerOrigin') is not None:
            self.layer_origin = m.get('LayerOrigin')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        self.shelf_position_info = []
        if m.get('ShelfPositionInfo') is not None:
            for k in m.get('ShelfPositionInfo'):
                temp_model = ComposePlanogramPositionsRequestShelfPositionInfo()
                self.shelf_position_info.append(temp_model.from_map(k))
        return self


class ComposePlanogramPositionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ComposePlanogramPositionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ComposePlanogramPositionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ComposePlanogramPositionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoreRequest(TeaModel):
    def __init__(
        self,
        parent_id: str = None,
        user_store_code: str = None,
        store_name: str = None,
        phone: str = None,
        client_token: str = None,
        extra_params: str = None,
    ):
        self.parent_id = parent_id
        self.user_store_code = user_store_code
        self.store_name = store_name
        self.phone = phone
        self.client_token = client_token
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class CreateStoreResponseBody(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.store_id = store_id
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateStoreResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApDeviceRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        store_id: str = None,
        extra_params: str = None,
    ):
        self.ap_mac = ap_mac
        self.store_id = store_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DeleteApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteApDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePlanogramShelfRequest(TeaModel):
    def __init__(
        self,
        be_auto_refresh: bool = None,
        store_id: str = None,
        shelf: str = None,
        extra_params: str = None,
    ):
        self.be_auto_refresh = be_auto_refresh
        self.store_id = store_id
        self.shelf = shelf
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.be_auto_refresh is not None:
            result['BeAutoRefresh'] = self.be_auto_refresh
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeAutoRefresh') is not None:
            self.be_auto_refresh = m.get('BeAutoRefresh')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DeletePlanogramShelfResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePlanogramShelfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeletePlanogramShelfResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeletePlanogramShelfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoleActionsRequest(TeaModel):
    def __init__(
        self,
        access_control_lists: str = None,
        extra_params: str = None,
        role_code: str = None,
    ):
        self.access_control_lists = access_control_lists
        self.extra_params = extra_params
        self.role_code = role_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_lists is not None:
            result['AccessControlLists'] = self.access_control_lists
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessControlLists') is not None:
            self.access_control_lists = m.get('AccessControlLists')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        return self


class DeleteRoleActionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRoleActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRoleActionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteRoleActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStoreRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        extra_params: str = None,
    ):
        self.store_id = store_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DeleteStoreResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteStoreResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        extra_params: str = None,
    ):
        self.user_id = user_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmsRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        device_mac: str = None,
        page_number: int = None,
        error_type: str = None,
        page_size: int = None,
        alarm_type: str = None,
        alarm_status: str = None,
        store_id: str = None,
        extra_params: str = None,
    ):
        self.alarm_id = alarm_id
        self.device_mac = device_mac
        self.page_number = page_number
        self.error_type = error_type
        self.page_size = page_size
        self.alarm_type = alarm_type
        self.alarm_status = alarm_status
        self.store_id = store_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.device_mac is not None:
            result['DeviceMac'] = self.device_mac
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.error_type is not None:
            result['ErrorType'] = self.error_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('DeviceMac') is not None:
            self.device_mac = m.get('DeviceMac')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeAlarmsResponseBodyAlarms(TeaModel):
    def __init__(
        self,
        alarm_status: str = None,
        remark: str = None,
        item_title: str = None,
        device_type: str = None,
        device_bar_code: str = None,
        retry_times: int = None,
        alarm_type: str = None,
        retry_gmt_create: str = None,
        store_id: str = None,
        deal_time: str = None,
        device_mac: str = None,
        alarm_time: str = None,
        deal_user_id: str = None,
        alarm_id: str = None,
        error_type: str = None,
        retry_gmt_modified: str = None,
        item_bar_code: str = None,
    ):
        self.alarm_status = alarm_status
        self.remark = remark
        self.item_title = item_title
        self.device_type = device_type
        self.device_bar_code = device_bar_code
        self.retry_times = retry_times
        self.alarm_type = alarm_type
        self.retry_gmt_create = retry_gmt_create
        self.store_id = store_id
        self.deal_time = deal_time
        self.device_mac = device_mac
        self.alarm_time = alarm_time
        self.deal_user_id = deal_user_id
        self.alarm_id = alarm_id
        self.error_type = error_type
        self.retry_gmt_modified = retry_gmt_modified
        self.item_bar_code = item_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.device_bar_code is not None:
            result['DeviceBarCode'] = self.device_bar_code
        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.retry_gmt_create is not None:
            result['RetryGmtCreate'] = self.retry_gmt_create
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.device_mac is not None:
            result['DeviceMac'] = self.device_mac
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.error_type is not None:
            result['ErrorType'] = self.error_type
        if self.retry_gmt_modified is not None:
            result['RetryGmtModified'] = self.retry_gmt_modified
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('DeviceBarCode') is not None:
            self.device_bar_code = m.get('DeviceBarCode')
        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('RetryGmtCreate') is not None:
            self.retry_gmt_create = m.get('RetryGmtCreate')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('DeviceMac') is not None:
            self.device_mac = m.get('DeviceMac')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')
        if m.get('RetryGmtModified') is not None:
            self.retry_gmt_modified = m.get('RetryGmtModified')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        return self


class DescribeAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        alarms: List[DescribeAlarmsResponseBodyAlarms] = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.alarms = alarms
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.alarms:
            for k in self.alarms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Alarms'] = []
        if self.alarms is not None:
            for k in self.alarms:
                result['Alarms'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.alarms = []
        if m.get('Alarms') is not None:
            for k in m.get('Alarms'):
                temp_model = DescribeAlarmsResponseBodyAlarms()
                self.alarms.append(temp_model.from_map(k))
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAlarmsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApDevicesRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        ap_mac: str = None,
        status: bool = None,
        page_size: int = None,
        page_number: int = None,
        model: str = None,
        be_activate: bool = None,
        extra_params: str = None,
    ):
        self.store_id = store_id
        self.ap_mac = ap_mac
        self.status = status
        self.page_size = page_size
        self.page_number = page_number
        self.model = model
        self.be_activate = be_activate
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.status is not None:
            result['Status'] = self.status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.model is not None:
            result['Model'] = self.model
        if self.be_activate is not None:
            result['BeActivate'] = self.be_activate
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('BeActivate') is not None:
            self.be_activate = m.get('BeActivate')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeApDevicesResponseBodyApDevices(TeaModel):
    def __init__(
        self,
        status: bool = None,
        store_id: str = None,
        model: str = None,
        remark: str = None,
        be_activate: bool = None,
        mac: str = None,
    ):
        self.status = status
        self.store_id = store_id
        self.model = model
        self.remark = remark
        self.be_activate = be_activate
        self.mac = mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.model is not None:
            result['Model'] = self.model
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.be_activate is not None:
            result['BeActivate'] = self.be_activate
        if self.mac is not None:
            result['Mac'] = self.mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('BeActivate') is not None:
            self.be_activate = m.get('BeActivate')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        return self


class DescribeApDevicesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        ap_devices: List[DescribeApDevicesResponseBodyApDevices] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.ap_devices = ap_devices
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.ap_devices:
            for k in self.ap_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['ApDevices'] = []
        if self.ap_devices is not None:
            for k in self.ap_devices:
                result['ApDevices'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.ap_devices = []
        if m.get('ApDevices') is not None:
            for k in m.get('ApDevices'):
                temp_model = DescribeApDevicesResponseBodyApDevices()
                self.ap_devices.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeApDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeApDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeApDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBindersRequest(TeaModel):
    def __init__(
        self,
        item_bar_code: str = None,
        esl_bar_code: str = None,
        store_id: str = None,
        page_number: int = None,
        item_title: str = None,
        page_size: int = None,
        extra_params: str = None,
    ):
        self.item_bar_code = item_bar_code
        self.esl_bar_code = esl_bar_code
        self.store_id = store_id
        self.page_number = page_number
        self.item_title = item_title
        self.page_size = page_size
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeBindersResponseBodyEslItemBindInfos(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        template_scene_id: str = None,
        action_price: str = None,
        item_title: str = None,
        promotion_start: str = None,
        price_unit: str = None,
        original_price: str = None,
        item_id: str = None,
        esl_pic: str = None,
        gmt_modified: str = None,
        store_id: str = None,
        item_short_title: str = None,
        bind_id: str = None,
        promotion_text: str = None,
        esl_model: str = None,
        be_promotion: bool = None,
        sku_id: str = None,
        esl_connect_ap: str = None,
        esl_status: str = None,
        template_id: str = None,
        promotion_end: str = None,
        item_bar_code: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.template_scene_id = template_scene_id
        self.action_price = action_price
        self.item_title = item_title
        self.promotion_start = promotion_start
        self.price_unit = price_unit
        self.original_price = original_price
        self.item_id = item_id
        self.esl_pic = esl_pic
        self.gmt_modified = gmt_modified
        self.store_id = store_id
        self.item_short_title = item_short_title
        self.bind_id = bind_id
        self.promotion_text = promotion_text
        self.esl_model = esl_model
        self.be_promotion = be_promotion
        self.sku_id = sku_id
        self.esl_connect_ap = esl_connect_ap
        self.esl_status = esl_status
        self.template_id = template_id
        self.promotion_end = promotion_end
        self.item_bar_code = item_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.template_scene_id is not None:
            result['TemplateSceneId'] = self.template_scene_id
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.promotion_start is not None:
            result['PromotionStart'] = self.promotion_start
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.esl_pic is not None:
            result['EslPic'] = self.esl_pic
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.bind_id is not None:
            result['BindId'] = self.bind_id
        if self.promotion_text is not None:
            result['PromotionText'] = self.promotion_text
        if self.esl_model is not None:
            result['EslModel'] = self.esl_model
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.esl_connect_ap is not None:
            result['EslConnectAp'] = self.esl_connect_ap
        if self.esl_status is not None:
            result['EslStatus'] = self.esl_status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.promotion_end is not None:
            result['PromotionEnd'] = self.promotion_end
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('TemplateSceneId') is not None:
            self.template_scene_id = m.get('TemplateSceneId')
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('PromotionStart') is not None:
            self.promotion_start = m.get('PromotionStart')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('EslPic') is not None:
            self.esl_pic = m.get('EslPic')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')
        if m.get('PromotionText') is not None:
            self.promotion_text = m.get('PromotionText')
        if m.get('EslModel') is not None:
            self.esl_model = m.get('EslModel')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('EslConnectAp') is not None:
            self.esl_connect_ap = m.get('EslConnectAp')
        if m.get('EslStatus') is not None:
            self.esl_status = m.get('EslStatus')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('PromotionEnd') is not None:
            self.promotion_end = m.get('PromotionEnd')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        return self


class DescribeBindersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
        esl_item_bind_infos: List[DescribeBindersResponseBodyEslItemBindInfos] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success
        self.esl_item_bind_infos = esl_item_bind_infos

    def validate(self):
        if self.esl_item_bind_infos:
            for k in self.esl_item_bind_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['EslItemBindInfos'] = []
        if self.esl_item_bind_infos is not None:
            for k in self.esl_item_bind_infos:
                result['EslItemBindInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.esl_item_bind_infos = []
        if m.get('EslItemBindInfos') is not None:
            for k in m.get('EslItemBindInfos'):
                temp_model = DescribeBindersResponseBodyEslItemBindInfos()
                self.esl_item_bind_infos.append(temp_model.from_map(k))
        return self


class DescribeBindersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBindersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeBindersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClientPackageRequest(TeaModel):
    def __init__(
        self,
        client_type: str = None,
        extra_params: str = None,
    ):
        self.client_type = client_type
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeClientPackageResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        message: str = None,
        request_id: str = None,
        version: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        code: str = None,
        update_type: str = None,
        success: bool = None,
        url: str = None,
    ):
        self.description = description
        self.message = message
        self.request_id = request_id
        self.version = version
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.code = code
        self.update_type = update_type
        self.success = success
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.update_type is not None:
            result['UpdateType'] = self.update_type
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('UpdateType') is not None:
            self.update_type = m.get('UpdateType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeClientPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClientPackageResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeClientPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEslDevicesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        type: str = None,
        page_size: int = None,
        to_battery_level: int = None,
        store_id: str = None,
        esl_status: str = None,
        esl_bar_code: str = None,
        from_battery_level: int = None,
        extra_params: str = None,
    ):
        self.page_number = page_number
        self.type = type
        self.page_size = page_size
        self.to_battery_level = to_battery_level
        self.store_id = store_id
        self.esl_status = esl_status
        self.esl_bar_code = esl_bar_code
        self.from_battery_level = from_battery_level
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.type is not None:
            result['Type'] = self.type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.to_battery_level is not None:
            result['ToBatteryLevel'] = self.to_battery_level
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.esl_status is not None:
            result['EslStatus'] = self.esl_status
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.from_battery_level is not None:
            result['FromBatteryLevel'] = self.from_battery_level
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ToBatteryLevel') is not None:
            self.to_battery_level = m.get('ToBatteryLevel')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('EslStatus') is not None:
            self.esl_status = m.get('EslStatus')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('FromBatteryLevel') is not None:
            self.from_battery_level = m.get('FromBatteryLevel')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeEslDevicesResponseBodyEslDevices(TeaModel):
    def __init__(
        self,
        type: str = None,
        store_id: str = None,
        esl_bar_code: str = None,
        model: str = None,
        last_communicate_time: str = None,
        screen_height: int = None,
        screen_width: int = None,
        battery_level: int = None,
        esl_status: str = None,
        mac: str = None,
    ):
        self.type = type
        self.store_id = store_id
        self.esl_bar_code = esl_bar_code
        self.model = model
        self.last_communicate_time = last_communicate_time
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.battery_level = battery_level
        self.esl_status = esl_status
        self.mac = mac

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.model is not None:
            result['Model'] = self.model
        if self.last_communicate_time is not None:
            result['LastCommunicateTime'] = self.last_communicate_time
        if self.screen_height is not None:
            result['ScreenHeight'] = self.screen_height
        if self.screen_width is not None:
            result['ScreenWidth'] = self.screen_width
        if self.battery_level is not None:
            result['BatteryLevel'] = self.battery_level
        if self.esl_status is not None:
            result['EslStatus'] = self.esl_status
        if self.mac is not None:
            result['Mac'] = self.mac
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('LastCommunicateTime') is not None:
            self.last_communicate_time = m.get('LastCommunicateTime')
        if m.get('ScreenHeight') is not None:
            self.screen_height = m.get('ScreenHeight')
        if m.get('ScreenWidth') is not None:
            self.screen_width = m.get('ScreenWidth')
        if m.get('BatteryLevel') is not None:
            self.battery_level = m.get('BatteryLevel')
        if m.get('EslStatus') is not None:
            self.esl_status = m.get('EslStatus')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        return self


class DescribeEslDevicesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        esl_devices: List[DescribeEslDevicesResponseBodyEslDevices] = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.esl_devices = esl_devices
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.esl_devices:
            for k in self.esl_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['EslDevices'] = []
        if self.esl_devices is not None:
            for k in self.esl_devices:
                result['EslDevices'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.esl_devices = []
        if m.get('EslDevices') is not None:
            for k in m.get('EslDevices'):
                temp_model = DescribeEslDevicesResponseBodyEslDevices()
                self.esl_devices.append(temp_model.from_map(k))
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeEslDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEslDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeEslDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeItemsRequest(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        item_title: str = None,
        sku_id: str = None,
        store_id: str = None,
        item_bar_code: str = None,
        item_id: str = None,
        be_promotion: bool = None,
        extra_params: str = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.item_title = item_title
        self.sku_id = sku_id
        self.store_id = store_id
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.be_promotion = be_promotion
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeItemsResponseBodyItems(TeaModel):
    def __init__(
        self,
        action_price: int = None,
        item_title: str = None,
        brand_name: str = None,
        price_unit: str = None,
        source_code: str = None,
        forest_first_id: str = None,
        customize_feature_f: str = None,
        customize_feature_a: str = None,
        customize_feature_k: str = None,
        member_price: int = None,
        customize_feature_d: str = None,
        promotion_start: str = None,
        model_number: str = None,
        category_name: str = None,
        customize_feature_e: str = None,
        suggest_price: int = None,
        sale_spec: str = None,
        promotion_text: str = None,
        rank: str = None,
        promotion_reason: str = None,
        customize_feature_g: str = None,
        sales_price: int = None,
        customize_feature_h: str = None,
        original_price: int = None,
        gmt_modified: str = None,
        customize_feature_i: str = None,
        production_place: str = None,
        item_short_title: str = None,
        customize_feature_b: str = None,
        customize_feature_n: str = None,
        tax_fee: str = None,
        inventory_status: str = None,
        item_pic_url: str = None,
        supplier_name: str = None,
        customize_feature_l: str = None,
        energy_efficiency: str = None,
        customize_feature_c: str = None,
        item_id: str = None,
        manufacturer: str = None,
        material: str = None,
        customize_feature_j: str = None,
        customize_feature_o: str = None,
        sku_id: str = None,
        be_promotion: bool = None,
        customize_feature_m: str = None,
        gmt_create: str = None,
        be_source_code: bool = None,
        forest_second_id: str = None,
        item_qr_code: str = None,
        item_info_index: int = None,
        promotion_end: str = None,
        item_bar_code: str = None,
    ):
        self.action_price = action_price
        self.item_title = item_title
        self.brand_name = brand_name
        self.price_unit = price_unit
        self.source_code = source_code
        self.forest_first_id = forest_first_id
        self.customize_feature_f = customize_feature_f
        self.customize_feature_a = customize_feature_a
        self.customize_feature_k = customize_feature_k
        self.member_price = member_price
        self.customize_feature_d = customize_feature_d
        self.promotion_start = promotion_start
        self.model_number = model_number
        self.category_name = category_name
        self.customize_feature_e = customize_feature_e
        self.suggest_price = suggest_price
        self.sale_spec = sale_spec
        self.promotion_text = promotion_text
        self.rank = rank
        self.promotion_reason = promotion_reason
        self.customize_feature_g = customize_feature_g
        self.sales_price = sales_price
        self.customize_feature_h = customize_feature_h
        self.original_price = original_price
        self.gmt_modified = gmt_modified
        self.customize_feature_i = customize_feature_i
        self.production_place = production_place
        self.item_short_title = item_short_title
        self.customize_feature_b = customize_feature_b
        self.customize_feature_n = customize_feature_n
        self.tax_fee = tax_fee
        self.inventory_status = inventory_status
        self.item_pic_url = item_pic_url
        self.supplier_name = supplier_name
        self.customize_feature_l = customize_feature_l
        self.energy_efficiency = energy_efficiency
        self.customize_feature_c = customize_feature_c
        self.item_id = item_id
        self.manufacturer = manufacturer
        self.material = material
        self.customize_feature_j = customize_feature_j
        self.customize_feature_o = customize_feature_o
        self.sku_id = sku_id
        self.be_promotion = be_promotion
        self.customize_feature_m = customize_feature_m
        self.gmt_create = gmt_create
        self.be_source_code = be_source_code
        self.forest_second_id = forest_second_id
        self.item_qr_code = item_qr_code
        self.item_info_index = item_info_index
        self.promotion_end = promotion_end
        self.item_bar_code = item_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.forest_first_id is not None:
            result['ForestFirstId'] = self.forest_first_id
        if self.customize_feature_f is not None:
            result['CustomizeFeatureF'] = self.customize_feature_f
        if self.customize_feature_a is not None:
            result['CustomizeFeatureA'] = self.customize_feature_a
        if self.customize_feature_k is not None:
            result['CustomizeFeatureK'] = self.customize_feature_k
        if self.member_price is not None:
            result['MemberPrice'] = self.member_price
        if self.customize_feature_d is not None:
            result['CustomizeFeatureD'] = self.customize_feature_d
        if self.promotion_start is not None:
            result['PromotionStart'] = self.promotion_start
        if self.model_number is not None:
            result['ModelNumber'] = self.model_number
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.customize_feature_e is not None:
            result['CustomizeFeatureE'] = self.customize_feature_e
        if self.suggest_price is not None:
            result['SuggestPrice'] = self.suggest_price
        if self.sale_spec is not None:
            result['SaleSpec'] = self.sale_spec
        if self.promotion_text is not None:
            result['PromotionText'] = self.promotion_text
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.promotion_reason is not None:
            result['PromotionReason'] = self.promotion_reason
        if self.customize_feature_g is not None:
            result['CustomizeFeatureG'] = self.customize_feature_g
        if self.sales_price is not None:
            result['SalesPrice'] = self.sales_price
        if self.customize_feature_h is not None:
            result['CustomizeFeatureH'] = self.customize_feature_h
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.customize_feature_i is not None:
            result['CustomizeFeatureI'] = self.customize_feature_i
        if self.production_place is not None:
            result['ProductionPlace'] = self.production_place
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.customize_feature_b is not None:
            result['CustomizeFeatureB'] = self.customize_feature_b
        if self.customize_feature_n is not None:
            result['CustomizeFeatureN'] = self.customize_feature_n
        if self.tax_fee is not None:
            result['TaxFee'] = self.tax_fee
        if self.inventory_status is not None:
            result['InventoryStatus'] = self.inventory_status
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.customize_feature_l is not None:
            result['CustomizeFeatureL'] = self.customize_feature_l
        if self.energy_efficiency is not None:
            result['EnergyEfficiency'] = self.energy_efficiency
        if self.customize_feature_c is not None:
            result['CustomizeFeatureC'] = self.customize_feature_c
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.material is not None:
            result['Material'] = self.material
        if self.customize_feature_j is not None:
            result['CustomizeFeatureJ'] = self.customize_feature_j
        if self.customize_feature_o is not None:
            result['CustomizeFeatureO'] = self.customize_feature_o
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.customize_feature_m is not None:
            result['CustomizeFeatureM'] = self.customize_feature_m
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.be_source_code is not None:
            result['BeSourceCode'] = self.be_source_code
        if self.forest_second_id is not None:
            result['ForestSecondId'] = self.forest_second_id
        if self.item_qr_code is not None:
            result['ItemQrCode'] = self.item_qr_code
        if self.item_info_index is not None:
            result['ItemInfoIndex'] = self.item_info_index
        if self.promotion_end is not None:
            result['PromotionEnd'] = self.promotion_end
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('ForestFirstId') is not None:
            self.forest_first_id = m.get('ForestFirstId')
        if m.get('CustomizeFeatureF') is not None:
            self.customize_feature_f = m.get('CustomizeFeatureF')
        if m.get('CustomizeFeatureA') is not None:
            self.customize_feature_a = m.get('CustomizeFeatureA')
        if m.get('CustomizeFeatureK') is not None:
            self.customize_feature_k = m.get('CustomizeFeatureK')
        if m.get('MemberPrice') is not None:
            self.member_price = m.get('MemberPrice')
        if m.get('CustomizeFeatureD') is not None:
            self.customize_feature_d = m.get('CustomizeFeatureD')
        if m.get('PromotionStart') is not None:
            self.promotion_start = m.get('PromotionStart')
        if m.get('ModelNumber') is not None:
            self.model_number = m.get('ModelNumber')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CustomizeFeatureE') is not None:
            self.customize_feature_e = m.get('CustomizeFeatureE')
        if m.get('SuggestPrice') is not None:
            self.suggest_price = m.get('SuggestPrice')
        if m.get('SaleSpec') is not None:
            self.sale_spec = m.get('SaleSpec')
        if m.get('PromotionText') is not None:
            self.promotion_text = m.get('PromotionText')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('PromotionReason') is not None:
            self.promotion_reason = m.get('PromotionReason')
        if m.get('CustomizeFeatureG') is not None:
            self.customize_feature_g = m.get('CustomizeFeatureG')
        if m.get('SalesPrice') is not None:
            self.sales_price = m.get('SalesPrice')
        if m.get('CustomizeFeatureH') is not None:
            self.customize_feature_h = m.get('CustomizeFeatureH')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('CustomizeFeatureI') is not None:
            self.customize_feature_i = m.get('CustomizeFeatureI')
        if m.get('ProductionPlace') is not None:
            self.production_place = m.get('ProductionPlace')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('CustomizeFeatureB') is not None:
            self.customize_feature_b = m.get('CustomizeFeatureB')
        if m.get('CustomizeFeatureN') is not None:
            self.customize_feature_n = m.get('CustomizeFeatureN')
        if m.get('TaxFee') is not None:
            self.tax_fee = m.get('TaxFee')
        if m.get('InventoryStatus') is not None:
            self.inventory_status = m.get('InventoryStatus')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('CustomizeFeatureL') is not None:
            self.customize_feature_l = m.get('CustomizeFeatureL')
        if m.get('EnergyEfficiency') is not None:
            self.energy_efficiency = m.get('EnergyEfficiency')
        if m.get('CustomizeFeatureC') is not None:
            self.customize_feature_c = m.get('CustomizeFeatureC')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('CustomizeFeatureJ') is not None:
            self.customize_feature_j = m.get('CustomizeFeatureJ')
        if m.get('CustomizeFeatureO') is not None:
            self.customize_feature_o = m.get('CustomizeFeatureO')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('CustomizeFeatureM') is not None:
            self.customize_feature_m = m.get('CustomizeFeatureM')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('BeSourceCode') is not None:
            self.be_source_code = m.get('BeSourceCode')
        if m.get('ForestSecondId') is not None:
            self.forest_second_id = m.get('ForestSecondId')
        if m.get('ItemQrCode') is not None:
            self.item_qr_code = m.get('ItemQrCode')
        if m.get('ItemInfoIndex') is not None:
            self.item_info_index = m.get('ItemInfoIndex')
        if m.get('PromotionEnd') is not None:
            self.promotion_end = m.get('PromotionEnd')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        return self


class DescribeItemsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        dynamic_code: str = None,
        items: List[DescribeItemsResponseBodyItems] = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.items = items
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeItemsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeItemsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlanogramEslDevicesRequest(TeaModel):
    def __init__(
        self,
        layer: int = None,
        shelf: str = None,
        store_id: str = None,
        esl_bar_code: str = None,
        extra_params: str = None,
    ):
        self.layer = layer
        self.shelf = shelf
        self.store_id = store_id
        self.esl_bar_code = esl_bar_code
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfosEslDevicePositionInfosEslDevicePlanogramInfos(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        item_title: str = None,
        esl_model: str = None,
        item_bar_code: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.item_title = item_title
        self.esl_model = esl_model
        self.item_bar_code = item_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.esl_model is not None:
            result['EslModel'] = self.esl_model
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('EslModel') is not None:
            self.esl_model = m.get('EslModel')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        return self


class DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfosEslDevicePositionInfos(TeaModel):
    def __init__(
        self,
        esl_device_planogram_infos: List[DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfosEslDevicePositionInfosEslDevicePlanogramInfos] = None,
        column: str = None,
    ):
        self.esl_device_planogram_infos = esl_device_planogram_infos
        self.column = column

    def validate(self):
        if self.esl_device_planogram_infos:
            for k in self.esl_device_planogram_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EslDevicePlanogramInfos'] = []
        if self.esl_device_planogram_infos is not None:
            for k in self.esl_device_planogram_infos:
                result['EslDevicePlanogramInfos'].append(k.to_map() if k else None)
        if self.column is not None:
            result['Column'] = self.column
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.esl_device_planogram_infos = []
        if m.get('EslDevicePlanogramInfos') is not None:
            for k in m.get('EslDevicePlanogramInfos'):
                temp_model = DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfosEslDevicePositionInfosEslDevicePlanogramInfos()
                self.esl_device_planogram_infos.append(temp_model.from_map(k))
        if m.get('Column') is not None:
            self.column = m.get('Column')
        return self


class DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfos(TeaModel):
    def __init__(
        self,
        layer: int = None,
        esl_device_position_infos: List[DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfosEslDevicePositionInfos] = None,
    ):
        self.layer = layer
        self.esl_device_position_infos = esl_device_position_infos

    def validate(self):
        if self.esl_device_position_infos:
            for k in self.esl_device_position_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer is not None:
            result['Layer'] = self.layer
        result['EslDevicePositionInfos'] = []
        if self.esl_device_position_infos is not None:
            for k in self.esl_device_position_infos:
                result['EslDevicePositionInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        self.esl_device_position_infos = []
        if m.get('EslDevicePositionInfos') is not None:
            for k in m.get('EslDevicePositionInfos'):
                temp_model = DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfosEslDevicePositionInfos()
                self.esl_device_position_infos.append(temp_model.from_map(k))
        return self


class DescribePlanogramEslDevicesResponseBody(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        request_id: str = None,
        message: str = None,
        shelf: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        esl_device_layer_infos: List[DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfos] = None,
        code: str = None,
        success: bool = None,
    ):
        self.store_id = store_id
        self.request_id = request_id
        self.message = message
        self.shelf = shelf
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.esl_device_layer_infos = esl_device_layer_infos
        self.code = code
        self.success = success

    def validate(self):
        if self.esl_device_layer_infos:
            for k in self.esl_device_layer_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['EslDeviceLayerInfos'] = []
        if self.esl_device_layer_infos is not None:
            for k in self.esl_device_layer_infos:
                result['EslDeviceLayerInfos'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.esl_device_layer_infos = []
        if m.get('EslDeviceLayerInfos') is not None:
            for k in m.get('EslDeviceLayerInfos'):
                temp_model = DescribePlanogramEslDevicesResponseBodyEslDeviceLayerInfos()
                self.esl_device_layer_infos.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePlanogramEslDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePlanogramEslDevicesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePlanogramEslDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlanogramPositionsRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        layer: int = None,
        shelf: str = None,
        extra_params: str = None,
    ):
        self.store_id = store_id
        self.layer = layer
        self.shelf = shelf
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribePlanogramPositionsResponseBodyLayerInfosShelfPositionInfos(TeaModel):
    def __init__(
        self,
        depth: float = None,
        item_title: str = None,
        facing: int = None,
        offset_to: float = None,
        offset_from: float = None,
        column: str = None,
        item_bar_code: str = None,
    ):
        self.depth = depth
        self.item_title = item_title
        self.facing = facing
        self.offset_to = offset_to
        self.offset_from = offset_from
        self.column = column
        self.item_bar_code = item_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth is not None:
            result['Depth'] = self.depth
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.facing is not None:
            result['Facing'] = self.facing
        if self.offset_to is not None:
            result['OffsetTo'] = self.offset_to
        if self.offset_from is not None:
            result['OffsetFrom'] = self.offset_from
        if self.column is not None:
            result['Column'] = self.column
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('Facing') is not None:
            self.facing = m.get('Facing')
        if m.get('OffsetTo') is not None:
            self.offset_to = m.get('OffsetTo')
        if m.get('OffsetFrom') is not None:
            self.offset_from = m.get('OffsetFrom')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        return self


class DescribePlanogramPositionsResponseBodyLayerInfos(TeaModel):
    def __init__(
        self,
        layer_origin: str = None,
        layer: int = None,
        rail_code: str = None,
        shelf_position_infos: List[DescribePlanogramPositionsResponseBodyLayerInfosShelfPositionInfos] = None,
    ):
        self.layer_origin = layer_origin
        self.layer = layer
        self.rail_code = rail_code
        self.shelf_position_infos = shelf_position_infos

    def validate(self):
        if self.shelf_position_infos:
            for k in self.shelf_position_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer_origin is not None:
            result['LayerOrigin'] = self.layer_origin
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        result['ShelfPositionInfos'] = []
        if self.shelf_position_infos is not None:
            for k in self.shelf_position_infos:
                result['ShelfPositionInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayerOrigin') is not None:
            self.layer_origin = m.get('LayerOrigin')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        self.shelf_position_infos = []
        if m.get('ShelfPositionInfos') is not None:
            for k in m.get('ShelfPositionInfos'):
                temp_model = DescribePlanogramPositionsResponseBodyLayerInfosShelfPositionInfos()
                self.shelf_position_infos.append(temp_model.from_map(k))
        return self


class DescribePlanogramPositionsResponseBody(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        shelf_type: str = None,
        request_id: str = None,
        message: str = None,
        shelf: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        layer_infos: List[DescribePlanogramPositionsResponseBodyLayerInfos] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.store_id = store_id
        self.shelf_type = shelf_type
        self.request_id = request_id
        self.message = message
        self.shelf = shelf
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.layer_infos = layer_infos
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.layer_infos:
            for k in self.layer_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.shelf_type is not None:
            result['ShelfType'] = self.shelf_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['LayerInfos'] = []
        if self.layer_infos is not None:
            for k in self.layer_infos:
                result['LayerInfos'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ShelfType') is not None:
            self.shelf_type = m.get('ShelfType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.layer_infos = []
        if m.get('LayerInfos') is not None:
            for k in m.get('LayerInfos'):
                temp_model = DescribePlanogramPositionsResponseBodyLayerInfos()
                self.layer_infos.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribePlanogramPositionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePlanogramPositionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePlanogramPositionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlanogramRailsRequest(TeaModel):
    def __init__(
        self,
        rail_code: str = None,
        page_size: int = None,
        store_id: str = None,
        shelf: str = None,
        layer: int = None,
        page_number: int = None,
        extra_params: str = None,
    ):
        self.rail_code = rail_code
        self.page_size = page_size
        self.store_id = store_id
        self.shelf = shelf
        self.layer = layer
        self.page_number = page_number
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribePlanogramRailsResponseBodyPlanogramRailInfos(TeaModel):
    def __init__(
        self,
        shelf: str = None,
        gap_unit: int = None,
        layer: int = None,
        rail_code: str = None,
    ):
        self.shelf = shelf
        self.gap_unit = gap_unit
        self.layer = layer
        self.rail_code = rail_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.gap_unit is not None:
            result['GapUnit'] = self.gap_unit
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('GapUnit') is not None:
            self.gap_unit = m.get('GapUnit')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        return self


class DescribePlanogramRailsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        page_size: int = None,
        dynamic_message: str = None,
        code: str = None,
        success: bool = None,
        planogram_rail_infos: List[DescribePlanogramRailsResponseBodyPlanogramRailInfos] = None,
        total_count: int = None,
        store_id: str = None,
        page_number: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.page_size = page_size
        self.dynamic_message = dynamic_message
        self.code = code
        self.success = success
        self.planogram_rail_infos = planogram_rail_infos
        self.total_count = total_count
        self.store_id = store_id
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        if self.planogram_rail_infos:
            for k in self.planogram_rail_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['PlanogramRailInfos'] = []
        if self.planogram_rail_infos is not None:
            for k in self.planogram_rail_infos:
                result['PlanogramRailInfos'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.planogram_rail_infos = []
        if m.get('PlanogramRailInfos') is not None:
            for k in m.get('PlanogramRailInfos'):
                temp_model = DescribePlanogramRailsResponseBodyPlanogramRailInfos()
                self.planogram_rail_infos.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DescribePlanogramRailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePlanogramRailsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePlanogramRailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlanogramShelvesRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        page_number: int = None,
        page_size: int = None,
        extra_params: str = None,
    ):
        self.store_id = store_id
        self.page_number = page_number
        self.page_size = page_size
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribePlanogramShelvesResponseBodyShelfInfosLayerInfos(TeaModel):
    def __init__(
        self,
        layer: int = None,
    ):
        self.layer = layer

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer is not None:
            result['Layer'] = self.layer
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        return self


class DescribePlanogramShelvesResponseBodyShelfInfos(TeaModel):
    def __init__(
        self,
        shelf: str = None,
        layer_infos: List[DescribePlanogramShelvesResponseBodyShelfInfosLayerInfos] = None,
        shelf_type: str = None,
        be_match: bool = None,
        category: str = None,
        zone: str = None,
    ):
        self.shelf = shelf
        self.layer_infos = layer_infos
        self.shelf_type = shelf_type
        self.be_match = be_match
        self.category = category
        self.zone = zone

    def validate(self):
        if self.layer_infos:
            for k in self.layer_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        result['LayerInfos'] = []
        if self.layer_infos is not None:
            for k in self.layer_infos:
                result['LayerInfos'].append(k.to_map() if k else None)
        if self.shelf_type is not None:
            result['ShelfType'] = self.shelf_type
        if self.be_match is not None:
            result['BeMatch'] = self.be_match
        if self.category is not None:
            result['Category'] = self.category
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        self.layer_infos = []
        if m.get('LayerInfos') is not None:
            for k in m.get('LayerInfos'):
                temp_model = DescribePlanogramShelvesResponseBodyShelfInfosLayerInfos()
                self.layer_infos.append(temp_model.from_map(k))
        if m.get('ShelfType') is not None:
            self.shelf_type = m.get('ShelfType')
        if m.get('BeMatch') is not None:
            self.be_match = m.get('BeMatch')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribePlanogramShelvesResponseBody(TeaModel):
    def __init__(
        self,
        shelf_infos: List[DescribePlanogramShelvesResponseBodyShelfInfos] = None,
        message: str = None,
        request_id: str = None,
        page_size: int = None,
        dynamic_message: str = None,
        code: str = None,
        success: bool = None,
        total_count: int = None,
        store_id: str = None,
        page_number: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        self.shelf_infos = shelf_infos
        self.message = message
        self.request_id = request_id
        self.page_size = page_size
        self.dynamic_message = dynamic_message
        self.code = code
        self.success = success
        self.total_count = total_count
        self.store_id = store_id
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.error_message = error_message

    def validate(self):
        if self.shelf_infos:
            for k in self.shelf_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ShelfInfos'] = []
        if self.shelf_infos is not None:
            for k in self.shelf_infos:
                result['ShelfInfos'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.shelf_infos = []
        if m.get('ShelfInfos') is not None:
            for k in m.get('ShelfInfos'):
                temp_model = DescribePlanogramShelvesResponseBodyShelfInfos()
                self.shelf_infos.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class DescribePlanogramShelvesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribePlanogramShelvesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribePlanogramShelvesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRoleActionsRequest(TeaModel):
    def __init__(
        self,
        role_code: str = None,
        extra_params: str = None,
    ):
        self.role_code = role_code
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeRoleActionsResponseBodyRoleAclInfosAccessControlLists(TeaModel):
    def __init__(
        self,
        code: str = None,
    ):
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DescribeRoleActionsResponseBodyRoleAclInfos(TeaModel):
    def __init__(
        self,
        role_code: str = None,
        name: str = None,
        access_control_lists: List[DescribeRoleActionsResponseBodyRoleAclInfosAccessControlLists] = None,
    ):
        self.role_code = role_code
        self.name = name
        self.access_control_lists = access_control_lists

    def validate(self):
        if self.access_control_lists:
            for k in self.access_control_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_code is not None:
            result['RoleCode'] = self.role_code
        if self.name is not None:
            result['Name'] = self.name
        result['AccessControlLists'] = []
        if self.access_control_lists is not None:
            for k in self.access_control_lists:
                result['AccessControlLists'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleCode') is not None:
            self.role_code = m.get('RoleCode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.access_control_lists = []
        if m.get('AccessControlLists') is not None:
            for k in m.get('AccessControlLists'):
                temp_model = DescribeRoleActionsResponseBodyRoleAclInfosAccessControlLists()
                self.access_control_lists.append(temp_model.from_map(k))
        return self


class DescribeRoleActionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        role_acl_infos: List[DescribeRoleActionsResponseBodyRoleAclInfos] = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.role_acl_infos = role_acl_infos
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.role_acl_infos:
            for k in self.role_acl_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        result['RoleAclInfos'] = []
        if self.role_acl_infos is not None:
            for k in self.role_acl_infos:
                result['RoleAclInfos'].append(k.to_map() if k else None)
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.role_acl_infos = []
        if m.get('RoleAclInfos') is not None:
            for k in m.get('RoleAclInfos'):
                temp_model = DescribeRoleActionsResponseBodyRoleAclInfos()
                self.role_acl_infos.append(temp_model.from_map(k))
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRoleActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRoleActionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRoleActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoreConfigRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        extra_params: str = None,
    ):
        self.store_id = store_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeStoreConfigResponseBodyStoreConfigInfo(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        enable_notification: bool = None,
        notification_web_hook: str = None,
        notification_silent_times: str = None,
    ):
        self.store_id = store_id
        self.enable_notification = enable_notification
        self.notification_web_hook = notification_web_hook
        self.notification_silent_times = notification_silent_times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.enable_notification is not None:
            result['EnableNotification'] = self.enable_notification
        if self.notification_web_hook is not None:
            result['NotificationWebHook'] = self.notification_web_hook
        if self.notification_silent_times is not None:
            result['NotificationSilentTimes'] = self.notification_silent_times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('EnableNotification') is not None:
            self.enable_notification = m.get('EnableNotification')
        if m.get('NotificationWebHook') is not None:
            self.notification_web_hook = m.get('NotificationWebHook')
        if m.get('NotificationSilentTimes') is not None:
            self.notification_silent_times = m.get('NotificationSilentTimes')
        return self


class DescribeStoreConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        store_config_info: DescribeStoreConfigResponseBodyStoreConfigInfo = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.store_config_info = store_config_info
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.store_config_info:
            self.store_config_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.store_config_info is not None:
            result['StoreConfigInfo'] = self.store_config_info.to_map()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StoreConfigInfo') is not None:
            temp_model = DescribeStoreConfigResponseBodyStoreConfigInfo()
            self.store_config_info = temp_model.from_map(m['StoreConfigInfo'])
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStoreConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStoreConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStoreConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoresRequest(TeaModel):
    def __init__(
        self,
        user_store_code: str = None,
        page_number: int = None,
        page_size: int = None,
        store_name: str = None,
        to_date: str = None,
        store_id: str = None,
        from_date: str = None,
        extra_params: str = None,
    ):
        self.user_store_code = user_store_code
        self.page_number = page_number
        self.page_size = page_size
        self.store_name = store_name
        self.to_date = to_date
        self.store_id = store_id
        self.from_date = from_date
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeStoresResponseBodyStores(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        parent_id: str = None,
        gmt_create: str = None,
        store_name: str = None,
        gmt_modified: str = None,
        level: str = None,
        phone: str = None,
        user_store_code: str = None,
    ):
        self.store_id = store_id
        self.parent_id = parent_id
        self.gmt_create = gmt_create
        self.store_name = store_name
        self.gmt_modified = gmt_modified
        self.level = level
        self.phone = phone
        self.user_store_code = user_store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.level is not None:
            result['Level'] = self.level
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        return self


class DescribeStoresResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        stores: List[DescribeStoresResponseBodyStores] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.stores = stores
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.stores:
            for k in self.stores:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['Stores'] = []
        if self.stores is not None:
            for k in self.stores:
                result['Stores'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.stores = []
        if m.get('Stores') is not None:
            for k in m.get('Stores'):
                temp_model = DescribeStoresResponseBodyStores()
                self.stores.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeStoresResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserLogRequest(TeaModel):
    def __init__(
        self,
        item_short_title: str = None,
        operation_type: str = None,
        esl_bar_code: str = None,
        from_date: str = None,
        item_bar_code: str = None,
        store_id: str = None,
        to_date: str = None,
        log_id: str = None,
        page_size: int = None,
        operation_status: str = None,
        page_number: int = None,
        user_id: str = None,
        extra_params: str = None,
    ):
        self.item_short_title = item_short_title
        self.operation_type = operation_type
        self.esl_bar_code = esl_bar_code
        self.from_date = from_date
        self.item_bar_code = item_bar_code
        self.store_id = store_id
        self.to_date = to_date
        self.log_id = log_id
        self.page_size = page_size
        self.operation_status = operation_status
        self.page_number = page_number
        self.user_id = user_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        if self.log_id is not None:
            result['LogId'] = self.log_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeUserLogResponseBodyUserLogs(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        operation_send_time: str = None,
        action_price: str = None,
        price_unit: str = None,
        user_id: str = None,
        result_code: str = None,
        item_id: str = None,
        gmt_modified: str = None,
        operation_type: str = None,
        operation_status: str = None,
        operation_response_time: str = None,
        store_id: str = None,
        item_short_title: str = None,
        log_id: str = None,
        be_promotion: bool = None,
        gmt_create: str = None,
        spend_time: str = None,
        item_bar_code: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.operation_send_time = operation_send_time
        self.action_price = action_price
        self.price_unit = price_unit
        self.user_id = user_id
        self.result_code = result_code
        self.item_id = item_id
        self.gmt_modified = gmt_modified
        self.operation_type = operation_type
        self.operation_status = operation_status
        self.operation_response_time = operation_response_time
        self.store_id = store_id
        self.item_short_title = item_short_title
        self.log_id = log_id
        self.be_promotion = be_promotion
        self.gmt_create = gmt_create
        self.spend_time = spend_time
        self.item_bar_code = item_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.operation_send_time is not None:
            result['OperationSendTime'] = self.operation_send_time
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.operation_response_time is not None:
            result['OperationResponseTime'] = self.operation_response_time
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.log_id is not None:
            result['LogId'] = self.log_id
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.spend_time is not None:
            result['SpendTime'] = self.spend_time
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('OperationSendTime') is not None:
            self.operation_send_time = m.get('OperationSendTime')
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('OperationResponseTime') is not None:
            self.operation_response_time = m.get('OperationResponseTime')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SpendTime') is not None:
            self.spend_time = m.get('SpendTime')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        return self


class DescribeUserLogResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
        user_logs: List[DescribeUserLogResponseBodyUserLogs] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success
        self.user_logs = user_logs

    def validate(self):
        if self.user_logs:
            for k in self.user_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['UserLogs'] = []
        if self.user_logs is not None:
            for k in self.user_logs:
                result['UserLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.user_logs = []
        if m.get('UserLogs') is not None:
            for k in m.get('UserLogs'):
                temp_model = DescribeUserLogResponseBodyUserLogs()
                self.user_logs.append(temp_model.from_map(k))
        return self


class DescribeUserLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUserLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUserLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersRequest(TeaModel):
    def __init__(
        self,
        user_type: str = None,
        page_number: int = None,
        user_id: str = None,
        user_name: str = None,
        page_size: int = None,
        extra_params: str = None,
    ):
        self.user_type = user_type
        self.page_number = page_number
        self.user_id = user_id
        self.user_name = user_name
        self.page_size = page_size
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_type is not None:
            result['UserType'] = self.user_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DescribeUsersResponseBodyUsersDingTalkInfos(TeaModel):
    def __init__(
        self,
        ding_talk_user_id: str = None,
        ding_talk_company_id: str = None,
    ):
        self.ding_talk_user_id = ding_talk_user_id
        self.ding_talk_company_id = ding_talk_company_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_talk_user_id is not None:
            result['DingTalkUserId'] = self.ding_talk_user_id
        if self.ding_talk_company_id is not None:
            result['DingTalkCompanyId'] = self.ding_talk_company_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingTalkUserId') is not None:
            self.ding_talk_user_id = m.get('DingTalkUserId')
        if m.get('DingTalkCompanyId') is not None:
            self.ding_talk_company_id = m.get('DingTalkCompanyId')
        return self


class DescribeUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user_type: str = None,
        ding_talk_infos: List[DescribeUsersResponseBodyUsersDingTalkInfos] = None,
        user_id: str = None,
        stores: str = None,
        user_name: str = None,
        bid: str = None,
        owner_id: str = None,
    ):
        self.user_type = user_type
        self.ding_talk_infos = ding_talk_infos
        self.user_id = user_id
        self.stores = stores
        self.user_name = user_name
        self.bid = bid
        self.owner_id = owner_id

    def validate(self):
        if self.ding_talk_infos:
            for k in self.ding_talk_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_type is not None:
            result['UserType'] = self.user_type
        result['DingTalkInfos'] = []
        if self.ding_talk_infos is not None:
            for k in self.ding_talk_infos:
                result['DingTalkInfos'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        self.ding_talk_infos = []
        if m.get('DingTalkInfos') is not None:
            for k in m.get('DingTalkInfos'):
                temp_model = DescribeUsersResponseBodyUsersDingTalkInfos()
                self.ding_talk_infos.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class DescribeUsersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        users: List[DescribeUsersResponseBodyUsers] = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.users = users
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = DescribeUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeUsersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociatePlanogramRailRequest(TeaModel):
    def __init__(
        self,
        rail_code: str = None,
        store_id: str = None,
        extra_params: str = None,
    ):
        self.rail_code = rail_code
        self.store_id = store_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class DissociatePlanogramRailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DissociatePlanogramRailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DissociatePlanogramRailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DissociatePlanogramRailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        extra_params: str = None,
    ):
        self.user_id = user_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class GetUserResponseBodyUserDingTalkInfos(TeaModel):
    def __init__(
        self,
        ding_talk_user_id: str = None,
        ding_talk_company_id: str = None,
    ):
        self.ding_talk_user_id = ding_talk_user_id
        self.ding_talk_company_id = ding_talk_company_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_talk_user_id is not None:
            result['DingTalkUserId'] = self.ding_talk_user_id
        if self.ding_talk_company_id is not None:
            result['DingTalkCompanyId'] = self.ding_talk_company_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingTalkUserId') is not None:
            self.ding_talk_user_id = m.get('DingTalkUserId')
        if m.get('DingTalkCompanyId') is not None:
            self.ding_talk_company_id = m.get('DingTalkCompanyId')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        user_type: str = None,
        ding_talk_infos: List[GetUserResponseBodyUserDingTalkInfos] = None,
        user_id: str = None,
        stores: str = None,
        user_name: str = None,
        bid: str = None,
        owner_id: str = None,
    ):
        self.user_type = user_type
        self.ding_talk_infos = ding_talk_infos
        self.user_id = user_id
        self.stores = stores
        self.user_name = user_name
        self.bid = bid
        self.owner_id = owner_id

    def validate(self):
        if self.ding_talk_infos:
            for k in self.ding_talk_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_type is not None:
            result['UserType'] = self.user_type
        result['DingTalkInfos'] = []
        if self.ding_talk_infos is not None:
            for k in self.ding_talk_infos:
                result['DingTalkInfos'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        self.ding_talk_infos = []
        if m.get('DingTalkInfos') is not None:
            for k in m.get('DingTalkInfos'):
                temp_model = GetUserResponseBodyUserDingTalkInfos()
                self.ding_talk_infos.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        user: GetUserResponseBodyUser = None,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.user = user
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['User'] = self.user.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassignUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        extra_params: str = None,
    ):
        self.user_id = user_id
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class UnassignUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnassignUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnassignUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnassignUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEslDeviceRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        item_bar_code: str = None,
        column: str = None,
        store_id: str = None,
        shelf: str = None,
        layer: int = None,
        extra_params: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.item_bar_code = item_bar_code
        self.column = column
        self.store_id = store_id
        self.shelf = shelf
        self.layer = layer
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.column is not None:
            result['Column'] = self.column
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class UnbindEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindEslDeviceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEslDeviceLightRequest(TeaModel):
    def __init__(
        self,
        led_color: str = None,
        frequency: str = None,
        store_id: str = None,
        item_bar_code: str = None,
        light_up_time: int = None,
        esl_bar_code: str = None,
        extra_params: str = None,
    ):
        self.led_color = led_color
        self.frequency = frequency
        self.store_id = store_id
        self.item_bar_code = item_bar_code
        self.light_up_time = light_up_time
        self.esl_bar_code = esl_bar_code
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.led_color is not None:
            result['LedColor'] = self.led_color
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.light_up_time is not None:
            result['LightUpTime'] = self.light_up_time
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LedColor') is not None:
            self.led_color = m.get('LedColor')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('LightUpTime') is not None:
            self.light_up_time = m.get('LightUpTime')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class UpdateEslDeviceLightResponseBodyLightFailEslInfos(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        error_message: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class UpdateEslDeviceLightResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        light_fail_esl_infos: List[UpdateEslDeviceLightResponseBodyLightFailEslInfos] = None,
        fail_count: int = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        success_count: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.light_fail_esl_infos = light_fail_esl_infos
        self.fail_count = fail_count
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.success_count = success_count
        self.code = code
        self.success = success

    def validate(self):
        if self.light_fail_esl_infos:
            for k in self.light_fail_esl_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        result['LightFailEslInfos'] = []
        if self.light_fail_esl_infos is not None:
            for k in self.light_fail_esl_infos:
                result['LightFailEslInfos'].append(k.to_map() if k else None)
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.light_fail_esl_infos = []
        if m.get('LightFailEslInfos') is not None:
            for k in m.get('LightFailEslInfos'):
                temp_model = UpdateEslDeviceLightResponseBodyLightFailEslInfos()
                self.light_fail_esl_infos.append(temp_model.from_map(k))
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEslDeviceLightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateEslDeviceLightResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateEslDeviceLightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoreRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
        user_store_code: str = None,
        store_name: str = None,
        phone: str = None,
        extra_params: str = None,
    ):
        self.store_id = store_id
        self.user_store_code = user_store_code
        self.store_name = store_name
        self.phone = phone
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class UpdateStoreResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateStoreResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoreConfigRequest(TeaModel):
    def __init__(
        self,
        notification_silent_times: str = None,
        enable_notification: bool = None,
        store_id: str = None,
        notification_web_hook: str = None,
        extra_params: str = None,
    ):
        self.notification_silent_times = notification_silent_times
        self.enable_notification = enable_notification
        self.store_id = store_id
        self.notification_web_hook = notification_web_hook
        self.extra_params = extra_params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_silent_times is not None:
            result['NotificationSilentTimes'] = self.notification_silent_times
        if self.enable_notification is not None:
            result['EnableNotification'] = self.enable_notification
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.notification_web_hook is not None:
            result['NotificationWebHook'] = self.notification_web_hook
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationSilentTimes') is not None:
            self.notification_silent_times = m.get('NotificationSilentTimes')
        if m.get('EnableNotification') is not None:
            self.enable_notification = m.get('EnableNotification')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('NotificationWebHook') is not None:
            self.notification_web_hook = m.get('NotificationWebHook')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        return self


class UpdateStoreConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateStoreConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateStoreConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateStoreConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        ding_talk_user_id: str = None,
        ding_talk_company_id: str = None,
        extra_params: str = None,
        user_id: str = None,
    ):
        self.ding_talk_user_id = ding_talk_user_id
        self.ding_talk_company_id = ding_talk_company_id
        self.extra_params = extra_params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_talk_user_id is not None:
            result['DingTalkUserId'] = self.ding_talk_user_id
        if self.ding_talk_company_id is not None:
            result['DingTalkCompanyId'] = self.ding_talk_company_id
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingTalkUserId') is not None:
            self.ding_talk_user_id = m.get('DingTalkUserId')
        if m.get('DingTalkCompanyId') is not None:
            self.ding_talk_company_id = m.get('DingTalkCompanyId')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        dynamic_code: str = None,
        error_code: str = None,
        dynamic_message: str = None,
        error_message: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.dynamic_code = dynamic_code
        self.error_code = error_code
        self.dynamic_message = dynamic_message
        self.error_message = error_message
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


