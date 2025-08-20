# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AppUseTimeReportHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class AppUseTimeReportRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AppUseTimeReportRequestPayload(TeaModel):
    def __init__(
        self,
        action: str = None,
        is_privilege: int = None,
        resource_id: str = None,
        resource_type: int = None,
        step_code: str = None,
        vip_type: int = None,
        origin_uuid: str = None,
    ):
        # This parameter is required.
        self.action = action
        # This parameter is required.
        self.is_privilege = is_privilege
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type
        # This parameter is required.
        self.step_code = step_code
        # This parameter is required.
        self.vip_type = vip_type
        self.origin_uuid = origin_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.is_privilege is not None:
            result['IsPrivilege'] = self.is_privilege
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.step_code is not None:
            result['StepCode'] = self.step_code
        if self.vip_type is not None:
            result['VipType'] = self.vip_type
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('IsPrivilege') is not None:
            self.is_privilege = m.get('IsPrivilege')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StepCode') is not None:
            self.step_code = m.get('StepCode')
        if m.get('VipType') is not None:
            self.vip_type = m.get('VipType')
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        return self


class AppUseTimeReportRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class AppUseTimeReportRequest(TeaModel):
    def __init__(
        self,
        device_info: AppUseTimeReportRequestDeviceInfo = None,
        payload: AppUseTimeReportRequestPayload = None,
        user_info: AppUseTimeReportRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = AppUseTimeReportRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = AppUseTimeReportRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = AppUseTimeReportRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class AppUseTimeReportShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class AppUseTimeReportResponseBody(TeaModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: bool = None,
    ):
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.ret_value = ret_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        return self


class AppUseTimeReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AppUseTimeReportResponseBody = None,
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
            temp_model = AppUseTimeReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CallBackThirdRightSendPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CallBackThirdRightSendPlanRequest(TeaModel):
    def __init__(
        self,
        biz_group: str = None,
        biz_type: str = None,
        card_type: int = None,
        error_msg: str = None,
        extend_info: Dict[str, Any] = None,
        genie_open_id: str = None,
        receive_status: int = None,
        sn: str = None,
        supplier_id: int = None,
    ):
        self.biz_group = biz_group
        self.biz_type = biz_type
        self.card_type = card_type
        self.error_msg = error_msg
        self.extend_info = extend_info
        self.genie_open_id = genie_open_id
        self.receive_status = receive_status
        self.sn = sn
        self.supplier_id = supplier_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.genie_open_id is not None:
            result['GenieOpenId'] = self.genie_open_id
        if self.receive_status is not None:
            result['ReceiveStatus'] = self.receive_status
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('GenieOpenId') is not None:
            self.genie_open_id = m.get('GenieOpenId')
        if m.get('ReceiveStatus') is not None:
            self.receive_status = m.get('ReceiveStatus')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')
        return self


class CallBackThirdRightSendPlanShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_group: str = None,
        biz_type: str = None,
        card_type: int = None,
        error_msg: str = None,
        extend_info_shrink: str = None,
        genie_open_id: str = None,
        receive_status: int = None,
        sn: str = None,
        supplier_id: int = None,
    ):
        self.biz_group = biz_group
        self.biz_type = biz_type
        self.card_type = card_type
        self.error_msg = error_msg
        self.extend_info_shrink = extend_info_shrink
        self.genie_open_id = genie_open_id
        self.receive_status = receive_status
        self.sn = sn
        self.supplier_id = supplier_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.extend_info_shrink is not None:
            result['ExtendInfo'] = self.extend_info_shrink
        if self.genie_open_id is not None:
            result['GenieOpenId'] = self.genie_open_id
        if self.receive_status is not None:
            result['ReceiveStatus'] = self.receive_status
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('ExtendInfo') is not None:
            self.extend_info_shrink = m.get('ExtendInfo')
        if m.get('GenieOpenId') is not None:
            self.genie_open_id = m.get('GenieOpenId')
        if m.get('ReceiveStatus') is not None:
            self.receive_status = m.get('ReceiveStatus')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')
        return self


