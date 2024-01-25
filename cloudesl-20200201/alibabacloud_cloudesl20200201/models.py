# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActivateApDeviceRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        extra_params: str = None,
        store_id: str = None,
    ):
        self.ap_mac = ap_mac
        self.extra_params = extra_params
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class ActivateApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateApDeviceResponseBody = None,
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
            temp_model = ActivateApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddApDeviceRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        client_token: str = None,
        extra_params: str = None,
        remark: str = None,
        serial_number: str = None,
        store_id: str = None,
    ):
        self.ap_mac = ap_mac
        self.client_token = client_token
        self.extra_params = extra_params
        self.remark = remark
        self.serial_number = serial_number
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class AddApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddApDeviceResponseBody = None,
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
            temp_model = AddApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCompanyTemplateRequest(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        esl_size: str = None,
        extra_params: str = None,
        group_id: str = None,
        if_default: bool = None,
        if_member: bool = None,
        if_out_of_inventory: bool = None,
        if_promotion: bool = None,
        if_source_code: bool = None,
        layout: int = None,
        scene: str = None,
        template_name: str = None,
        template_scene_id: str = None,
        template_type: str = None,
        template_version: str = None,
        vendor: str = None,
    ):
        self.device_type = device_type
        self.esl_size = esl_size
        self.extra_params = extra_params
        self.group_id = group_id
        self.if_default = if_default
        self.if_member = if_member
        self.if_out_of_inventory = if_out_of_inventory
        self.if_promotion = if_promotion
        self.if_source_code = if_source_code
        self.layout = layout
        self.scene = scene
        self.template_name = template_name
        self.template_scene_id = template_scene_id
        self.template_type = template_type
        self.template_version = template_version
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.esl_size is not None:
            result['EslSize'] = self.esl_size
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.if_default is not None:
            result['IfDefault'] = self.if_default
        if self.if_member is not None:
            result['IfMember'] = self.if_member
        if self.if_out_of_inventory is not None:
            result['IfOutOfInventory'] = self.if_out_of_inventory
        if self.if_promotion is not None:
            result['IfPromotion'] = self.if_promotion
        if self.if_source_code is not None:
            result['IfSourceCode'] = self.if_source_code
        if self.layout is not None:
            result['Layout'] = self.layout
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_scene_id is not None:
            result['TemplateSceneId'] = self.template_scene_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EslSize') is not None:
            self.esl_size = m.get('EslSize')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IfDefault') is not None:
            self.if_default = m.get('IfDefault')
        if m.get('IfMember') is not None:
            self.if_member = m.get('IfMember')
        if m.get('IfOutOfInventory') is not None:
            self.if_out_of_inventory = m.get('IfOutOfInventory')
        if m.get('IfPromotion') is not None:
            self.if_promotion = m.get('IfPromotion')
        if m.get('IfSourceCode') is not None:
            self.if_source_code = m.get('IfSourceCode')
        if m.get('Layout') is not None:
            self.layout = m.get('Layout')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateSceneId') is not None:
            self.template_scene_id = m.get('TemplateSceneId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class AddCompanyTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddCompanyTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddCompanyTemplateResponseBody = None,
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
            temp_model = AddCompanyTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        extra_params: str = None,
        user_id: str = None,
    ):
        self.client_token = client_token
        self.extra_params = extra_params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserResponseBody = None,
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
            temp_model = AddUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyCompanyTemplateVersionToStoresRequest(TeaModel):
    def __init__(
        self,
        stores: str = None,
        template_version: str = None,
    ):
        self.stores = stores
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class ApplyCompanyTemplateVersionToStoresResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApplyCompanyTemplateVersionToStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyCompanyTemplateVersionToStoresResponseBody = None,
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
            temp_model = ApplyCompanyTemplateVersionToStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignUserRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        stores: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        self.extra_params = extra_params
        self.stores = stores
        self.user_id = user_id
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class AssignUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssignUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssignUserResponseBody = None,
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
            temp_model = AssignUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchInsertItemsRequestItemInfo(TeaModel):
    def __init__(
        self,
        action_price: int = None,
        be_clearance: bool = None,
        be_member: bool = None,
        be_promotion: bool = None,
        be_source_code: bool = None,
        brand_name: str = None,
        category_name: str = None,
        customize_feature_a: str = None,
        customize_feature_b: str = None,
        customize_feature_c: str = None,
        customize_feature_d: str = None,
        customize_feature_e: str = None,
        customize_feature_f: str = None,
        customize_feature_g: str = None,
        customize_feature_h: str = None,
        customize_feature_i: str = None,
        customize_feature_j: str = None,
        customize_feature_k: str = None,
        customize_feature_l: str = None,
        customize_feature_m: str = None,
        customize_feature_n: str = None,
        customize_feature_o: str = None,
        customize_feature_p: str = None,
        customize_feature_q: str = None,
        customize_feature_r: str = None,
        customize_feature_s: str = None,
        customize_feature_t: str = None,
        customize_feature_u: str = None,
        customize_feature_v: str = None,
        customize_feature_w: str = None,
        customize_feature_x: str = None,
        customize_feature_y: str = None,
        customize_feature_z: str = None,
        energy_efficiency: str = None,
        forest_first_id: str = None,
        forest_second_id: str = None,
        inventory_status: str = None,
        item_bar_code: str = None,
        item_id: str = None,
        item_info_index: int = None,
        item_pic_url: str = None,
        item_qr_code: str = None,
        item_short_title: str = None,
        item_title: str = None,
        manufacturer: str = None,
        material: str = None,
        member_price: int = None,
        model_number: str = None,
        original_price: int = None,
        price_unit: str = None,
        production_place: str = None,
        promotion_end: str = None,
        promotion_reason: str = None,
        promotion_start: str = None,
        promotion_text: str = None,
        rank: str = None,
        sale_spec: str = None,
        sales_price: int = None,
        sku_id: str = None,
        source_code: str = None,
        suggest_price: int = None,
        supplier_name: str = None,
        tax_fee: str = None,
        template_scene_id: str = None,
    ):
        self.action_price = action_price
        self.be_clearance = be_clearance
        self.be_member = be_member
        self.be_promotion = be_promotion
        self.be_source_code = be_source_code
        self.brand_name = brand_name
        self.category_name = category_name
        self.customize_feature_a = customize_feature_a
        self.customize_feature_b = customize_feature_b
        self.customize_feature_c = customize_feature_c
        self.customize_feature_d = customize_feature_d
        self.customize_feature_e = customize_feature_e
        self.customize_feature_f = customize_feature_f
        self.customize_feature_g = customize_feature_g
        self.customize_feature_h = customize_feature_h
        self.customize_feature_i = customize_feature_i
        self.customize_feature_j = customize_feature_j
        self.customize_feature_k = customize_feature_k
        self.customize_feature_l = customize_feature_l
        self.customize_feature_m = customize_feature_m
        self.customize_feature_n = customize_feature_n
        self.customize_feature_o = customize_feature_o
        self.customize_feature_p = customize_feature_p
        self.customize_feature_q = customize_feature_q
        self.customize_feature_r = customize_feature_r
        self.customize_feature_s = customize_feature_s
        self.customize_feature_t = customize_feature_t
        self.customize_feature_u = customize_feature_u
        self.customize_feature_v = customize_feature_v
        self.customize_feature_w = customize_feature_w
        self.customize_feature_x = customize_feature_x
        self.customize_feature_y = customize_feature_y
        self.customize_feature_z = customize_feature_z
        self.energy_efficiency = energy_efficiency
        self.forest_first_id = forest_first_id
        self.forest_second_id = forest_second_id
        self.inventory_status = inventory_status
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_info_index = item_info_index
        self.item_pic_url = item_pic_url
        self.item_qr_code = item_qr_code
        self.item_short_title = item_short_title
        self.item_title = item_title
        self.manufacturer = manufacturer
        self.material = material
        self.member_price = member_price
        self.model_number = model_number
        self.original_price = original_price
        self.price_unit = price_unit
        self.production_place = production_place
        self.promotion_end = promotion_end
        self.promotion_reason = promotion_reason
        self.promotion_start = promotion_start
        self.promotion_text = promotion_text
        self.rank = rank
        self.sale_spec = sale_spec
        self.sales_price = sales_price
        self.sku_id = sku_id
        self.source_code = source_code
        self.suggest_price = suggest_price
        self.supplier_name = supplier_name
        self.tax_fee = tax_fee
        self.template_scene_id = template_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.be_clearance is not None:
            result['BeClearance'] = self.be_clearance
        if self.be_member is not None:
            result['BeMember'] = self.be_member
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.be_source_code is not None:
            result['BeSourceCode'] = self.be_source_code
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.customize_feature_a is not None:
            result['CustomizeFeatureA'] = self.customize_feature_a
        if self.customize_feature_b is not None:
            result['CustomizeFeatureB'] = self.customize_feature_b
        if self.customize_feature_c is not None:
            result['CustomizeFeatureC'] = self.customize_feature_c
        if self.customize_feature_d is not None:
            result['CustomizeFeatureD'] = self.customize_feature_d
        if self.customize_feature_e is not None:
            result['CustomizeFeatureE'] = self.customize_feature_e
        if self.customize_feature_f is not None:
            result['CustomizeFeatureF'] = self.customize_feature_f
        if self.customize_feature_g is not None:
            result['CustomizeFeatureG'] = self.customize_feature_g
        if self.customize_feature_h is not None:
            result['CustomizeFeatureH'] = self.customize_feature_h
        if self.customize_feature_i is not None:
            result['CustomizeFeatureI'] = self.customize_feature_i
        if self.customize_feature_j is not None:
            result['CustomizeFeatureJ'] = self.customize_feature_j
        if self.customize_feature_k is not None:
            result['CustomizeFeatureK'] = self.customize_feature_k
        if self.customize_feature_l is not None:
            result['CustomizeFeatureL'] = self.customize_feature_l
        if self.customize_feature_m is not None:
            result['CustomizeFeatureM'] = self.customize_feature_m
        if self.customize_feature_n is not None:
            result['CustomizeFeatureN'] = self.customize_feature_n
        if self.customize_feature_o is not None:
            result['CustomizeFeatureO'] = self.customize_feature_o
        if self.customize_feature_p is not None:
            result['CustomizeFeatureP'] = self.customize_feature_p
        if self.customize_feature_q is not None:
            result['CustomizeFeatureQ'] = self.customize_feature_q
        if self.customize_feature_r is not None:
            result['CustomizeFeatureR'] = self.customize_feature_r
        if self.customize_feature_s is not None:
            result['CustomizeFeatureS'] = self.customize_feature_s
        if self.customize_feature_t is not None:
            result['CustomizeFeatureT'] = self.customize_feature_t
        if self.customize_feature_u is not None:
            result['CustomizeFeatureU'] = self.customize_feature_u
        if self.customize_feature_v is not None:
            result['CustomizeFeatureV'] = self.customize_feature_v
        if self.customize_feature_w is not None:
            result['CustomizeFeatureW'] = self.customize_feature_w
        if self.customize_feature_x is not None:
            result['CustomizeFeatureX'] = self.customize_feature_x
        if self.customize_feature_y is not None:
            result['CustomizeFeatureY'] = self.customize_feature_y
        if self.customize_feature_z is not None:
            result['CustomizeFeatureZ'] = self.customize_feature_z
        if self.energy_efficiency is not None:
            result['EnergyEfficiency'] = self.energy_efficiency
        if self.forest_first_id is not None:
            result['ForestFirstId'] = self.forest_first_id
        if self.forest_second_id is not None:
            result['ForestSecondId'] = self.forest_second_id
        if self.inventory_status is not None:
            result['InventoryStatus'] = self.inventory_status
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_info_index is not None:
            result['ItemInfoIndex'] = self.item_info_index
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        if self.item_qr_code is not None:
            result['ItemQrCode'] = self.item_qr_code
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.material is not None:
            result['Material'] = self.material
        if self.member_price is not None:
            result['MemberPrice'] = self.member_price
        if self.model_number is not None:
            result['ModelNumber'] = self.model_number
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.production_place is not None:
            result['ProductionPlace'] = self.production_place
        if self.promotion_end is not None:
            result['PromotionEnd'] = self.promotion_end
        if self.promotion_reason is not None:
            result['PromotionReason'] = self.promotion_reason
        if self.promotion_start is not None:
            result['PromotionStart'] = self.promotion_start
        if self.promotion_text is not None:
            result['PromotionText'] = self.promotion_text
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.sale_spec is not None:
            result['SaleSpec'] = self.sale_spec
        if self.sales_price is not None:
            result['SalesPrice'] = self.sales_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.suggest_price is not None:
            result['SuggestPrice'] = self.suggest_price
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.tax_fee is not None:
            result['TaxFee'] = self.tax_fee
        if self.template_scene_id is not None:
            result['TemplateSceneId'] = self.template_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('BeClearance') is not None:
            self.be_clearance = m.get('BeClearance')
        if m.get('BeMember') is not None:
            self.be_member = m.get('BeMember')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('BeSourceCode') is not None:
            self.be_source_code = m.get('BeSourceCode')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CustomizeFeatureA') is not None:
            self.customize_feature_a = m.get('CustomizeFeatureA')
        if m.get('CustomizeFeatureB') is not None:
            self.customize_feature_b = m.get('CustomizeFeatureB')
        if m.get('CustomizeFeatureC') is not None:
            self.customize_feature_c = m.get('CustomizeFeatureC')
        if m.get('CustomizeFeatureD') is not None:
            self.customize_feature_d = m.get('CustomizeFeatureD')
        if m.get('CustomizeFeatureE') is not None:
            self.customize_feature_e = m.get('CustomizeFeatureE')
        if m.get('CustomizeFeatureF') is not None:
            self.customize_feature_f = m.get('CustomizeFeatureF')
        if m.get('CustomizeFeatureG') is not None:
            self.customize_feature_g = m.get('CustomizeFeatureG')
        if m.get('CustomizeFeatureH') is not None:
            self.customize_feature_h = m.get('CustomizeFeatureH')
        if m.get('CustomizeFeatureI') is not None:
            self.customize_feature_i = m.get('CustomizeFeatureI')
        if m.get('CustomizeFeatureJ') is not None:
            self.customize_feature_j = m.get('CustomizeFeatureJ')
        if m.get('CustomizeFeatureK') is not None:
            self.customize_feature_k = m.get('CustomizeFeatureK')
        if m.get('CustomizeFeatureL') is not None:
            self.customize_feature_l = m.get('CustomizeFeatureL')
        if m.get('CustomizeFeatureM') is not None:
            self.customize_feature_m = m.get('CustomizeFeatureM')
        if m.get('CustomizeFeatureN') is not None:
            self.customize_feature_n = m.get('CustomizeFeatureN')
        if m.get('CustomizeFeatureO') is not None:
            self.customize_feature_o = m.get('CustomizeFeatureO')
        if m.get('CustomizeFeatureP') is not None:
            self.customize_feature_p = m.get('CustomizeFeatureP')
        if m.get('CustomizeFeatureQ') is not None:
            self.customize_feature_q = m.get('CustomizeFeatureQ')
        if m.get('CustomizeFeatureR') is not None:
            self.customize_feature_r = m.get('CustomizeFeatureR')
        if m.get('CustomizeFeatureS') is not None:
            self.customize_feature_s = m.get('CustomizeFeatureS')
        if m.get('CustomizeFeatureT') is not None:
            self.customize_feature_t = m.get('CustomizeFeatureT')
        if m.get('CustomizeFeatureU') is not None:
            self.customize_feature_u = m.get('CustomizeFeatureU')
        if m.get('CustomizeFeatureV') is not None:
            self.customize_feature_v = m.get('CustomizeFeatureV')
        if m.get('CustomizeFeatureW') is not None:
            self.customize_feature_w = m.get('CustomizeFeatureW')
        if m.get('CustomizeFeatureX') is not None:
            self.customize_feature_x = m.get('CustomizeFeatureX')
        if m.get('CustomizeFeatureY') is not None:
            self.customize_feature_y = m.get('CustomizeFeatureY')
        if m.get('CustomizeFeatureZ') is not None:
            self.customize_feature_z = m.get('CustomizeFeatureZ')
        if m.get('EnergyEfficiency') is not None:
            self.energy_efficiency = m.get('EnergyEfficiency')
        if m.get('ForestFirstId') is not None:
            self.forest_first_id = m.get('ForestFirstId')
        if m.get('ForestSecondId') is not None:
            self.forest_second_id = m.get('ForestSecondId')
        if m.get('InventoryStatus') is not None:
            self.inventory_status = m.get('InventoryStatus')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemInfoIndex') is not None:
            self.item_info_index = m.get('ItemInfoIndex')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        if m.get('ItemQrCode') is not None:
            self.item_qr_code = m.get('ItemQrCode')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('MemberPrice') is not None:
            self.member_price = m.get('MemberPrice')
        if m.get('ModelNumber') is not None:
            self.model_number = m.get('ModelNumber')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('ProductionPlace') is not None:
            self.production_place = m.get('ProductionPlace')
        if m.get('PromotionEnd') is not None:
            self.promotion_end = m.get('PromotionEnd')
        if m.get('PromotionReason') is not None:
            self.promotion_reason = m.get('PromotionReason')
        if m.get('PromotionStart') is not None:
            self.promotion_start = m.get('PromotionStart')
        if m.get('PromotionText') is not None:
            self.promotion_text = m.get('PromotionText')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('SaleSpec') is not None:
            self.sale_spec = m.get('SaleSpec')
        if m.get('SalesPrice') is not None:
            self.sales_price = m.get('SalesPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SuggestPrice') is not None:
            self.suggest_price = m.get('SuggestPrice')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('TaxFee') is not None:
            self.tax_fee = m.get('TaxFee')
        if m.get('TemplateSceneId') is not None:
            self.template_scene_id = m.get('TemplateSceneId')
        return self


class BatchInsertItemsRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        item_info: List[BatchInsertItemsRequestItemInfo] = None,
        store_id: str = None,
        sync_by_item_id: bool = None,
    ):
        self.extra_params = extra_params
        self.item_info = item_info
        self.store_id = store_id
        self.sync_by_item_id = sync_by_item_id

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
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        result['ItemInfo'] = []
        if self.item_info is not None:
            for k in self.item_info:
                result['ItemInfo'].append(k.to_map() if k else None)
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.sync_by_item_id is not None:
            result['SyncByItemId'] = self.sync_by_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        self.item_info = []
        if m.get('ItemInfo') is not None:
            for k in m.get('ItemInfo'):
                temp_model = BatchInsertItemsRequestItemInfo()
                self.item_info.append(temp_model.from_map(k))
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('SyncByItemId') is not None:
            self.sync_by_item_id = m.get('SyncByItemId')
        return self


class BatchInsertItemsResponseBodyBatchResults(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        index: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.index = index
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.index is not None:
            result['Index'] = self.index
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchInsertItemsResponseBody(TeaModel):
    def __init__(
        self,
        batch_results: List[BatchInsertItemsResponseBodyBatchResults] = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.batch_results = batch_results
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
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
        result['BatchResults'] = []
        if self.batch_results is not None:
            for k in self.batch_results:
                result['BatchResults'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_results = []
        if m.get('BatchResults') is not None:
            for k in m.get('BatchResults'):
                temp_model = BatchInsertItemsResponseBodyBatchResults()
                self.batch_results.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchInsertItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchInsertItemsResponseBody = None,
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
            temp_model = BatchInsertItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindEslDeviceRequest(TeaModel):
    def __init__(
        self,
        column: str = None,
        container_id: str = None,
        container_name: str = None,
        esl_bar_code: str = None,
        extra_params: str = None,
        item_bar_code: str = None,
        layer: int = None,
        layout_id: str = None,
        layout_name: str = None,
        shelf: str = None,
        store_id: str = None,
    ):
        self.column = column
        self.container_id = container_id
        self.container_name = container_name
        self.esl_bar_code = esl_bar_code
        self.extra_params = extra_params
        self.item_bar_code = item_bar_code
        self.layer = layer
        self.layout_id = layout_id
        self.layout_name = layout_name
        self.shelf = shelf
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['Column'] = self.column
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.layout_name is not None:
            result['LayoutName'] = self.layout_name
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('LayoutName') is not None:
            self.layout_name = m.get('LayoutName')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class BindEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindEslDeviceResponseBody = None,
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
            temp_model = BindEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoreRequest(TeaModel):
    def __init__(
        self,
        auto_unbind_days: int = None,
        auto_unbind_offline_esl: bool = None,
        bar_code_encode: int = None,
        client_token: str = None,
        extra_params: str = None,
        parent_id: str = None,
        phone: str = None,
        store_name: str = None,
        time_zone: str = None,
        user_store_code: str = None,
    ):
        self.auto_unbind_days = auto_unbind_days
        self.auto_unbind_offline_esl = auto_unbind_offline_esl
        self.bar_code_encode = bar_code_encode
        self.client_token = client_token
        self.extra_params = extra_params
        self.parent_id = parent_id
        self.phone = phone
        self.store_name = store_name
        self.time_zone = time_zone
        self.user_store_code = user_store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_unbind_days is not None:
            result['AutoUnbindDays'] = self.auto_unbind_days
        if self.auto_unbind_offline_esl is not None:
            result['AutoUnbindOfflineEsl'] = self.auto_unbind_offline_esl
        if self.bar_code_encode is not None:
            result['BarCodeEncode'] = self.bar_code_encode
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUnbindDays') is not None:
            self.auto_unbind_days = m.get('AutoUnbindDays')
        if m.get('AutoUnbindOfflineEsl') is not None:
            self.auto_unbind_offline_esl = m.get('AutoUnbindOfflineEsl')
        if m.get('BarCodeEncode') is not None:
            self.bar_code_encode = m.get('BarCodeEncode')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        return self


class CreateStoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        store_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.store_id = store_id
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStoreResponseBody = None,
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
            temp_model = CreateStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApDeviceRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        extra_params: str = None,
        store_id: str = None,
    ):
        self.ap_mac = ap_mac
        self.extra_params = extra_params
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DeleteApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApDeviceResponseBody = None,
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
            temp_model = DeleteApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCompanyTemplateRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        template_id: str = None,
    ):
        self.extra_params = extra_params
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteCompanyTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCompanyTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCompanyTemplateResponseBody = None,
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
            temp_model = DeleteCompanyTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteItemRequest(TeaModel):
    def __init__(
        self,
        item_bar_code: str = None,
        store_id: str = None,
        unbind_esl_device: bool = None,
    ):
        self.item_bar_code = item_bar_code
        self.store_id = store_id
        self.unbind_esl_device = unbind_esl_device

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.unbind_esl_device is not None:
            result['UnbindEslDevice'] = self.unbind_esl_device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('UnbindEslDevice') is not None:
            self.unbind_esl_device = m.get('UnbindEslDevice')
        return self


class DeleteItemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteItemResponseBody = None,
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
            temp_model = DeleteItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStoreRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        store_id: str = None,
    ):
        self.extra_params = extra_params
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DeleteStoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStoreResponseBody = None,
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
            temp_model = DeleteStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        user_id: str = None,
    ):
        self.extra_params = extra_params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApDevicesRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        be_activate: bool = None,
        extra_params: str = None,
        model: str = None,
        page_number: int = None,
        page_size: int = None,
        status: bool = None,
        store_id: str = None,
    ):
        self.ap_mac = ap_mac
        self.be_activate = be_activate
        self.extra_params = extra_params
        self.model = model
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.be_activate is not None:
            result['BeActivate'] = self.be_activate
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.model is not None:
            result['Model'] = self.model
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('BeActivate') is not None:
            self.be_activate = m.get('BeActivate')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeApDevicesResponseBodyApDevices(TeaModel):
    def __init__(
        self,
        be_activate: bool = None,
        mac: str = None,
        model: str = None,
        remark: str = None,
        status: bool = None,
        store_id: str = None,
    ):
        self.be_activate = be_activate
        self.mac = mac
        self.model = model
        self.remark = remark
        self.status = status
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.be_activate is not None:
            result['BeActivate'] = self.be_activate
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.model is not None:
            result['Model'] = self.model
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeActivate') is not None:
            self.be_activate = m.get('BeActivate')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeApDevicesResponseBody(TeaModel):
    def __init__(
        self,
        ap_devices: List[DescribeApDevicesResponseBodyApDevices] = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.ap_devices = ap_devices
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        result['ApDevices'] = []
        if self.ap_devices is not None:
            for k in self.ap_devices:
                result['ApDevices'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ap_devices = []
        if m.get('ApDevices') is not None:
            for k in m.get('ApDevices'):
                temp_model = DescribeApDevicesResponseBodyApDevices()
                self.ap_devices.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApDevicesResponseBody = None,
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
            temp_model = DescribeApDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableEslModelsRequest(TeaModel):
    def __init__(
        self,
        model_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.model_id = model_id
        self.name = name
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeAvailableEslModelsResponseBodyEslModels(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        esl_size: str = None,
        model_id: str = None,
        name: str = None,
        screen_height: int = None,
        screen_width: int = None,
        vendor: str = None,
    ):
        self.device_type = device_type
        self.esl_size = esl_size
        self.model_id = model_id
        self.name = name
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.esl_size is not None:
            result['EslSize'] = self.esl_size
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.name is not None:
            result['Name'] = self.name
        if self.screen_height is not None:
            result['ScreenHeight'] = self.screen_height
        if self.screen_width is not None:
            result['ScreenWidth'] = self.screen_width
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EslSize') is not None:
            self.esl_size = m.get('EslSize')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScreenHeight') is not None:
            self.screen_height = m.get('ScreenHeight')
        if m.get('ScreenWidth') is not None:
            self.screen_width = m.get('ScreenWidth')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeAvailableEslModelsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        esl_models: List[DescribeAvailableEslModelsResponseBodyEslModels] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.esl_models = esl_models
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.esl_models:
            for k in self.esl_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['EslModels'] = []
        if self.esl_models is not None:
            for k in self.esl_models:
                result['EslModels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.esl_models = []
        if m.get('EslModels') is not None:
            for k in m.get('EslModels'):
                temp_model = DescribeAvailableEslModelsResponseBodyEslModels()
                self.esl_models.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAvailableEslModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableEslModelsResponseBody = None,
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
            temp_model = DescribeAvailableEslModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBindersRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        extra_params: str = None,
        item_bar_code: str = None,
        item_title: str = None,
        page_number: int = None,
        page_size: int = None,
        store_id: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.extra_params = extra_params
        self.item_bar_code = item_bar_code
        self.item_title = item_title
        self.page_number = page_number
        self.page_size = page_size
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeBindersResponseBodyEslItemBindInfos(TeaModel):
    def __init__(
        self,
        action_price: str = None,
        be_promotion: bool = None,
        bind_id: str = None,
        container_name: str = None,
        esl_bar_code: str = None,
        esl_connect_ap: str = None,
        esl_model: str = None,
        esl_pic: str = None,
        esl_status: str = None,
        gmt_modified: str = None,
        item_bar_code: str = None,
        item_id: str = None,
        item_short_title: str = None,
        item_title: str = None,
        original_price: str = None,
        price_unit: str = None,
        promotion_end: str = None,
        promotion_start: str = None,
        promotion_text: str = None,
        sku_id: str = None,
        store_id: str = None,
        template_id: str = None,
        template_scene_id: str = None,
    ):
        self.action_price = action_price
        self.be_promotion = be_promotion
        self.bind_id = bind_id
        self.container_name = container_name
        self.esl_bar_code = esl_bar_code
        self.esl_connect_ap = esl_connect_ap
        self.esl_model = esl_model
        self.esl_pic = esl_pic
        self.esl_status = esl_status
        self.gmt_modified = gmt_modified
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_short_title = item_short_title
        self.item_title = item_title
        self.original_price = original_price
        self.price_unit = price_unit
        self.promotion_end = promotion_end
        self.promotion_start = promotion_start
        self.promotion_text = promotion_text
        # SkuID。
        self.sku_id = sku_id
        self.store_id = store_id
        self.template_id = template_id
        self.template_scene_id = template_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.bind_id is not None:
            result['BindId'] = self.bind_id
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.esl_connect_ap is not None:
            result['EslConnectAp'] = self.esl_connect_ap
        if self.esl_model is not None:
            result['EslModel'] = self.esl_model
        if self.esl_pic is not None:
            result['EslPic'] = self.esl_pic
        if self.esl_status is not None:
            result['EslStatus'] = self.esl_status
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.promotion_end is not None:
            result['PromotionEnd'] = self.promotion_end
        if self.promotion_start is not None:
            result['PromotionStart'] = self.promotion_start
        if self.promotion_text is not None:
            result['PromotionText'] = self.promotion_text
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_scene_id is not None:
            result['TemplateSceneId'] = self.template_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('EslConnectAp') is not None:
            self.esl_connect_ap = m.get('EslConnectAp')
        if m.get('EslModel') is not None:
            self.esl_model = m.get('EslModel')
        if m.get('EslPic') is not None:
            self.esl_pic = m.get('EslPic')
        if m.get('EslStatus') is not None:
            self.esl_status = m.get('EslStatus')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('PromotionEnd') is not None:
            self.promotion_end = m.get('PromotionEnd')
        if m.get('PromotionStart') is not None:
            self.promotion_start = m.get('PromotionStart')
        if m.get('PromotionText') is not None:
            self.promotion_text = m.get('PromotionText')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateSceneId') is not None:
            self.template_scene_id = m.get('TemplateSceneId')
        return self


class DescribeBindersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        esl_item_bind_infos: List[DescribeBindersResponseBodyEslItemBindInfos] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.esl_item_bind_infos = esl_item_bind_infos
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['EslItemBindInfos'] = []
        if self.esl_item_bind_infos is not None:
            for k in self.esl_item_bind_infos:
                result['EslItemBindInfos'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.esl_item_bind_infos = []
        if m.get('EslItemBindInfos') is not None:
            for k in m.get('EslItemBindInfos'):
                temp_model = DescribeBindersResponseBodyEslItemBindInfos()
                self.esl_item_bind_infos.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBindersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBindersResponseBody = None,
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
            temp_model = DescribeBindersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCompanyTemplateVersionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeCompanyTemplateVersionsResponseBodyVersions(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeCompanyTemplateVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        versions: List[DescribeCompanyTemplateVersionsResponseBodyVersions] = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = DescribeCompanyTemplateVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class DescribeCompanyTemplateVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCompanyTemplateVersionsResponseBody = None,
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
            temp_model = DescribeCompanyTemplateVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEslDeviceRequest(TeaModel):
    def __init__(
        self,
        from_date: str = None,
        page_number: int = None,
        page_size: int = None,
        store_id: str = None,
        to_date: str = None,
    ):
        self.from_date = from_date
        self.page_number = page_number
        self.page_size = page_size
        self.store_id = store_id
        self.to_date = to_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        return self


class DescribeEslDeviceResponseBodyEslDetails(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        item_bar_code: int = None,
        item_id: int = None,
        item_short_title: str = None,
        last_update_time: str = None,
        status: str = None,
        store_id: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_short_title = item_short_title
        self.last_update_time = last_update_time
        self.status = status
        self.store_id = store_id

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
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.status is not None:
            result['Status'] = self.status
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        esl_details: List[DescribeEslDeviceResponseBodyEslDetails] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.esl_details = esl_details
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.esl_details:
            for k in self.esl_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EslDetails'] = []
        if self.esl_details is not None:
            for k in self.esl_details:
                result['EslDetails'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.esl_details = []
        if m.get('EslDetails') is not None:
            for k in m.get('EslDetails'):
                temp_model = DescribeEslDeviceResponseBodyEslDetails()
                self.esl_details.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEslDeviceResponseBody = None,
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
            temp_model = DescribeEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEslDevicesRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        esl_status: str = None,
        extra_params: str = None,
        from_battery_level: int = None,
        page_number: int = None,
        page_size: int = None,
        store_id: str = None,
        to_battery_level: int = None,
        type: str = None,
        type_encode: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.esl_status = esl_status
        self.extra_params = extra_params
        self.from_battery_level = from_battery_level
        self.page_number = page_number
        self.page_size = page_size
        self.store_id = store_id
        self.to_battery_level = to_battery_level
        self.type = type
        self.type_encode = type_encode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.esl_status is not None:
            result['EslStatus'] = self.esl_status
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.from_battery_level is not None:
            result['FromBatteryLevel'] = self.from_battery_level
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.to_battery_level is not None:
            result['ToBatteryLevel'] = self.to_battery_level
        if self.type is not None:
            result['Type'] = self.type
        if self.type_encode is not None:
            result['TypeEncode'] = self.type_encode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('EslStatus') is not None:
            self.esl_status = m.get('EslStatus')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('FromBatteryLevel') is not None:
            self.from_battery_level = m.get('FromBatteryLevel')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ToBatteryLevel') is not None:
            self.to_battery_level = m.get('ToBatteryLevel')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeEncode') is not None:
            self.type_encode = m.get('TypeEncode')
        return self


class DescribeEslDevicesResponseBodyEslDevices(TeaModel):
    def __init__(
        self,
        battery_level: int = None,
        esl_bar_code: str = None,
        esl_signal: int = None,
        esl_status: str = None,
        last_communicate_time: str = None,
        layout_id: str = None,
        layout_name: str = None,
        mac: str = None,
        model: str = None,
        screen_height: int = None,
        screen_width: int = None,
        store_id: str = None,
        type: str = None,
        type_encode: str = None,
    ):
        self.battery_level = battery_level
        self.esl_bar_code = esl_bar_code
        self.esl_signal = esl_signal
        self.esl_status = esl_status
        self.last_communicate_time = last_communicate_time
        self.layout_id = layout_id
        self.layout_name = layout_name
        self.mac = mac
        self.model = model
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.store_id = store_id
        self.type = type
        self.type_encode = type_encode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.battery_level is not None:
            result['BatteryLevel'] = self.battery_level
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.esl_signal is not None:
            result['EslSignal'] = self.esl_signal
        if self.esl_status is not None:
            result['EslStatus'] = self.esl_status
        if self.last_communicate_time is not None:
            result['LastCommunicateTime'] = self.last_communicate_time
        if self.layout_id is not None:
            result['LayoutId'] = self.layout_id
        if self.layout_name is not None:
            result['LayoutName'] = self.layout_name
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.model is not None:
            result['Model'] = self.model
        if self.screen_height is not None:
            result['ScreenHeight'] = self.screen_height
        if self.screen_width is not None:
            result['ScreenWidth'] = self.screen_width
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.type is not None:
            result['Type'] = self.type
        if self.type_encode is not None:
            result['TypeEncode'] = self.type_encode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatteryLevel') is not None:
            self.battery_level = m.get('BatteryLevel')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('EslSignal') is not None:
            self.esl_signal = m.get('EslSignal')
        if m.get('EslStatus') is not None:
            self.esl_status = m.get('EslStatus')
        if m.get('LastCommunicateTime') is not None:
            self.last_communicate_time = m.get('LastCommunicateTime')
        if m.get('LayoutId') is not None:
            self.layout_id = m.get('LayoutId')
        if m.get('LayoutName') is not None:
            self.layout_name = m.get('LayoutName')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('ScreenHeight') is not None:
            self.screen_height = m.get('ScreenHeight')
        if m.get('ScreenWidth') is not None:
            self.screen_width = m.get('ScreenWidth')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('TypeEncode') is not None:
            self.type_encode = m.get('TypeEncode')
        return self


class DescribeEslDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        esl_devices: List[DescribeEslDevicesResponseBodyEslDevices] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.esl_devices = esl_devices
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['EslDevices'] = []
        if self.esl_devices is not None:
            for k in self.esl_devices:
                result['EslDevices'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.esl_devices = []
        if m.get('EslDevices') is not None:
            for k in m.get('EslDevices'):
                temp_model = DescribeEslDevicesResponseBodyEslDevices()
                self.esl_devices.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEslDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEslDevicesResponseBody = None,
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
            temp_model = DescribeEslDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEslModelByTemplateVersionRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        template_version: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class DescribeEslModelByTemplateVersionResponseBodyEslModels(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        esl_physical_size: str = None,
        esl_size: str = None,
        image: str = None,
        model_id: str = None,
        name: str = None,
        screen_height: int = None,
        screen_width: int = None,
        vendor: str = None,
    ):
        self.device_type = device_type
        self.esl_physical_size = esl_physical_size
        self.esl_size = esl_size
        self.image = image
        self.model_id = model_id
        self.name = name
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.esl_physical_size is not None:
            result['EslPhysicalSize'] = self.esl_physical_size
        if self.esl_size is not None:
            result['EslSize'] = self.esl_size
        if self.image is not None:
            result['Image'] = self.image
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.name is not None:
            result['Name'] = self.name
        if self.screen_height is not None:
            result['ScreenHeight'] = self.screen_height
        if self.screen_width is not None:
            result['ScreenWidth'] = self.screen_width
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EslPhysicalSize') is not None:
            self.esl_physical_size = m.get('EslPhysicalSize')
        if m.get('EslSize') is not None:
            self.esl_size = m.get('EslSize')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScreenHeight') is not None:
            self.screen_height = m.get('ScreenHeight')
        if m.get('ScreenWidth') is not None:
            self.screen_width = m.get('ScreenWidth')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeEslModelByTemplateVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        esl_models: List[DescribeEslModelByTemplateVersionResponseBodyEslModels] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.esl_models = esl_models
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.esl_models:
            for k in self.esl_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['EslModels'] = []
        if self.esl_models is not None:
            for k in self.esl_models:
                result['EslModels'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.esl_models = []
        if m.get('EslModels') is not None:
            for k in m.get('EslModels'):
                temp_model = DescribeEslModelByTemplateVersionResponseBodyEslModels()
                self.esl_models.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEslModelByTemplateVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEslModelByTemplateVersionResponseBody = None,
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
            temp_model = DescribeEslModelByTemplateVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeItemsRequest(TeaModel):
    def __init__(
        self,
        be_promotion: bool = None,
        extra_params: str = None,
        item_bar_code: str = None,
        item_id: str = None,
        item_title: str = None,
        page_number: int = None,
        page_size: int = None,
        sku_id: str = None,
        store_id: str = None,
    ):
        self.be_promotion = be_promotion
        self.extra_params = extra_params
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_title = item_title
        self.page_number = page_number
        self.page_size = page_size
        # SkuID。
        self.sku_id = sku_id
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeItemsResponseBodyItems(TeaModel):
    def __init__(
        self,
        action_price: int = None,
        be_clearance: bool = None,
        be_member: bool = None,
        be_promotion: bool = None,
        be_source_code: bool = None,
        brand_name: str = None,
        category_name: str = None,
        customize_feature_a: str = None,
        customize_feature_b: str = None,
        customize_feature_c: str = None,
        customize_feature_d: str = None,
        customize_feature_e: str = None,
        customize_feature_f: str = None,
        customize_feature_g: str = None,
        customize_feature_h: str = None,
        customize_feature_i: str = None,
        customize_feature_j: str = None,
        customize_feature_k: str = None,
        customize_feature_l: str = None,
        customize_feature_m: str = None,
        customize_feature_n: str = None,
        customize_feature_o: str = None,
        customize_feature_p: str = None,
        customize_feature_q: str = None,
        customize_feature_r: str = None,
        customize_feature_s: str = None,
        customize_feature_t: str = None,
        customize_feature_u: str = None,
        customize_feature_v: str = None,
        customize_feature_w: str = None,
        customize_feature_x: str = None,
        customize_feature_y: str = None,
        customize_feature_z: str = None,
        energy_efficiency: str = None,
        forest_first_id: str = None,
        forest_second_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        inventory_status: str = None,
        item_bar_code: str = None,
        item_id: str = None,
        item_info_index: int = None,
        item_pic_url: str = None,
        item_qr_code: str = None,
        item_short_title: str = None,
        item_title: str = None,
        manufacturer: str = None,
        material: str = None,
        member_price: int = None,
        model_number: str = None,
        original_price: int = None,
        price_unit: str = None,
        production_place: str = None,
        promotion_end: str = None,
        promotion_reason: str = None,
        promotion_start: str = None,
        promotion_text: str = None,
        rank: str = None,
        sale_spec: str = None,
        sales_price: int = None,
        sku_id: str = None,
        source_code: str = None,
        suggest_price: int = None,
        supplier_name: str = None,
        tax_fee: str = None,
        template_scene_id: str = None,
    ):
        self.action_price = action_price
        self.be_clearance = be_clearance
        self.be_member = be_member
        self.be_promotion = be_promotion
        self.be_source_code = be_source_code
        self.brand_name = brand_name
        self.category_name = category_name
        self.customize_feature_a = customize_feature_a
        self.customize_feature_b = customize_feature_b
        self.customize_feature_c = customize_feature_c
        self.customize_feature_d = customize_feature_d
        self.customize_feature_e = customize_feature_e
        self.customize_feature_f = customize_feature_f
        self.customize_feature_g = customize_feature_g
        self.customize_feature_h = customize_feature_h
        self.customize_feature_i = customize_feature_i
        self.customize_feature_j = customize_feature_j
        self.customize_feature_k = customize_feature_k
        self.customize_feature_l = customize_feature_l
        self.customize_feature_m = customize_feature_m
        self.customize_feature_n = customize_feature_n
        self.customize_feature_o = customize_feature_o
        self.customize_feature_p = customize_feature_p
        self.customize_feature_q = customize_feature_q
        self.customize_feature_r = customize_feature_r
        self.customize_feature_s = customize_feature_s
        self.customize_feature_t = customize_feature_t
        self.customize_feature_u = customize_feature_u
        self.customize_feature_v = customize_feature_v
        self.customize_feature_w = customize_feature_w
        self.customize_feature_x = customize_feature_x
        self.customize_feature_y = customize_feature_y
        self.customize_feature_z = customize_feature_z
        self.energy_efficiency = energy_efficiency
        self.forest_first_id = forest_first_id
        self.forest_second_id = forest_second_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.inventory_status = inventory_status
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_info_index = item_info_index
        self.item_pic_url = item_pic_url
        self.item_qr_code = item_qr_code
        self.item_short_title = item_short_title
        self.item_title = item_title
        self.manufacturer = manufacturer
        self.material = material
        self.member_price = member_price
        self.model_number = model_number
        self.original_price = original_price
        self.price_unit = price_unit
        self.production_place = production_place
        self.promotion_end = promotion_end
        self.promotion_reason = promotion_reason
        self.promotion_start = promotion_start
        self.promotion_text = promotion_text
        self.rank = rank
        self.sale_spec = sale_spec
        self.sales_price = sales_price
        # SKuID。
        self.sku_id = sku_id
        self.source_code = source_code
        self.suggest_price = suggest_price
        self.supplier_name = supplier_name
        self.tax_fee = tax_fee
        self.template_scene_id = template_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.be_clearance is not None:
            result['BeClearance'] = self.be_clearance
        if self.be_member is not None:
            result['BeMember'] = self.be_member
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.be_source_code is not None:
            result['BeSourceCode'] = self.be_source_code
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.customize_feature_a is not None:
            result['CustomizeFeatureA'] = self.customize_feature_a
        if self.customize_feature_b is not None:
            result['CustomizeFeatureB'] = self.customize_feature_b
        if self.customize_feature_c is not None:
            result['CustomizeFeatureC'] = self.customize_feature_c
        if self.customize_feature_d is not None:
            result['CustomizeFeatureD'] = self.customize_feature_d
        if self.customize_feature_e is not None:
            result['CustomizeFeatureE'] = self.customize_feature_e
        if self.customize_feature_f is not None:
            result['CustomizeFeatureF'] = self.customize_feature_f
        if self.customize_feature_g is not None:
            result['CustomizeFeatureG'] = self.customize_feature_g
        if self.customize_feature_h is not None:
            result['CustomizeFeatureH'] = self.customize_feature_h
        if self.customize_feature_i is not None:
            result['CustomizeFeatureI'] = self.customize_feature_i
        if self.customize_feature_j is not None:
            result['CustomizeFeatureJ'] = self.customize_feature_j
        if self.customize_feature_k is not None:
            result['CustomizeFeatureK'] = self.customize_feature_k
        if self.customize_feature_l is not None:
            result['CustomizeFeatureL'] = self.customize_feature_l
        if self.customize_feature_m is not None:
            result['CustomizeFeatureM'] = self.customize_feature_m
        if self.customize_feature_n is not None:
            result['CustomizeFeatureN'] = self.customize_feature_n
        if self.customize_feature_o is not None:
            result['CustomizeFeatureO'] = self.customize_feature_o
        if self.customize_feature_p is not None:
            result['CustomizeFeatureP'] = self.customize_feature_p
        if self.customize_feature_q is not None:
            result['CustomizeFeatureQ'] = self.customize_feature_q
        if self.customize_feature_r is not None:
            result['CustomizeFeatureR'] = self.customize_feature_r
        if self.customize_feature_s is not None:
            result['CustomizeFeatureS'] = self.customize_feature_s
        if self.customize_feature_t is not None:
            result['CustomizeFeatureT'] = self.customize_feature_t
        if self.customize_feature_u is not None:
            result['CustomizeFeatureU'] = self.customize_feature_u
        if self.customize_feature_v is not None:
            result['CustomizeFeatureV'] = self.customize_feature_v
        if self.customize_feature_w is not None:
            result['CustomizeFeatureW'] = self.customize_feature_w
        if self.customize_feature_x is not None:
            result['CustomizeFeatureX'] = self.customize_feature_x
        if self.customize_feature_y is not None:
            result['CustomizeFeatureY'] = self.customize_feature_y
        if self.customize_feature_z is not None:
            result['CustomizeFeatureZ'] = self.customize_feature_z
        if self.energy_efficiency is not None:
            result['EnergyEfficiency'] = self.energy_efficiency
        if self.forest_first_id is not None:
            result['ForestFirstId'] = self.forest_first_id
        if self.forest_second_id is not None:
            result['ForestSecondId'] = self.forest_second_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.inventory_status is not None:
            result['InventoryStatus'] = self.inventory_status
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_info_index is not None:
            result['ItemInfoIndex'] = self.item_info_index
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        if self.item_qr_code is not None:
            result['ItemQrCode'] = self.item_qr_code
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.material is not None:
            result['Material'] = self.material
        if self.member_price is not None:
            result['MemberPrice'] = self.member_price
        if self.model_number is not None:
            result['ModelNumber'] = self.model_number
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.production_place is not None:
            result['ProductionPlace'] = self.production_place
        if self.promotion_end is not None:
            result['PromotionEnd'] = self.promotion_end
        if self.promotion_reason is not None:
            result['PromotionReason'] = self.promotion_reason
        if self.promotion_start is not None:
            result['PromotionStart'] = self.promotion_start
        if self.promotion_text is not None:
            result['PromotionText'] = self.promotion_text
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.sale_spec is not None:
            result['SaleSpec'] = self.sale_spec
        if self.sales_price is not None:
            result['SalesPrice'] = self.sales_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.suggest_price is not None:
            result['SuggestPrice'] = self.suggest_price
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.tax_fee is not None:
            result['TaxFee'] = self.tax_fee
        if self.template_scene_id is not None:
            result['TemplateSceneId'] = self.template_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('BeClearance') is not None:
            self.be_clearance = m.get('BeClearance')
        if m.get('BeMember') is not None:
            self.be_member = m.get('BeMember')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('BeSourceCode') is not None:
            self.be_source_code = m.get('BeSourceCode')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CustomizeFeatureA') is not None:
            self.customize_feature_a = m.get('CustomizeFeatureA')
        if m.get('CustomizeFeatureB') is not None:
            self.customize_feature_b = m.get('CustomizeFeatureB')
        if m.get('CustomizeFeatureC') is not None:
            self.customize_feature_c = m.get('CustomizeFeatureC')
        if m.get('CustomizeFeatureD') is not None:
            self.customize_feature_d = m.get('CustomizeFeatureD')
        if m.get('CustomizeFeatureE') is not None:
            self.customize_feature_e = m.get('CustomizeFeatureE')
        if m.get('CustomizeFeatureF') is not None:
            self.customize_feature_f = m.get('CustomizeFeatureF')
        if m.get('CustomizeFeatureG') is not None:
            self.customize_feature_g = m.get('CustomizeFeatureG')
        if m.get('CustomizeFeatureH') is not None:
            self.customize_feature_h = m.get('CustomizeFeatureH')
        if m.get('CustomizeFeatureI') is not None:
            self.customize_feature_i = m.get('CustomizeFeatureI')
        if m.get('CustomizeFeatureJ') is not None:
            self.customize_feature_j = m.get('CustomizeFeatureJ')
        if m.get('CustomizeFeatureK') is not None:
            self.customize_feature_k = m.get('CustomizeFeatureK')
        if m.get('CustomizeFeatureL') is not None:
            self.customize_feature_l = m.get('CustomizeFeatureL')
        if m.get('CustomizeFeatureM') is not None:
            self.customize_feature_m = m.get('CustomizeFeatureM')
        if m.get('CustomizeFeatureN') is not None:
            self.customize_feature_n = m.get('CustomizeFeatureN')
        if m.get('CustomizeFeatureO') is not None:
            self.customize_feature_o = m.get('CustomizeFeatureO')
        if m.get('CustomizeFeatureP') is not None:
            self.customize_feature_p = m.get('CustomizeFeatureP')
        if m.get('CustomizeFeatureQ') is not None:
            self.customize_feature_q = m.get('CustomizeFeatureQ')
        if m.get('CustomizeFeatureR') is not None:
            self.customize_feature_r = m.get('CustomizeFeatureR')
        if m.get('CustomizeFeatureS') is not None:
            self.customize_feature_s = m.get('CustomizeFeatureS')
        if m.get('CustomizeFeatureT') is not None:
            self.customize_feature_t = m.get('CustomizeFeatureT')
        if m.get('CustomizeFeatureU') is not None:
            self.customize_feature_u = m.get('CustomizeFeatureU')
        if m.get('CustomizeFeatureV') is not None:
            self.customize_feature_v = m.get('CustomizeFeatureV')
        if m.get('CustomizeFeatureW') is not None:
            self.customize_feature_w = m.get('CustomizeFeatureW')
        if m.get('CustomizeFeatureX') is not None:
            self.customize_feature_x = m.get('CustomizeFeatureX')
        if m.get('CustomizeFeatureY') is not None:
            self.customize_feature_y = m.get('CustomizeFeatureY')
        if m.get('CustomizeFeatureZ') is not None:
            self.customize_feature_z = m.get('CustomizeFeatureZ')
        if m.get('EnergyEfficiency') is not None:
            self.energy_efficiency = m.get('EnergyEfficiency')
        if m.get('ForestFirstId') is not None:
            self.forest_first_id = m.get('ForestFirstId')
        if m.get('ForestSecondId') is not None:
            self.forest_second_id = m.get('ForestSecondId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InventoryStatus') is not None:
            self.inventory_status = m.get('InventoryStatus')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemInfoIndex') is not None:
            self.item_info_index = m.get('ItemInfoIndex')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        if m.get('ItemQrCode') is not None:
            self.item_qr_code = m.get('ItemQrCode')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('MemberPrice') is not None:
            self.member_price = m.get('MemberPrice')
        if m.get('ModelNumber') is not None:
            self.model_number = m.get('ModelNumber')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('ProductionPlace') is not None:
            self.production_place = m.get('ProductionPlace')
        if m.get('PromotionEnd') is not None:
            self.promotion_end = m.get('PromotionEnd')
        if m.get('PromotionReason') is not None:
            self.promotion_reason = m.get('PromotionReason')
        if m.get('PromotionStart') is not None:
            self.promotion_start = m.get('PromotionStart')
        if m.get('PromotionText') is not None:
            self.promotion_text = m.get('PromotionText')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('SaleSpec') is not None:
            self.sale_spec = m.get('SaleSpec')
        if m.get('SalesPrice') is not None:
            self.sales_price = m.get('SalesPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('SuggestPrice') is not None:
            self.suggest_price = m.get('SuggestPrice')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('TaxFee') is not None:
            self.tax_fee = m.get('TaxFee')
        if m.get('TemplateSceneId') is not None:
            self.template_scene_id = m.get('TemplateSceneId')
        return self


class DescribeItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        items: List[DescribeItemsResponseBodyItems] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        template_scene_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.items = items
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.template_scene_id = template_scene_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template_scene_id is not None:
            result['TemplateSceneId'] = self.template_scene_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeItemsResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateSceneId') is not None:
            self.template_scene_id = m.get('TemplateSceneId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeItemsResponseBody = None,
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
            temp_model = DescribeItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoreByTemplateVersionRequest(TeaModel):
    def __init__(
        self,
        template_version: str = None,
    ):
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class DescribeStoreByTemplateVersionResponseBodyStores(TeaModel):
    def __init__(
        self,
        gmt_modified: str = None,
        level: str = None,
        parent_id: str = None,
        phone: str = None,
        store_id: str = None,
        store_name: str = None,
        template_version: str = None,
        time_zone: str = None,
        user_store_code: str = None,
    ):
        self.gmt_modified = gmt_modified
        self.level = level
        self.parent_id = parent_id
        self.phone = phone
        self.store_id = store_id
        self.store_name = store_name
        self.template_version = template_version
        self.time_zone = time_zone
        self.user_store_code = user_store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.level is not None:
            result['Level'] = self.level
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        return self


class DescribeStoreByTemplateVersionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        stores: List[DescribeStoreByTemplateVersionResponseBodyStores] = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.stores = stores
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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Stores'] = []
        if self.stores is not None:
            for k in self.stores:
                result['Stores'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stores = []
        if m.get('Stores') is not None:
            for k in m.get('Stores'):
                temp_model = DescribeStoreByTemplateVersionResponseBodyStores()
                self.stores.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStoreByTemplateVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStoreByTemplateVersionResponseBody = None,
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
            temp_model = DescribeStoreByTemplateVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoreConfigRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        store_id: str = None,
    ):
        self.extra_params = extra_params
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeStoreConfigResponseBodyStoreConfigInfoSubscribeContents(TeaModel):
    def __init__(
        self,
        at_all: bool = None,
        at_mobile_list: str = None,
        category: str = None,
        enable: bool = None,
        threshold: str = None,
    ):
        self.at_all = at_all
        self.at_mobile_list = at_mobile_list
        self.category = category
        self.enable = enable
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_all is not None:
            result['AtAll'] = self.at_all
        if self.at_mobile_list is not None:
            result['AtMobileList'] = self.at_mobile_list
        if self.category is not None:
            result['Category'] = self.category
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AtAll') is not None:
            self.at_all = m.get('AtAll')
        if m.get('AtMobileList') is not None:
            self.at_mobile_list = m.get('AtMobileList')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class DescribeStoreConfigResponseBodyStoreConfigInfo(TeaModel):
    def __init__(
        self,
        enable_notification: bool = None,
        notification_silent_times: str = None,
        notification_web_hook: str = None,
        store_id: str = None,
        subscribe_contents: List[DescribeStoreConfigResponseBodyStoreConfigInfoSubscribeContents] = None,
    ):
        self.enable_notification = enable_notification
        self.notification_silent_times = notification_silent_times
        self.notification_web_hook = notification_web_hook
        self.store_id = store_id
        self.subscribe_contents = subscribe_contents

    def validate(self):
        if self.subscribe_contents:
            for k in self.subscribe_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_notification is not None:
            result['EnableNotification'] = self.enable_notification
        if self.notification_silent_times is not None:
            result['NotificationSilentTimes'] = self.notification_silent_times
        if self.notification_web_hook is not None:
            result['NotificationWebHook'] = self.notification_web_hook
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        result['SubscribeContents'] = []
        if self.subscribe_contents is not None:
            for k in self.subscribe_contents:
                result['SubscribeContents'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableNotification') is not None:
            self.enable_notification = m.get('EnableNotification')
        if m.get('NotificationSilentTimes') is not None:
            self.notification_silent_times = m.get('NotificationSilentTimes')
        if m.get('NotificationWebHook') is not None:
            self.notification_web_hook = m.get('NotificationWebHook')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        self.subscribe_contents = []
        if m.get('SubscribeContents') is not None:
            for k in m.get('SubscribeContents'):
                temp_model = DescribeStoreConfigResponseBodyStoreConfigInfoSubscribeContents()
                self.subscribe_contents.append(temp_model.from_map(k))
        return self


class DescribeStoreConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        store_config_info: DescribeStoreConfigResponseBodyStoreConfigInfo = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.store_config_info = store_config_info
        self.success = success

    def validate(self):
        if self.store_config_info:
            self.store_config_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.store_config_info is not None:
            result['StoreConfigInfo'] = self.store_config_info.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StoreConfigInfo') is not None:
            temp_model = DescribeStoreConfigResponseBodyStoreConfigInfo()
            self.store_config_info = temp_model.from_map(m['StoreConfigInfo'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeStoreConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStoreConfigResponseBody = None,
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
            temp_model = DescribeStoreConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoresRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        from_date: str = None,
        page_number: int = None,
        page_size: int = None,
        store_id: str = None,
        store_name: str = None,
        template_version: str = None,
        to_date: str = None,
        user_store_code: str = None,
    ):
        self.extra_params = extra_params
        self.from_date = from_date
        self.page_number = page_number
        self.page_size = page_size
        self.store_id = store_id
        self.store_name = store_name
        self.template_version = template_version
        self.to_date = to_date
        self.user_store_code = user_store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        return self


class DescribeStoresResponseBodyStores(TeaModel):
    def __init__(
        self,
        auto_unbind_days: int = None,
        auto_unbind_offline_esl: bool = None,
        bar_code_encode: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        level: str = None,
        parent_id: str = None,
        phone: str = None,
        store_id: str = None,
        store_name: str = None,
        template_version: str = None,
        time_zone: str = None,
        user_store_code: str = None,
    ):
        self.auto_unbind_days = auto_unbind_days
        self.auto_unbind_offline_esl = auto_unbind_offline_esl
        self.bar_code_encode = bar_code_encode
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.level = level
        self.parent_id = parent_id
        self.phone = phone
        self.store_id = store_id
        self.store_name = store_name
        self.template_version = template_version
        self.time_zone = time_zone
        self.user_store_code = user_store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_unbind_days is not None:
            result['AutoUnbindDays'] = self.auto_unbind_days
        if self.auto_unbind_offline_esl is not None:
            result['AutoUnbindOfflineEsl'] = self.auto_unbind_offline_esl
        if self.bar_code_encode is not None:
            result['BarCodeEncode'] = self.bar_code_encode
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.level is not None:
            result['Level'] = self.level
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUnbindDays') is not None:
            self.auto_unbind_days = m.get('AutoUnbindDays')
        if m.get('AutoUnbindOfflineEsl') is not None:
            self.auto_unbind_offline_esl = m.get('AutoUnbindOfflineEsl')
        if m.get('BarCodeEncode') is not None:
            self.bar_code_encode = m.get('BarCodeEncode')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        return self


class DescribeStoresResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stores: List[DescribeStoresResponseBodyStores] = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.stores = stores
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Stores'] = []
        if self.stores is not None:
            for k in self.stores:
                result['Stores'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stores = []
        if m.get('Stores') is not None:
            for k in m.get('Stores'):
                temp_model = DescribeStoresResponseBodyStores()
                self.stores.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStoresResponseBody = None,
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
            temp_model = DescribeStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplateByModelRequest(TeaModel):
    def __init__(
        self,
        device_type: str = None,
        esl_size: str = None,
        page_number: int = None,
        page_size: int = None,
        template_version: str = None,
    ):
        self.device_type = device_type
        self.esl_size = esl_size
        self.page_number = page_number
        self.page_size = page_size
        self.template_version = template_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.esl_size is not None:
            result['EslSize'] = self.esl_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('EslSize') is not None:
            self.esl_size = m.get('EslSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        return self


class DescribeTemplateByModelResponseBodyItems(TeaModel):
    def __init__(
        self,
        base_picture: str = None,
        brand: str = None,
        esl_size: str = None,
        esl_type: str = None,
        height: int = None,
        layout: str = None,
        scene: str = None,
        template_id: str = None,
        template_name: str = None,
        template_scene_id: str = None,
        template_version: str = None,
        width: int = None,
    ):
        self.base_picture = base_picture
        self.brand = brand
        self.esl_size = esl_size
        self.esl_type = esl_type
        self.height = height
        self.layout = layout
        self.scene = scene
        self.template_id = template_id
        self.template_name = template_name
        self.template_scene_id = template_scene_id
        self.template_version = template_version
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_picture is not None:
            result['BasePicture'] = self.base_picture
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.esl_size is not None:
            result['EslSize'] = self.esl_size
        if self.esl_type is not None:
            result['EslType'] = self.esl_type
        if self.height is not None:
            result['Height'] = self.height
        if self.layout is not None:
            result['Layout'] = self.layout
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_scene_id is not None:
            result['TemplateSceneId'] = self.template_scene_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasePicture') is not None:
            self.base_picture = m.get('BasePicture')
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('EslSize') is not None:
            self.esl_size = m.get('EslSize')
        if m.get('EslType') is not None:
            self.esl_type = m.get('EslType')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Layout') is not None:
            self.layout = m.get('Layout')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateSceneId') is not None:
            self.template_scene_id = m.get('TemplateSceneId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeTemplateByModelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        items: List[DescribeTemplateByModelResponseBodyItems] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.items = items
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeTemplateByModelResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTemplateByModelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTemplateByModelResponseBody = None,
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
            temp_model = DescribeTemplateByModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserLogRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        extra_params: str = None,
        from_date: str = None,
        item_bar_code: str = None,
        item_short_title: str = None,
        log_id: str = None,
        operation_status: str = None,
        operation_type: str = None,
        page_number: int = None,
        page_size: int = None,
        store_id: str = None,
        to_date: str = None,
        user_id: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.extra_params = extra_params
        self.from_date = from_date
        self.item_bar_code = item_bar_code
        self.item_short_title = item_short_title
        self.log_id = log_id
        self.operation_status = operation_status
        self.operation_type = operation_type
        self.page_number = page_number
        self.page_size = page_size
        self.store_id = store_id
        self.to_date = to_date
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.log_id is not None:
            result['LogId'] = self.log_id
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeUserLogResponseBodyUserLogs(TeaModel):
    def __init__(
        self,
        action_price: str = None,
        be_promotion: bool = None,
        esl_bar_code: str = None,
        esl_signal: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        i_18n_result_key: str = None,
        item_bar_code: str = None,
        item_id: str = None,
        item_short_title: str = None,
        log_id: str = None,
        operation_response_time: str = None,
        operation_send_time: str = None,
        operation_status: str = None,
        operation_type: str = None,
        price_unit: str = None,
        result_code: str = None,
        spend_time: str = None,
        store_id: str = None,
        user_id: str = None,
    ):
        self.action_price = action_price
        self.be_promotion = be_promotion
        self.esl_bar_code = esl_bar_code
        self.esl_signal = esl_signal
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.i_18n_result_key = i_18n_result_key
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_short_title = item_short_title
        self.log_id = log_id
        self.operation_response_time = operation_response_time
        self.operation_send_time = operation_send_time
        self.operation_status = operation_status
        self.operation_type = operation_type
        self.price_unit = price_unit
        self.result_code = result_code
        self.spend_time = spend_time
        self.store_id = store_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.esl_signal is not None:
            result['EslSignal'] = self.esl_signal
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.i_18n_result_key is not None:
            result['I18nResultKey'] = self.i_18n_result_key
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.log_id is not None:
            result['LogId'] = self.log_id
        if self.operation_response_time is not None:
            result['OperationResponseTime'] = self.operation_response_time
        if self.operation_send_time is not None:
            result['OperationSendTime'] = self.operation_send_time
        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.result_code is not None:
            result['ResultCode'] = self.result_code
        if self.spend_time is not None:
            result['SpendTime'] = self.spend_time
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('EslSignal') is not None:
            self.esl_signal = m.get('EslSignal')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('I18nResultKey') is not None:
            self.i_18n_result_key = m.get('I18nResultKey')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')
        if m.get('OperationResponseTime') is not None:
            self.operation_response_time = m.get('OperationResponseTime')
        if m.get('OperationSendTime') is not None:
            self.operation_send_time = m.get('OperationSendTime')
        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')
        if m.get('SpendTime') is not None:
            self.spend_time = m.get('SpendTime')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DescribeUserLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        user_logs: List[DescribeUserLogResponseBodyUserLogs] = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserLogs'] = []
        if self.user_logs is not None:
            for k in self.user_logs:
                result['UserLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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
        status_code: int = None,
        body: DescribeUserLogResponseBody = None,
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
            temp_model = DescribeUserLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        page_number: int = None,
        page_size: int = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.extra_params = extra_params
        self.page_number = page_number
        self.page_size = page_size
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeUsersResponseBodyUsersDingTalkInfos(TeaModel):
    def __init__(
        self,
        ding_talk_company_id: str = None,
        ding_talk_user_id: str = None,
    ):
        self.ding_talk_company_id = ding_talk_company_id
        self.ding_talk_user_id = ding_talk_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_talk_company_id is not None:
            result['DingTalkCompanyId'] = self.ding_talk_company_id
        if self.ding_talk_user_id is not None:
            result['DingTalkUserId'] = self.ding_talk_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingTalkCompanyId') is not None:
            self.ding_talk_company_id = m.get('DingTalkCompanyId')
        if m.get('DingTalkUserId') is not None:
            self.ding_talk_user_id = m.get('DingTalkUserId')
        return self


class DescribeUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        bid: str = None,
        ding_talk_infos: List[DescribeUsersResponseBodyUsersDingTalkInfos] = None,
        owner_id: str = None,
        stores: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.bid = bid
        self.ding_talk_infos = ding_talk_infos
        self.owner_id = owner_id
        self.stores = stores
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

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
        if self.bid is not None:
            result['Bid'] = self.bid
        result['DingTalkInfos'] = []
        if self.ding_talk_infos is not None:
            for k in self.ding_talk_infos:
                result['DingTalkInfos'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        self.ding_talk_infos = []
        if m.get('DingTalkInfos') is not None:
            for k in m.get('DingTalkInfos'):
                temp_model = DescribeUsersResponseBodyUsersDingTalkInfos()
                self.ding_talk_infos.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        users: List[DescribeUsersResponseBodyUsers] = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.users = users

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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = DescribeUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class DescribeUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsersResponseBody = None,
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
            temp_model = DescribeUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        user_id: str = None,
    ):
        self.extra_params = extra_params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserResponseBodyUserDingTalkInfos(TeaModel):
    def __init__(
        self,
        ding_talk_company_id: str = None,
        ding_talk_user_id: str = None,
    ):
        self.ding_talk_company_id = ding_talk_company_id
        self.ding_talk_user_id = ding_talk_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_talk_company_id is not None:
            result['DingTalkCompanyId'] = self.ding_talk_company_id
        if self.ding_talk_user_id is not None:
            result['DingTalkUserId'] = self.ding_talk_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DingTalkCompanyId') is not None:
            self.ding_talk_company_id = m.get('DingTalkCompanyId')
        if m.get('DingTalkUserId') is not None:
            self.ding_talk_user_id = m.get('DingTalkUserId')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        bid: str = None,
        ding_talk_infos: List[GetUserResponseBodyUserDingTalkInfos] = None,
        owner_id: str = None,
        stores: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.bid = bid
        self.ding_talk_infos = ding_talk_infos
        self.owner_id = owner_id
        self.stores = stores
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

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
        if self.bid is not None:
            result['Bid'] = self.bid
        result['DingTalkInfos'] = []
        if self.ding_talk_infos is not None:
            for k in self.ding_talk_infos:
                result['DingTalkInfos'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        self.ding_talk_infos = []
        if m.get('DingTalkInfos') is not None:
            for k in m.get('DingTalkInfos'):
                temp_model = GetUserResponseBodyUserDingTalkInfos()
                self.ding_talk_infos.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user: GetUserResponseBodyUser = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTemplateListByGroupIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.group_id = group_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTemplateListByGroupIdResponseBodyTemplateList(TeaModel):
    def __init__(
        self,
        base_picture: str = None,
        brand: str = None,
        esl_size: str = None,
        esl_type: str = None,
        group_id: str = None,
        height: int = None,
        layout: str = None,
        relation: bool = None,
        scene: str = None,
        template_id: str = None,
        template_name: str = None,
        template_scene_id: str = None,
        template_version: str = None,
        width: int = None,
    ):
        self.base_picture = base_picture
        self.brand = brand
        self.esl_size = esl_size
        self.esl_type = esl_type
        self.group_id = group_id
        self.height = height
        self.layout = layout
        self.relation = relation
        self.scene = scene
        self.template_id = template_id
        self.template_name = template_name
        self.template_scene_id = template_scene_id
        self.template_version = template_version
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_picture is not None:
            result['BasePicture'] = self.base_picture
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.esl_size is not None:
            result['EslSize'] = self.esl_size
        if self.esl_type is not None:
            result['EslType'] = self.esl_type
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.height is not None:
            result['Height'] = self.height
        if self.layout is not None:
            result['Layout'] = self.layout
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_scene_id is not None:
            result['TemplateSceneId'] = self.template_scene_id
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasePicture') is not None:
            self.base_picture = m.get('BasePicture')
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('EslSize') is not None:
            self.esl_size = m.get('EslSize')
        if m.get('EslType') is not None:
            self.esl_type = m.get('EslType')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Layout') is not None:
            self.layout = m.get('Layout')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateSceneId') is not None:
            self.template_scene_id = m.get('TemplateSceneId')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryTemplateListByGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        template_list: List[QueryTemplateListByGroupIdResponseBodyTemplateList] = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.template_list = template_list
        self.total_count = total_count

    def validate(self):
        if self.template_list:
            for k in self.template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['TemplateList'] = []
        if self.template_list is not None:
            for k in self.template_list:
                result['TemplateList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.template_list = []
        if m.get('TemplateList') is not None:
            for k in m.get('TemplateList'):
                temp_model = QueryTemplateListByGroupIdResponseBodyTemplateList()
                self.template_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryTemplateListByGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTemplateListByGroupIdResponseBody = None,
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
            temp_model = QueryTemplateListByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncAddMaterialRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
    ):
        self.content = content
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SyncAddMaterialResponseBodyResult(TeaModel):
    def __init__(
        self,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncAddMaterialResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        result: SyncAddMaterialResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SyncAddMaterialResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncAddMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncAddMaterialResponseBody = None,
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
            temp_model = SyncAddMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassignUserRequest(TeaModel):
    def __init__(
        self,
        extra_params: str = None,
        user_id: str = None,
    ):
        self.extra_params = extra_params
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UnassignUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnassignUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnassignUserResponseBody = None,
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
            temp_model = UnassignUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEslDeviceRequest(TeaModel):
    def __init__(
        self,
        column: str = None,
        container_name: str = None,
        esl_bar_code: str = None,
        extra_params: str = None,
        item_bar_code: str = None,
        layer: int = None,
        shelf: str = None,
        store_id: str = None,
    ):
        self.column = column
        self.container_name = container_name
        self.esl_bar_code = esl_bar_code
        self.extra_params = extra_params
        self.item_bar_code = item_bar_code
        self.layer = layer
        self.shelf = shelf
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['Column'] = self.column
        if self.container_name is not None:
            result['ContainerName'] = self.container_name
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class UnbindEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindEslDeviceResponseBody = None,
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
            temp_model = UnbindEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEslDeviceLightRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        extra_params: str = None,
        frequency: str = None,
        item_bar_code: str = None,
        led_color: str = None,
        light_up_time: int = None,
        store_id: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.extra_params = extra_params
        self.frequency = frequency
        self.item_bar_code = item_bar_code
        self.led_color = led_color
        self.light_up_time = light_up_time
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.led_color is not None:
            result['LedColor'] = self.led_color
        if self.light_up_time is not None:
            result['LightUpTime'] = self.light_up_time
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('LedColor') is not None:
            self.led_color = m.get('LedColor')
        if m.get('LightUpTime') is not None:
            self.light_up_time = m.get('LightUpTime')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class UpdateEslDeviceLightResponseBodyLightFailEslInfos(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        esl_bar_code: str = None,
    ):
        self.error_message = error_message
        self.esl_bar_code = esl_bar_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        return self


class UpdateEslDeviceLightResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        fail_count: int = None,
        light_fail_esl_infos: List[UpdateEslDeviceLightResponseBodyLightFailEslInfos] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        success_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.fail_count = fail_count
        self.light_fail_esl_infos = light_fail_esl_infos
        self.message = message
        self.request_id = request_id
        self.success = success
        self.success_count = success_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        result['LightFailEslInfos'] = []
        if self.light_fail_esl_infos is not None:
            for k in self.light_fail_esl_infos:
                result['LightFailEslInfos'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        self.light_fail_esl_infos = []
        if m.get('LightFailEslInfos') is not None:
            for k in m.get('LightFailEslInfos'):
                temp_model = UpdateEslDeviceLightResponseBodyLightFailEslInfos()
                self.light_fail_esl_infos.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class UpdateEslDeviceLightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEslDeviceLightResponseBody = None,
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
            temp_model = UpdateEslDeviceLightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoreRequest(TeaModel):
    def __init__(
        self,
        auto_unbind_days: int = None,
        auto_unbind_offline_esl: bool = None,
        bar_code_encode: int = None,
        extra_params: str = None,
        phone: str = None,
        store_id: str = None,
        store_name: str = None,
        template_version: str = None,
        timezone: str = None,
        user_store_code: str = None,
    ):
        self.auto_unbind_days = auto_unbind_days
        self.auto_unbind_offline_esl = auto_unbind_offline_esl
        self.bar_code_encode = bar_code_encode
        self.extra_params = extra_params
        self.phone = phone
        self.store_id = store_id
        self.store_name = store_name
        self.template_version = template_version
        self.timezone = timezone
        self.user_store_code = user_store_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_unbind_days is not None:
            result['AutoUnbindDays'] = self.auto_unbind_days
        if self.auto_unbind_offline_esl is not None:
            result['AutoUnbindOfflineEsl'] = self.auto_unbind_offline_esl
        if self.bar_code_encode is not None:
            result['BarCodeEncode'] = self.bar_code_encode
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.user_store_code is not None:
            result['UserStoreCode'] = self.user_store_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUnbindDays') is not None:
            self.auto_unbind_days = m.get('AutoUnbindDays')
        if m.get('AutoUnbindOfflineEsl') is not None:
            self.auto_unbind_offline_esl = m.get('AutoUnbindOfflineEsl')
        if m.get('BarCodeEncode') is not None:
            self.bar_code_encode = m.get('BarCodeEncode')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('UserStoreCode') is not None:
            self.user_store_code = m.get('UserStoreCode')
        return self


class UpdateStoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStoreResponseBody = None,
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
            temp_model = UpdateStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoreConfigRequest(TeaModel):
    def __init__(
        self,
        enable_notification: bool = None,
        extra_params: str = None,
        notification_silent_times: str = None,
        notification_web_hook: str = None,
        store_id: str = None,
        subscribe_contents: str = None,
    ):
        self.enable_notification = enable_notification
        self.extra_params = extra_params
        self.notification_silent_times = notification_silent_times
        self.notification_web_hook = notification_web_hook
        self.store_id = store_id
        self.subscribe_contents = subscribe_contents

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_notification is not None:
            result['EnableNotification'] = self.enable_notification
        if self.extra_params is not None:
            result['ExtraParams'] = self.extra_params
        if self.notification_silent_times is not None:
            result['NotificationSilentTimes'] = self.notification_silent_times
        if self.notification_web_hook is not None:
            result['NotificationWebHook'] = self.notification_web_hook
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.subscribe_contents is not None:
            result['SubscribeContents'] = self.subscribe_contents
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableNotification') is not None:
            self.enable_notification = m.get('EnableNotification')
        if m.get('ExtraParams') is not None:
            self.extra_params = m.get('ExtraParams')
        if m.get('NotificationSilentTimes') is not None:
            self.notification_silent_times = m.get('NotificationSilentTimes')
        if m.get('NotificationWebHook') is not None:
            self.notification_web_hook = m.get('NotificationWebHook')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('SubscribeContents') is not None:
            self.subscribe_contents = m.get('SubscribeContents')
        return self


class UpdateStoreConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
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
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateStoreConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStoreConfigResponseBody = None,
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
            temp_model = UpdateStoreConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


