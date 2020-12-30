# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DoIotChgBindOrUnBindRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
        imei: str = None,
        new_imei: str = None,
        opion_type: str = None,
        mid_channel_id: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid
        self.imei = imei
        self.new_imei = new_imei
        self.opion_type = opion_type
        self.mid_channel_id = mid_channel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.imei is not None:
            result['Imei'] = self.imei
        if self.new_imei is not None:
            result['NewImei'] = self.new_imei
        if self.opion_type is not None:
            result['OpionType'] = self.opion_type
        if self.mid_channel_id is not None:
            result['MidChannelId'] = self.mid_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('Imei') is not None:
            self.imei = m.get('Imei')
        if m.get('NewImei') is not None:
            self.new_imei = m.get('NewImei')
        if m.get('OpionType') is not None:
            self.opion_type = m.get('OpionType')
        if m.get('MidChannelId') is not None:
            self.mid_channel_id = m.get('MidChannelId')
        return self


class DoIotChgBindOrUnBindResponseBodyIotModBind(TeaModel):
    def __init__(
        self,
        is_mod_success: bool = None,
    ):
        self.is_mod_success = is_mod_success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_mod_success is not None:
            result['IsModSuccess'] = self.is_mod_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsModSuccess') is not None:
            self.is_mod_success = m.get('IsModSuccess')
        return self