class CallBackThirdRightSendPlanResponseBody(TeaModel):
    def __init__(
        self,
        ret_code: str = None,
        ret_msg: str = None,
        ret_value: bool = None,
        request_id: str = None,
    ):
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.ret_value = ret_value
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CallBackThirdRightSendPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CallBackThirdRightSendPlanResponseBody = None,
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
            temp_model = CallBackThirdRightSendPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckThirdRightSendPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CheckThirdRightSendPlanRequest(TeaModel):
    def __init__(
        self,
        biz_group: str = None,
        biz_type: str = None,
        extend_info: Dict[str, Any] = None,
        sn: str = None,
        supplier_id: int = None,
    ):
        self.biz_group = biz_group
        self.biz_type = biz_type
        self.extend_info = extend_info
        self.sn = sn
        self.supplier_id = supplier_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')
        return self


class CheckThirdRightSendPlanShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_group: str = None,
        biz_type: str = None,
        extend_info_shrink: str = None,
        sn: str = None,
        supplier_id: int = None,
    ):
        self.biz_group = biz_group
        self.biz_type = biz_type
        self.extend_info_shrink = extend_info_shrink
        self.sn = sn
        self.supplier_id = supplier_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.extend_info_shrink is not None:
            result['ExtendInfo'] = self.extend_info_shrink
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ExtendInfo') is not None:
            self.extend_info_shrink = m.get('ExtendInfo')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')
        return self


class CheckThirdRightSendPlanResponseBodyRetValue(TeaModel):
    def __init__(
        self,
        activate_date: str = None,
        card_type: int = None,
        channel_code: str = None,
        channel_name: str = None,
        extend_info: Dict[str, Any] = None,
        request_id: str = None,
        rights_expired_date: str = None,
    ):
        self.activate_date = activate_date
        self.card_type = card_type
        self.channel_code = channel_code
        self.channel_name = channel_name
        self.extend_info = extend_info
        self.request_id = request_id
        self.rights_expired_date = rights_expired_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activate_date is not None:
            result['ActivateDate'] = self.activate_date
        if self.card_type is not None:
            result['CardType'] = self.card_type
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rights_expired_date is not None:
            result['RightsExpiredDate'] = self.rights_expired_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateDate') is not None:
            self.activate_date = m.get('ActivateDate')
        if m.get('CardType') is not None:
            self.card_type = m.get('CardType')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RightsExpiredDate') is not None:
            self.rights_expired_date = m.get('RightsExpiredDate')
        return self


class CheckThirdRightSendPlanResponseBody(TeaModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: CheckThirdRightSendPlanResponseBodyRetValue = None,
    ):
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.ret_value = ret_value

    def validate(self):
        if self.ret_value:
            self.ret_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            temp_model = CheckThirdRightSendPlanResponseBodyRetValue()
            self.ret_value = temp_model.from_map(m['RetValue'])
        return self


class CheckThirdRightSendPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckThirdRightSendPlanResponseBody = None,
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
            temp_model = CheckThirdRightSendPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateReminderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class CreateReminderRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateReminderRequestPayloadRecurrenceRule(TeaModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: int = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: int = None,
        year: int = None,
    ):
        self.day = day
        self.days_of_month = days_of_month
        self.days_of_week = days_of_week
        # This parameter is required.
        self.end_date_time = end_date_time
        # This parameter is required.
        self.freq = freq
        # This parameter is required.
        self.hour = hour
        self.minute = minute
        self.month = month
        self.second = second
        # This parameter is required.
        self.start_date_time = start_date_time
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateReminderRequestPayload(TeaModel):
    def __init__(
        self,
        content: str = None,
        is_debug: bool = None,
        recurrence_rule: CreateReminderRequestPayloadRecurrenceRule = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.is_debug = is_debug
        # This parameter is required.
        self.recurrence_rule = recurrence_rule

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('RecurrenceRule') is not None:
            temp_model = CreateReminderRequestPayloadRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        return self


class CreateReminderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreateReminderRequest(TeaModel):
    def __init__(
        self,
        device_info: CreateReminderRequestDeviceInfo = None,
        payload: CreateReminderRequestPayload = None,
        user_info: CreateReminderRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreateReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = CreateReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = CreateReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreateReminderShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreateReminderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        model: int = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.model = model
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateReminderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateReminderResponseBody = None,
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
            temp_model = CreateReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteReminderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class DeleteReminderRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteReminderRequestPayload(TeaModel):
    def __init__(
        self,
        id: int = None,
        is_debug: bool = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.is_debug = is_debug

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class DeleteReminderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class DeleteReminderRequest(TeaModel):
    def __init__(
        self,
        device_info: DeleteReminderRequestDeviceInfo = None,
        payload: DeleteReminderRequestPayload = None,
        user_info: DeleteReminderRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = DeleteReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = DeleteReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeleteReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeleteReminderShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeleteReminderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteReminderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteReminderResponseBody = None,
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
            temp_model = DeleteReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccountForAppHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetAccountForAppRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetAccountForAppRequestPayload(TeaModel):
    def __init__(
        self,
        phone: str = None,
        origin_uuid: str = None,
    ):
        self.phone = phone
        self.origin_uuid = origin_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        return self


class GetAccountForAppRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetAccountForAppRequest(TeaModel):
    def __init__(
        self,
        device_info: GetAccountForAppRequestDeviceInfo = None,
        payload: GetAccountForAppRequestPayload = None,
        user_info: GetAccountForAppRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetAccountForAppRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetAccountForAppRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetAccountForAppRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetAccountForAppShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetAccountForAppResponseBodyRetValue(TeaModel):
    def __init__(
        self,
        is_vip: bool = None,
        str_vip_expire: str = None,
        vip_expire_at: int = None,
    ):
        self.is_vip = is_vip
        self.str_vip_expire = str_vip_expire
        self.vip_expire_at = vip_expire_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_vip is not None:
            result['IsVip'] = self.is_vip
        if self.str_vip_expire is not None:
            result['StrVipExpire'] = self.str_vip_expire
        if self.vip_expire_at is not None:
            result['VipExpireAt'] = self.vip_expire_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsVip') is not None:
            self.is_vip = m.get('IsVip')
        if m.get('StrVipExpire') is not None:
            self.str_vip_expire = m.get('StrVipExpire')
        if m.get('VipExpireAt') is not None:
            self.vip_expire_at = m.get('VipExpireAt')
        return self


class GetAccountForAppResponseBody(TeaModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: GetAccountForAppResponseBodyRetValue = None,
    ):
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.ret_value = ret_value

    def validate(self):
        if self.ret_value:
            self.ret_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            temp_model = GetAccountForAppResponseBodyRetValue()
            self.ret_value = temp_model.from_map(m['RetValue'])
        return self


class GetAccountForAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAccountForAppResponseBody = None,
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
            temp_model = GetAccountForAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBusAppConfigHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetBusAppConfigRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetBusAppConfigRequestPayload(TeaModel):
    def __init__(
        self,
        origin_uuid: str = None,
        phone: str = None,
    ):
        self.origin_uuid = origin_uuid
        self.phone = phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        if self.phone is not None:
            result['phone'] = self.phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        return self


class GetBusAppConfigRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetBusAppConfigRequest(TeaModel):
    def __init__(
        self,
        device_info: GetBusAppConfigRequestDeviceInfo = None,
        payload: GetBusAppConfigRequestPayload = None,
        user_info: GetBusAppConfigRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetBusAppConfigRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetBusAppConfigRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetBusAppConfigRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetBusAppConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetBusAppConfigResponseBodyRetValue(TeaModel):
    def __init__(
        self,
        cashier: str = None,
        shopping_bar: str = None,
        shopping_window: str = None,
        vip_label: str = None,
    ):
        self.cashier = cashier
        self.shopping_bar = shopping_bar
        self.shopping_window = shopping_window
        self.vip_label = vip_label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cashier is not None:
            result['Cashier'] = self.cashier
        if self.shopping_bar is not None:
            result['ShoppingBar'] = self.shopping_bar
        if self.shopping_window is not None:
            result['ShoppingWindow'] = self.shopping_window
        if self.vip_label is not None:
            result['VipLabel'] = self.vip_label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cashier') is not None:
            self.cashier = m.get('Cashier')
        if m.get('ShoppingBar') is not None:
            self.shopping_bar = m.get('ShoppingBar')
        if m.get('ShoppingWindow') is not None:
            self.shopping_window = m.get('ShoppingWindow')
        if m.get('VipLabel') is not None:
            self.vip_label = m.get('VipLabel')
        return self


class GetBusAppConfigResponseBody(TeaModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: GetBusAppConfigResponseBodyRetValue = None,
    ):
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.ret_value = ret_value

    def validate(self):
        if self.ret_value:
            self.ret_value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            temp_model = GetBusAppConfigResponseBodyRetValue()
            self.ret_value = temp_model.from_map(m['RetValue'])
        return self


class GetBusAppConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBusAppConfigResponseBody = None,
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
            temp_model = GetBusAppConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPhoneNumberHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetPhoneNumberRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetPhoneNumberRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        device_info: GetPhoneNumberRequestDeviceInfo = None,
        user_info: GetPhoneNumberRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetPhoneNumberRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetPhoneNumberRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetPhoneNumberShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
    ):
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['phoneNumber'] = self.phone_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phoneNumber') is not None:
            self.phone_number = m.get('phoneNumber')
        return self


class GetPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPhoneNumberResponseBody = None,
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
            temp_model = GetPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReminderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class GetReminderRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetReminderRequestPayload(TeaModel):
    def __init__(
        self,
        id: int = None,
        is_debug: bool = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.is_debug = is_debug

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class GetReminderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetReminderRequest(TeaModel):
    def __init__(
        self,
        device_info: GetReminderRequestDeviceInfo = None,
        payload: GetReminderRequestPayload = None,
        user_info: GetReminderRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetReminderShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetReminderResponseBodyModelRemindResponsesRecurrenceRule(TeaModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: str = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: str = None,
        year: int = None,
    ):
        self.day = day
        self.days_of_month = days_of_month
        self.days_of_week = days_of_week
        self.end_date_time = end_date_time
        self.freq = freq
        self.hour = hour
        self.minute = minute
        self.month = month
        self.second = second
        self.start_date_time = start_date_time
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class GetReminderResponseBodyModelRemindResponses(TeaModel):
    def __init__(
        self,
        action_topic: str = None,
        day_desc: str = None,
        recurrence_rule: GetReminderResponseBodyModelRemindResponsesRecurrenceRule = None,
        remind_id: int = None,
        remind_time: str = None,
        repeat_count: int = None,
        week: str = None,
    ):
        self.action_topic = action_topic
        self.day_desc = day_desc
        self.recurrence_rule = recurrence_rule
        self.remind_id = remind_id
        self.remind_time = remind_time
        self.repeat_count = repeat_count
        self.week = week

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_topic is not None:
            result['ActionTopic'] = self.action_topic
        if self.day_desc is not None:
            result['DayDesc'] = self.day_desc
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        if self.remind_id is not None:
            result['RemindId'] = self.remind_id
        if self.remind_time is not None:
            result['RemindTime'] = self.remind_time
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.week is not None:
            result['Week'] = self.week
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTopic') is not None:
            self.action_topic = m.get('ActionTopic')
        if m.get('DayDesc') is not None:
            self.day_desc = m.get('DayDesc')
        if m.get('RecurrenceRule') is not None:
            temp_model = GetReminderResponseBodyModelRemindResponsesRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')
        if m.get('RemindTime') is not None:
            self.remind_time = m.get('RemindTime')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('Week') is not None:
            self.week = m.get('Week')
        return self


class GetReminderResponseBodyModel(TeaModel):
    def __init__(
        self,
        remind_responses: List[GetReminderResponseBodyModelRemindResponses] = None,
    ):
        self.remind_responses = remind_responses

    def validate(self):
        if self.remind_responses:
            for k in self.remind_responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemindResponses'] = []
        if self.remind_responses is not None:
            for k in self.remind_responses:
                result['RemindResponses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remind_responses = []
        if m.get('RemindResponses') is not None:
            for k in m.get('RemindResponses'):
                temp_model = GetReminderResponseBodyModelRemindResponses()
                self.remind_responses.append(temp_model.from_map(k))
        return self


class GetReminderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        model: GetReminderResponseBodyModel = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.model = model
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            temp_model = GetReminderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetReminderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReminderResponseBody = None,
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
            temp_model = GetReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRemindersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ListRemindersRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRemindersRequestPayload(TeaModel):
    def __init__(
        self,
        is_debug: bool = None,
    ):
        # This parameter is required.
        self.is_debug = is_debug

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        return self


class ListRemindersRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListRemindersRequest(TeaModel):
    def __init__(
        self,
        device_info: ListRemindersRequestDeviceInfo = None,
        payload: ListRemindersRequestPayload = None,
        user_info: ListRemindersRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListRemindersRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = ListRemindersRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListRemindersRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListRemindersShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListRemindersResponseBodyModelRemindResponsesRecurrenceRule(TeaModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: str = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: str = None,
        year: int = None,
    ):
        self.day = day
        self.days_of_month = days_of_month
        self.days_of_week = days_of_week
        self.end_date_time = end_date_time
        self.freq = freq
        self.hour = hour
        self.minute = minute
        self.month = month
        self.second = second
        self.start_date_time = start_date_time
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class ListRemindersResponseBodyModelRemindResponses(TeaModel):
    def __init__(
        self,
        action_topic: str = None,
        day_desc: str = None,
        recurrence_rule: ListRemindersResponseBodyModelRemindResponsesRecurrenceRule = None,
        remind_id: int = None,
        remind_time: str = None,
        repeat_count: int = None,
        week: str = None,
    ):
        self.action_topic = action_topic
        self.day_desc = day_desc
        self.recurrence_rule = recurrence_rule
        self.remind_id = remind_id
        self.remind_time = remind_time
        self.repeat_count = repeat_count
        self.week = week

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_topic is not None:
            result['ActionTopic'] = self.action_topic
        if self.day_desc is not None:
            result['DayDesc'] = self.day_desc
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        if self.remind_id is not None:
            result['RemindId'] = self.remind_id
        if self.remind_time is not None:
            result['RemindTime'] = self.remind_time
        if self.repeat_count is not None:
            result['RepeatCount'] = self.repeat_count
        if self.week is not None:
            result['Week'] = self.week
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionTopic') is not None:
            self.action_topic = m.get('ActionTopic')
        if m.get('DayDesc') is not None:
            self.day_desc = m.get('DayDesc')
        if m.get('RecurrenceRule') is not None:
            temp_model = ListRemindersResponseBodyModelRemindResponsesRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')
        if m.get('RemindTime') is not None:
            self.remind_time = m.get('RemindTime')
        if m.get('RepeatCount') is not None:
            self.repeat_count = m.get('RepeatCount')
        if m.get('Week') is not None:
            self.week = m.get('Week')
        return self


class ListRemindersResponseBodyModel(TeaModel):
    def __init__(
        self,
        remind_responses: List[ListRemindersResponseBodyModelRemindResponses] = None,
    ):
        self.remind_responses = remind_responses

    def validate(self):
        if self.remind_responses:
            for k in self.remind_responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RemindResponses'] = []
        if self.remind_responses is not None:
            for k in self.remind_responses:
                result['RemindResponses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.remind_responses = []
        if m.get('RemindResponses') is not None:
            for k in m.get('RemindResponses'):
                temp_model = ListRemindersResponseBodyModelRemindResponses()
                self.remind_responses.append(temp_model.from_map(k))
        return self


class ListRemindersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        model: ListRemindersResponseBodyModel = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.model = model
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            temp_model = ListRemindersResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRemindersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRemindersResponseBody = None,
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
            temp_model = ListRemindersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PullCashierHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PullCashierRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PullCashierRequestPayload(TeaModel):
    def __init__(
        self,
        origin_uuid: str = None,
    ):
        self.origin_uuid = origin_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        return self


class PullCashierRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class PullCashierRequest(TeaModel):
    def __init__(
        self,
        device_info: PullCashierRequestDeviceInfo = None,
        payload: PullCashierRequestPayload = None,
        user_info: PullCashierRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = PullCashierRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = PullCashierRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = PullCashierRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class PullCashierShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class PullCashierResponseBody(TeaModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: bool = None,
    ):
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.ret_value = ret_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        return self


class PullCashierResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PullCashierResponseBody = None,
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
            temp_model = PullCashierResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushNotificationsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class PushNotificationsRequestNotificationUnicastRequestSendTarget(TeaModel):
    def __init__(
        self,
        target_identity: str = None,
        target_type: str = None,
    ):
        self.target_identity = target_identity
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class PushNotificationsRequestNotificationUnicastRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        is_debug: bool = None,
        message_template_id: str = None,
        organization_id: str = None,
        place_holder: Dict[str, str] = None,
        send_target: PushNotificationsRequestNotificationUnicastRequestSendTarget = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        self.is_debug = is_debug
        # This parameter is required.
        self.message_template_id = message_template_id
        self.organization_id = organization_id
        self.place_holder = place_holder
        # This parameter is required.
        self.send_target = send_target

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.send_target is not None:
            result['SendTarget'] = self.send_target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('SendTarget') is not None:
            temp_model = PushNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m['SendTarget'])
        return self


class PushNotificationsRequestTenantInfo(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PushNotificationsRequest(TeaModel):
    def __init__(
        self,
        notification_unicast_request: PushNotificationsRequestNotificationUnicastRequest = None,
        tenant_info: PushNotificationsRequestTenantInfo = None,
    ):
        # This parameter is required.
        self.notification_unicast_request = notification_unicast_request
        self.tenant_info = tenant_info

    def validate(self):
        if self.notification_unicast_request:
            self.notification_unicast_request.validate()
        if self.tenant_info:
            self.tenant_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_unicast_request is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request.to_map()
        if self.tenant_info is not None:
            result['TenantInfo'] = self.tenant_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationUnicastRequest') is not None:
            temp_model = PushNotificationsRequestNotificationUnicastRequest()
            self.notification_unicast_request = temp_model.from_map(m['NotificationUnicastRequest'])
        if m.get('TenantInfo') is not None:
            temp_model = PushNotificationsRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m['TenantInfo'])
        return self


class PushNotificationsShrinkRequest(TeaModel):
    def __init__(
        self,
        notification_unicast_request_shrink: str = None,
        tenant_info_shrink: str = None,
    ):
        # This parameter is required.
        self.notification_unicast_request_shrink = notification_unicast_request_shrink
        self.tenant_info_shrink = tenant_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notification_unicast_request_shrink is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request_shrink
        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotificationUnicastRequest') is not None:
            self.notification_unicast_request_shrink = m.get('NotificationUnicastRequest')
        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')
        return self


class PushNotificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class SendNotificationsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class SendNotificationsRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SendNotificationsRequestNotificationUnicastRequestSendTarget(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SendNotificationsRequestNotificationUnicastRequest(TeaModel):
    def __init__(
        self,
        is_debug: bool = None,
        message_template_id: str = None,
        place_holder: Dict[str, str] = None,
        send_target: SendNotificationsRequestNotificationUnicastRequestSendTarget = None,
    ):
        self.is_debug = is_debug
        # This parameter is required.
        self.message_template_id = message_template_id
        self.place_holder = place_holder
        # This parameter is required.
        self.send_target = send_target

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.send_target is not None:
            result['SendTarget'] = self.send_target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('SendTarget') is not None:
            temp_model = SendNotificationsRequestNotificationUnicastRequestSendTarget()
            self.send_target = temp_model.from_map(m['SendTarget'])
        return self


class SendNotificationsRequestTenantInfo(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SendNotificationsRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class SendNotificationsRequest(TeaModel):
    def __init__(
        self,
        device_info: SendNotificationsRequestDeviceInfo = None,
        notification_unicast_request: SendNotificationsRequestNotificationUnicastRequest = None,
        tenant_info: SendNotificationsRequestTenantInfo = None,
        user_info: SendNotificationsRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.notification_unicast_request = notification_unicast_request
        self.tenant_info = tenant_info
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.notification_unicast_request:
            self.notification_unicast_request.validate()
        if self.tenant_info:
            self.tenant_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.notification_unicast_request is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request.to_map()
        if self.tenant_info is not None:
            result['TenantInfo'] = self.tenant_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = SendNotificationsRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('NotificationUnicastRequest') is not None:
            temp_model = SendNotificationsRequestNotificationUnicastRequest()
            self.notification_unicast_request = temp_model.from_map(m['NotificationUnicastRequest'])
        if m.get('TenantInfo') is not None:
            temp_model = SendNotificationsRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m['TenantInfo'])
        if m.get('UserInfo') is not None:
            temp_model = SendNotificationsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SendNotificationsShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        notification_unicast_request_shrink: str = None,
        tenant_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.notification_unicast_request_shrink = notification_unicast_request_shrink
        self.tenant_info_shrink = tenant_info_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.notification_unicast_request_shrink is not None:
            result['NotificationUnicastRequest'] = self.notification_unicast_request_shrink
        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('NotificationUnicastRequest') is not None:
            self.notification_unicast_request_shrink = m.get('NotificationUnicastRequest')
        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SendNotificationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ThirdImmediateMsgPushHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class ThirdImmediateMsgPushRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        change_detail: str = None,
        order_id: str = None,
        psg_ids: str = None,
        traffic_change_type: str = None,
        traffic_change_type_desc: str = None,
        traffic_journey_ids: str = None,
        traffic_sub_order_ids: str = None,
        user_id: str = None,
    ):
        self.biz_type = biz_type
        self.change_detail = change_detail
        self.order_id = order_id
        self.psg_ids = psg_ids
        self.traffic_change_type = traffic_change_type
        self.traffic_change_type_desc = traffic_change_type_desc
        self.traffic_journey_ids = traffic_journey_ids
        self.traffic_sub_order_ids = traffic_sub_order_ids
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.change_detail is not None:
            result['ChangeDetail'] = self.change_detail
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.psg_ids is not None:
            result['PsgIds'] = self.psg_ids
        if self.traffic_change_type is not None:
            result['TrafficChangeType'] = self.traffic_change_type
        if self.traffic_change_type_desc is not None:
            result['TrafficChangeTypeDesc'] = self.traffic_change_type_desc
        if self.traffic_journey_ids is not None:
            result['TrafficJourneyIds'] = self.traffic_journey_ids
        if self.traffic_sub_order_ids is not None:
            result['TrafficSubOrderIds'] = self.traffic_sub_order_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ChangeDetail') is not None:
            self.change_detail = m.get('ChangeDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PsgIds') is not None:
            self.psg_ids = m.get('PsgIds')
        if m.get('TrafficChangeType') is not None:
            self.traffic_change_type = m.get('TrafficChangeType')
        if m.get('TrafficChangeTypeDesc') is not None:
            self.traffic_change_type_desc = m.get('TrafficChangeTypeDesc')
        if m.get('TrafficJourneyIds') is not None:
            self.traffic_journey_ids = m.get('TrafficJourneyIds')
        if m.get('TrafficSubOrderIds') is not None:
            self.traffic_sub_order_ids = m.get('TrafficSubOrderIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ThirdImmediateMsgPushResponseBodyModel(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ThirdImmediateMsgPushResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        model: ThirdImmediateMsgPushResponseBodyModel = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.model = model
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            temp_model = ThirdImmediateMsgPushResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ThirdImmediateMsgPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ThirdImmediateMsgPushResponseBody = None,
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
            temp_model = ThirdImmediateMsgPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateReminderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class UpdateReminderRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateReminderRequestPayloadRecurrenceRule(TeaModel):
    def __init__(
        self,
        day: int = None,
        days_of_month: List[int] = None,
        days_of_week: List[int] = None,
        end_date_time: int = None,
        freq: str = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        second: int = None,
        start_date_time: int = None,
        year: int = None,
    ):
        self.day = day
        self.days_of_month = days_of_month
        self.days_of_week = days_of_week
        # This parameter is required.
        self.end_date_time = end_date_time
        # This parameter is required.
        self.freq = freq
        # This parameter is required.
        self.hour = hour
        self.minute = minute
        self.month = month
        self.second = second
        # This parameter is required.
        self.start_date_time = start_date_time
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.days_of_month is not None:
            result['DaysOfMonth'] = self.days_of_month
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.end_date_time is not None:
            result['EndDateTime'] = self.end_date_time
        if self.freq is not None:
            result['Freq'] = self.freq
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.second is not None:
            result['Second'] = self.second
        if self.start_date_time is not None:
            result['StartDateTime'] = self.start_date_time
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DaysOfMonth') is not None:
            self.days_of_month = m.get('DaysOfMonth')
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('EndDateTime') is not None:
            self.end_date_time = m.get('EndDateTime')
        if m.get('Freq') is not None:
            self.freq = m.get('Freq')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        if m.get('StartDateTime') is not None:
            self.start_date_time = m.get('StartDateTime')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class UpdateReminderRequestPayload(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        is_debug: bool = None,
        recurrence_rule: UpdateReminderRequestPayloadRecurrenceRule = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.is_debug = is_debug
        # This parameter is required.
        self.recurrence_rule = recurrence_rule

    def validate(self):
        if self.recurrence_rule:
            self.recurrence_rule.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.recurrence_rule is not None:
            result['RecurrenceRule'] = self.recurrence_rule.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('RecurrenceRule') is not None:
            temp_model = UpdateReminderRequestPayloadRecurrenceRule()
            self.recurrence_rule = temp_model.from_map(m['RecurrenceRule'])
        return self


class UpdateReminderRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class UpdateReminderRequest(TeaModel):
    def __init__(
        self,
        device_info: UpdateReminderRequestDeviceInfo = None,
        payload: UpdateReminderRequestPayload = None,
        user_info: UpdateReminderRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = UpdateReminderRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = UpdateReminderRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = UpdateReminderRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class UpdateReminderShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class UpdateReminderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: int = None,
        error_msg: str = None,
        model: int = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.model = model
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
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateReminderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateReminderResponseBody = None,
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
            temp_model = UpdateReminderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VideoAppReportHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class VideoAppReportRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class VideoAppReportRequestPayload(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        is_login: bool = None,
        is_vip: bool = None,
        login_nick: str = None,
        origin_uuid: str = None,
        phone: str = None,
        pkg_name: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.is_login = is_login
        # This parameter is required.
        self.is_vip = is_vip
        self.login_nick = login_nick
        self.origin_uuid = origin_uuid
        self.phone = phone
        # This parameter is required.
        self.pkg_name = pkg_name
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.is_login is not None:
            result['isLogin'] = self.is_login
        if self.is_vip is not None:
            result['isVip'] = self.is_vip
        if self.login_nick is not None:
            result['loginNick'] = self.login_nick
        if self.origin_uuid is not None:
            result['originUuid'] = self.origin_uuid
        if self.phone is not None:
            result['phone'] = self.phone
        if self.pkg_name is not None:
            result['pkgName'] = self.pkg_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('isLogin') is not None:
            self.is_login = m.get('isLogin')
        if m.get('isVip') is not None:
            self.is_vip = m.get('isVip')
        if m.get('loginNick') is not None:
            self.login_nick = m.get('loginNick')
        if m.get('originUuid') is not None:
            self.origin_uuid = m.get('originUuid')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('pkgName') is not None:
            self.pkg_name = m.get('pkgName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class VideoAppReportRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class VideoAppReportRequest(TeaModel):
    def __init__(
        self,
        device_info: VideoAppReportRequestDeviceInfo = None,
        payload: VideoAppReportRequestPayload = None,
        user_info: VideoAppReportRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = VideoAppReportRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = VideoAppReportRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = VideoAppReportRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class VideoAppReportShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class VideoAppReportResponseBody(TeaModel):
    def __init__(
        self,
        ret_code: int = None,
        ret_msg: str = None,
        ret_value: bool = None,
    ):
        self.ret_code = ret_code
        self.ret_msg = ret_msg
        self.ret_value = ret_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_msg is not None:
            result['RetMsg'] = self.ret_msg
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetMsg') is not None:
            self.ret_msg = m.get('RetMsg')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        return self


class VideoAppReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VideoAppReportResponseBody = None,
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
            temp_model = VideoAppReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WakeUpAppHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class WakeUpAppRequestTargetInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        organization_id: str = None,
        target_identity: str = None,
        target_type: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        self.organization_id = organization_id
        # This parameter is required.
        self.target_identity = target_identity
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class WakeUpAppRequest(TeaModel):
    def __init__(
        self,
        is_debug: bool = None,
        path: str = None,
        target_info: WakeUpAppRequestTargetInfo = None,
    ):
        self.is_debug = is_debug
        # This parameter is required.
        self.path = path
        # This parameter is required.
        self.target_info = target_info

    def validate(self):
        if self.target_info:
            self.target_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.path is not None:
            result['Path'] = self.path
        if self.target_info is not None:
            result['TargetInfo'] = self.target_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('TargetInfo') is not None:
            temp_model = WakeUpAppRequestTargetInfo()
            self.target_info = temp_model.from_map(m['TargetInfo'])
        return self


class WakeUpAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