class DoIotChgBindOrUnBindResponseBody(TeaModel):
    def __init__(
        self,
        iot_mod_bind: DoIotChgBindOrUnBindResponseBodyIotModBind = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.iot_mod_bind = iot_mod_bind
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.iot_mod_bind:
            self.iot_mod_bind.validate()

    def to_map(self):
        result = dict()
        if self.iot_mod_bind is not None:
            result['IotModBind'] = self.iot_mod_bind.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotModBind') is not None:
            temp_model = DoIotChgBindOrUnBindResponseBodyIotModBind()
            self.iot_mod_bind = temp_model.from_map(m['IotModBind'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DoIotChgBindOrUnBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoIotChgBindOrUnBindResponseBody = None,
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
            temp_model = DoIotChgBindOrUnBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoIotIsImeiExistRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        imei: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.imei = imei

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.imei is not None:
            result['Imei'] = self.imei
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Imei') is not None:
            self.imei = m.get('Imei')
        return self


class DoIotIsImeiExistResponseBodyIotImeiExist(TeaModel):
    def __init__(
        self,
        is_imei_exist: bool = None,
    ):
        self.is_imei_exist = is_imei_exist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_imei_exist is not None:
            result['IsImeiExist'] = self.is_imei_exist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsImeiExist') is not None:
            self.is_imei_exist = m.get('IsImeiExist')
        return self


class DoIotIsImeiExistResponseBody(TeaModel):
    def __init__(
        self,
        iot_imei_exist: DoIotIsImeiExistResponseBodyIotImeiExist = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.iot_imei_exist = iot_imei_exist
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.iot_imei_exist:
            self.iot_imei_exist.validate()

    def to_map(self):
        result = dict()
        if self.iot_imei_exist is not None:
            result['IotImeiExist'] = self.iot_imei_exist.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotImeiExist') is not None:
            temp_model = DoIotIsImeiExistResponseBodyIotImeiExist()
            self.iot_imei_exist = temp_model.from_map(m['IotImeiExist'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DoIotIsImeiExistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoIotIsImeiExistResponseBody = None,
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
            temp_model = DoIotIsImeiExistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoIotPostImeiRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        imei: str = None,
        comments: str = None,
        device_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.imei = imei
        self.comments = comments
        self.device_type = device_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.imei is not None:
            result['Imei'] = self.imei
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Imei') is not None:
            self.imei = m.get('Imei')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        return self


class DoIotPostImeiResponseBodyIotPostImei(TeaModel):
    def __init__(
        self,
        is_post_success: bool = None,
    ):
        self.is_post_success = is_post_success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_post_success is not None:
            result['IsPostSuccess'] = self.is_post_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPostSuccess') is not None:
            self.is_post_success = m.get('IsPostSuccess')
        return self


class DoIotPostImeiResponseBody(TeaModel):
    def __init__(
        self,
        iot_post_imei: DoIotPostImeiResponseBodyIotPostImei = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.iot_post_imei = iot_post_imei
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.iot_post_imei:
            self.iot_post_imei.validate()

    def to_map(self):
        result = dict()
        if self.iot_post_imei is not None:
            result['IotPostImei'] = self.iot_post_imei.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotPostImei') is not None:
            temp_model = DoIotPostImeiResponseBodyIotPostImei()
            self.iot_post_imei = temp_model.from_map(m['IotPostImei'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DoIotPostImeiResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoIotPostImeiResponseBody = None,
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
            temp_model = DoIotPostImeiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoIotRechargeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
        offer_ids: str = None,
        out_id: str = None,
        amount: int = None,
        eff_code: str = None,
        order_num: int = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid
        self.offer_ids = offer_ids
        self.out_id = out_id
        self.amount = amount
        self.eff_code = eff_code
        self.order_num = order_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.offer_ids is not None:
            result['OfferIds'] = self.offer_ids
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.eff_code is not None:
            result['EffCode'] = self.eff_code
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OfferIds') is not None:
            self.offer_ids = m.get('OfferIds')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EffCode') is not None:
            self.eff_code = m.get('EffCode')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        return self


class DoIotRechargeResponseBodyIotRecharge(TeaModel):
    def __init__(
        self,
        order_no: str = None,
        done_code: str = None,
        order_result: str = None,
    ):
        self.order_no = order_no
        self.done_code = done_code
        self.order_result = order_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_no is not None:
            result['OrderNo'] = self.order_no
        if self.done_code is not None:
            result['DoneCode'] = self.done_code
        if self.order_result is not None:
            result['OrderResult'] = self.order_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderNo') is not None:
            self.order_no = m.get('OrderNo')
        if m.get('DoneCode') is not None:
            self.done_code = m.get('DoneCode')
        if m.get('OrderResult') is not None:
            self.order_result = m.get('OrderResult')
        return self


class DoIotRechargeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        iot_recharge: DoIotRechargeResponseBodyIotRecharge = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.iot_recharge = iot_recharge
        self.code = code

    def validate(self):
        if self.iot_recharge:
            self.iot_recharge.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.iot_recharge is not None:
            result['IotRecharge'] = self.iot_recharge.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IotRecharge') is not None:
            temp_model = DoIotRechargeResponseBodyIotRecharge()
            self.iot_recharge = temp_model.from_map(m['IotRecharge'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DoIotRechargeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoIotRechargeResponseBody = None,
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
            temp_model = DoIotRechargeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoIotSetAbsoluteRemindConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        biz_type: str = None,
        biz_id: str = None,
        config_info: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.config_info = config_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.config_info is not None:
            result['ConfigInfo'] = self.config_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ConfigInfo') is not None:
            self.config_info = m.get('ConfigInfo')
        return self


class DoIotSetAbsoluteRemindConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DoIotSetAbsoluteRemindConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoIotSetAbsoluteRemindConfigResponseBody = None,
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
            temp_model = DoIotSetAbsoluteRemindConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoIotSetRemindConfigRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        biz_type: str = None,
        biz_id: str = None,
        operation_type: str = None,
        config_info: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.biz_type = biz_type
        self.biz_id = biz_id
        self.operation_type = operation_type
        self.config_info = config_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.config_info is not None:
            result['ConfigInfo'] = self.config_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('ConfigInfo') is not None:
            self.config_info = m.get('ConfigInfo')
        return self


class DoIotSetRemindConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DoIotSetRemindConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoIotSetRemindConfigResponseBody = None,
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
            temp_model = DoIotSetRemindConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoIotUnbindResumeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class DoIotUnbindResumeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: bool = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DoIotUnbindResumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoIotUnbindResumeResponseBody = None,
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
            temp_model = DoIotUnbindResumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoIotUserStopResumeRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
        option_type: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid
        self.option_type = option_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.option_type is not None:
            result['OptionType'] = self.option_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('OptionType') is not None:
            self.option_type = m.get('OptionType')
        return self


class DoIotUserStopResumeResponseBodyResult(TeaModel):
    def __init__(
        self,
        control_result: bool = None,
    ):
        self.control_result = control_result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.control_result is not None:
            result['ControlResult'] = self.control_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlResult') is not None:
            self.control_result = m.get('ControlResult')
        return self


class DoIotUserStopResumeResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        result: DoIotUserStopResumeResponseBodyResult = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Result') is not None:
            temp_model = DoIotUserStopResumeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class DoIotUserStopResumeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoIotUserStopResumeResponseBody = None,
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
            temp_model = DoIotUserStopResumeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoSendIotSmsRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        template_code: str = None,
        phone_numbers: str = None,
        template_param: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.sign_name = sign_name
        self.template_code = template_code
        self.phone_numbers = phone_numbers
        self.template_param = template_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers
        if self.template_param is not None:
            result['TemplateParam'] = self.template_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')
        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')
        return self


class DoSendIotSmsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        module: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.module = module
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.module is not None:
            result['Module'] = self.module
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class DoSendIotSmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DoSendIotSmsResponseBody = None,
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
            temp_model = DoSendIotSmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardFlowInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class QueryCardFlowInfoResponseBodyCardFlowInfosCardFlowInfo(TeaModel):
    def __init__(
        self,
        valid_date: str = None,
        voice_used: int = None,
        resource_type: str = None,
        flow_used: int = None,
        voice_total: int = None,
        expire_date: str = None,
        sms_used: int = None,
        rest_of_flow: int = None,
        flow_resource: int = None,
        res_name: str = None,
    ):
        self.valid_date = valid_date
        self.voice_used = voice_used
        self.resource_type = resource_type
        self.flow_used = flow_used
        self.voice_total = voice_total
        self.expire_date = expire_date
        self.sms_used = sms_used
        self.rest_of_flow = rest_of_flow
        self.flow_resource = flow_resource
        self.res_name = res_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.valid_date is not None:
            result['ValidDate'] = self.valid_date
        if self.voice_used is not None:
            result['VoiceUsed'] = self.voice_used
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.flow_used is not None:
            result['FlowUsed'] = self.flow_used
        if self.voice_total is not None:
            result['VoiceTotal'] = self.voice_total
        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date
        if self.sms_used is not None:
            result['SmsUsed'] = self.sms_used
        if self.rest_of_flow is not None:
            result['RestOfFlow'] = self.rest_of_flow
        if self.flow_resource is not None:
            result['FlowResource'] = self.flow_resource
        if self.res_name is not None:
            result['ResName'] = self.res_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ValidDate') is not None:
            self.valid_date = m.get('ValidDate')
        if m.get('VoiceUsed') is not None:
            self.voice_used = m.get('VoiceUsed')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('FlowUsed') is not None:
            self.flow_used = m.get('FlowUsed')
        if m.get('VoiceTotal') is not None:
            self.voice_total = m.get('VoiceTotal')
        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')
        if m.get('SmsUsed') is not None:
            self.sms_used = m.get('SmsUsed')
        if m.get('RestOfFlow') is not None:
            self.rest_of_flow = m.get('RestOfFlow')
        if m.get('FlowResource') is not None:
            self.flow_resource = m.get('FlowResource')
        if m.get('ResName') is not None:
            self.res_name = m.get('ResName')
        return self


class QueryCardFlowInfoResponseBodyCardFlowInfos(TeaModel):
    def __init__(
        self,
        card_flow_info: List[QueryCardFlowInfoResponseBodyCardFlowInfosCardFlowInfo] = None,
    ):
        self.card_flow_info = card_flow_info

    def validate(self):
        if self.card_flow_info:
            for k in self.card_flow_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CardFlowInfo'] = []
        if self.card_flow_info is not None:
            for k in self.card_flow_info:
                result['CardFlowInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_flow_info = []
        if m.get('CardFlowInfo') is not None:
            for k in m.get('CardFlowInfo'):
                temp_model = QueryCardFlowInfoResponseBodyCardFlowInfosCardFlowInfo()
                self.card_flow_info.append(temp_model.from_map(k))
        return self


class QueryCardFlowInfoResponseBody(TeaModel):
    def __init__(
        self,
        card_flow_infos: QueryCardFlowInfoResponseBodyCardFlowInfos = None,
        message: str = None,
        request_id: str = None,
        code: str = None,
    ):
        self.card_flow_infos = card_flow_infos
        self.message = message
        self.request_id = request_id
        self.code = code

    def validate(self):
        if self.card_flow_infos:
            self.card_flow_infos.validate()

    def to_map(self):
        result = dict()
        if self.card_flow_infos is not None:
            result['CardFlowInfos'] = self.card_flow_infos.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardFlowInfos') is not None:
            temp_model = QueryCardFlowInfoResponseBodyCardFlowInfos()
            self.card_flow_infos = temp_model.from_map(m['CardFlowInfos'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryCardFlowInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCardFlowInfoResponseBody = None,
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
            temp_model = QueryCardFlowInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardHistoryFlowInfoRequest(TeaModel):
    def __init__(
        self,
        iccid: str = None,
        start_time: str = None,
        end_time: str = None,
    ):
        self.iccid = iccid
        self.start_time = start_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QueryCardHistoryFlowInfoResponseBodyDataDayUsageList(TeaModel):
    def __init__(
        self,
        day: int = None,
        value: int = None,
    ):
        self.day = day
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryCardHistoryFlowInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        day_usage_list: List[QueryCardHistoryFlowInfoResponseBodyDataDayUsageList] = None,
        month: int = None,
        cur_value: int = None,
    ):
        self.day_usage_list = day_usage_list
        self.month = month
        self.cur_value = cur_value

    def validate(self):
        if self.day_usage_list:
            for k in self.day_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DayUsageList'] = []
        if self.day_usage_list is not None:
            for k in self.day_usage_list:
                result['DayUsageList'].append(k.to_map() if k else None)
        if self.month is not None:
            result['Month'] = self.month
        if self.cur_value is not None:
            result['CurValue'] = self.cur_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.day_usage_list = []
        if m.get('DayUsageList') is not None:
            for k in m.get('DayUsageList'):
                temp_model = QueryCardHistoryFlowInfoResponseBodyDataDayUsageList()
                self.day_usage_list.append(temp_model.from_map(k))
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('CurValue') is not None:
            self.cur_value = m.get('CurValue')
        return self


class QueryCardHistoryFlowInfoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: List[QueryCardHistoryFlowInfoResponseBodyData] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryCardHistoryFlowInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCardHistoryFlowInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCardHistoryFlowInfoResponseBody = None,
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
            temp_model = QueryCardHistoryFlowInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class QueryCardInfoResponseBodyCardInfo(TeaModel):
    def __init__(
        self,
        imsi: str = None,
        msisdn: str = None,
        gprs_status: str = None,
        voice_status: str = None,
        sms_status: str = None,
        iccid: str = None,
        first_active_time: str = None,
        open_time: str = None,
    ):
        self.imsi = imsi
        self.msisdn = msisdn
        self.gprs_status = gprs_status
        self.voice_status = voice_status
        self.sms_status = sms_status
        self.iccid = iccid
        self.first_active_time = first_active_time
        self.open_time = open_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.gprs_status is not None:
            result['GprsStatus'] = self.gprs_status
        if self.voice_status is not None:
            result['VoiceStatus'] = self.voice_status
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.first_active_time is not None:
            result['FirstActiveTime'] = self.first_active_time
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('GprsStatus') is not None:
            self.gprs_status = m.get('GprsStatus')
        if m.get('VoiceStatus') is not None:
            self.voice_status = m.get('VoiceStatus')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('FirstActiveTime') is not None:
            self.first_active_time = m.get('FirstActiveTime')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        return self


class QueryCardInfoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        card_info: QueryCardInfoResponseBodyCardInfo = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.card_info = card_info
        self.code = code

    def validate(self):
        if self.card_info:
            self.card_info.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.card_info is not None:
            result['CardInfo'] = self.card_info.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CardInfo') is not None:
            temp_model = QueryCardInfoResponseBodyCardInfo()
            self.card_info = temp_model.from_map(m['CardInfo'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryCardInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCardInfoResponseBody = None,
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
            temp_model = QueryCardInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardsInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class QueryCardsInfoResponseBodyCardsInfo(TeaModel):
    def __init__(
        self,
        imsi: str = None,
        msisdn: str = None,
        gprs_status: str = None,
        voice_status: str = None,
        sms_status: str = None,
        iccid: str = None,
        first_active_time: str = None,
        open_time: str = None,
    ):
        self.imsi = imsi
        self.msisdn = msisdn
        self.gprs_status = gprs_status
        self.voice_status = voice_status
        self.sms_status = sms_status
        self.iccid = iccid
        self.first_active_time = first_active_time
        self.open_time = open_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.gprs_status is not None:
            result['GprsStatus'] = self.gprs_status
        if self.voice_status is not None:
            result['VoiceStatus'] = self.voice_status
        if self.sms_status is not None:
            result['SmsStatus'] = self.sms_status
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        if self.first_active_time is not None:
            result['FirstActiveTime'] = self.first_active_time
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('GprsStatus') is not None:
            self.gprs_status = m.get('GprsStatus')
        if m.get('VoiceStatus') is not None:
            self.voice_status = m.get('VoiceStatus')
        if m.get('SmsStatus') is not None:
            self.sms_status = m.get('SmsStatus')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        if m.get('FirstActiveTime') is not None:
            self.first_active_time = m.get('FirstActiveTime')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        return self


class QueryCardsInfoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        cards_info: List[QueryCardsInfoResponseBodyCardsInfo] = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.cards_info = cards_info
        self.code = code

    def validate(self):
        if self.cards_info:
            for k in self.cards_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CardsInfo'] = []
        if self.cards_info is not None:
            for k in self.cards_info:
                result['CardsInfo'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.cards_info = []
        if m.get('CardsInfo') is not None:
            for k in m.get('CardsInfo'):
                temp_model = QueryCardsInfoResponseBodyCardsInfo()
                self.cards_info.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryCardsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCardsInfoResponseBody = None,
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
            temp_model = QueryCardsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCardStatusRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class QueryCardStatusResponseBodyCardStatus(TeaModel):
    def __init__(
        self,
        msisdn: str = None,
        user_status: str = None,
        iccid: str = None,
    ):
        self.msisdn = msisdn
        self.user_status = user_status
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.msisdn is not None:
            result['Msisdn'] = self.msisdn
        if self.user_status is not None:
            result['UserStatus'] = self.user_status
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msisdn') is not None:
            self.msisdn = m.get('Msisdn')
        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class QueryCardStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        card_status: QueryCardStatusResponseBodyCardStatus = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.card_status = card_status
        self.code = code

    def validate(self):
        if self.card_status:
            self.card_status.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.card_status is not None:
            result['CardStatus'] = self.card_status.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CardStatus') is not None:
            temp_model = QueryCardStatusResponseBodyCardStatus()
            self.card_status = temp_model.from_map(m['CardStatus'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryCardStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryCardStatusResponseBody = None,
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
            temp_model = QueryCardStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryIotCardOfferDtlRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class QueryIotCardOfferDtlResponseBodyCardOfferDetailDetail(TeaModel):
    def __init__(
        self,
        effective_time: str = None,
        offer_id: str = None,
        offer_name: str = None,
        expire_time: str = None,
        order_time: str = None,
    ):
        self.effective_time = effective_time
        self.offer_id = offer_id
        self.offer_name = offer_name
        self.expire_time = expire_time
        self.order_time = order_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.offer_id is not None:
            result['OfferId'] = self.offer_id
        if self.offer_name is not None:
            result['OfferName'] = self.offer_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.order_time is not None:
            result['OrderTime'] = self.order_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('OfferId') is not None:
            self.offer_id = m.get('OfferId')
        if m.get('OfferName') is not None:
            self.offer_name = m.get('OfferName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('OrderTime') is not None:
            self.order_time = m.get('OrderTime')
        return self


class QueryIotCardOfferDtlResponseBodyCardOfferDetail(TeaModel):
    def __init__(
        self,
        detail: List[QueryIotCardOfferDtlResponseBodyCardOfferDetailDetail] = None,
    ):
        self.detail = detail

    def validate(self):
        if self.detail:
            for k in self.detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['detail'] = []
        if self.detail is not None:
            for k in self.detail:
                result['detail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail = []
        if m.get('detail') is not None:
            for k in m.get('detail'):
                temp_model = QueryIotCardOfferDtlResponseBodyCardOfferDetailDetail()
                self.detail.append(temp_model.from_map(k))
        return self


class QueryIotCardOfferDtlResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        card_offer_detail: QueryIotCardOfferDtlResponseBodyCardOfferDetail = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.card_offer_detail = card_offer_detail
        self.code = code

    def validate(self):
        if self.card_offer_detail:
            self.card_offer_detail.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.card_offer_detail is not None:
            result['CardOfferDetail'] = self.card_offer_detail.to_map()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CardOfferDetail') is not None:
            temp_model = QueryIotCardOfferDtlResponseBodyCardOfferDetail()
            self.card_offer_detail = temp_model.from_map(m['CardOfferDetail'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryIotCardOfferDtlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryIotCardOfferDtlResponseBody = None,
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
            temp_model = QueryIotCardOfferDtlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPersonalInfoRequest(TeaModel):
    def __init__(
        self,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        iccid: str = None,
    ):
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.iccid = iccid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.iccid is not None:
            result['Iccid'] = self.iccid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Iccid') is not None:
            self.iccid = m.get('Iccid')
        return self


class QueryPersonalInfoResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        module: str = None,
        code: str = None,
    ):
        self.message = message
        self.request_id = request_id
        self.module = module
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.module is not None:
            result['Module'] = self.module
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class QueryPersonalInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryPersonalInfoResponseBody = None,
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
            temp_model = QueryPersonalInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


