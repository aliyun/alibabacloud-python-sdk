# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class AddAddressRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        third_party_user_id: str = None,
        use_anonymous_tb_account: bool = None,
        address_info: str = None,
    ):
        self.biz_id = biz_id
        self.third_party_user_id = third_party_user_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.address_info = address_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('AddressInfo') is not None:
            self.address_info = m.get('AddressInfo')
        return self


class AddAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        address_id: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.address_id = address_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        return self


class AddAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddAddressResponseBody = None,
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
            temp_model = AddAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddItemLimitRuleRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_code: str = None,
        lm_activity_id: int = None,
        lm_item_id: str = None,
        item_id: int = None,
        upper_num: int = None,
        rule_type: int = None,
        begin_time: int = None,
        end_time: int = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_code = sub_biz_code
        self.lm_activity_id = lm_activity_id
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.upper_num = upper_num
        self.rule_type = rule_type
        self.begin_time = begin_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.upper_num is not None:
            result['UpperNum'] = self.upper_num
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('UpperNum') is not None:
            self.upper_num = m.get('UpperNum')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class AddItemLimitRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        model: int = None,
        message: str = None,
        request_id: str = None,
        rule_id: int = None,
    ):
        self.code = code
        self.model = model
        self.message = message
        self.request_id = request_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.model is not None:
            result['Model'] = self.model
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class AddItemLimitRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddItemLimitRuleResponseBody = None,
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
            temp_model = AddItemLimitRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddItemToSubBizsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        item_id: int = None,
        lm_item_id: str = None,
        sub_biz_ids: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.sub_biz_ids = sub_biz_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.sub_biz_ids is not None:
            result['SubBizIds'] = self.sub_biz_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SubBizIds') is not None:
            self.sub_biz_ids = m.get('SubBizIds')
        return self


class AddItemToSubBizsShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        item_id: int = None,
        lm_item_id: str = None,
        sub_biz_ids_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.sub_biz_ids_shrink = sub_biz_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.sub_biz_ids_shrink is not None:
            result['SubBizIds'] = self.sub_biz_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SubBizIds') is not None:
            self.sub_biz_ids_shrink = m.get('SubBizIds')
        return self


class AddItemToSubBizsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddItemToSubBizsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddItemToSubBizsResponseBody = None,
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
            temp_model = AddItemToSubBizsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSupplierNewItemsRequestItemList(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        sku_list: List[int] = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.sku_list = sku_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_list is not None:
            result['SkuList'] = self.sku_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuList') is not None:
            self.sku_list = m.get('SkuList')
        return self


class AddSupplierNewItemsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        item_list: List[AddSupplierNewItemsRequestItemList] = None,
    ):
        self.biz_id = biz_id
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = AddSupplierNewItemsRequestItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class AddSupplierNewItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddSupplierNewItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSupplierNewItemsResponseBody = None,
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
            temp_model = AddSupplierNewItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyRefundRequestLeavePictureList(TeaModel):
    def __init__(
        self,
        picture: str = None,
        desc: str = None,
    ):
        self.picture = picture
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.picture is not None:
            result['Picture'] = self.picture
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Picture') is not None:
            self.picture = m.get('Picture')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class ApplyRefundRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        sub_lm_order_id: str = None,
        biz_claim_type: int = None,
        apply_refund_fee: int = None,
        apply_refund_count: int = None,
        apply_reason_text_id: int = None,
        leave_message: str = None,
        goods_status: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
        leave_picture_list: List[ApplyRefundRequestLeavePictureList] = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.sub_lm_order_id = sub_lm_order_id
        self.biz_claim_type = biz_claim_type
        self.apply_refund_fee = apply_refund_fee
        self.apply_refund_count = apply_refund_count
        self.apply_reason_text_id = apply_reason_text_id
        self.leave_message = leave_message
        self.goods_status = goods_status
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type
        self.leave_picture_list = leave_picture_list

    def validate(self):
        if self.leave_picture_list:
            for k in self.leave_picture_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.apply_refund_fee is not None:
            result['ApplyRefundFee'] = self.apply_refund_fee
        if self.apply_refund_count is not None:
            result['ApplyRefundCount'] = self.apply_refund_count
        if self.apply_reason_text_id is not None:
            result['ApplyReasonTextId'] = self.apply_reason_text_id
        if self.leave_message is not None:
            result['LeaveMessage'] = self.leave_message
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        result['LeavePictureList'] = []
        if self.leave_picture_list is not None:
            for k in self.leave_picture_list:
                result['LeavePictureList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('ApplyRefundFee') is not None:
            self.apply_refund_fee = m.get('ApplyRefundFee')
        if m.get('ApplyRefundCount') is not None:
            self.apply_refund_count = m.get('ApplyRefundCount')
        if m.get('ApplyReasonTextId') is not None:
            self.apply_reason_text_id = m.get('ApplyReasonTextId')
        if m.get('LeaveMessage') is not None:
            self.leave_message = m.get('LeaveMessage')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        self.leave_picture_list = []
        if m.get('LeavePictureList') is not None:
            for k in m.get('LeavePictureList'):
                temp_model = ApplyRefundRequestLeavePictureList()
                self.leave_picture_list.append(temp_model.from_map(k))
        return self


class ApplyRefundResponseBodyRefundApplicationData(TeaModel):
    def __init__(
        self,
        dispute_type: int = None,
        sub_lm_order_id: str = None,
        dispute_status: int = None,
    ):
        self.dispute_type = dispute_type
        self.sub_lm_order_id = sub_lm_order_id
        self.dispute_status = dispute_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        return self


class ApplyRefundResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        refund_application_data: ApplyRefundResponseBodyRefundApplicationData = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.refund_application_data = refund_application_data

    def validate(self):
        if self.refund_application_data:
            self.refund_application_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refund_application_data is not None:
            result['RefundApplicationData'] = self.refund_application_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefundApplicationData') is not None:
            temp_model = ApplyRefundResponseBodyRefundApplicationData()
            self.refund_application_data = temp_model.from_map(m['RefundApplicationData'])
        return self


class ApplyRefundResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyRefundResponseBody = None,
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
            temp_model = ApplyRefundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchRegistAnonymousTbAccountRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        id_json_list: str = None,
    ):
        self.biz_id = biz_id
        self.id_json_list = id_json_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.id_json_list is not None:
            result['IdJsonList'] = self.id_json_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('IdJsonList') is not None:
            self.id_json_list = m.get('IdJsonList')
        return self


class BatchRegistAnonymousTbAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        batch_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.batch_id = batch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class BatchRegistAnonymousTbAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchRegistAnonymousTbAccountResponseBody = None,
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
            temp_model = BatchRegistAnonymousTbAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        lm_order_id: str = None,
        account_type: str = None,
        third_party_user_id: str = None,
        use_anonymous_tb_account: bool = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.lm_order_id = lm_order_id
        self.account_type = account_type
        self.third_party_user_id = third_party_user_id
        self.use_anonymous_tb_account = use_anonymous_tb_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        return self


class CancelOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        logs_id: str = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.logs_id = logs_id

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
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        return self


class CancelOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelOrderResponseBody = None,
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
            temp_model = CancelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRefundRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        sub_lm_order_id: str = None,
        dispute_id: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.sub_lm_order_id = sub_lm_order_id
        self.dispute_id = dispute_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class CancelRefundResponseBodyRefundApplicationData(TeaModel):
    def __init__(
        self,
        dispute_type: int = None,
        sub_lm_order_id: str = None,
        dispute_status: int = None,
    ):
        self.dispute_type = dispute_type
        self.sub_lm_order_id = sub_lm_order_id
        self.dispute_status = dispute_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        return self


class CancelRefundResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        refund_application_data: CancelRefundResponseBodyRefundApplicationData = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.refund_application_data = refund_application_data

    def validate(self):
        if self.refund_application_data:
            self.refund_application_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refund_application_data is not None:
            result['RefundApplicationData'] = self.refund_application_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefundApplicationData') is not None:
            temp_model = CancelRefundResponseBodyRefundApplicationData()
            self.refund_application_data = temp_model.from_map(m['RefundApplicationData'])
        return self


class CancelRefundResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelRefundResponseBody = None,
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
            temp_model = CancelRefundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmDisburseRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        lm_order_id: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.lm_order_id = lm_order_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class ConfirmDisburseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfirmDisburseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConfirmDisburseResponseBody = None,
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
            temp_model = ConfirmDisburseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMovieTicketOrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        out_trade_id: str = None,
        lock_seat_app_key: str = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.out_trade_id = out_trade_id
        self.lock_seat_app_key = lock_seat_app_key
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.out_trade_id is not None:
            result['OutTradeId'] = self.out_trade_id
        if self.lock_seat_app_key is not None:
            result['LockSeatAppKey'] = self.lock_seat_app_key
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('OutTradeId') is not None:
            self.out_trade_id = m.get('OutTradeId')
        if m.get('LockSeatAppKey') is not None:
            self.lock_seat_app_key = m.get('LockSeatAppKey')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class CreateMovieTicketOrderResponseBodyModelPayTradeIds(TeaModel):
    def __init__(
        self,
        pay_trade_ids: List[str] = None,
    ):
        self.pay_trade_ids = pay_trade_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayTradeIds') is not None:
            self.pay_trade_ids = m.get('PayTradeIds')
        return self


class CreateMovieTicketOrderResponseBodyModelOrderIds(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateMovieTicketOrderResponseBodyModel(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        pay_trade_ids: CreateMovieTicketOrderResponseBodyModelPayTradeIds = None,
        order_ids: CreateMovieTicketOrderResponseBodyModelOrderIds = None,
    ):
        self.redirect_url = redirect_url
        self.pay_trade_ids = pay_trade_ids
        self.order_ids = order_ids

    def validate(self):
        if self.pay_trade_ids:
            self.pay_trade_ids.validate()
        if self.order_ids:
            self.order_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids.to_map()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')
        if m.get('PayTradeIds') is not None:
            temp_model = CreateMovieTicketOrderResponseBodyModelPayTradeIds()
            self.pay_trade_ids = temp_model.from_map(m['PayTradeIds'])
        if m.get('OrderIds') is not None:
            temp_model = CreateMovieTicketOrderResponseBodyModelOrderIds()
            self.order_ids = temp_model.from_map(m['OrderIds'])
        return self


class CreateMovieTicketOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: CreateMovieTicketOrderResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = CreateMovieTicketOrderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class CreateMovieTicketOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMovieTicketOrderResponseBody = None,
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
            temp_model = CreateMovieTicketOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequestItemList(TeaModel):
    def __init__(
        self,
        sku_id: int = None,
        lm_item_id: str = None,
        item_id: int = None,
        quantity: int = None,
    ):
        self.sku_id = sku_id
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        out_trade_id: str = None,
        item_id: int = None,
        quantity: int = None,
        total_amount: int = None,
        ext_json: str = None,
        delivery_address: str = None,
        order_expire_time: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
        lm_item_id: str = None,
        buyer_message_map: str = None,
        item_list: List[CreateOrderRequestItemList] = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.out_trade_id = out_trade_id
        self.item_id = item_id
        self.quantity = quantity
        self.total_amount = total_amount
        self.ext_json = ext_json
        self.delivery_address = delivery_address
        self.order_expire_time = order_expire_time
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type
        self.lm_item_id = lm_item_id
        self.buyer_message_map = buyer_message_map
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.out_trade_id is not None:
            result['OutTradeId'] = self.out_trade_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.order_expire_time is not None:
            result['OrderExpireTime'] = self.order_expire_time
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.buyer_message_map is not None:
            result['BuyerMessageMap'] = self.buyer_message_map
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('OutTradeId') is not None:
            self.out_trade_id = m.get('OutTradeId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('OrderExpireTime') is not None:
            self.order_expire_time = m.get('OrderExpireTime')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('BuyerMessageMap') is not None:
            self.buyer_message_map = m.get('BuyerMessageMap')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = CreateOrderRequestItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class CreateOrderResponseBodyModelLmOrderListLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: str = None,
    ):
        self.lm_order_id = lm_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        return self


class CreateOrderResponseBodyModelLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_list: List[CreateOrderResponseBodyModelLmOrderListLmOrderList] = None,
    ):
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.lm_order_list:
            for k in self.lm_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmOrderList'] = []
        if self.lm_order_list is not None:
            for k in self.lm_order_list:
                result['LmOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_order_list = []
        if m.get('LmOrderList') is not None:
            for k in m.get('LmOrderList'):
                temp_model = CreateOrderResponseBodyModelLmOrderListLmOrderList()
                self.lm_order_list.append(temp_model.from_map(k))
        return self


class CreateOrderResponseBodyModelPayTradeIds(TeaModel):
    def __init__(
        self,
        pay_trade_ids: List[str] = None,
    ):
        self.pay_trade_ids = pay_trade_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayTradeIds') is not None:
            self.pay_trade_ids = m.get('PayTradeIds')
        return self


class CreateOrderResponseBodyModelOrderIds(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateOrderResponseBodyModel(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        lm_order_list: CreateOrderResponseBodyModelLmOrderList = None,
        pay_trade_ids: CreateOrderResponseBodyModelPayTradeIds = None,
        order_ids: CreateOrderResponseBodyModelOrderIds = None,
    ):
        self.redirect_url = redirect_url
        self.lm_order_list = lm_order_list
        self.pay_trade_ids = pay_trade_ids
        self.order_ids = order_ids

    def validate(self):
        if self.lm_order_list:
            self.lm_order_list.validate()
        if self.pay_trade_ids:
            self.pay_trade_ids.validate()
        if self.order_ids:
            self.order_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url
        if self.lm_order_list is not None:
            result['LmOrderList'] = self.lm_order_list.to_map()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids.to_map()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')
        if m.get('LmOrderList') is not None:
            temp_model = CreateOrderResponseBodyModelLmOrderList()
            self.lm_order_list = temp_model.from_map(m['LmOrderList'])
        if m.get('PayTradeIds') is not None:
            temp_model = CreateOrderResponseBodyModelPayTradeIds()
            self.pay_trade_ids = temp_model.from_map(m['PayTradeIds'])
        if m.get('OrderIds') is not None:
            temp_model = CreateOrderResponseBodyModelOrderIds()
            self.order_ids = temp_model.from_map(m['OrderIds'])
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: CreateOrderResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = CreateOrderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderResponseBody = None,
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderV2RequestItemList(TeaModel):
    def __init__(
        self,
        sku_id: int = None,
        lm_item_id: str = None,
        item_id: int = None,
        quantity: int = None,
    ):
        self.sku_id = sku_id
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class CreateOrderV2Request(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        out_trade_id: str = None,
        item_id: int = None,
        quantity: int = None,
        total_amount: int = None,
        ext_json: str = None,
        delivery_address: str = None,
        order_expire_time: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
        lm_item_id: str = None,
        buyer_message_map: str = None,
        item_list: List[CreateOrderV2RequestItemList] = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.out_trade_id = out_trade_id
        self.item_id = item_id
        self.quantity = quantity
        self.total_amount = total_amount
        self.ext_json = ext_json
        self.delivery_address = delivery_address
        self.order_expire_time = order_expire_time
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type
        self.lm_item_id = lm_item_id
        self.buyer_message_map = buyer_message_map
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.out_trade_id is not None:
            result['OutTradeId'] = self.out_trade_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.order_expire_time is not None:
            result['OrderExpireTime'] = self.order_expire_time
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.buyer_message_map is not None:
            result['BuyerMessageMap'] = self.buyer_message_map
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('OutTradeId') is not None:
            self.out_trade_id = m.get('OutTradeId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('OrderExpireTime') is not None:
            self.order_expire_time = m.get('OrderExpireTime')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('BuyerMessageMap') is not None:
            self.buyer_message_map = m.get('BuyerMessageMap')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = CreateOrderV2RequestItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class CreateOrderV2ResponseBodyModelLmOrderListLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: str = None,
    ):
        self.lm_order_id = lm_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        return self


class CreateOrderV2ResponseBodyModelLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_list: List[CreateOrderV2ResponseBodyModelLmOrderListLmOrderList] = None,
    ):
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.lm_order_list:
            for k in self.lm_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmOrderList'] = []
        if self.lm_order_list is not None:
            for k in self.lm_order_list:
                result['LmOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_order_list = []
        if m.get('LmOrderList') is not None:
            for k in m.get('LmOrderList'):
                temp_model = CreateOrderV2ResponseBodyModelLmOrderListLmOrderList()
                self.lm_order_list.append(temp_model.from_map(k))
        return self


class CreateOrderV2ResponseBodyModelPayTradeIds(TeaModel):
    def __init__(
        self,
        pay_trade_ids: List[str] = None,
    ):
        self.pay_trade_ids = pay_trade_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayTradeIds') is not None:
            self.pay_trade_ids = m.get('PayTradeIds')
        return self


class CreateOrderV2ResponseBodyModelOrderIds(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateOrderV2ResponseBodyModel(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        lm_order_list: CreateOrderV2ResponseBodyModelLmOrderList = None,
        pay_trade_ids: CreateOrderV2ResponseBodyModelPayTradeIds = None,
        order_ids: CreateOrderV2ResponseBodyModelOrderIds = None,
    ):
        self.redirect_url = redirect_url
        self.lm_order_list = lm_order_list
        self.pay_trade_ids = pay_trade_ids
        self.order_ids = order_ids

    def validate(self):
        if self.lm_order_list:
            self.lm_order_list.validate()
        if self.pay_trade_ids:
            self.pay_trade_ids.validate()
        if self.order_ids:
            self.order_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url
        if self.lm_order_list is not None:
            result['LmOrderList'] = self.lm_order_list.to_map()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids.to_map()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')
        if m.get('LmOrderList') is not None:
            temp_model = CreateOrderV2ResponseBodyModelLmOrderList()
            self.lm_order_list = temp_model.from_map(m['LmOrderList'])
        if m.get('PayTradeIds') is not None:
            temp_model = CreateOrderV2ResponseBodyModelPayTradeIds()
            self.pay_trade_ids = temp_model.from_map(m['PayTradeIds'])
        if m.get('OrderIds') is not None:
            temp_model = CreateOrderV2ResponseBodyModelOrderIds()
            self.order_ids = temp_model.from_map(m['OrderIds'])
        return self


class CreateOrderV2ResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: CreateOrderV2ResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = CreateOrderV2ResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class CreateOrderV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOrderV2ResponseBody = None,
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
            temp_model = CreateOrderV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePayUrlRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        buy_info: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.buy_info = buy_info
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.buy_info is not None:
            result['BuyInfo'] = self.buy_info
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('BuyInfo') is not None:
            self.buy_info = m.get('BuyInfo')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        return self


class CreatePayUrlResponseBodyModel(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        pay_trade_ids: List[str] = None,
        lm_order_list: List[str] = None,
        order_ids: List[str] = None,
    ):
        self.redirect_url = redirect_url
        self.pay_trade_ids = pay_trade_ids
        self.lm_order_list = lm_order_list
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids
        if self.lm_order_list is not None:
            result['LmOrderList'] = self.lm_order_list
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')
        if m.get('PayTradeIds') is not None:
            self.pay_trade_ids = m.get('PayTradeIds')
        if m.get('LmOrderList') is not None:
            self.lm_order_list = m.get('LmOrderList')
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreatePayUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        model: CreatePayUrlResponseBodyModel = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Model') is not None:
            temp_model = CreatePayUrlResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class CreatePayUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreatePayUrlResponseBody = None,
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
            temp_model = CreatePayUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVirtualProductOrderRequestItemList(TeaModel):
    def __init__(
        self,
        sku_id: int = None,
        lm_item_id: str = None,
        item_id: int = None,
        quantity: int = None,
    ):
        self.sku_id = sku_id
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class CreateVirtualProductOrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        out_trade_id: str = None,
        item_id: int = None,
        quantity: int = None,
        total_amount: int = None,
        ext_json: str = None,
        delivery_address: str = None,
        order_expire_time: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
        lm_item_id: str = None,
        item_list: List[CreateVirtualProductOrderRequestItemList] = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.out_trade_id = out_trade_id
        self.item_id = item_id
        self.quantity = quantity
        self.total_amount = total_amount
        self.ext_json = ext_json
        self.delivery_address = delivery_address
        self.order_expire_time = order_expire_time
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type
        self.lm_item_id = lm_item_id
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.out_trade_id is not None:
            result['OutTradeId'] = self.out_trade_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.order_expire_time is not None:
            result['OrderExpireTime'] = self.order_expire_time
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('OutTradeId') is not None:
            self.out_trade_id = m.get('OutTradeId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('OrderExpireTime') is not None:
            self.order_expire_time = m.get('OrderExpireTime')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = CreateVirtualProductOrderRequestItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class CreateVirtualProductOrderResponseBodyModelLmOrderListLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: str = None,
    ):
        self.lm_order_id = lm_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        return self


class CreateVirtualProductOrderResponseBodyModelLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_list: List[CreateVirtualProductOrderResponseBodyModelLmOrderListLmOrderList] = None,
    ):
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.lm_order_list:
            for k in self.lm_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmOrderList'] = []
        if self.lm_order_list is not None:
            for k in self.lm_order_list:
                result['LmOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_order_list = []
        if m.get('LmOrderList') is not None:
            for k in m.get('LmOrderList'):
                temp_model = CreateVirtualProductOrderResponseBodyModelLmOrderListLmOrderList()
                self.lm_order_list.append(temp_model.from_map(k))
        return self


class CreateVirtualProductOrderResponseBodyModelPayTradeIds(TeaModel):
    def __init__(
        self,
        pay_trade_ids: List[str] = None,
    ):
        self.pay_trade_ids = pay_trade_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayTradeIds') is not None:
            self.pay_trade_ids = m.get('PayTradeIds')
        return self


class CreateVirtualProductOrderResponseBodyModelOrderIds(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class CreateVirtualProductOrderResponseBodyModel(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        lm_order_list: CreateVirtualProductOrderResponseBodyModelLmOrderList = None,
        pay_trade_ids: CreateVirtualProductOrderResponseBodyModelPayTradeIds = None,
        order_ids: CreateVirtualProductOrderResponseBodyModelOrderIds = None,
    ):
        self.redirect_url = redirect_url
        self.lm_order_list = lm_order_list
        self.pay_trade_ids = pay_trade_ids
        self.order_ids = order_ids

    def validate(self):
        if self.lm_order_list:
            self.lm_order_list.validate()
        if self.pay_trade_ids:
            self.pay_trade_ids.validate()
        if self.order_ids:
            self.order_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url
        if self.lm_order_list is not None:
            result['LmOrderList'] = self.lm_order_list.to_map()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids.to_map()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')
        if m.get('LmOrderList') is not None:
            temp_model = CreateVirtualProductOrderResponseBodyModelLmOrderList()
            self.lm_order_list = temp_model.from_map(m['LmOrderList'])
        if m.get('PayTradeIds') is not None:
            temp_model = CreateVirtualProductOrderResponseBodyModelPayTradeIds()
            self.pay_trade_ids = temp_model.from_map(m['PayTradeIds'])
        if m.get('OrderIds') is not None:
            temp_model = CreateVirtualProductOrderResponseBodyModelOrderIds()
            self.order_ids = temp_model.from_map(m['OrderIds'])
        return self


class CreateVirtualProductOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: CreateVirtualProductOrderResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = CreateVirtualProductOrderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class CreateVirtualProductOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateVirtualProductOrderResponseBody = None,
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
            temp_model = CreateVirtualProductOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWithholdTradeRequest(TeaModel):
    def __init__(
        self,
        out_request_no: str = None,
        out_trade_no: str = None,
        subject: str = None,
        buyer_id: str = None,
        merchant_id: str = None,
        total_amount: str = None,
        body: str = None,
        goods_detail: str = None,
        agreement_no: str = None,
        settle_mode: str = None,
        ext_info: str = None,
    ):
        self.out_request_no = out_request_no
        self.out_trade_no = out_trade_no
        self.subject = subject
        self.buyer_id = buyer_id
        self.merchant_id = merchant_id
        self.total_amount = total_amount
        self.body = body
        self.goods_detail = goods_detail
        self.agreement_no = agreement_no
        self.settle_mode = settle_mode
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        if self.out_trade_no is not None:
            result['OutTradeNo'] = self.out_trade_no
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.body is not None:
            result['Body'] = self.body
        if self.goods_detail is not None:
            result['GoodsDetail'] = self.goods_detail
        if self.agreement_no is not None:
            result['AgreementNo'] = self.agreement_no
        if self.settle_mode is not None:
            result['SettleMode'] = self.settle_mode
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        if m.get('OutTradeNo') is not None:
            self.out_trade_no = m.get('OutTradeNo')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('GoodsDetail') is not None:
            self.goods_detail = m.get('GoodsDetail')
        if m.get('AgreementNo') is not None:
            self.agreement_no = m.get('AgreementNo')
        if m.get('SettleMode') is not None:
            self.settle_mode = m.get('SettleMode')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class CreateWithholdTradeResponseBodyWithholdTradeResponse(TeaModel):
    def __init__(
        self,
        payment_date: str = None,
        trade_no: str = None,
        out_request_no: str = None,
        out_trade_no: str = None,
    ):
        self.payment_date = payment_date
        self.trade_no = trade_no
        self.out_request_no = out_request_no
        self.out_trade_no = out_trade_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payment_date is not None:
            result['PaymentDate'] = self.payment_date
        if self.trade_no is not None:
            result['TradeNo'] = self.trade_no
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        if self.out_trade_no is not None:
            result['OutTradeNo'] = self.out_trade_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PaymentDate') is not None:
            self.payment_date = m.get('PaymentDate')
        if m.get('TradeNo') is not None:
            self.trade_no = m.get('TradeNo')
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        if m.get('OutTradeNo') is not None:
            self.out_trade_no = m.get('OutTradeNo')
        return self


class CreateWithholdTradeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        withhold_trade_response: CreateWithholdTradeResponseBodyWithholdTradeResponse = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.withhold_trade_response = withhold_trade_response

    def validate(self):
        if self.withhold_trade_response:
            self.withhold_trade_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.withhold_trade_response is not None:
            result['WithholdTradeResponse'] = self.withhold_trade_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WithholdTradeResponse') is not None:
            temp_model = CreateWithholdTradeResponseBodyWithholdTradeResponse()
            self.withhold_trade_response = temp_model.from_map(m['WithholdTradeResponse'])
        return self


class CreateWithholdTradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateWithholdTradeResponseBody = None,
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
            temp_model = CreateWithholdTradeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBizItemsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_id: str = None,
        item_id_list: List[int] = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_id = sub_biz_id
        self.item_id_list = item_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        if self.item_id_list is not None:
            result['ItemIdList'] = self.item_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        if m.get('ItemIdList') is not None:
            self.item_id_list = m.get('ItemIdList')
        return self


class DeleteBizItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBizItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBizItemsResponseBody = None,
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
            temp_model = DeleteBizItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteItemLimitRuleRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_code: str = None,
        lm_activity_id: int = None,
        lm_item_id: str = None,
        item_id: int = None,
        rule_id: int = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_code = sub_biz_code
        self.lm_activity_id = lm_activity_id
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteItemLimitRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        model: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.model = model
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.model is not None:
            result['Model'] = self.model
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteItemLimitRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteItemLimitRuleResponseBody = None,
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
            temp_model = DeleteItemLimitRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableOrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        out_trade_id: str = None,
        lm_order_id: str = None,
        ext_json: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.out_trade_id = out_trade_id
        self.lm_order_id = lm_order_id
        self.ext_json = ext_json
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.out_trade_id is not None:
            result['OutTradeId'] = self.out_trade_id
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('OutTradeId') is not None:
            self.out_trade_id = m.get('OutTradeId')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class EnableOrderResponseBodyModelLmOrderListLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: str = None,
    ):
        self.lm_order_id = lm_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        return self


class EnableOrderResponseBodyModelLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_list: List[EnableOrderResponseBodyModelLmOrderListLmOrderList] = None,
    ):
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.lm_order_list:
            for k in self.lm_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmOrderList'] = []
        if self.lm_order_list is not None:
            for k in self.lm_order_list:
                result['LmOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_order_list = []
        if m.get('LmOrderList') is not None:
            for k in m.get('LmOrderList'):
                temp_model = EnableOrderResponseBodyModelLmOrderListLmOrderList()
                self.lm_order_list.append(temp_model.from_map(k))
        return self


class EnableOrderResponseBodyModelPayTradeIds(TeaModel):
    def __init__(
        self,
        pay_trade_ids: List[str] = None,
    ):
        self.pay_trade_ids = pay_trade_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayTradeIds') is not None:
            self.pay_trade_ids = m.get('PayTradeIds')
        return self


class EnableOrderResponseBodyModelOrderIds(TeaModel):
    def __init__(
        self,
        order_ids: List[str] = None,
    ):
        self.order_ids = order_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class EnableOrderResponseBodyModel(TeaModel):
    def __init__(
        self,
        redirect_url: str = None,
        lm_order_list: EnableOrderResponseBodyModelLmOrderList = None,
        pay_trade_ids: EnableOrderResponseBodyModelPayTradeIds = None,
        order_ids: EnableOrderResponseBodyModelOrderIds = None,
    ):
        self.redirect_url = redirect_url
        self.lm_order_list = lm_order_list
        self.pay_trade_ids = pay_trade_ids
        self.order_ids = order_ids

    def validate(self):
        if self.lm_order_list:
            self.lm_order_list.validate()
        if self.pay_trade_ids:
            self.pay_trade_ids.validate()
        if self.order_ids:
            self.order_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.redirect_url is not None:
            result['RedirectUrl'] = self.redirect_url
        if self.lm_order_list is not None:
            result['LmOrderList'] = self.lm_order_list.to_map()
        if self.pay_trade_ids is not None:
            result['PayTradeIds'] = self.pay_trade_ids.to_map()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedirectUrl') is not None:
            self.redirect_url = m.get('RedirectUrl')
        if m.get('LmOrderList') is not None:
            temp_model = EnableOrderResponseBodyModelLmOrderList()
            self.lm_order_list = temp_model.from_map(m['LmOrderList'])
        if m.get('PayTradeIds') is not None:
            temp_model = EnableOrderResponseBodyModelPayTradeIds()
            self.pay_trade_ids = temp_model.from_map(m['PayTradeIds'])
        if m.get('OrderIds') is not None:
            temp_model = EnableOrderResponseBodyModelOrderIds()
            self.order_ids = temp_model.from_map(m['OrderIds'])
        return self


class EnableOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: EnableOrderResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = EnableOrderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class EnableOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableOrderResponseBody = None,
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
            temp_model = EnableOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteNodeRequest(TeaModel):
    def __init__(
        self,
        process_instance_id: str = None,
        process_id: str = None,
        node_instance_id: str = None,
        node_id: str = None,
        request_data: str = None,
    ):
        self.process_instance_id = process_instance_id
        self.process_id = process_id
        self.node_instance_id = node_instance_id
        self.node_id = node_id
        self.request_data = request_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id
        if self.process_id is not None:
            result['ProcessId'] = self.process_id
        if self.node_instance_id is not None:
            result['NodeInstanceId'] = self.node_instance_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.request_data is not None:
            result['RequestData'] = self.request_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')
        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')
        if m.get('NodeInstanceId') is not None:
            self.node_instance_id = m.get('NodeInstanceId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RequestData') is not None:
            self.request_data = m.get('RequestData')
        return self


class ExecuteNodeResponseBodyModel(TeaModel):
    def __init__(
        self,
        response_data: Dict[str, Any] = None,
        process_instance_id: str = None,
    ):
        self.response_data = response_data
        self.process_instance_id = process_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.response_data is not None:
            result['ResponseData'] = self.response_data
        if self.process_instance_id is not None:
            result['ProcessInstanceId'] = self.process_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResponseData') is not None:
            self.response_data = m.get('ResponseData')
        if m.get('ProcessInstanceId') is not None:
            self.process_instance_id = m.get('ProcessInstanceId')
        return self


class ExecuteNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: ExecuteNodeResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = ExecuteNodeResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class ExecuteNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteNodeResponseBody = None,
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
            temp_model = ExecuteNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCategoryChainRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        category_id: int = None,
        item_id: int = None,
        lm_item_id: str = None,
    ):
        self.biz_id = biz_id
        self.category_id = category_id
        self.item_id = item_id
        self.lm_item_id = lm_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        return self


class GetCategoryChainResponseBodyCategoryList(TeaModel):
    def __init__(
        self,
        name: str = None,
        category_id: int = None,
    ):
        self.name = name
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class GetCategoryChainResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        category_list: List[GetCategoryChainResponseBodyCategoryList] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.category_list = category_list

    def validate(self):
        if self.category_list:
            for k in self.category_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CategoryList'] = []
        if self.category_list is not None:
            for k in self.category_list:
                result['CategoryList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.category_list = []
        if m.get('CategoryList') is not None:
            for k in m.get('CategoryList'):
                temp_model = GetCategoryChainResponseBodyCategoryList()
                self.category_list.append(temp_model.from_map(k))
        return self


class GetCategoryChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCategoryChainResponseBody = None,
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
            temp_model = GetCategoryChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCategoryListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        category_id: int = None,
    ):
        self.biz_id = biz_id
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class GetCategoryListResponseBodyCategoryListCategory(TeaModel):
    def __init__(
        self,
        name: str = None,
        category_id: int = None,
    ):
        self.name = name
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class GetCategoryListResponseBodyCategoryList(TeaModel):
    def __init__(
        self,
        category: List[GetCategoryListResponseBodyCategoryListCategory] = None,
    ):
        self.category = category

    def validate(self):
        if self.category:
            for k in self.category:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Category'] = []
        if self.category is not None:
            for k in self.category:
                result['Category'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category = []
        if m.get('Category') is not None:
            for k in m.get('Category'):
                temp_model = GetCategoryListResponseBodyCategoryListCategory()
                self.category.append(temp_model.from_map(k))
        return self


class GetCategoryListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        category_list: GetCategoryListResponseBodyCategoryList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.category_list = category_list

    def validate(self):
        if self.category_list:
            self.category_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.category_list is not None:
            result['CategoryList'] = self.category_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CategoryList') is not None:
            temp_model = GetCategoryListResponseBodyCategoryList()
            self.category_list = temp_model.from_map(m['CategoryList'])
        return self


class GetCategoryListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCategoryListResponseBody = None,
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
            temp_model = GetCategoryListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomServiceUrlRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        seller_id: str = None,
        cuid: str = None,
        nick: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.seller_id = seller_id
        self.cuid = cuid
        self.nick = nick
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.cuid is not None:
            result['Cuid'] = self.cuid
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('Cuid') is not None:
            self.cuid = m.get('Cuid')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class GetCustomServiceUrlResponseBodyUrlData(TeaModel):
    def __init__(
        self,
        return_url: str = None,
    ):
        self.return_url = return_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        return self


class GetCustomServiceUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        url_data: GetCustomServiceUrlResponseBodyUrlData = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.url_data = url_data

    def validate(self):
        if self.url_data:
            self.url_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url_data is not None:
            result['UrlData'] = self.url_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UrlData') is not None:
            temp_model = GetCustomServiceUrlResponseBodyUrlData()
            self.url_data = temp_model.from_map(m['UrlData'])
        return self


class GetCustomServiceUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCustomServiceUrlResponseBody = None,
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
            temp_model = GetCustomServiceUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGuidePageRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
    ):
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class GetGuidePageResponseBodyMiniShopInfo(TeaModel):
    def __init__(
        self,
        lite_shop_id: str = None,
        src: str = None,
        biz_id: str = None,
        name: str = None,
    ):
        self.lite_shop_id = lite_shop_id
        self.src = src
        self.biz_id = biz_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lite_shop_id is not None:
            result['LiteShopId'] = self.lite_shop_id
        if self.src is not None:
            result['Src'] = self.src
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiteShopId') is not None:
            self.lite_shop_id = m.get('LiteShopId')
        if m.get('Src') is not None:
            self.src = m.get('Src')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetGuidePageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        mini_shop_info: List[GetGuidePageResponseBodyMiniShopInfo] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.mini_shop_info = mini_shop_info

    def validate(self):
        if self.mini_shop_info:
            for k in self.mini_shop_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MiniShopInfo'] = []
        if self.mini_shop_info is not None:
            for k in self.mini_shop_info:
                result['MiniShopInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.mini_shop_info = []
        if m.get('MiniShopInfo') is not None:
            for k in m.get('MiniShopInfo'):
                temp_model = GetGuidePageResponseBodyMiniShopInfo()
                self.mini_shop_info.append(temp_model.from_map(k))
        return self


class GetGuidePageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGuidePageResponseBody = None,
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
            temp_model = GetGuidePageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetItemPromotionRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        item_id: int = None,
        lm_item_id: str = None,
    ):
        self.biz_id = biz_id
        self.item_id = item_id
        self.lm_item_id = lm_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        return self


class GetItemPromotionResponseBodyItemPromotionModel(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        sku_promotion: Dict[str, Any] = None,
        promotion_flag: bool = None,
        promotion_name: str = None,
        lm_item_id: str = None,
        promotion_desc: str = None,
        item_id: int = None,
        promotion_id: str = None,
        ext_info: Dict[str, Any] = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.sku_promotion = sku_promotion
        self.promotion_flag = promotion_flag
        self.promotion_name = promotion_name
        self.lm_item_id = lm_item_id
        self.promotion_desc = promotion_desc
        self.item_id = item_id
        self.promotion_id = promotion_id
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.sku_promotion is not None:
            result['SkuPromotion'] = self.sku_promotion
        if self.promotion_flag is not None:
            result['PromotionFlag'] = self.promotion_flag
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SkuPromotion') is not None:
            self.sku_promotion = m.get('SkuPromotion')
        if m.get('PromotionFlag') is not None:
            self.promotion_flag = m.get('PromotionFlag')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class GetItemPromotionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        item_promotion_model: GetItemPromotionResponseBodyItemPromotionModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.item_promotion_model = item_promotion_model

    def validate(self):
        if self.item_promotion_model:
            self.item_promotion_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.item_promotion_model is not None:
            result['ItemPromotionModel'] = self.item_promotion_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('ItemPromotionModel') is not None:
            temp_model = GetItemPromotionResponseBodyItemPromotionModel()
            self.item_promotion_model = temp_model.from_map(m['ItemPromotionModel'])
        return self


class GetItemPromotionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetItemPromotionResponseBody = None,
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
            temp_model = GetItemPromotionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginPageRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        target_url: str = None,
        fail_url: str = None,
    ):
        self.biz_id = biz_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.target_url = target_url
        self.fail_url = fail_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.target_url is not None:
            result['TargetUrl'] = self.target_url
        if self.fail_url is not None:
            result['FailUrl'] = self.fail_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('TargetUrl') is not None:
            self.target_url = m.get('TargetUrl')
        if m.get('FailUrl') is not None:
            self.fail_url = m.get('FailUrl')
        return self


class GetLoginPageResponseBodyUrlData(TeaModel):
    def __init__(
        self,
        return_url: str = None,
    ):
        self.return_url = return_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        return self


class GetLoginPageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        url_data: GetLoginPageResponseBodyUrlData = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.url_data = url_data

    def validate(self):
        if self.url_data:
            self.url_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url_data is not None:
            result['UrlData'] = self.url_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UrlData') is not None:
            temp_model = GetLoginPageResponseBodyUrlData()
            self.url_data = temp_model.from_map(m['UrlData'])
        return self


class GetLoginPageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLoginPageResponseBody = None,
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
            temp_model = GetLoginPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSwitchUrlRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        url: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.url = url
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.url is not None:
            result['Url'] = self.url
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        return self


class GetSwitchUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        url: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.url = url
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.url is not None:
            result['Url'] = self.url
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSwitchUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSwitchUrlResponseBody = None,
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
            temp_model = GetSwitchUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInfoRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        user_flag: str = None,
        app_name: str = None,
        query_json: str = None,
    ):
        self.biz_id = biz_id
        self.user_flag = user_flag
        self.app_name = app_name
        self.query_json = query_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.user_flag is not None:
            result['UserFlag'] = self.user_flag
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.query_json is not None:
            result['QueryJson'] = self.query_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('UserFlag') is not None:
            self.user_flag = m.get('UserFlag')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('QueryJson') is not None:
            self.query_json = m.get('QueryJson')
        return self


class GetUserInfoResponseBodyLoginResult(TeaModel):
    def __init__(
        self,
        return_url: str = None,
        biz_user_name: str = None,
        biz_uid: str = None,
        biz_id: str = None,
        lm_user_id: int = None,
        ext_info: Dict[str, Any] = None,
        sub_biz_id: List[str] = None,
    ):
        self.return_url = return_url
        self.biz_user_name = biz_user_name
        self.biz_uid = biz_uid
        self.biz_id = biz_id
        self.lm_user_id = lm_user_id
        self.ext_info = ext_info
        self.sub_biz_id = sub_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.biz_user_name is not None:
            result['BizUserName'] = self.biz_user_name
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_user_id is not None:
            result['LmUserId'] = self.lm_user_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('BizUserName') is not None:
            self.biz_user_name = m.get('BizUserName')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmUserId') is not None:
            self.lm_user_id = m.get('LmUserId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        return self


class GetUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        login_result: GetUserInfoResponseBodyLoginResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.login_result = login_result

    def validate(self):
        if self.login_result:
            self.login_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.login_result is not None:
            result['LoginResult'] = self.login_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LoginResult') is not None:
            temp_model = GetUserInfoResponseBodyLoginResult()
            self.login_result = temp_model.from_map(m['LoginResult'])
        return self


class GetUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetUserInfoResponseBody = None,
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
            temp_model = GetUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWithholdSignPageUrlRequest(TeaModel):
    def __init__(
        self,
        out_request_no: str = None,
        external_agreement_no: str = None,
        merchant_id: str = None,
        merchant_service_name: str = None,
        merchant_service_description: str = None,
        identity_parameters: str = None,
        return_url: str = None,
        notify_url: str = None,
        device_type: str = None,
        ext_info: str = None,
    ):
        self.out_request_no = out_request_no
        self.external_agreement_no = external_agreement_no
        self.merchant_id = merchant_id
        self.merchant_service_name = merchant_service_name
        self.merchant_service_description = merchant_service_description
        self.identity_parameters = identity_parameters
        self.return_url = return_url
        self.notify_url = notify_url
        self.device_type = device_type
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        if self.external_agreement_no is not None:
            result['ExternalAgreementNo'] = self.external_agreement_no
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.merchant_service_name is not None:
            result['MerchantServiceName'] = self.merchant_service_name
        if self.merchant_service_description is not None:
            result['MerchantServiceDescription'] = self.merchant_service_description
        if self.identity_parameters is not None:
            result['IdentityParameters'] = self.identity_parameters
        if self.return_url is not None:
            result['ReturnUrl'] = self.return_url
        if self.notify_url is not None:
            result['NotifyUrl'] = self.notify_url
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        if m.get('ExternalAgreementNo') is not None:
            self.external_agreement_no = m.get('ExternalAgreementNo')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('MerchantServiceName') is not None:
            self.merchant_service_name = m.get('MerchantServiceName')
        if m.get('MerchantServiceDescription') is not None:
            self.merchant_service_description = m.get('MerchantServiceDescription')
        if m.get('IdentityParameters') is not None:
            self.identity_parameters = m.get('IdentityParameters')
        if m.get('ReturnUrl') is not None:
            self.return_url = m.get('ReturnUrl')
        if m.get('NotifyUrl') is not None:
            self.notify_url = m.get('NotifyUrl')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class GetWithholdSignPageUrlResponseBodyWithholdSignResponse(TeaModel):
    def __init__(
        self,
        page_url: str = None,
        out_request_no: str = None,
    ):
        self.page_url = page_url
        self.out_request_no = out_request_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_url is not None:
            result['PageUrl'] = self.page_url
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageUrl') is not None:
            self.page_url = m.get('PageUrl')
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        return self


class GetWithholdSignPageUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        withhold_sign_response: GetWithholdSignPageUrlResponseBodyWithholdSignResponse = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.withhold_sign_response = withhold_sign_response

    def validate(self):
        if self.withhold_sign_response:
            self.withhold_sign_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.withhold_sign_response is not None:
            result['WithholdSignResponse'] = self.withhold_sign_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WithholdSignResponse') is not None:
            temp_model = GetWithholdSignPageUrlResponseBodyWithholdSignResponse()
            self.withhold_sign_response = temp_model.from_map(m['WithholdSignResponse'])
        return self


class GetWithholdSignPageUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWithholdSignPageUrlResponseBody = None,
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
            temp_model = GetWithholdSignPageUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitApplyRefundRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        sub_lm_order_id: str = None,
        biz_claim_type: int = None,
        goods_status: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.sub_lm_order_id = sub_lm_order_id
        self.biz_claim_type = biz_claim_type
        self.goods_status = goods_status
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.goods_status is not None:
            result['GoodsStatus'] = self.goods_status
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('GoodsStatus') is not None:
            self.goods_status = m.get('GoodsStatus')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class InitApplyRefundResponseBodyInitApplyRefundDataRefundReasonListRefundReasonList(TeaModel):
    def __init__(
        self,
        reason_text_id: int = None,
        reason_tips: str = None,
        proof_required: bool = None,
        refund_desc_required: bool = None,
    ):
        self.reason_text_id = reason_text_id
        self.reason_tips = reason_tips
        self.proof_required = proof_required
        self.refund_desc_required = refund_desc_required

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason_text_id is not None:
            result['ReasonTextId'] = self.reason_text_id
        if self.reason_tips is not None:
            result['ReasonTips'] = self.reason_tips
        if self.proof_required is not None:
            result['ProofRequired'] = self.proof_required
        if self.refund_desc_required is not None:
            result['RefundDescRequired'] = self.refund_desc_required
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonTextId') is not None:
            self.reason_text_id = m.get('ReasonTextId')
        if m.get('ReasonTips') is not None:
            self.reason_tips = m.get('ReasonTips')
        if m.get('ProofRequired') is not None:
            self.proof_required = m.get('ProofRequired')
        if m.get('RefundDescRequired') is not None:
            self.refund_desc_required = m.get('RefundDescRequired')
        return self


class InitApplyRefundResponseBodyInitApplyRefundDataRefundReasonList(TeaModel):
    def __init__(
        self,
        refund_reason_list: List[InitApplyRefundResponseBodyInitApplyRefundDataRefundReasonListRefundReasonList] = None,
    ):
        self.refund_reason_list = refund_reason_list

    def validate(self):
        if self.refund_reason_list:
            for k in self.refund_reason_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RefundReasonList'] = []
        if self.refund_reason_list is not None:
            for k in self.refund_reason_list:
                result['RefundReasonList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.refund_reason_list = []
        if m.get('RefundReasonList') is not None:
            for k in m.get('RefundReasonList'):
                temp_model = InitApplyRefundResponseBodyInitApplyRefundDataRefundReasonListRefundReasonList()
                self.refund_reason_list.append(temp_model.from_map(k))
        return self


class InitApplyRefundResponseBodyInitApplyRefundDataMaxRefundFeeData(TeaModel):
    def __init__(
        self,
        max_refund_fee: int = None,
        min_refund_fee: int = None,
    ):
        self.max_refund_fee = max_refund_fee
        self.min_refund_fee = min_refund_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['MaxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['MinRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRefundFee') is not None:
            self.max_refund_fee = m.get('MaxRefundFee')
        if m.get('MinRefundFee') is not None:
            self.min_refund_fee = m.get('MinRefundFee')
        return self


class InitApplyRefundResponseBodyInitApplyRefundData(TeaModel):
    def __init__(
        self,
        main_order_refund: bool = None,
        biz_claim_type: int = None,
        refund_reason_list: InitApplyRefundResponseBodyInitApplyRefundDataRefundReasonList = None,
        max_refund_fee_data: InitApplyRefundResponseBodyInitApplyRefundDataMaxRefundFeeData = None,
    ):
        self.main_order_refund = main_order_refund
        self.biz_claim_type = biz_claim_type
        self.refund_reason_list = refund_reason_list
        self.max_refund_fee_data = max_refund_fee_data

    def validate(self):
        if self.refund_reason_list:
            self.refund_reason_list.validate()
        if self.max_refund_fee_data:
            self.max_refund_fee_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_order_refund is not None:
            result['MainOrderRefund'] = self.main_order_refund
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.refund_reason_list is not None:
            result['RefundReasonList'] = self.refund_reason_list.to_map()
        if self.max_refund_fee_data is not None:
            result['MaxRefundFeeData'] = self.max_refund_fee_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MainOrderRefund') is not None:
            self.main_order_refund = m.get('MainOrderRefund')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('RefundReasonList') is not None:
            temp_model = InitApplyRefundResponseBodyInitApplyRefundDataRefundReasonList()
            self.refund_reason_list = temp_model.from_map(m['RefundReasonList'])
        if m.get('MaxRefundFeeData') is not None:
            temp_model = InitApplyRefundResponseBodyInitApplyRefundDataMaxRefundFeeData()
            self.max_refund_fee_data = temp_model.from_map(m['MaxRefundFeeData'])
        return self


class InitApplyRefundResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        sub_lm_order_id: str = None,
        request_id: str = None,
        init_apply_refund_data: InitApplyRefundResponseBodyInitApplyRefundData = None,
    ):
        self.code = code
        self.message = message
        self.sub_lm_order_id = sub_lm_order_id
        self.request_id = request_id
        self.init_apply_refund_data = init_apply_refund_data

    def validate(self):
        if self.init_apply_refund_data:
            self.init_apply_refund_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.init_apply_refund_data is not None:
            result['InitApplyRefundData'] = self.init_apply_refund_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InitApplyRefundData') is not None:
            temp_model = InitApplyRefundResponseBodyInitApplyRefundData()
            self.init_apply_refund_data = temp_model.from_map(m['InitApplyRefundData'])
        return self


class InitApplyRefundResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitApplyRefundResponseBody = None,
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
            temp_model = InitApplyRefundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListItemActivitiesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lm_item_ids: Dict[str, Any] = None,
        item_ids: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.lm_item_ids = lm_item_ids
        self.item_ids = item_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_item_ids is not None:
            result['LmItemIds'] = self.lm_item_ids
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        return self


class ListItemActivitiesShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lm_item_ids_shrink: str = None,
        item_ids_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.lm_item_ids_shrink = lm_item_ids_shrink
        self.item_ids_shrink = item_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_item_ids_shrink is not None:
            result['LmItemIds'] = self.lm_item_ids_shrink
        if self.item_ids_shrink is not None:
            result['ItemIds'] = self.item_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids_shrink = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids_shrink = m.get('ItemIds')
        return self


class ListItemActivitiesResponseBodyLmItemActivityModelListLmItemActivityModelLmActivityPopModel(TeaModel):
    def __init__(
        self,
        sub_biz_code: str = None,
        end_date: str = None,
        display_date: str = None,
        biz_id: str = None,
        start_date: str = None,
        title: str = None,
        ext_info: Dict[str, Any] = None,
        id: int = None,
    ):
        self.sub_biz_code = sub_biz_code
        self.end_date = end_date
        self.display_date = display_date
        self.biz_id = biz_id
        self.start_date = start_date
        self.title = title
        self.ext_info = ext_info
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.display_date is not None:
            result['DisplayDate'] = self.display_date
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.title is not None:
            result['Title'] = self.title
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DisplayDate') is not None:
            self.display_date = m.get('DisplayDate')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListItemActivitiesResponseBodyLmItemActivityModelListLmItemActivityModel(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        lm_activity_pop_model: ListItemActivitiesResponseBodyLmItemActivityModelListLmItemActivityModelLmActivityPopModel = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.lm_activity_pop_model = lm_activity_pop_model

    def validate(self):
        if self.lm_activity_pop_model:
            self.lm_activity_pop_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_activity_pop_model is not None:
            result['LmActivityPopModel'] = self.lm_activity_pop_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmActivityPopModel') is not None:
            temp_model = ListItemActivitiesResponseBodyLmItemActivityModelListLmItemActivityModelLmActivityPopModel()
            self.lm_activity_pop_model = temp_model.from_map(m['LmActivityPopModel'])
        return self


class ListItemActivitiesResponseBodyLmItemActivityModelList(TeaModel):
    def __init__(
        self,
        lm_item_activity_model: List[ListItemActivitiesResponseBodyLmItemActivityModelListLmItemActivityModel] = None,
    ):
        self.lm_item_activity_model = lm_item_activity_model

    def validate(self):
        if self.lm_item_activity_model:
            for k in self.lm_item_activity_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmItemActivityModel'] = []
        if self.lm_item_activity_model is not None:
            for k in self.lm_item_activity_model:
                result['LmItemActivityModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_item_activity_model = []
        if m.get('LmItemActivityModel') is not None:
            for k in m.get('LmItemActivityModel'):
                temp_model = ListItemActivitiesResponseBodyLmItemActivityModelListLmItemActivityModel()
                self.lm_item_activity_model.append(temp_model.from_map(k))
        return self


class ListItemActivitiesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        lm_item_activity_model_list: ListItemActivitiesResponseBodyLmItemActivityModelList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.lm_item_activity_model_list = lm_item_activity_model_list

    def validate(self):
        if self.lm_item_activity_model_list:
            self.lm_item_activity_model_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.lm_item_activity_model_list is not None:
            result['LmItemActivityModelList'] = self.lm_item_activity_model_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LmItemActivityModelList') is not None:
            temp_model = ListItemActivitiesResponseBodyLmItemActivityModelList()
            self.lm_item_activity_model_list = temp_model.from_map(m['LmItemActivityModelList'])
        return self


class ListItemActivitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListItemActivitiesResponseBody = None,
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
            temp_model = ListItemActivitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBasicAndBizItemsRequestItemListSkuList(TeaModel):
    def __init__(
        self,
        status_action: int = None,
        price_cent: int = None,
        supplier_price: int = None,
        sku_id: int = None,
        points: int = None,
        points_amount: int = None,
        benefit_id: str = None,
        quantity: int = None,
    ):
        self.status_action = status_action
        self.price_cent = price_cent
        self.supplier_price = supplier_price
        self.sku_id = sku_id
        self.points = points
        self.points_amount = points_amount
        self.benefit_id = benefit_id
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_action is not None:
            result['StatusAction'] = self.status_action
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.supplier_price is not None:
            result['SupplierPrice'] = self.supplier_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.benefit_id is not None:
            result['BenefitId'] = self.benefit_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusAction') is not None:
            self.status_action = m.get('StatusAction')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('SupplierPrice') is not None:
            self.supplier_price = m.get('SupplierPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('BenefitId') is not None:
            self.benefit_id = m.get('BenefitId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class ModifyBasicAndBizItemsRequestItemList(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        sku_list: List[ModifyBasicAndBizItemsRequestItemListSkuList] = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.sku_list = sku_list

    def validate(self):
        if self.sku_list:
            for k in self.sku_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        result['SkuList'] = []
        if self.sku_list is not None:
            for k in self.sku_list:
                result['SkuList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        self.sku_list = []
        if m.get('SkuList') is not None:
            for k in m.get('SkuList'):
                temp_model = ModifyBasicAndBizItemsRequestItemListSkuList()
                self.sku_list.append(temp_model.from_map(k))
        return self


class ModifyBasicAndBizItemsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_id: str = None,
        item_list: List[ModifyBasicAndBizItemsRequestItemList] = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_id = sub_biz_id
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = ModifyBasicAndBizItemsRequestItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class ModifyBasicAndBizItemsResponseBodyFailedItemListItemSkuIdList(TeaModel):
    def __init__(
        self,
        sku: List[str] = None,
    ):
        self.sku = sku

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku is not None:
            result['Sku'] = self.sku
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sku') is not None:
            self.sku = m.get('Sku')
        return self


class ModifyBasicAndBizItemsResponseBodyFailedItemListItem(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        sku_id_list: ModifyBasicAndBizItemsResponseBodyFailedItemListItemSkuIdList = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.sku_id_list = sku_id_list

    def validate(self):
        if self.sku_id_list:
            self.sku_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_id_list is not None:
            result['SkuIdList'] = self.sku_id_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuIdList') is not None:
            temp_model = ModifyBasicAndBizItemsResponseBodyFailedItemListItemSkuIdList()
            self.sku_id_list = temp_model.from_map(m['SkuIdList'])
        return self


class ModifyBasicAndBizItemsResponseBodyFailedItemList(TeaModel):
    def __init__(
        self,
        item: List[ModifyBasicAndBizItemsResponseBodyFailedItemListItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = ModifyBasicAndBizItemsResponseBodyFailedItemListItem()
                self.item.append(temp_model.from_map(k))
        return self


class ModifyBasicAndBizItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        failed_item_list: ModifyBasicAndBizItemsResponseBodyFailedItemList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.failed_item_list = failed_item_list

    def validate(self):
        if self.failed_item_list:
            self.failed_item_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.failed_item_list is not None:
            result['FailedItemList'] = self.failed_item_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FailedItemList') is not None:
            temp_model = ModifyBasicAndBizItemsResponseBodyFailedItemList()
            self.failed_item_list = temp_model.from_map(m['FailedItemList'])
        return self


class ModifyBasicAndBizItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBasicAndBizItemsResponseBody = None,
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
            temp_model = ModifyBasicAndBizItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBizItemsRequestItemListSkuList(TeaModel):
    def __init__(
        self,
        status_action: int = None,
        price_cent: int = None,
        sku_id: int = None,
        points: int = None,
        points_amount: int = None,
        benefit_id: str = None,
        quantity: int = None,
    ):
        self.status_action = status_action
        self.price_cent = price_cent
        self.sku_id = sku_id
        self.points = points
        self.points_amount = points_amount
        self.benefit_id = benefit_id
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_action is not None:
            result['StatusAction'] = self.status_action
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.benefit_id is not None:
            result['BenefitId'] = self.benefit_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatusAction') is not None:
            self.status_action = m.get('StatusAction')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('BenefitId') is not None:
            self.benefit_id = m.get('BenefitId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class ModifyBizItemsRequestItemList(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        sku_list: List[ModifyBizItemsRequestItemListSkuList] = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.sku_list = sku_list

    def validate(self):
        if self.sku_list:
            for k in self.sku_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        result['SkuList'] = []
        if self.sku_list is not None:
            for k in self.sku_list:
                result['SkuList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        self.sku_list = []
        if m.get('SkuList') is not None:
            for k in m.get('SkuList'):
                temp_model = ModifyBizItemsRequestItemListSkuList()
                self.sku_list.append(temp_model.from_map(k))
        return self


class ModifyBizItemsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_id: str = None,
        item_list: List[ModifyBizItemsRequestItemList] = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_id = sub_biz_id
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = ModifyBizItemsRequestItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class ModifyBizItemsResponseBodyFailedItemListItemSkuIdList(TeaModel):
    def __init__(
        self,
        sku: List[str] = None,
    ):
        self.sku = sku

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku is not None:
            result['Sku'] = self.sku
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sku') is not None:
            self.sku = m.get('Sku')
        return self


class ModifyBizItemsResponseBodyFailedItemListItem(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        sku_id_list: ModifyBizItemsResponseBodyFailedItemListItemSkuIdList = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.sku_id_list = sku_id_list

    def validate(self):
        if self.sku_id_list:
            self.sku_id_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_id_list is not None:
            result['SkuIdList'] = self.sku_id_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuIdList') is not None:
            temp_model = ModifyBizItemsResponseBodyFailedItemListItemSkuIdList()
            self.sku_id_list = temp_model.from_map(m['SkuIdList'])
        return self


class ModifyBizItemsResponseBodyFailedItemList(TeaModel):
    def __init__(
        self,
        item: List[ModifyBizItemsResponseBodyFailedItemListItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = ModifyBizItemsResponseBodyFailedItemListItem()
                self.item.append(temp_model.from_map(k))
        return self


class ModifyBizItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        failed_item_list: ModifyBizItemsResponseBodyFailedItemList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.failed_item_list = failed_item_list

    def validate(self):
        if self.failed_item_list:
            self.failed_item_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.failed_item_list is not None:
            result['FailedItemList'] = self.failed_item_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('FailedItemList') is not None:
            temp_model = ModifyBizItemsResponseBodyFailedItemList()
            self.failed_item_list = temp_model.from_map(m['FailedItemList'])
        return self


class ModifyBizItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBizItemsResponseBody = None,
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
            temp_model = ModifyBizItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyItemLimitRuleRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_code: str = None,
        lm_activity_id: int = None,
        lm_item_id: str = None,
        item_id: int = None,
        upper_num: int = None,
        rule_id: int = None,
        rule_type: int = None,
        begin_time: int = None,
        end_time: int = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_code = sub_biz_code
        self.lm_activity_id = lm_activity_id
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.upper_num = upper_num
        self.rule_id = rule_id
        self.rule_type = rule_type
        self.begin_time = begin_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.upper_num is not None:
            result['UpperNum'] = self.upper_num
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_type is not None:
            result['RuleType'] = self.rule_type
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('UpperNum') is not None:
            self.upper_num = m.get('UpperNum')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class ModifyItemLimitRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        model: bool = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.model = model
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.model is not None:
            result['Model'] = self.model
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyItemLimitRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyItemLimitRuleResponseBody = None,
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
            temp_model = ModifyItemLimitRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NotifyPayOrderStatusRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        request_id: str = None,
        operation_date: str = None,
        pay_types: str = None,
        amount: int = None,
    ):
        self.channel_id = channel_id
        self.request_id = request_id
        self.operation_date = operation_date
        self.pay_types = pay_types
        self.amount = amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_date is not None:
            result['OperationDate'] = self.operation_date
        if self.pay_types is not None:
            result['PayTypes'] = self.pay_types
        if self.amount is not None:
            result['Amount'] = self.amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationDate') is not None:
            self.operation_date = m.get('OperationDate')
        if m.get('PayTypes') is not None:
            self.pay_types = m.get('PayTypes')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        return self


class NotifyPayOrderStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class NotifyPayOrderStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: NotifyPayOrderStatusResponseBody = None,
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
            temp_model = NotifyPayOrderStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NotifyWithholdFundRequest(TeaModel):
    def __init__(
        self,
        channel_id: str = None,
        request_id: str = None,
        operation_date: str = None,
        pay_types: str = None,
        amount: int = None,
        tenant_order_id: str = None,
    ):
        self.channel_id = channel_id
        self.request_id = request_id
        self.operation_date = operation_date
        self.pay_types = pay_types
        self.amount = amount
        self.tenant_order_id = tenant_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.operation_date is not None:
            result['OperationDate'] = self.operation_date
        if self.pay_types is not None:
            result['PayTypes'] = self.pay_types
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.tenant_order_id is not None:
            result['TenantOrderId'] = self.tenant_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OperationDate') is not None:
            self.operation_date = m.get('OperationDate')
        if m.get('PayTypes') is not None:
            self.pay_types = m.get('PayTypes')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('TenantOrderId') is not None:
            self.tenant_order_id = m.get('TenantOrderId')
        return self


class NotifyWithholdFundResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NotifyWithholdFundResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: NotifyWithholdFundResponseBody = None,
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
            temp_model = NotifyWithholdFundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryActivityItemsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
        lm_activity_id: int = None,
    ):
        self.biz_id = biz_id
        self.page_number = page_number
        self.page_size = page_size
        self.lm_activity_id = lm_activity_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        return self


class QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModelSkuModelListLmActivityItemSkuModel(TeaModel):
    def __init__(
        self,
        reserved_price: int = None,
        tips: str = None,
        lm_item_id: str = None,
        sku_id: int = None,
        lm_activity_id: int = None,
        activity_status: str = None,
        biz_id: str = None,
        item_id: int = None,
        sku_pic_url: str = None,
        activity_price: int = None,
        sku_title: str = None,
    ):
        self.reserved_price = reserved_price
        self.tips = tips
        self.lm_item_id = lm_item_id
        self.sku_id = sku_id
        self.lm_activity_id = lm_activity_id
        self.activity_status = activity_status
        self.biz_id = biz_id
        self.item_id = item_id
        self.sku_pic_url = sku_pic_url
        self.activity_price = activity_price
        self.sku_title = sku_title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reserved_price is not None:
            result['ReservedPrice'] = self.reserved_price
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.activity_status is not None:
            result['ActivityStatus'] = self.activity_status
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.activity_price is not None:
            result['ActivityPrice'] = self.activity_price
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReservedPrice') is not None:
            self.reserved_price = m.get('ReservedPrice')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('ActivityStatus') is not None:
            self.activity_status = m.get('ActivityStatus')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('ActivityPrice') is not None:
            self.activity_price = m.get('ActivityPrice')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        return self


class QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModelSkuModelList(TeaModel):
    def __init__(
        self,
        lm_activity_item_sku_model: List[QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModelSkuModelListLmActivityItemSkuModel] = None,
    ):
        self.lm_activity_item_sku_model = lm_activity_item_sku_model

    def validate(self):
        if self.lm_activity_item_sku_model:
            for k in self.lm_activity_item_sku_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmActivityItemSkuModel'] = []
        if self.lm_activity_item_sku_model is not None:
            for k in self.lm_activity_item_sku_model:
                result['LmActivityItemSkuModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_activity_item_sku_model = []
        if m.get('LmActivityItemSkuModel') is not None:
            for k in m.get('LmActivityItemSkuModel'):
                temp_model = QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModelSkuModelListLmActivityItemSkuModel()
                self.lm_activity_item_sku_model.append(temp_model.from_map(k))
        return self


class QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModel(TeaModel):
    def __init__(
        self,
        item_title: str = None,
        tb_seller_id: int = None,
        sellable_quantity: int = None,
        tb_shop_id: int = None,
        lm_item_id: str = None,
        tb_shop_name: str = None,
        item_activity_quantity: int = None,
        lm_activity_id: int = None,
        can_sell: bool = None,
        item_id: int = None,
        main_pic_url: str = None,
        tips: str = None,
        lm_shop_id: str = None,
        item_activity_status: str = None,
        sku_model_list: QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModelSkuModelList = None,
    ):
        self.item_title = item_title
        self.tb_seller_id = tb_seller_id
        self.sellable_quantity = sellable_quantity
        self.tb_shop_id = tb_shop_id
        self.lm_item_id = lm_item_id
        self.tb_shop_name = tb_shop_name
        self.item_activity_quantity = item_activity_quantity
        self.lm_activity_id = lm_activity_id
        self.can_sell = can_sell
        self.item_id = item_id
        self.main_pic_url = main_pic_url
        self.tips = tips
        self.lm_shop_id = lm_shop_id
        self.item_activity_status = item_activity_status
        self.sku_model_list = sku_model_list

    def validate(self):
        if self.sku_model_list:
            self.sku_model_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.tb_seller_id is not None:
            result['TbSellerId'] = self.tb_seller_id
        if self.sellable_quantity is not None:
            result['SellableQuantity'] = self.sellable_quantity
        if self.tb_shop_id is not None:
            result['TbShopId'] = self.tb_shop_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.tb_shop_name is not None:
            result['TbShopName'] = self.tb_shop_name
        if self.item_activity_quantity is not None:
            result['ItemActivityQuantity'] = self.item_activity_quantity
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.tips is not None:
            result['Tips'] = self.tips
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.item_activity_status is not None:
            result['ItemActivityStatus'] = self.item_activity_status
        if self.sku_model_list is not None:
            result['SkuModelList'] = self.sku_model_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('TbSellerId') is not None:
            self.tb_seller_id = m.get('TbSellerId')
        if m.get('SellableQuantity') is not None:
            self.sellable_quantity = m.get('SellableQuantity')
        if m.get('TbShopId') is not None:
            self.tb_shop_id = m.get('TbShopId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('TbShopName') is not None:
            self.tb_shop_name = m.get('TbShopName')
        if m.get('ItemActivityQuantity') is not None:
            self.item_activity_quantity = m.get('ItemActivityQuantity')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('Tips') is not None:
            self.tips = m.get('Tips')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('ItemActivityStatus') is not None:
            self.item_activity_status = m.get('ItemActivityStatus')
        if m.get('SkuModelList') is not None:
            temp_model = QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModelSkuModelList()
            self.sku_model_list = temp_model.from_map(m['SkuModelList'])
        return self


class QueryActivityItemsResponseBodyLmActivityItemModelList(TeaModel):
    def __init__(
        self,
        lm_activity_item_model: List[QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModel] = None,
    ):
        self.lm_activity_item_model = lm_activity_item_model

    def validate(self):
        if self.lm_activity_item_model:
            for k in self.lm_activity_item_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmActivityItemModel'] = []
        if self.lm_activity_item_model is not None:
            for k in self.lm_activity_item_model:
                result['LmActivityItemModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_activity_item_model = []
        if m.get('LmActivityItemModel') is not None:
            for k in m.get('LmActivityItemModel'):
                temp_model = QueryActivityItemsResponseBodyLmActivityItemModelListLmActivityItemModel()
                self.lm_activity_item_model.append(temp_model.from_map(k))
        return self


class QueryActivityItemsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        lm_activity_item_model_list: QueryActivityItemsResponseBodyLmActivityItemModelList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.lm_activity_item_model_list = lm_activity_item_model_list

    def validate(self):
        if self.lm_activity_item_model_list:
            self.lm_activity_item_model_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.lm_activity_item_model_list is not None:
            result['LmActivityItemModelList'] = self.lm_activity_item_model_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LmActivityItemModelList') is not None:
            temp_model = QueryActivityItemsResponseBodyLmActivityItemModelList()
            self.lm_activity_item_model_list = temp_model.from_map(m['LmActivityItemModelList'])
        return self


class QueryActivityItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryActivityItemsResponseBody = None,
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
            temp_model = QueryActivityItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAddressRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        ip: str = None,
        division_code: str = None,
    ):
        self.biz_id = biz_id
        self.ip = ip
        self.division_code = division_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        return self


class QueryAddressResponseBodyDivisionAddressDivisionAddress(TeaModel):
    def __init__(
        self,
        parent_id: int = None,
        division_code: int = None,
        division_level: int = None,
        division_name: str = None,
    ):
        self.parent_id = parent_id
        self.division_code = division_code
        self.division_level = division_level
        self.division_name = division_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.division_level is not None:
            result['DivisionLevel'] = self.division_level
        if self.division_name is not None:
            result['DivisionName'] = self.division_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('DivisionLevel') is not None:
            self.division_level = m.get('DivisionLevel')
        if m.get('DivisionName') is not None:
            self.division_name = m.get('DivisionName')
        return self


class QueryAddressResponseBodyDivisionAddress(TeaModel):
    def __init__(
        self,
        division_address: List[QueryAddressResponseBodyDivisionAddressDivisionAddress] = None,
    ):
        self.division_address = division_address

    def validate(self):
        if self.division_address:
            for k in self.division_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DivisionAddress'] = []
        if self.division_address is not None:
            for k in self.division_address:
                result['DivisionAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.division_address = []
        if m.get('DivisionAddress') is not None:
            for k in m.get('DivisionAddress'):
                temp_model = QueryAddressResponseBodyDivisionAddressDivisionAddress()
                self.division_address.append(temp_model.from_map(k))
        return self


class QueryAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        division_address: QueryAddressResponseBodyDivisionAddress = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.division_address = division_address

    def validate(self):
        if self.division_address:
            self.division_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.division_address is not None:
            result['DivisionAddress'] = self.division_address.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DivisionAddress') is not None:
            temp_model = QueryAddressResponseBodyDivisionAddress()
            self.division_address = temp_model.from_map(m['DivisionAddress'])
        return self


class QueryAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAddressResponseBody = None,
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
            temp_model = QueryAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAddressDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        third_party_user_id: str = None,
        use_anonymous_tb_account: bool = None,
        address_info: str = None,
    ):
        self.biz_id = biz_id
        self.third_party_user_id = third_party_user_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.address_info = address_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('AddressInfo') is not None:
            self.address_info = m.get('AddressInfo')
        return self


class QueryAddressDetailResponseBodyDeliveryAddress(TeaModel):
    def __init__(
        self,
        status: int = None,
        post_code: str = None,
        full_name: str = None,
        address_detail: str = None,
        city: str = None,
        address_id: int = None,
        division_code: str = None,
        mobile: str = None,
        country: str = None,
        area: str = None,
        town_division_code: str = None,
        town: str = None,
        province: str = None,
    ):
        self.status = status
        self.post_code = post_code
        self.full_name = full_name
        self.address_detail = address_detail
        self.city = city
        self.address_id = address_id
        self.division_code = division_code
        self.mobile = mobile
        self.country = country
        self.area = area
        self.town_division_code = town_division_code
        self.town = town
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.city is not None:
            result['City'] = self.city
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.country is not None:
            result['Country'] = self.country
        if self.area is not None:
            result['Area'] = self.area
        if self.town_division_code is not None:
            result['TownDivisionCode'] = self.town_division_code
        if self.town is not None:
            result['Town'] = self.town
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('TownDivisionCode') is not None:
            self.town_division_code = m.get('TownDivisionCode')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class QueryAddressDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        delivery_address: QueryAddressDetailResponseBodyDeliveryAddress = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.delivery_address = delivery_address

    def validate(self):
        if self.delivery_address:
            self.delivery_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeliveryAddress') is not None:
            temp_model = QueryAddressDetailResponseBodyDeliveryAddress()
            self.delivery_address = temp_model.from_map(m['DeliveryAddress'])
        return self


class QueryAddressDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAddressDetailResponseBody = None,
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
            temp_model = QueryAddressDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAddressListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        third_party_user_id: str = None,
        use_anonymous_tb_account: bool = None,
    ):
        self.biz_id = biz_id
        self.third_party_user_id = third_party_user_id
        self.use_anonymous_tb_account = use_anonymous_tb_account

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        return self


class QueryAddressListResponseBodyAddressList(TeaModel):
    def __init__(
        self,
        status: int = None,
        post_code: str = None,
        full_name: str = None,
        address_detail: str = None,
        city: str = None,
        address_id: int = None,
        division_code: str = None,
        mobile: str = None,
        country: str = None,
        area: str = None,
        town_division_code: str = None,
        town: str = None,
        province: str = None,
    ):
        self.status = status
        self.post_code = post_code
        self.full_name = full_name
        self.address_detail = address_detail
        self.city = city
        self.address_id = address_id
        self.division_code = division_code
        self.mobile = mobile
        self.country = country
        self.area = area
        self.town_division_code = town_division_code
        self.town = town
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.post_code is not None:
            result['PostCode'] = self.post_code
        if self.full_name is not None:
            result['FullName'] = self.full_name
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.city is not None:
            result['City'] = self.city
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.country is not None:
            result['Country'] = self.country
        if self.area is not None:
            result['Area'] = self.area
        if self.town_division_code is not None:
            result['TownDivisionCode'] = self.town_division_code
        if self.town is not None:
            result['Town'] = self.town
        if self.province is not None:
            result['Province'] = self.province
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PostCode') is not None:
            self.post_code = m.get('PostCode')
        if m.get('FullName') is not None:
            self.full_name = m.get('FullName')
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('TownDivisionCode') is not None:
            self.town_division_code = m.get('TownDivisionCode')
        if m.get('Town') is not None:
            self.town = m.get('Town')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        return self


class QueryAddressListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        address_list: List[QueryAddressListResponseBodyAddressList] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.address_list = address_list

    def validate(self):
        if self.address_list:
            for k in self.address_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AddressList'] = []
        if self.address_list is not None:
            for k in self.address_list:
                result['AddressList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.address_list = []
        if m.get('AddressList') is not None:
            for k in m.get('AddressList'):
                temp_model = QueryAddressListResponseBodyAddressList()
                self.address_list.append(temp_model.from_map(k))
        return self


class QueryAddressListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAddressListResponseBody = None,
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
            temp_model = QueryAddressListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAdvertisementSettleInfoRequest(TeaModel):
    def __init__(
        self,
        media_settle_detail_id: str = None,
        channel_id: str = None,
        settle_no: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        ext_info: str = None,
    ):
        self.media_settle_detail_id = media_settle_detail_id
        self.channel_id = channel_id
        self.settle_no = settle_no
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_settle_detail_id is not None:
            result['MediaSettleDetailId'] = self.media_settle_detail_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.settle_no is not None:
            result['SettleNo'] = self.settle_no
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaSettleDetailId') is not None:
            self.media_settle_detail_id = m.get('MediaSettleDetailId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('SettleNo') is not None:
            self.settle_no = m.get('SettleNo')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class QueryAdvertisementSettleInfoResponseBodyModelAdvertiseSettleInfoList(TeaModel):
    def __init__(
        self,
        advertise_settle_detail_id: str = None,
        create_date: str = None,
        media_settle_detail_id: str = None,
        ext_info: str = None,
        end_time: str = None,
        start_time: str = None,
        settle_no: str = None,
        advertise_settle_amount: str = None,
        settle_status: str = None,
        advertise_name: str = None,
        channel_id: str = None,
        modified_date: str = None,
    ):
        self.advertise_settle_detail_id = advertise_settle_detail_id
        self.create_date = create_date
        self.media_settle_detail_id = media_settle_detail_id
        self.ext_info = ext_info
        self.end_time = end_time
        self.start_time = start_time
        self.settle_no = settle_no
        self.advertise_settle_amount = advertise_settle_amount
        self.settle_status = settle_status
        self.advertise_name = advertise_name
        self.channel_id = channel_id
        self.modified_date = modified_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advertise_settle_detail_id is not None:
            result['AdvertiseSettleDetailId'] = self.advertise_settle_detail_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.media_settle_detail_id is not None:
            result['MediaSettleDetailId'] = self.media_settle_detail_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.settle_no is not None:
            result['SettleNo'] = self.settle_no
        if self.advertise_settle_amount is not None:
            result['AdvertiseSettleAmount'] = self.advertise_settle_amount
        if self.settle_status is not None:
            result['SettleStatus'] = self.settle_status
        if self.advertise_name is not None:
            result['AdvertiseName'] = self.advertise_name
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvertiseSettleDetailId') is not None:
            self.advertise_settle_detail_id = m.get('AdvertiseSettleDetailId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('MediaSettleDetailId') is not None:
            self.media_settle_detail_id = m.get('MediaSettleDetailId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SettleNo') is not None:
            self.settle_no = m.get('SettleNo')
        if m.get('AdvertiseSettleAmount') is not None:
            self.advertise_settle_amount = m.get('AdvertiseSettleAmount')
        if m.get('SettleStatus') is not None:
            self.settle_status = m.get('SettleStatus')
        if m.get('AdvertiseName') is not None:
            self.advertise_name = m.get('AdvertiseName')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ModifiedDate') is not None:
            self.modified_date = m.get('ModifiedDate')
        return self


class QueryAdvertisementSettleInfoResponseBodyModel(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        advertise_settle_info_list: List[QueryAdvertisementSettleInfoResponseBodyModelAdvertiseSettleInfoList] = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.advertise_settle_info_list = advertise_settle_info_list

    def validate(self):
        if self.advertise_settle_info_list:
            for k in self.advertise_settle_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['AdvertiseSettleInfoList'] = []
        if self.advertise_settle_info_list is not None:
            for k in self.advertise_settle_info_list:
                result['AdvertiseSettleInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.advertise_settle_info_list = []
        if m.get('AdvertiseSettleInfoList') is not None:
            for k in m.get('AdvertiseSettleInfoList'):
                temp_model = QueryAdvertisementSettleInfoResponseBodyModelAdvertiseSettleInfoList()
                self.advertise_settle_info_list.append(temp_model.from_map(k))
        return self


class QueryAdvertisementSettleInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: QueryAdvertisementSettleInfoResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = QueryAdvertisementSettleInfoResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class QueryAdvertisementSettleInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAdvertisementSettleInfoResponseBody = None,
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
            temp_model = QueryAdvertisementSettleInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAgreementRequest(TeaModel):
    def __init__(
        self,
        external_agreement_no: str = None,
        merchant_id: str = None,
        agreement_no: str = None,
    ):
        self.external_agreement_no = external_agreement_no
        self.merchant_id = merchant_id
        self.agreement_no = agreement_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_agreement_no is not None:
            result['ExternalAgreementNo'] = self.external_agreement_no
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.agreement_no is not None:
            result['AgreementNo'] = self.agreement_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExternalAgreementNo') is not None:
            self.external_agreement_no = m.get('ExternalAgreementNo')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('AgreementNo') is not None:
            self.agreement_no = m.get('AgreementNo')
        return self


class QueryAgreementResponseBodyQueryAgreementResponse(TeaModel):
    def __init__(
        self,
        status: str = None,
        external_agreement_no: str = None,
        valid_time: str = None,
        invalid_time: str = None,
        agreement_no: str = None,
        sign_time: str = None,
    ):
        self.status = status
        self.external_agreement_no = external_agreement_no
        self.valid_time = valid_time
        self.invalid_time = invalid_time
        self.agreement_no = agreement_no
        self.sign_time = sign_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.external_agreement_no is not None:
            result['ExternalAgreementNo'] = self.external_agreement_no
        if self.valid_time is not None:
            result['ValidTime'] = self.valid_time
        if self.invalid_time is not None:
            result['InvalidTime'] = self.invalid_time
        if self.agreement_no is not None:
            result['AgreementNo'] = self.agreement_no
        if self.sign_time is not None:
            result['SignTime'] = self.sign_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExternalAgreementNo') is not None:
            self.external_agreement_no = m.get('ExternalAgreementNo')
        if m.get('ValidTime') is not None:
            self.valid_time = m.get('ValidTime')
        if m.get('InvalidTime') is not None:
            self.invalid_time = m.get('InvalidTime')
        if m.get('AgreementNo') is not None:
            self.agreement_no = m.get('AgreementNo')
        if m.get('SignTime') is not None:
            self.sign_time = m.get('SignTime')
        return self


class QueryAgreementResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        query_agreement_response: QueryAgreementResponseBodyQueryAgreementResponse = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.query_agreement_response = query_agreement_response

    def validate(self):
        if self.query_agreement_response:
            self.query_agreement_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.query_agreement_response is not None:
            result['QueryAgreementResponse'] = self.query_agreement_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('QueryAgreementResponse') is not None:
            temp_model = QueryAgreementResponseBodyQueryAgreementResponse()
            self.query_agreement_response = temp_model.from_map(m['QueryAgreementResponse'])
        return self


class QueryAgreementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAgreementResponseBody = None,
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
            temp_model = QueryAgreementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAllCinemasRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        city_code: int = None,
        page_number: int = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.city_code = city_code
        self.page_number = page_number
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryAllCinemasResponseBodyCinemasCinema(TeaModel):
    def __init__(
        self,
        standard_id: str = None,
        schedule_close_time: int = None,
        city_id: int = None,
        cinema_name: str = None,
        city_name: str = None,
        address: str = None,
        longitude: str = None,
        latitude: str = None,
        phone: str = None,
        id: int = None,
    ):
        self.standard_id = standard_id
        self.schedule_close_time = schedule_close_time
        self.city_id = city_id
        self.cinema_name = cinema_name
        self.city_name = city_name
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.standard_id is not None:
            result['StandardId'] = self.standard_id
        if self.schedule_close_time is not None:
            result['ScheduleCloseTime'] = self.schedule_close_time
        if self.city_id is not None:
            result['CityId'] = self.city_id
        if self.cinema_name is not None:
            result['CinemaName'] = self.cinema_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.address is not None:
            result['Address'] = self.address
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')
        if m.get('ScheduleCloseTime') is not None:
            self.schedule_close_time = m.get('ScheduleCloseTime')
        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')
        if m.get('CinemaName') is not None:
            self.cinema_name = m.get('CinemaName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryAllCinemasResponseBodyCinemas(TeaModel):
    def __init__(
        self,
        cinema: List[QueryAllCinemasResponseBodyCinemasCinema] = None,
    ):
        self.cinema = cinema

    def validate(self):
        if self.cinema:
            for k in self.cinema:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Cinema'] = []
        if self.cinema is not None:
            for k in self.cinema:
                result['Cinema'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cinema = []
        if m.get('Cinema') is not None:
            for k in m.get('Cinema'):
                temp_model = QueryAllCinemasResponseBodyCinemasCinema()
                self.cinema.append(temp_model.from_map(k))
        return self


class QueryAllCinemasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        cinemas: QueryAllCinemasResponseBodyCinemas = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.cinemas = cinemas

    def validate(self):
        if self.cinemas:
            self.cinemas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.cinemas is not None:
            result['Cinemas'] = self.cinemas.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Cinemas') is not None:
            temp_model = QueryAllCinemasResponseBodyCinemas()
            self.cinemas = temp_model.from_map(m['Cinemas'])
        return self


class QueryAllCinemasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAllCinemasResponseBody = None,
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
            temp_model = QueryAllCinemasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAllCitiesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        ext_json: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryAllCitiesShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        ext_json_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.ext_json_shrink = ext_json_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.ext_json_shrink is not None:
            result['ExtJson'] = self.ext_json_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ExtJson') is not None:
            self.ext_json_shrink = m.get('ExtJson')
        return self


class QueryAllCitiesResponseBodyCitiesCity(TeaModel):
    def __init__(
        self,
        city_code: int = None,
        parent_id: int = None,
        name: str = None,
        pin_yin: str = None,
        id: int = None,
    ):
        self.city_code = city_code
        self.parent_id = parent_id
        self.name = name
        self.pin_yin = pin_yin
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.name is not None:
            result['Name'] = self.name
        if self.pin_yin is not None:
            result['PinYin'] = self.pin_yin
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PinYin') is not None:
            self.pin_yin = m.get('PinYin')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryAllCitiesResponseBodyCities(TeaModel):
    def __init__(
        self,
        city: List[QueryAllCitiesResponseBodyCitiesCity] = None,
    ):
        self.city = city

    def validate(self):
        if self.city:
            for k in self.city:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['City'] = []
        if self.city is not None:
            for k in self.city:
                result['City'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.city = []
        if m.get('City') is not None:
            for k in m.get('City'):
                temp_model = QueryAllCitiesResponseBodyCitiesCity()
                self.city.append(temp_model.from_map(k))
        return self


class QueryAllCitiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        logs_id: str = None,
        cities: QueryAllCitiesResponseBodyCities = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.logs_id = logs_id
        self.cities = cities

    def validate(self):
        if self.cities:
            self.cities.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.cities is not None:
            result['Cities'] = self.cities.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Cities') is not None:
            temp_model = QueryAllCitiesResponseBodyCities()
            self.cities = temp_model.from_map(m['Cities'])
        return self


class QueryAllCitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryAllCitiesResponseBody = None,
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
            temp_model = QueryAllCitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBatchRegistAnonymousTbAccountResultRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        batch_id: str = None,
    ):
        self.biz_id = biz_id
        self.batch_id = batch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class QueryBatchRegistAnonymousTbAccountResultResponseBodyFailIds(TeaModel):
    def __init__(
        self,
        fail_id: List[str] = None,
    ):
        self.fail_id = fail_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id is not None:
            result['FailId'] = self.fail_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailId') is not None:
            self.fail_id = m.get('FailId')
        return self


class QueryBatchRegistAnonymousTbAccountResultResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        batch_id: str = None,
        fail_ids: QueryBatchRegistAnonymousTbAccountResultResponseBodyFailIds = None,
    ):
        self.status = status
        self.code = code
        self.message = message
        self.request_id = request_id
        self.batch_id = batch_id
        self.fail_ids = fail_ids

    def validate(self):
        if self.fail_ids:
            self.fail_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.fail_ids is not None:
            result['FailIds'] = self.fail_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('FailIds') is not None:
            temp_model = QueryBatchRegistAnonymousTbAccountResultResponseBodyFailIds()
            self.fail_ids = temp_model.from_map(m['FailIds'])
        return self


class QueryBatchRegistAnonymousTbAccountResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBatchRegistAnonymousTbAccountResultResponseBody = None,
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
            temp_model = QueryBatchRegistAnonymousTbAccountResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBestSession4ItemsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lm_item_ids: Dict[str, Any] = None,
        item_ids: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.lm_item_ids = lm_item_ids
        self.item_ids = item_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_item_ids is not None:
            result['LmItemIds'] = self.lm_item_ids
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        return self


class QueryBestSession4ItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lm_item_ids_shrink: str = None,
        item_ids_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.lm_item_ids_shrink = lm_item_ids_shrink
        self.item_ids_shrink = item_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_item_ids_shrink is not None:
            result['LmItemIds'] = self.lm_item_ids_shrink
        if self.item_ids_shrink is not None:
            result['ItemIds'] = self.item_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids_shrink = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids_shrink = m.get('ItemIds')
        return self


class QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelListLmItemActivitySessionModelLmActivitySessionModel(TeaModel):
    def __init__(
        self,
        sub_biz_code: str = None,
        end_date: str = None,
        display_date: str = None,
        lm_session_id: int = None,
        description: str = None,
        start_date: str = None,
        lm_activity_id: int = None,
        biz_id: str = None,
        name: str = None,
        ext_info: Dict[str, Any] = None,
    ):
        self.sub_biz_code = sub_biz_code
        self.end_date = end_date
        self.display_date = display_date
        self.lm_session_id = lm_session_id
        self.description = description
        self.start_date = start_date
        self.lm_activity_id = lm_activity_id
        self.biz_id = biz_id
        self.name = name
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.display_date is not None:
            result['DisplayDate'] = self.display_date
        if self.lm_session_id is not None:
            result['LmSessionId'] = self.lm_session_id
        if self.description is not None:
            result['Description'] = self.description
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DisplayDate') is not None:
            self.display_date = m.get('DisplayDate')
        if m.get('LmSessionId') is not None:
            self.lm_session_id = m.get('LmSessionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelListLmItemActivitySessionModel(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        lm_activity_session_model: QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelListLmItemActivitySessionModelLmActivitySessionModel = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.lm_activity_session_model = lm_activity_session_model

    def validate(self):
        if self.lm_activity_session_model:
            self.lm_activity_session_model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_activity_session_model is not None:
            result['LmActivitySessionModel'] = self.lm_activity_session_model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmActivitySessionModel') is not None:
            temp_model = QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelListLmItemActivitySessionModelLmActivitySessionModel()
            self.lm_activity_session_model = temp_model.from_map(m['LmActivitySessionModel'])
        return self


class QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelList(TeaModel):
    def __init__(
        self,
        lm_item_activity_session_model: List[QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelListLmItemActivitySessionModel] = None,
    ):
        self.lm_item_activity_session_model = lm_item_activity_session_model

    def validate(self):
        if self.lm_item_activity_session_model:
            for k in self.lm_item_activity_session_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmItemActivitySessionModel'] = []
        if self.lm_item_activity_session_model is not None:
            for k in self.lm_item_activity_session_model:
                result['LmItemActivitySessionModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_item_activity_session_model = []
        if m.get('LmItemActivitySessionModel') is not None:
            for k in m.get('LmItemActivitySessionModel'):
                temp_model = QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelListLmItemActivitySessionModel()
                self.lm_item_activity_session_model.append(temp_model.from_map(k))
        return self


class QueryBestSession4ItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        lm_item_activity_session_model_list: QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.lm_item_activity_session_model_list = lm_item_activity_session_model_list

    def validate(self):
        if self.lm_item_activity_session_model_list:
            self.lm_item_activity_session_model_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.lm_item_activity_session_model_list is not None:
            result['LmItemActivitySessionModelList'] = self.lm_item_activity_session_model_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LmItemActivitySessionModelList') is not None:
            temp_model = QueryBestSession4ItemsResponseBodyLmItemActivitySessionModelList()
            self.lm_item_activity_session_model_list = temp_model.from_map(m['LmItemActivitySessionModelList'])
        return self


class QueryBestSession4ItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBestSession4ItemsResponseBody = None,
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
            temp_model = QueryBestSession4ItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBizItemListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_id: str = None,
        page_size: int = None,
        page_number: int = None,
        user_id: str = None,
        lm_item_ids: Dict[str, Any] = None,
        item_ids: Dict[str, Any] = None,
        category_id: int = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_id = sub_biz_id
        self.page_size = page_size
        self.page_number = page_number
        self.user_id = user_id
        self.lm_item_ids = lm_item_ids
        self.item_ids = item_ids
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.lm_item_ids is not None:
            result['LmItemIds'] = self.lm_item_ids
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class QueryBizItemListShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_id: str = None,
        page_size: int = None,
        page_number: int = None,
        user_id: str = None,
        lm_item_ids_shrink: str = None,
        item_ids_shrink: str = None,
        category_id: int = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_id = sub_biz_id
        self.page_size = page_size
        self.page_number = page_number
        self.user_id = user_id
        self.lm_item_ids_shrink = lm_item_ids_shrink
        self.item_ids_shrink = item_ids_shrink
        self.category_id = category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.lm_item_ids_shrink is not None:
            result['LmItemIds'] = self.lm_item_ids_shrink
        if self.item_ids_shrink is not None:
            result['ItemIds'] = self.item_ids_shrink
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids_shrink = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids_shrink = m.get('ItemIds')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        return self


class QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModelsGradePriceModelUserLabelList(TeaModel):
    def __init__(
        self,
        user_label_list: List[str] = None,
    ):
        self.user_label_list = user_label_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_label_list is not None:
            result['UserLabelList'] = self.user_label_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserLabelList') is not None:
            self.user_label_list = m.get('UserLabelList')
        return self


class QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModelsGradePriceModel(TeaModel):
    def __init__(
        self,
        recommend: bool = None,
        show_name: str = None,
        price_cent: int = None,
        icon: str = None,
        point_price: int = None,
        exclusive: bool = None,
        characteristic_name: str = None,
        access_url: str = None,
        sub_biz_code: str = None,
        characteristic_code: str = None,
        can_buy: bool = None,
        points: int = None,
        points_amount: int = None,
        user_label_list: QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModelsGradePriceModelUserLabelList = None,
    ):
        self.recommend = recommend
        self.show_name = show_name
        self.price_cent = price_cent
        self.icon = icon
        self.point_price = point_price
        self.exclusive = exclusive
        self.characteristic_name = characteristic_name
        self.access_url = access_url
        self.sub_biz_code = sub_biz_code
        self.characteristic_code = characteristic_code
        self.can_buy = can_buy
        self.points = points
        self.points_amount = points_amount
        self.user_label_list = user_label_list

    def validate(self):
        if self.user_label_list:
            self.user_label_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend is not None:
            result['Recommend'] = self.recommend
        if self.show_name is not None:
            result['ShowName'] = self.show_name
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.point_price is not None:
            result['PointPrice'] = self.point_price
        if self.exclusive is not None:
            result['Exclusive'] = self.exclusive
        if self.characteristic_name is not None:
            result['CharacteristicName'] = self.characteristic_name
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.characteristic_code is not None:
            result['CharacteristicCode'] = self.characteristic_code
        if self.can_buy is not None:
            result['CanBuy'] = self.can_buy
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.user_label_list is not None:
            result['UserLabelList'] = self.user_label_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Recommend') is not None:
            self.recommend = m.get('Recommend')
        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('PointPrice') is not None:
            self.point_price = m.get('PointPrice')
        if m.get('Exclusive') is not None:
            self.exclusive = m.get('Exclusive')
        if m.get('CharacteristicName') is not None:
            self.characteristic_name = m.get('CharacteristicName')
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('CharacteristicCode') is not None:
            self.characteristic_code = m.get('CharacteristicCode')
        if m.get('CanBuy') is not None:
            self.can_buy = m.get('CanBuy')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('UserLabelList') is not None:
            temp_model = QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModelsGradePriceModelUserLabelList()
            self.user_label_list = temp_model.from_map(m['UserLabelList'])
        return self


class QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModels(TeaModel):
    def __init__(
        self,
        grade_price_model: List[QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModelsGradePriceModel] = None,
    ):
        self.grade_price_model = grade_price_model

    def validate(self):
        if self.grade_price_model:
            for k in self.grade_price_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GradePriceModel'] = []
        if self.grade_price_model is not None:
            for k in self.grade_price_model:
                result['GradePriceModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grade_price_model = []
        if m.get('GradePriceModel') is not None:
            for k in m.get('GradePriceModel'):
                temp_model = QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModelsGradePriceModel()
                self.grade_price_model.append(temp_model.from_map(k))
        return self


class QueryBizItemListResponseBodyItemListItemSkuListSkuUserLabelList(TeaModel):
    def __init__(
        self,
        user_label_list: List[str] = None,
    ):
        self.user_label_list = user_label_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_label_list is not None:
            result['UserLabelList'] = self.user_label_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserLabelList') is not None:
            self.user_label_list = m.get('UserLabelList')
        return self


class QueryBizItemListResponseBodyItemListItemSkuListSku(TeaModel):
    def __init__(
        self,
        price_cent: int = None,
        sku_id: int = None,
        tao_bao_current_price: int = None,
        can_sell: bool = None,
        sku_pic_url: str = None,
        points: int = None,
        sku_title: str = None,
        points_amount: int = None,
        benefit_id: str = None,
        customized_attribute_map: Dict[str, Any] = None,
        grade_price_models: QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModels = None,
        user_label_list: QueryBizItemListResponseBodyItemListItemSkuListSkuUserLabelList = None,
    ):
        self.price_cent = price_cent
        self.sku_id = sku_id
        self.tao_bao_current_price = tao_bao_current_price
        self.can_sell = can_sell
        self.sku_pic_url = sku_pic_url
        self.points = points
        self.sku_title = sku_title
        self.points_amount = points_amount
        self.benefit_id = benefit_id
        self.customized_attribute_map = customized_attribute_map
        self.grade_price_models = grade_price_models
        self.user_label_list = user_label_list

    def validate(self):
        if self.grade_price_models:
            self.grade_price_models.validate()
        if self.user_label_list:
            self.user_label_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.tao_bao_current_price is not None:
            result['TaoBaoCurrentPrice'] = self.tao_bao_current_price
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.points is not None:
            result['Points'] = self.points
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.benefit_id is not None:
            result['BenefitId'] = self.benefit_id
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.grade_price_models is not None:
            result['GradePriceModels'] = self.grade_price_models.to_map()
        if self.user_label_list is not None:
            result['UserLabelList'] = self.user_label_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('TaoBaoCurrentPrice') is not None:
            self.tao_bao_current_price = m.get('TaoBaoCurrentPrice')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('BenefitId') is not None:
            self.benefit_id = m.get('BenefitId')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('GradePriceModels') is not None:
            temp_model = QueryBizItemListResponseBodyItemListItemSkuListSkuGradePriceModels()
            self.grade_price_models = temp_model.from_map(m['GradePriceModels'])
        if m.get('UserLabelList') is not None:
            temp_model = QueryBizItemListResponseBodyItemListItemSkuListSkuUserLabelList()
            self.user_label_list = temp_model.from_map(m['UserLabelList'])
        return self


class QueryBizItemListResponseBodyItemListItemSkuList(TeaModel):
    def __init__(
        self,
        sku: List[QueryBizItemListResponseBodyItemListItemSkuListSku] = None,
    ):
        self.sku = sku

    def validate(self):
        if self.sku:
            for k in self.sku:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sku'] = []
        if self.sku is not None:
            for k in self.sku:
                result['Sku'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sku = []
        if m.get('Sku') is not None:
            for k in m.get('Sku'):
                temp_model = QueryBizItemListResponseBodyItemListItemSkuListSku()
                self.sku.append(temp_model.from_map(k))
        return self


class QueryBizItemListResponseBodyItemListItem(TeaModel):
    def __init__(
        self,
        ext_json: str = None,
        main_pic_url: str = None,
        item_title: str = None,
        lm_item_id: str = None,
        seller_id: int = None,
        category_id: int = None,
        can_sell: bool = None,
        customized_item_name: str = None,
        item_id: int = None,
        reserve_price: int = None,
        taobao_shop_name: str = None,
        sku_list: QueryBizItemListResponseBodyItemListItemSkuList = None,
    ):
        self.ext_json = ext_json
        self.main_pic_url = main_pic_url
        self.item_title = item_title
        self.lm_item_id = lm_item_id
        self.seller_id = seller_id
        self.category_id = category_id
        self.can_sell = can_sell
        self.customized_item_name = customized_item_name
        self.item_id = item_id
        self.reserve_price = reserve_price
        self.taobao_shop_name = taobao_shop_name
        self.sku_list = sku_list

    def validate(self):
        if self.sku_list:
            self.sku_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.customized_item_name is not None:
            result['CustomizedItemName'] = self.customized_item_name
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.taobao_shop_name is not None:
            result['TaobaoShopName'] = self.taobao_shop_name
        if self.sku_list is not None:
            result['SkuList'] = self.sku_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('CustomizedItemName') is not None:
            self.customized_item_name = m.get('CustomizedItemName')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('TaobaoShopName') is not None:
            self.taobao_shop_name = m.get('TaobaoShopName')
        if m.get('SkuList') is not None:
            temp_model = QueryBizItemListResponseBodyItemListItemSkuList()
            self.sku_list = temp_model.from_map(m['SkuList'])
        return self


class QueryBizItemListResponseBodyItemList(TeaModel):
    def __init__(
        self,
        item: List[QueryBizItemListResponseBodyItemListItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryBizItemListResponseBodyItemListItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryBizItemListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        item_list: QueryBizItemListResponseBodyItemList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            self.item_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.item_list is not None:
            result['ItemList'] = self.item_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ItemList') is not None:
            temp_model = QueryBizItemListResponseBodyItemList()
            self.item_list = temp_model.from_map(m['ItemList'])
        return self


class QueryBizItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBizItemListResponseBody = None,
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
            temp_model = QueryBizItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBizItemsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        sub_biz_id: str = None,
        page_size: int = None,
        page_number: int = None,
        user_id: str = None,
    ):
        self.biz_id = biz_id
        self.sub_biz_id = sub_biz_id
        self.page_size = page_size
        self.page_number = page_number
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryBizItemsResponseBody(TeaModel):
    def __init__(
        self,
        model: str = None,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.model = model
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model is not None:
            result['Model'] = self.model
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryBizItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBizItemsResponseBody = None,
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
            temp_model = QueryBizItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBizItemsWithActivityRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lm_item_ids: Dict[str, Any] = None,
        item_ids: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.lm_item_ids = lm_item_ids
        self.item_ids = item_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_item_ids is not None:
            result['LmItemIds'] = self.lm_item_ids
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        return self


class QueryBizItemsWithActivityShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lm_item_ids_shrink: str = None,
        item_ids_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.lm_item_ids_shrink = lm_item_ids_shrink
        self.item_ids_shrink = item_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_item_ids_shrink is not None:
            result['LmItemIds'] = self.lm_item_ids_shrink
        if self.item_ids_shrink is not None:
            result['ItemIds'] = self.item_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids_shrink = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids_shrink = m.get('ItemIds')
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemSkuListSku(TeaModel):
    def __init__(
        self,
        status: int = None,
        price_cent: int = None,
        points_info: str = None,
        max_allowed_count: int = None,
        points_key: str = None,
        sku_id: int = None,
        points: int = None,
        points_amount: int = None,
        quantity: int = None,
    ):
        self.status = status
        self.price_cent = price_cent
        self.points_info = points_info
        self.max_allowed_count = max_allowed_count
        self.points_key = points_key
        self.sku_id = sku_id
        self.points = points
        self.points_amount = points_amount
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.points_info is not None:
            result['PointsInfo'] = self.points_info
        if self.max_allowed_count is not None:
            result['MaxAllowedCount'] = self.max_allowed_count
        if self.points_key is not None:
            result['PointsKey'] = self.points_key
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('PointsInfo') is not None:
            self.points_info = m.get('PointsInfo')
        if m.get('MaxAllowedCount') is not None:
            self.max_allowed_count = m.get('MaxAllowedCount')
        if m.get('PointsKey') is not None:
            self.points_key = m.get('PointsKey')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemSkuList(TeaModel):
    def __init__(
        self,
        sku: List[QueryBizItemsWithActivityResponseBodyItemListItemSkuListSku] = None,
    ):
        self.sku = sku

    def validate(self):
        if self.sku:
            for k in self.sku:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sku'] = []
        if self.sku is not None:
            for k in self.sku:
                result['Sku'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sku = []
        if m.get('Sku') is not None:
            for k in m.get('Sku'):
                temp_model = QueryBizItemsWithActivityResponseBodyItemListItemSkuListSku()
                self.sku.append(temp_model.from_map(k))
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySessionActivitySessionItemActivitySessionItemSkuList(TeaModel):
    def __init__(
        self,
        sku_id: int = None,
        price_cent: int = None,
        points: int = None,
        points_amount: int = None,
    ):
        self.sku_id = sku_id
        self.price_cent = price_cent
        self.points = points
        self.points_amount = points_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySessionActivitySessionItem(TeaModel):
    def __init__(
        self,
        session_quantity: int = None,
        limit_quantity_for_person: int = None,
        saleable_quantity: int = None,
        activity_session_item_sku_list: QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySessionActivitySessionItemActivitySessionItemSkuList = None,
    ):
        self.session_quantity = session_quantity
        self.limit_quantity_for_person = limit_quantity_for_person
        self.saleable_quantity = saleable_quantity
        self.activity_session_item_sku_list = activity_session_item_sku_list

    def validate(self):
        if self.activity_session_item_sku_list:
            self.activity_session_item_sku_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_quantity is not None:
            result['SessionQuantity'] = self.session_quantity
        if self.limit_quantity_for_person is not None:
            result['LimitQuantityForPerson'] = self.limit_quantity_for_person
        if self.saleable_quantity is not None:
            result['SaleableQuantity'] = self.saleable_quantity
        if self.activity_session_item_sku_list is not None:
            result['ActivitySessionItemSkuList'] = self.activity_session_item_sku_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionQuantity') is not None:
            self.session_quantity = m.get('SessionQuantity')
        if m.get('LimitQuantityForPerson') is not None:
            self.limit_quantity_for_person = m.get('LimitQuantityForPerson')
        if m.get('SaleableQuantity') is not None:
            self.saleable_quantity = m.get('SaleableQuantity')
        if m.get('ActivitySessionItemSkuList') is not None:
            temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySessionActivitySessionItemActivitySessionItemSkuList()
            self.activity_session_item_sku_list = temp_model.from_map(m['ActivitySessionItemSkuList'])
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySession(TeaModel):
    def __init__(
        self,
        sub_biz_code: str = None,
        end_date: int = None,
        display_date: int = None,
        lm_session_id: int = None,
        description: str = None,
        start_date: int = None,
        title: str = None,
        activity_session_item: QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySessionActivitySessionItem = None,
    ):
        self.sub_biz_code = sub_biz_code
        self.end_date = end_date
        self.display_date = display_date
        self.lm_session_id = lm_session_id
        self.description = description
        self.start_date = start_date
        self.title = title
        self.activity_session_item = activity_session_item

    def validate(self):
        if self.activity_session_item:
            self.activity_session_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.display_date is not None:
            result['DisplayDate'] = self.display_date
        if self.lm_session_id is not None:
            result['LmSessionId'] = self.lm_session_id
        if self.description is not None:
            result['Description'] = self.description
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.title is not None:
            result['Title'] = self.title
        if self.activity_session_item is not None:
            result['ActivitySessionItem'] = self.activity_session_item.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DisplayDate') is not None:
            self.display_date = m.get('DisplayDate')
        if m.get('LmSessionId') is not None:
            self.lm_session_id = m.get('LmSessionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('ActivitySessionItem') is not None:
            temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySessionActivitySessionItem()
            self.activity_session_item = temp_model.from_map(m['ActivitySessionItem'])
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessions(TeaModel):
    def __init__(
        self,
        activity_session: List[QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySession] = None,
    ):
        self.activity_session = activity_session

    def validate(self):
        if self.activity_session:
            for k in self.activity_session:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActivitySession'] = []
        if self.activity_session is not None:
            for k in self.activity_session:
                result['ActivitySession'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activity_session = []
        if m.get('ActivitySession') is not None:
            for k in m.get('ActivitySession'):
                temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessionsActivitySession()
                self.activity_session.append(temp_model.from_map(k))
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItemActivityItemSkuListActivityItemSku(TeaModel):
    def __init__(
        self,
        activity_price: int = None,
        sku_id: int = None,
    ):
        self.activity_price = activity_price
        self.sku_id = sku_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_price is not None:
            result['ActivityPrice'] = self.activity_price
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityPrice') is not None:
            self.activity_price = m.get('ActivityPrice')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItemActivityItemSkuList(TeaModel):
    def __init__(
        self,
        activity_item_sku: List[QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItemActivityItemSkuListActivityItemSku] = None,
    ):
        self.activity_item_sku = activity_item_sku

    def validate(self):
        if self.activity_item_sku:
            for k in self.activity_item_sku:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActivityItemSku'] = []
        if self.activity_item_sku is not None:
            for k in self.activity_item_sku:
                result['ActivityItemSku'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activity_item_sku = []
        if m.get('ActivityItemSku') is not None:
            for k in m.get('ActivityItemSku'):
                temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItemActivityItemSkuListActivityItemSku()
                self.activity_item_sku.append(temp_model.from_map(k))
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItem(TeaModel):
    def __init__(
        self,
        activity_quantity: int = None,
        limit_quantity_for_person: int = None,
        activity_item_sku_list: QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItemActivityItemSkuList = None,
    ):
        self.activity_quantity = activity_quantity
        self.limit_quantity_for_person = limit_quantity_for_person
        self.activity_item_sku_list = activity_item_sku_list

    def validate(self):
        if self.activity_item_sku_list:
            self.activity_item_sku_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_quantity is not None:
            result['ActivityQuantity'] = self.activity_quantity
        if self.limit_quantity_for_person is not None:
            result['LimitQuantityForPerson'] = self.limit_quantity_for_person
        if self.activity_item_sku_list is not None:
            result['ActivityItemSkuList'] = self.activity_item_sku_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityQuantity') is not None:
            self.activity_quantity = m.get('ActivityQuantity')
        if m.get('LimitQuantityForPerson') is not None:
            self.limit_quantity_for_person = m.get('LimitQuantityForPerson')
        if m.get('ActivityItemSkuList') is not None:
            temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItemActivityItemSkuList()
            self.activity_item_sku_list = temp_model.from_map(m['ActivityItemSkuList'])
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivity(TeaModel):
    def __init__(
        self,
        start_date: int = None,
        lm_activity_id: int = None,
        end_date: int = None,
        title: str = None,
        description: str = None,
        activity_sessions: QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessions = None,
        activity_item: QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItem = None,
    ):
        self.start_date = start_date
        self.lm_activity_id = lm_activity_id
        self.end_date = end_date
        self.title = title
        self.description = description
        self.activity_sessions = activity_sessions
        self.activity_item = activity_item

    def validate(self):
        if self.activity_sessions:
            self.activity_sessions.validate()
        if self.activity_item:
            self.activity_item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.title is not None:
            result['Title'] = self.title
        if self.description is not None:
            result['Description'] = self.description
        if self.activity_sessions is not None:
            result['ActivitySessions'] = self.activity_sessions.to_map()
        if self.activity_item is not None:
            result['ActivityItem'] = self.activity_item.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ActivitySessions') is not None:
            temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivitySessions()
            self.activity_sessions = temp_model.from_map(m['ActivitySessions'])
        if m.get('ActivityItem') is not None:
            temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivityActivityItem()
            self.activity_item = temp_model.from_map(m['ActivityItem'])
        return self


class QueryBizItemsWithActivityResponseBodyItemListItemActivities(TeaModel):
    def __init__(
        self,
        activity: List[QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivity] = None,
    ):
        self.activity = activity

    def validate(self):
        if self.activity:
            for k in self.activity:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Activity'] = []
        if self.activity is not None:
            for k in self.activity:
                result['Activity'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activity = []
        if m.get('Activity') is not None:
            for k in m.get('Activity'):
                temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivitiesActivity()
                self.activity.append(temp_model.from_map(k))
        return self


class QueryBizItemsWithActivityResponseBodyItemListItem(TeaModel):
    def __init__(
        self,
        pic_url: str = None,
        total_sold_quantity: int = None,
        item_title: str = None,
        max_allowed_count: int = None,
        seller_id: int = None,
        lm_item_id: str = None,
        category_id: int = None,
        item_id: int = None,
        reserve_price: int = None,
        quantity: int = None,
        taobao_shop_name: str = None,
        sku_list: QueryBizItemsWithActivityResponseBodyItemListItemSkuList = None,
        activities: QueryBizItemsWithActivityResponseBodyItemListItemActivities = None,
    ):
        self.pic_url = pic_url
        self.total_sold_quantity = total_sold_quantity
        self.item_title = item_title
        self.max_allowed_count = max_allowed_count
        self.seller_id = seller_id
        self.lm_item_id = lm_item_id
        self.category_id = category_id
        self.item_id = item_id
        self.reserve_price = reserve_price
        self.quantity = quantity
        self.taobao_shop_name = taobao_shop_name
        self.sku_list = sku_list
        self.activities = activities

    def validate(self):
        if self.sku_list:
            self.sku_list.validate()
        if self.activities:
            self.activities.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.total_sold_quantity is not None:
            result['TotalSoldQuantity'] = self.total_sold_quantity
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.max_allowed_count is not None:
            result['MaxAllowedCount'] = self.max_allowed_count
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.taobao_shop_name is not None:
            result['TaobaoShopName'] = self.taobao_shop_name
        if self.sku_list is not None:
            result['SkuList'] = self.sku_list.to_map()
        if self.activities is not None:
            result['Activities'] = self.activities.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('TotalSoldQuantity') is not None:
            self.total_sold_quantity = m.get('TotalSoldQuantity')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('MaxAllowedCount') is not None:
            self.max_allowed_count = m.get('MaxAllowedCount')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('TaobaoShopName') is not None:
            self.taobao_shop_name = m.get('TaobaoShopName')
        if m.get('SkuList') is not None:
            temp_model = QueryBizItemsWithActivityResponseBodyItemListItemSkuList()
            self.sku_list = temp_model.from_map(m['SkuList'])
        if m.get('Activities') is not None:
            temp_model = QueryBizItemsWithActivityResponseBodyItemListItemActivities()
            self.activities = temp_model.from_map(m['Activities'])
        return self


class QueryBizItemsWithActivityResponseBodyItemList(TeaModel):
    def __init__(
        self,
        item: List[QueryBizItemsWithActivityResponseBodyItemListItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryBizItemsWithActivityResponseBodyItemListItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryBizItemsWithActivityResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        item_list: QueryBizItemsWithActivityResponseBodyItemList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            self.item_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.item_list is not None:
            result['ItemList'] = self.item_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ItemList') is not None:
            temp_model = QueryBizItemsWithActivityResponseBodyItemList()
            self.item_list = temp_model.from_map(m['ItemList'])
        return self


class QueryBizItemsWithActivityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryBizItemsWithActivityResponseBody = None,
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
            temp_model = QueryBizItemsWithActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGuideItemGroupRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        group_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.biz_id = biz_id
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
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryGuideItemGroupResponseBodyGuideItemGroupItemInfo(TeaModel):
    def __init__(
        self,
        price_cent: int = None,
        main_pic_url: str = None,
        item_title: str = None,
        lm_item_id: str = None,
        point_price: int = None,
        item_id: int = None,
        points: int = None,
        points_amount: int = None,
        reserve_price: str = None,
        item_url: str = None,
    ):
        self.price_cent = price_cent
        self.main_pic_url = main_pic_url
        self.item_title = item_title
        self.lm_item_id = lm_item_id
        self.point_price = point_price
        self.item_id = item_id
        self.points = points
        self.points_amount = points_amount
        self.reserve_price = reserve_price
        self.item_url = item_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.point_price is not None:
            result['PointPrice'] = self.point_price
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PointPrice') is not None:
            self.point_price = m.get('PointPrice')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        return self


class QueryGuideItemGroupResponseBodyGuideItemGroup(TeaModel):
    def __init__(
        self,
        item_info: List[QueryGuideItemGroupResponseBodyGuideItemGroupItemInfo] = None,
    ):
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
        result['ItemInfo'] = []
        if self.item_info is not None:
            for k in self.item_info:
                result['ItemInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_info = []
        if m.get('ItemInfo') is not None:
            for k in m.get('ItemInfo'):
                temp_model = QueryGuideItemGroupResponseBodyGuideItemGroupItemInfo()
                self.item_info.append(temp_model.from_map(k))
        return self


class QueryGuideItemGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        guide_item_group: QueryGuideItemGroupResponseBodyGuideItemGroup = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.guide_item_group = guide_item_group

    def validate(self):
        if self.guide_item_group:
            self.guide_item_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.guide_item_group is not None:
            result['GuideItemGroup'] = self.guide_item_group.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('GuideItemGroup') is not None:
            temp_model = QueryGuideItemGroupResponseBodyGuideItemGroup()
            self.guide_item_group = temp_model.from_map(m['GuideItemGroup'])
        return self


class QueryGuideItemGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGuideItemGroupResponseBody = None,
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
            temp_model = QueryGuideItemGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGuideItemGroupWithOutInventoryRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        page_size: int = None,
        page_number: int = None,
        biz_id: str = None,
    ):
        self.group_id = group_id
        self.page_size = page_size
        self.page_number = page_number
        self.biz_id = biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        return self


class QueryGuideItemGroupWithOutInventoryResponseBodyItemList(TeaModel):
    def __init__(
        self,
        item_title: str = None,
        price_cent: int = None,
        lm_item_id: str = None,
        point_price: int = None,
        item_id: str = None,
        white_pic_url: str = None,
        main_pic_url: str = None,
        points: int = None,
        item_url: str = None,
        points_amount: int = None,
        reserve_price: str = None,
        customized_attribute_map: Dict[str, Any] = None,
        tags: List[str] = None,
    ):
        self.item_title = item_title
        self.price_cent = price_cent
        self.lm_item_id = lm_item_id
        self.point_price = point_price
        self.item_id = item_id
        self.white_pic_url = white_pic_url
        self.main_pic_url = main_pic_url
        self.points = points
        self.item_url = item_url
        self.points_amount = points_amount
        self.reserve_price = reserve_price
        self.customized_attribute_map = customized_attribute_map
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.point_price is not None:
            result['PointPrice'] = self.point_price
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.white_pic_url is not None:
            result['WhitePicUrl'] = self.white_pic_url
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.points is not None:
            result['Points'] = self.points
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PointPrice') is not None:
            self.point_price = m.get('PointPrice')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('WhitePicUrl') is not None:
            self.white_pic_url = m.get('WhitePicUrl')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class QueryGuideItemGroupWithOutInventoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        item_list: List[QueryGuideItemGroupWithOutInventoryResponseBodyItemList] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = QueryGuideItemGroupWithOutInventoryResponseBodyItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class QueryGuideItemGroupWithOutInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryGuideItemGroupWithOutInventoryResponseBody = None,
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
            temp_model = QueryGuideItemGroupWithOutInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHotMoviesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        city_code: int = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.city_code = city_code
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryHotMoviesResponseBodyMoviesMovieMovieTypeList(TeaModel):
    def __init__(
        self,
        movie_type_list: List[str] = None,
    ):
        self.movie_type_list = movie_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.movie_type_list is not None:
            result['MovieTypeList'] = self.movie_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MovieTypeList') is not None:
            self.movie_type_list = m.get('MovieTypeList')
        return self


class QueryHotMoviesResponseBodyMoviesMovieTrailerList(TeaModel):
    def __init__(
        self,
        trailer_list: List[str] = None,
    ):
        self.trailer_list = trailer_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trailer_list is not None:
            result['TrailerList'] = self.trailer_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrailerList') is not None:
            self.trailer_list = m.get('TrailerList')
        return self


class QueryHotMoviesResponseBodyMoviesMovie(TeaModel):
    def __init__(
        self,
        type: str = None,
        movie_version: str = None,
        background_picture: str = None,
        remark: str = None,
        open_day: str = None,
        highlight: str = None,
        language: str = None,
        open_time: str = None,
        director: str = None,
        poster: str = None,
        movie_name: str = None,
        description: str = None,
        country: str = None,
        duration: int = None,
        movie_name_en: str = None,
        leading_role: str = None,
        id: int = None,
        movie_type_list: QueryHotMoviesResponseBodyMoviesMovieMovieTypeList = None,
        trailer_list: QueryHotMoviesResponseBodyMoviesMovieTrailerList = None,
    ):
        self.type = type
        self.movie_version = movie_version
        self.background_picture = background_picture
        self.remark = remark
        self.open_day = open_day
        self.highlight = highlight
        self.language = language
        self.open_time = open_time
        self.director = director
        self.poster = poster
        self.movie_name = movie_name
        self.description = description
        self.country = country
        self.duration = duration
        self.movie_name_en = movie_name_en
        self.leading_role = leading_role
        self.id = id
        self.movie_type_list = movie_type_list
        self.trailer_list = trailer_list

    def validate(self):
        if self.movie_type_list:
            self.movie_type_list.validate()
        if self.trailer_list:
            self.trailer_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.movie_version is not None:
            result['MovieVersion'] = self.movie_version
        if self.background_picture is not None:
            result['BackgroundPicture'] = self.background_picture
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.open_day is not None:
            result['OpenDay'] = self.open_day
        if self.highlight is not None:
            result['Highlight'] = self.highlight
        if self.language is not None:
            result['Language'] = self.language
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.director is not None:
            result['Director'] = self.director
        if self.poster is not None:
            result['Poster'] = self.poster
        if self.movie_name is not None:
            result['MovieName'] = self.movie_name
        if self.description is not None:
            result['Description'] = self.description
        if self.country is not None:
            result['Country'] = self.country
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.movie_name_en is not None:
            result['MovieNameEn'] = self.movie_name_en
        if self.leading_role is not None:
            result['LeadingRole'] = self.leading_role
        if self.id is not None:
            result['Id'] = self.id
        if self.movie_type_list is not None:
            result['MovieTypeList'] = self.movie_type_list.to_map()
        if self.trailer_list is not None:
            result['TrailerList'] = self.trailer_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('MovieVersion') is not None:
            self.movie_version = m.get('MovieVersion')
        if m.get('BackgroundPicture') is not None:
            self.background_picture = m.get('BackgroundPicture')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('OpenDay') is not None:
            self.open_day = m.get('OpenDay')
        if m.get('Highlight') is not None:
            self.highlight = m.get('Highlight')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('Director') is not None:
            self.director = m.get('Director')
        if m.get('Poster') is not None:
            self.poster = m.get('Poster')
        if m.get('MovieName') is not None:
            self.movie_name = m.get('MovieName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MovieNameEn') is not None:
            self.movie_name_en = m.get('MovieNameEn')
        if m.get('LeadingRole') is not None:
            self.leading_role = m.get('LeadingRole')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MovieTypeList') is not None:
            temp_model = QueryHotMoviesResponseBodyMoviesMovieMovieTypeList()
            self.movie_type_list = temp_model.from_map(m['MovieTypeList'])
        if m.get('TrailerList') is not None:
            temp_model = QueryHotMoviesResponseBodyMoviesMovieTrailerList()
            self.trailer_list = temp_model.from_map(m['TrailerList'])
        return self


class QueryHotMoviesResponseBodyMovies(TeaModel):
    def __init__(
        self,
        movie: List[QueryHotMoviesResponseBodyMoviesMovie] = None,
    ):
        self.movie = movie

    def validate(self):
        if self.movie:
            for k in self.movie:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Movie'] = []
        if self.movie is not None:
            for k in self.movie:
                result['Movie'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.movie = []
        if m.get('Movie') is not None:
            for k in m.get('Movie'):
                temp_model = QueryHotMoviesResponseBodyMoviesMovie()
                self.movie.append(temp_model.from_map(k))
        return self


class QueryHotMoviesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        logs_id: str = None,
        movies: QueryHotMoviesResponseBodyMovies = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.logs_id = logs_id
        self.movies = movies

    def validate(self):
        if self.movies:
            self.movies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.movies is not None:
            result['Movies'] = self.movies.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Movies') is not None:
            temp_model = QueryHotMoviesResponseBodyMovies()
            self.movies = temp_model.from_map(m['Movies'])
        return self


class QueryHotMoviesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryHotMoviesResponseBody = None,
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
            temp_model = QueryHotMoviesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInventoryOfItemsInBizItemGroupRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        division_code: str = None,
        item_ids: Dict[str, Any] = None,
        lm_item_ids: Dict[str, Any] = None,
        sub_biz_id: str = None,
    ):
        self.biz_id = biz_id
        self.division_code = division_code
        self.item_ids = item_ids
        self.lm_item_ids = lm_item_ids
        self.sub_biz_id = sub_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        if self.lm_item_ids is not None:
            result['LmItemIds'] = self.lm_item_ids
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids = m.get('LmItemIds')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        return self


class QueryInventoryOfItemsInBizItemGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        division_code: str = None,
        item_ids_shrink: str = None,
        lm_item_ids_shrink: str = None,
        sub_biz_id: str = None,
    ):
        self.biz_id = biz_id
        self.division_code = division_code
        self.item_ids_shrink = item_ids_shrink
        self.lm_item_ids_shrink = lm_item_ids_shrink
        self.sub_biz_id = sub_biz_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.item_ids_shrink is not None:
            result['ItemIds'] = self.item_ids_shrink
        if self.lm_item_ids_shrink is not None:
            result['LmItemIds'] = self.lm_item_ids_shrink
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('ItemIds') is not None:
            self.item_ids_shrink = m.get('ItemIds')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids_shrink = m.get('LmItemIds')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        return self


class QueryInventoryOfItemsInBizItemGroupResponseBodyItemListSkuList(TeaModel):
    def __init__(
        self,
        sku_id: int = None,
        quantity: int = None,
    ):
        self.sku_id = sku_id
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class QueryInventoryOfItemsInBizItemGroupResponseBodyItemList(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        quantity: int = None,
        sku_list: List[QueryInventoryOfItemsInBizItemGroupResponseBodyItemListSkuList] = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.quantity = quantity
        self.sku_list = sku_list

    def validate(self):
        if self.sku_list:
            for k in self.sku_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        result['SkuList'] = []
        if self.sku_list is not None:
            for k in self.sku_list:
                result['SkuList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        self.sku_list = []
        if m.get('SkuList') is not None:
            for k in m.get('SkuList'):
                temp_model = QueryInventoryOfItemsInBizItemGroupResponseBodyItemListSkuList()
                self.sku_list.append(temp_model.from_map(k))
        return self


class QueryInventoryOfItemsInBizItemGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        item_list: List[QueryInventoryOfItemsInBizItemGroupResponseBodyItemList] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = QueryInventoryOfItemsInBizItemGroupResponseBodyItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class QueryInventoryOfItemsInBizItemGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryInventoryOfItemsInBizItemGroupResponseBody = None,
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
            temp_model = QueryInventoryOfItemsInBizItemGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        item_id: int = None,
        lm_item_id: str = None,
    ):
        self.biz_id = biz_id
        self.item_id = item_id
        self.lm_item_id = lm_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        return self


class QueryItemDetailResponseBodyItemSkusSku(TeaModel):
    def __init__(
        self,
        price_cent: int = None,
        lm_item_id: str = None,
        point_price: int = None,
        can_sell: bool = None,
        item_id: int = None,
        sku_title: str = None,
        sku_properties_json: str = None,
        ext_json: str = None,
        sku_properties: str = None,
        sku_id: int = None,
        sku_pic_url: str = None,
        points: int = None,
        reserve_price: int = None,
        points_amount: int = None,
        quantity: int = None,
        customized_attribute_map: Dict[str, Any] = None,
    ):
        self.price_cent = price_cent
        self.lm_item_id = lm_item_id
        self.point_price = point_price
        self.can_sell = can_sell
        self.item_id = item_id
        self.sku_title = sku_title
        self.sku_properties_json = sku_properties_json
        self.ext_json = ext_json
        self.sku_properties = sku_properties
        self.sku_id = sku_id
        self.sku_pic_url = sku_pic_url
        self.points = points
        self.reserve_price = reserve_price
        self.points_amount = points_amount
        self.quantity = quantity
        self.customized_attribute_map = customized_attribute_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.point_price is not None:
            result['PointPrice'] = self.point_price
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.sku_properties_json is not None:
            result['SkuPropertiesJson'] = self.sku_properties_json
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.sku_properties is not None:
            result['SkuProperties'] = self.sku_properties
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.points is not None:
            result['Points'] = self.points
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PointPrice') is not None:
            self.point_price = m.get('PointPrice')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('SkuPropertiesJson') is not None:
            self.sku_properties_json = m.get('SkuPropertiesJson')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('SkuProperties') is not None:
            self.sku_properties = m.get('SkuProperties')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        return self


class QueryItemDetailResponseBodyItemSkus(TeaModel):
    def __init__(
        self,
        sku: List[QueryItemDetailResponseBodyItemSkusSku] = None,
    ):
        self.sku = sku

    def validate(self):
        if self.sku:
            for k in self.sku:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sku'] = []
        if self.sku is not None:
            for k in self.sku:
                result['Sku'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sku = []
        if m.get('Sku') is not None:
            for k in m.get('Sku'):
                temp_model = QueryItemDetailResponseBodyItemSkusSku()
                self.sku.append(temp_model.from_map(k))
        return self


class QueryItemDetailResponseBodyItemItemImages(TeaModel):
    def __init__(
        self,
        item_image: List[str] = None,
    ):
        self.item_image = item_image

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_image is not None:
            result['ItemImage'] = self.item_image
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemImage') is not None:
            self.item_image = m.get('ItemImage')
        return self


class QueryItemDetailResponseBodyItem(TeaModel):
    def __init__(
        self,
        item_title: str = None,
        min_points: int = None,
        desc_option: str = None,
        video_pic_url: str = None,
        ext_json: str = None,
        is_seller_pay_postfee: bool = None,
        lm_item_category: str = None,
        seller_pay_postfee: bool = None,
        reserve_price: int = None,
        quantity: int = None,
        video_url: str = None,
        customized_attribute_map: Dict[str, Any] = None,
        iforest_props_json: str = None,
        properties_json: str = None,
        iforest_props: str = None,
        lm_item_id: str = None,
        seller_id: int = None,
        tb_shop_name: str = None,
        item_id: int = None,
        can_sell: bool = None,
        center_inventory: bool = None,
        seller_type: int = None,
        total_sold_quantity: int = None,
        main_pic_url: str = None,
        min_price: int = None,
        is_can_sell: bool = None,
        category_id: int = None,
        desc_path: str = None,
        properties: str = None,
        skus: QueryItemDetailResponseBodyItemSkus = None,
        item_images: QueryItemDetailResponseBodyItemItemImages = None,
    ):
        self.item_title = item_title
        self.min_points = min_points
        self.desc_option = desc_option
        self.video_pic_url = video_pic_url
        self.ext_json = ext_json
        self.is_seller_pay_postfee = is_seller_pay_postfee
        self.lm_item_category = lm_item_category
        self.seller_pay_postfee = seller_pay_postfee
        self.reserve_price = reserve_price
        self.quantity = quantity
        self.video_url = video_url
        self.customized_attribute_map = customized_attribute_map
        self.iforest_props_json = iforest_props_json
        self.properties_json = properties_json
        self.iforest_props = iforest_props
        self.lm_item_id = lm_item_id
        self.seller_id = seller_id
        self.tb_shop_name = tb_shop_name
        self.item_id = item_id
        self.can_sell = can_sell
        self.center_inventory = center_inventory
        self.seller_type = seller_type
        self.total_sold_quantity = total_sold_quantity
        self.main_pic_url = main_pic_url
        self.min_price = min_price
        self.is_can_sell = is_can_sell
        self.category_id = category_id
        self.desc_path = desc_path
        self.properties = properties
        self.skus = skus
        self.item_images = item_images

    def validate(self):
        if self.skus:
            self.skus.validate()
        if self.item_images:
            self.item_images.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.min_points is not None:
            result['MinPoints'] = self.min_points
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.video_pic_url is not None:
            result['VideoPicUrl'] = self.video_pic_url
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.is_seller_pay_postfee is not None:
            result['IsSellerPayPostfee'] = self.is_seller_pay_postfee
        if self.lm_item_category is not None:
            result['LmItemCategory'] = self.lm_item_category
        if self.seller_pay_postfee is not None:
            result['SellerPayPostfee'] = self.seller_pay_postfee
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        if self.iforest_props_json is not None:
            result['IforestPropsJson'] = self.iforest_props_json
        if self.properties_json is not None:
            result['PropertiesJson'] = self.properties_json
        if self.iforest_props is not None:
            result['IforestProps'] = self.iforest_props
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.tb_shop_name is not None:
            result['TbShopName'] = self.tb_shop_name
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.center_inventory is not None:
            result['CenterInventory'] = self.center_inventory
        if self.seller_type is not None:
            result['SellerType'] = self.seller_type
        if self.total_sold_quantity is not None:
            result['TotalSoldQuantity'] = self.total_sold_quantity
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.min_price is not None:
            result['MinPrice'] = self.min_price
        if self.is_can_sell is not None:
            result['IsCanSell'] = self.is_can_sell
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.desc_path is not None:
            result['DescPath'] = self.desc_path
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.skus is not None:
            result['Skus'] = self.skus.to_map()
        if self.item_images is not None:
            result['ItemImages'] = self.item_images.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('MinPoints') is not None:
            self.min_points = m.get('MinPoints')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('VideoPicUrl') is not None:
            self.video_pic_url = m.get('VideoPicUrl')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('IsSellerPayPostfee') is not None:
            self.is_seller_pay_postfee = m.get('IsSellerPayPostfee')
        if m.get('LmItemCategory') is not None:
            self.lm_item_category = m.get('LmItemCategory')
        if m.get('SellerPayPostfee') is not None:
            self.seller_pay_postfee = m.get('SellerPayPostfee')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        if m.get('IforestPropsJson') is not None:
            self.iforest_props_json = m.get('IforestPropsJson')
        if m.get('PropertiesJson') is not None:
            self.properties_json = m.get('PropertiesJson')
        if m.get('IforestProps') is not None:
            self.iforest_props = m.get('IforestProps')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('TbShopName') is not None:
            self.tb_shop_name = m.get('TbShopName')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('CenterInventory') is not None:
            self.center_inventory = m.get('CenterInventory')
        if m.get('SellerType') is not None:
            self.seller_type = m.get('SellerType')
        if m.get('TotalSoldQuantity') is not None:
            self.total_sold_quantity = m.get('TotalSoldQuantity')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('MinPrice') is not None:
            self.min_price = m.get('MinPrice')
        if m.get('IsCanSell') is not None:
            self.is_can_sell = m.get('IsCanSell')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('DescPath') is not None:
            self.desc_path = m.get('DescPath')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Skus') is not None:
            temp_model = QueryItemDetailResponseBodyItemSkus()
            self.skus = temp_model.from_map(m['Skus'])
        if m.get('ItemImages') is not None:
            temp_model = QueryItemDetailResponseBodyItemItemImages()
            self.item_images = temp_model.from_map(m['ItemImages'])
        return self


class QueryItemDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        item: QueryItemDetailResponseBodyItem = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.item = item

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.item is not None:
            result['Item'] = self.item.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('Item') is not None:
            temp_model = QueryItemDetailResponseBodyItem()
            self.item = temp_model.from_map(m['Item'])
        return self


class QueryItemDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryItemDetailResponseBody = None,
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
            temp_model = QueryItemDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemDetailInnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        item_id: int = None,
        lm_item_id: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        biz_uid: str = None,
        division_code: str = None,
        ip: str = None,
    ):
        self.biz_id = biz_id
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.biz_uid = biz_uid
        self.division_code = division_code
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class QueryItemDetailInnerResponseBodyItemSkus(TeaModel):
    def __init__(
        self,
        status: int = None,
        price_cent: int = None,
        sku_pvs: str = None,
        lm_item_id: str = None,
        point_price: int = None,
        item_id: int = None,
        sku_title: str = None,
        ext_json: str = None,
        sku_id: int = None,
        sku_pic_url: str = None,
        points: int = None,
        points_amount: int = None,
        reserve_price: int = None,
        sku_desc: str = None,
        quantity: int = None,
    ):
        self.status = status
        self.price_cent = price_cent
        self.sku_pvs = sku_pvs
        self.lm_item_id = lm_item_id
        self.point_price = point_price
        self.item_id = item_id
        self.sku_title = sku_title
        self.ext_json = ext_json
        self.sku_id = sku_id
        self.sku_pic_url = sku_pic_url
        self.points = points
        self.points_amount = points_amount
        self.reserve_price = reserve_price
        self.sku_desc = sku_desc
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.sku_pvs is not None:
            result['SkuPvs'] = self.sku_pvs
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.point_price is not None:
            result['PointPrice'] = self.point_price
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.sku_desc is not None:
            result['SkuDesc'] = self.sku_desc
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('SkuPvs') is not None:
            self.sku_pvs = m.get('SkuPvs')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('PointPrice') is not None:
            self.point_price = m.get('PointPrice')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('SkuDesc') is not None:
            self.sku_desc = m.get('SkuDesc')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class QueryItemDetailInnerResponseBodyItemSkuPropertysValues(TeaModel):
    def __init__(
        self,
        text: str = None,
        id: int = None,
    ):
        self.text = text
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryItemDetailInnerResponseBodyItemSkuPropertys(TeaModel):
    def __init__(
        self,
        text: str = None,
        id: int = None,
        values: List[QueryItemDetailInnerResponseBodyItemSkuPropertysValues] = None,
    ):
        self.text = text
        self.id = id
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        if self.id is not None:
            result['Id'] = self.id
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryItemDetailInnerResponseBodyItemSkuPropertysValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryItemDetailInnerResponseBodyItem(TeaModel):
    def __init__(
        self,
        item_title: str = None,
        city: str = None,
        min_points: int = None,
        desc_option: str = None,
        is_seller_pay_postfee: bool = None,
        lm_item_category: str = None,
        seller_pay_postfee: bool = None,
        reserve_price: int = None,
        quantity: int = None,
        seller_id: int = None,
        tb_shop_name: str = None,
        item_id: int = None,
        can_sell: bool = None,
        center_inventory: bool = None,
        total_sold_quantity: int = None,
        main_pic_url: str = None,
        min_price: int = None,
        is_can_sell: bool = None,
        lm_shop_id: int = None,
        category_id: int = None,
        seller_nick: str = None,
        desc_path: str = None,
        properties: Dict[str, Any] = None,
        province: str = None,
        skus: List[QueryItemDetailInnerResponseBodyItemSkus] = None,
        sku_propertys: List[QueryItemDetailInnerResponseBodyItemSkuPropertys] = None,
        category_ids: List[int] = None,
        iforest_props: List[Dict[str, Any]] = None,
        item_images: List[str] = None,
    ):
        self.item_title = item_title
        self.city = city
        self.min_points = min_points
        self.desc_option = desc_option
        self.is_seller_pay_postfee = is_seller_pay_postfee
        self.lm_item_category = lm_item_category
        self.seller_pay_postfee = seller_pay_postfee
        self.reserve_price = reserve_price
        self.quantity = quantity
        self.seller_id = seller_id
        self.tb_shop_name = tb_shop_name
        self.item_id = item_id
        self.can_sell = can_sell
        self.center_inventory = center_inventory
        self.total_sold_quantity = total_sold_quantity
        self.main_pic_url = main_pic_url
        self.min_price = min_price
        self.is_can_sell = is_can_sell
        self.lm_shop_id = lm_shop_id
        self.category_id = category_id
        self.seller_nick = seller_nick
        self.desc_path = desc_path
        self.properties = properties
        self.province = province
        self.skus = skus
        self.sku_propertys = sku_propertys
        self.category_ids = category_ids
        self.iforest_props = iforest_props
        self.item_images = item_images

    def validate(self):
        if self.skus:
            for k in self.skus:
                if k:
                    k.validate()
        if self.sku_propertys:
            for k in self.sku_propertys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.city is not None:
            result['City'] = self.city
        if self.min_points is not None:
            result['MinPoints'] = self.min_points
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.is_seller_pay_postfee is not None:
            result['IsSellerPayPostfee'] = self.is_seller_pay_postfee
        if self.lm_item_category is not None:
            result['LmItemCategory'] = self.lm_item_category
        if self.seller_pay_postfee is not None:
            result['SellerPayPostfee'] = self.seller_pay_postfee
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.tb_shop_name is not None:
            result['TbShopName'] = self.tb_shop_name
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.center_inventory is not None:
            result['CenterInventory'] = self.center_inventory
        if self.total_sold_quantity is not None:
            result['TotalSoldQuantity'] = self.total_sold_quantity
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.min_price is not None:
            result['MinPrice'] = self.min_price
        if self.is_can_sell is not None:
            result['IsCanSell'] = self.is_can_sell
        if self.lm_shop_id is not None:
            result['LmShopId'] = self.lm_shop_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.seller_nick is not None:
            result['SellerNick'] = self.seller_nick
        if self.desc_path is not None:
            result['DescPath'] = self.desc_path
        if self.properties is not None:
            result['Properties'] = self.properties
        if self.province is not None:
            result['Province'] = self.province
        result['Skus'] = []
        if self.skus is not None:
            for k in self.skus:
                result['Skus'].append(k.to_map() if k else None)
        result['SkuPropertys'] = []
        if self.sku_propertys is not None:
            for k in self.sku_propertys:
                result['SkuPropertys'].append(k.to_map() if k else None)
        if self.category_ids is not None:
            result['CategoryIds'] = self.category_ids
        if self.iforest_props is not None:
            result['IforestProps'] = self.iforest_props
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('MinPoints') is not None:
            self.min_points = m.get('MinPoints')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('IsSellerPayPostfee') is not None:
            self.is_seller_pay_postfee = m.get('IsSellerPayPostfee')
        if m.get('LmItemCategory') is not None:
            self.lm_item_category = m.get('LmItemCategory')
        if m.get('SellerPayPostfee') is not None:
            self.seller_pay_postfee = m.get('SellerPayPostfee')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('TbShopName') is not None:
            self.tb_shop_name = m.get('TbShopName')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('CenterInventory') is not None:
            self.center_inventory = m.get('CenterInventory')
        if m.get('TotalSoldQuantity') is not None:
            self.total_sold_quantity = m.get('TotalSoldQuantity')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('MinPrice') is not None:
            self.min_price = m.get('MinPrice')
        if m.get('IsCanSell') is not None:
            self.is_can_sell = m.get('IsCanSell')
        if m.get('LmShopId') is not None:
            self.lm_shop_id = m.get('LmShopId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('SellerNick') is not None:
            self.seller_nick = m.get('SellerNick')
        if m.get('DescPath') is not None:
            self.desc_path = m.get('DescPath')
        if m.get('Properties') is not None:
            self.properties = m.get('Properties')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        self.skus = []
        if m.get('Skus') is not None:
            for k in m.get('Skus'):
                temp_model = QueryItemDetailInnerResponseBodyItemSkus()
                self.skus.append(temp_model.from_map(k))
        self.sku_propertys = []
        if m.get('SkuPropertys') is not None:
            for k in m.get('SkuPropertys'):
                temp_model = QueryItemDetailInnerResponseBodyItemSkuPropertys()
                self.sku_propertys.append(temp_model.from_map(k))
        if m.get('CategoryIds') is not None:
            self.category_ids = m.get('CategoryIds')
        if m.get('IforestProps') is not None:
            self.iforest_props = m.get('IforestProps')
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        return self


class QueryItemDetailInnerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        item: QueryItemDetailInnerResponseBodyItem = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.item = item

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.item is not None:
            result['Item'] = self.item.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Item') is not None:
            temp_model = QueryItemDetailInnerResponseBodyItem()
            self.item = temp_model.from_map(m['Item'])
        return self


class QueryItemDetailInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryItemDetailInnerResponseBody = None,
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
            temp_model = QueryItemDetailInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemInSubBizsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        item_id: int = None,
        lm_item_id: str = None,
        sub_biz_ids: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.sub_biz_ids = sub_biz_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.sub_biz_ids is not None:
            result['SubBizIds'] = self.sub_biz_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SubBizIds') is not None:
            self.sub_biz_ids = m.get('SubBizIds')
        return self


class QueryItemInSubBizsShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        item_id: int = None,
        lm_item_id: str = None,
        sub_biz_ids_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.item_id = item_id
        self.lm_item_id = lm_item_id
        self.sub_biz_ids_shrink = sub_biz_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.sub_biz_ids_shrink is not None:
            result['SubBizIds'] = self.sub_biz_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SubBizIds') is not None:
            self.sub_biz_ids_shrink = m.get('SubBizIds')
        return self


class QueryItemInSubBizsResponseBodyItemBizListSkuList(TeaModel):
    def __init__(
        self,
        price_cent: int = None,
        point_price: int = None,
        can_sell: bool = None,
        sku_title: str = None,
        sku_properties_json: str = None,
        sku_properties: str = None,
        sku_id: int = None,
        sku_pic_url: str = None,
        points: int = None,
        points_amount: int = None,
        reserve_price: int = None,
        benefit_id: str = None,
        customized_attribute_map: Dict[str, Any] = None,
    ):
        self.price_cent = price_cent
        self.point_price = point_price
        self.can_sell = can_sell
        self.sku_title = sku_title
        self.sku_properties_json = sku_properties_json
        self.sku_properties = sku_properties
        self.sku_id = sku_id
        self.sku_pic_url = sku_pic_url
        self.points = points
        self.points_amount = points_amount
        self.reserve_price = reserve_price
        self.benefit_id = benefit_id
        self.customized_attribute_map = customized_attribute_map

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price_cent is not None:
            result['PriceCent'] = self.price_cent
        if self.point_price is not None:
            result['PointPrice'] = self.point_price
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.sku_title is not None:
            result['SkuTitle'] = self.sku_title
        if self.sku_properties_json is not None:
            result['SkuPropertiesJson'] = self.sku_properties_json
        if self.sku_properties is not None:
            result['SkuProperties'] = self.sku_properties
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.sku_pic_url is not None:
            result['SkuPicUrl'] = self.sku_pic_url
        if self.points is not None:
            result['Points'] = self.points
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.benefit_id is not None:
            result['BenefitId'] = self.benefit_id
        if self.customized_attribute_map is not None:
            result['CustomizedAttributeMap'] = self.customized_attribute_map
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceCent') is not None:
            self.price_cent = m.get('PriceCent')
        if m.get('PointPrice') is not None:
            self.point_price = m.get('PointPrice')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('SkuTitle') is not None:
            self.sku_title = m.get('SkuTitle')
        if m.get('SkuPropertiesJson') is not None:
            self.sku_properties_json = m.get('SkuPropertiesJson')
        if m.get('SkuProperties') is not None:
            self.sku_properties = m.get('SkuProperties')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SkuPicUrl') is not None:
            self.sku_pic_url = m.get('SkuPicUrl')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('BenefitId') is not None:
            self.benefit_id = m.get('BenefitId')
        if m.get('CustomizedAttributeMap') is not None:
            self.customized_attribute_map = m.get('CustomizedAttributeMap')
        return self


class QueryItemInSubBizsResponseBodyItemBizList(TeaModel):
    def __init__(
        self,
        item_title: str = None,
        properties_json: str = None,
        lm_item_id: str = None,
        seller_id: int = None,
        tb_shop_name: str = None,
        can_sell: bool = None,
        item_id: int = None,
        desc_option: str = None,
        main_pic_url: str = None,
        category_id: int = None,
        sub_biz_id: str = None,
        reserve_price: int = None,
        quantity: int = None,
        sku_list: List[QueryItemInSubBizsResponseBodyItemBizListSkuList] = None,
        item_images: List[str] = None,
    ):
        self.item_title = item_title
        self.properties_json = properties_json
        self.lm_item_id = lm_item_id
        self.seller_id = seller_id
        self.tb_shop_name = tb_shop_name
        self.can_sell = can_sell
        self.item_id = item_id
        self.desc_option = desc_option
        self.main_pic_url = main_pic_url
        self.category_id = category_id
        self.sub_biz_id = sub_biz_id
        self.reserve_price = reserve_price
        self.quantity = quantity
        self.sku_list = sku_list
        self.item_images = item_images

    def validate(self):
        if self.sku_list:
            for k in self.sku_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.properties_json is not None:
            result['PropertiesJson'] = self.properties_json
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.tb_shop_name is not None:
            result['TbShopName'] = self.tb_shop_name
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.desc_option is not None:
            result['DescOption'] = self.desc_option
        if self.main_pic_url is not None:
            result['MainPicUrl'] = self.main_pic_url
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.sub_biz_id is not None:
            result['SubBizId'] = self.sub_biz_id
        if self.reserve_price is not None:
            result['ReservePrice'] = self.reserve_price
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        result['SkuList'] = []
        if self.sku_list is not None:
            for k in self.sku_list:
                result['SkuList'].append(k.to_map() if k else None)
        if self.item_images is not None:
            result['ItemImages'] = self.item_images
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('PropertiesJson') is not None:
            self.properties_json = m.get('PropertiesJson')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('TbShopName') is not None:
            self.tb_shop_name = m.get('TbShopName')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('DescOption') is not None:
            self.desc_option = m.get('DescOption')
        if m.get('MainPicUrl') is not None:
            self.main_pic_url = m.get('MainPicUrl')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('SubBizId') is not None:
            self.sub_biz_id = m.get('SubBizId')
        if m.get('ReservePrice') is not None:
            self.reserve_price = m.get('ReservePrice')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        self.sku_list = []
        if m.get('SkuList') is not None:
            for k in m.get('SkuList'):
                temp_model = QueryItemInSubBizsResponseBodyItemBizListSkuList()
                self.sku_list.append(temp_model.from_map(k))
        if m.get('ItemImages') is not None:
            self.item_images = m.get('ItemImages')
        return self


class QueryItemInSubBizsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        item_biz_list: List[QueryItemInSubBizsResponseBodyItemBizList] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.item_biz_list = item_biz_list

    def validate(self):
        if self.item_biz_list:
            for k in self.item_biz_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ItemBizList'] = []
        if self.item_biz_list is not None:
            for k in self.item_biz_list:
                result['ItemBizList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.item_biz_list = []
        if m.get('ItemBizList') is not None:
            for k in m.get('ItemBizList'):
                temp_model = QueryItemInSubBizsResponseBodyItemBizList()
                self.item_biz_list.append(temp_model.from_map(k))
        return self


class QueryItemInSubBizsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryItemInSubBizsResponseBody = None,
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
            temp_model = QueryItemInSubBizsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemInventoryRequestItemList(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        sku_id_list: List[int] = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.sku_id_list = sku_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_id_list is not None:
            result['SkuIdList'] = self.sku_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuIdList') is not None:
            self.sku_id_list = m.get('SkuIdList')
        return self


class QueryItemInventoryRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        division_code: str = None,
        ip: str = None,
        item_list: List[QueryItemInventoryRequestItemList] = None,
    ):
        self.biz_id = biz_id
        self.division_code = division_code
        self.ip = ip
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.ip is not None:
            result['Ip'] = self.ip
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = QueryItemInventoryRequestItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class QueryItemInventoryResponseBodyItemListItemSkuListSkuInventory(TeaModel):
    def __init__(
        self,
        quantity: int = None,
    ):
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class QueryItemInventoryResponseBodyItemListItemSkuListSku(TeaModel):
    def __init__(
        self,
        sku_id: int = None,
        inventory: QueryItemInventoryResponseBodyItemListItemSkuListSkuInventory = None,
    ):
        self.sku_id = sku_id
        self.inventory = inventory

    def validate(self):
        if self.inventory:
            self.inventory.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.inventory is not None:
            result['Inventory'] = self.inventory.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Inventory') is not None:
            temp_model = QueryItemInventoryResponseBodyItemListItemSkuListSkuInventory()
            self.inventory = temp_model.from_map(m['Inventory'])
        return self


class QueryItemInventoryResponseBodyItemListItemSkuList(TeaModel):
    def __init__(
        self,
        sku: List[QueryItemInventoryResponseBodyItemListItemSkuListSku] = None,
    ):
        self.sku = sku

    def validate(self):
        if self.sku:
            for k in self.sku:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sku'] = []
        if self.sku is not None:
            for k in self.sku:
                result['Sku'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sku = []
        if m.get('Sku') is not None:
            for k in m.get('Sku'):
                temp_model = QueryItemInventoryResponseBodyItemListItemSkuListSku()
                self.sku.append(temp_model.from_map(k))
        return self


class QueryItemInventoryResponseBodyItemListItem(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        sku_list: QueryItemInventoryResponseBodyItemListItemSkuList = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.sku_list = sku_list

    def validate(self):
        if self.sku_list:
            self.sku_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.sku_list is not None:
            result['SkuList'] = self.sku_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('SkuList') is not None:
            temp_model = QueryItemInventoryResponseBodyItemListItemSkuList()
            self.sku_list = temp_model.from_map(m['SkuList'])
        return self


class QueryItemInventoryResponseBodyItemList(TeaModel):
    def __init__(
        self,
        item: List[QueryItemInventoryResponseBodyItemListItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryItemInventoryResponseBodyItemListItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryItemInventoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        item_list: QueryItemInventoryResponseBodyItemList = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            self.item_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.item_list is not None:
            result['ItemList'] = self.item_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('ItemList') is not None:
            temp_model = QueryItemInventoryResponseBodyItemList()
            self.item_list = temp_model.from_map(m['ItemList'])
        return self


class QueryItemInventoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryItemInventoryResponseBody = None,
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
            temp_model = QueryItemInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLogisticsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        lm_order_id: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.lm_order_id = lm_order_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class QueryLogisticsResponseBodyDataDataLogisticsDetailListLogisticsDetailList(TeaModel):
    def __init__(
        self,
        ocurr_time_str: str = None,
        standerd_desc: str = None,
    ):
        self.ocurr_time_str = ocurr_time_str
        self.standerd_desc = standerd_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocurr_time_str is not None:
            result['OcurrTimeStr'] = self.ocurr_time_str
        if self.standerd_desc is not None:
            result['StanderdDesc'] = self.standerd_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OcurrTimeStr') is not None:
            self.ocurr_time_str = m.get('OcurrTimeStr')
        if m.get('StanderdDesc') is not None:
            self.standerd_desc = m.get('StanderdDesc')
        return self


class QueryLogisticsResponseBodyDataDataLogisticsDetailList(TeaModel):
    def __init__(
        self,
        logistics_detail_list: List[QueryLogisticsResponseBodyDataDataLogisticsDetailListLogisticsDetailList] = None,
    ):
        self.logistics_detail_list = logistics_detail_list

    def validate(self):
        if self.logistics_detail_list:
            for k in self.logistics_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogisticsDetailList'] = []
        if self.logistics_detail_list is not None:
            for k in self.logistics_detail_list:
                result['LogisticsDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logistics_detail_list = []
        if m.get('LogisticsDetailList') is not None:
            for k in m.get('LogisticsDetailList'):
                temp_model = QueryLogisticsResponseBodyDataDataLogisticsDetailListLogisticsDetailList()
                self.logistics_detail_list.append(temp_model.from_map(k))
        return self


class QueryLogisticsResponseBodyDataDataGoodsGoods(TeaModel):
    def __init__(
        self,
        item_id: int = None,
        good_name: str = None,
        quantity: int = None,
    ):
        self.item_id = item_id
        self.good_name = good_name
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.good_name is not None:
            result['GoodName'] = self.good_name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('GoodName') is not None:
            self.good_name = m.get('GoodName')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class QueryLogisticsResponseBodyDataDataGoods(TeaModel):
    def __init__(
        self,
        goods: List[QueryLogisticsResponseBodyDataDataGoodsGoods] = None,
    ):
        self.goods = goods

    def validate(self):
        if self.goods:
            for k in self.goods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Goods'] = []
        if self.goods is not None:
            for k in self.goods:
                result['Goods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.goods = []
        if m.get('Goods') is not None:
            for k in m.get('Goods'):
                temp_model = QueryLogisticsResponseBodyDataDataGoodsGoods()
                self.goods.append(temp_model.from_map(k))
        return self


class QueryLogisticsResponseBodyDataData(TeaModel):
    def __init__(
        self,
        logistics_company_code: str = None,
        mail_no: str = None,
        logistics_company_name: str = None,
        data_provider: str = None,
        data_provider_title: str = None,
        logistics_detail_list: QueryLogisticsResponseBodyDataDataLogisticsDetailList = None,
        goods: QueryLogisticsResponseBodyDataDataGoods = None,
    ):
        self.logistics_company_code = logistics_company_code
        self.mail_no = mail_no
        self.logistics_company_name = logistics_company_name
        self.data_provider = data_provider
        self.data_provider_title = data_provider_title
        self.logistics_detail_list = logistics_detail_list
        self.goods = goods

    def validate(self):
        if self.logistics_detail_list:
            self.logistics_detail_list.validate()
        if self.goods:
            self.goods.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logistics_company_code is not None:
            result['LogisticsCompanyCode'] = self.logistics_company_code
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        if self.logistics_company_name is not None:
            result['LogisticsCompanyName'] = self.logistics_company_name
        if self.data_provider is not None:
            result['DataProvider'] = self.data_provider
        if self.data_provider_title is not None:
            result['DataProviderTitle'] = self.data_provider_title
        if self.logistics_detail_list is not None:
            result['LogisticsDetailList'] = self.logistics_detail_list.to_map()
        if self.goods is not None:
            result['Goods'] = self.goods.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogisticsCompanyCode') is not None:
            self.logistics_company_code = m.get('LogisticsCompanyCode')
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        if m.get('LogisticsCompanyName') is not None:
            self.logistics_company_name = m.get('LogisticsCompanyName')
        if m.get('DataProvider') is not None:
            self.data_provider = m.get('DataProvider')
        if m.get('DataProviderTitle') is not None:
            self.data_provider_title = m.get('DataProviderTitle')
        if m.get('LogisticsDetailList') is not None:
            temp_model = QueryLogisticsResponseBodyDataDataLogisticsDetailList()
            self.logistics_detail_list = temp_model.from_map(m['LogisticsDetailList'])
        if m.get('Goods') is not None:
            temp_model = QueryLogisticsResponseBodyDataDataGoods()
            self.goods = temp_model.from_map(m['Goods'])
        return self


class QueryLogisticsResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[QueryLogisticsResponseBodyDataData] = None,
    ):
        self.data = data

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryLogisticsResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class QueryLogisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        data: QueryLogisticsResponseBodyData = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.data = data

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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryLogisticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryLogisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryLogisticsResponseBody = None,
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
            temp_model = QueryLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMediaSettleInfoRequest(TeaModel):
    def __init__(
        self,
        media_name: str = None,
        channel_id: str = None,
        settle_no: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        ext_info: str = None,
    ):
        self.media_name = media_name
        self.channel_id = channel_id
        self.settle_no = settle_no
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_name is not None:
            result['MediaName'] = self.media_name
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.settle_no is not None:
            result['SettleNo'] = self.settle_no
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaName') is not None:
            self.media_name = m.get('MediaName')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('SettleNo') is not None:
            self.settle_no = m.get('SettleNo')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class QueryMediaSettleInfoResponseBodyModelMediaSettleInfoList(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        media_settle_amount: str = None,
        settle_no: str = None,
        settle_status: str = None,
        channel_id: str = None,
        media_name: str = None,
        media_settle_detail_id: str = None,
        modified_date: str = None,
        create_date: str = None,
        ext_info: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.media_settle_amount = media_settle_amount
        self.settle_no = settle_no
        self.settle_status = settle_status
        self.channel_id = channel_id
        self.media_name = media_name
        self.media_settle_detail_id = media_settle_detail_id
        self.modified_date = modified_date
        self.create_date = create_date
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.media_settle_amount is not None:
            result['MediaSettleAmount'] = self.media_settle_amount
        if self.settle_no is not None:
            result['SettleNo'] = self.settle_no
        if self.settle_status is not None:
            result['SettleStatus'] = self.settle_status
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.media_name is not None:
            result['MediaName'] = self.media_name
        if self.media_settle_detail_id is not None:
            result['MediaSettleDetailId'] = self.media_settle_detail_id
        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('MediaSettleAmount') is not None:
            self.media_settle_amount = m.get('MediaSettleAmount')
        if m.get('SettleNo') is not None:
            self.settle_no = m.get('SettleNo')
        if m.get('SettleStatus') is not None:
            self.settle_status = m.get('SettleStatus')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('MediaName') is not None:
            self.media_name = m.get('MediaName')
        if m.get('MediaSettleDetailId') is not None:
            self.media_settle_detail_id = m.get('MediaSettleDetailId')
        if m.get('ModifiedDate') is not None:
            self.modified_date = m.get('ModifiedDate')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class QueryMediaSettleInfoResponseBodyModel(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        media_settle_info_list: List[QueryMediaSettleInfoResponseBodyModelMediaSettleInfoList] = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.media_settle_info_list = media_settle_info_list

    def validate(self):
        if self.media_settle_info_list:
            for k in self.media_settle_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['MediaSettleInfoList'] = []
        if self.media_settle_info_list is not None:
            for k in self.media_settle_info_list:
                result['MediaSettleInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.media_settle_info_list = []
        if m.get('MediaSettleInfoList') is not None:
            for k in m.get('MediaSettleInfoList'):
                temp_model = QueryMediaSettleInfoResponseBodyModelMediaSettleInfoList()
                self.media_settle_info_list.append(temp_model.from_map(k))
        return self


class QueryMediaSettleInfoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: QueryMediaSettleInfoResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = QueryMediaSettleInfoResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class QueryMediaSettleInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMediaSettleInfoResponseBody = None,
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
            temp_model = QueryMediaSettleInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessagesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        topic: str = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.topic = topic
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryMessagesResponseBodyBizMessagesBizMessage(TeaModel):
    def __init__(
        self,
        content_map_json: str = None,
        pub_time: str = None,
        data_id: int = None,
        topic: str = None,
    ):
        self.content_map_json = content_map_json
        self.pub_time = pub_time
        self.data_id = data_id
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_map_json is not None:
            result['ContentMapJson'] = self.content_map_json
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentMapJson') is not None:
            self.content_map_json = m.get('ContentMapJson')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class QueryMessagesResponseBodyBizMessages(TeaModel):
    def __init__(
        self,
        biz_message: List[QueryMessagesResponseBodyBizMessagesBizMessage] = None,
    ):
        self.biz_message = biz_message

    def validate(self):
        if self.biz_message:
            for k in self.biz_message:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BizMessage'] = []
        if self.biz_message is not None:
            for k in self.biz_message:
                result['BizMessage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_message = []
        if m.get('BizMessage') is not None:
            for k in m.get('BizMessage'):
                temp_model = QueryMessagesResponseBodyBizMessagesBizMessage()
                self.biz_message.append(temp_model.from_map(k))
        return self


class QueryMessagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        sub_code: str = None,
        message: str = None,
        logs_id: str = None,
        biz_messages: QueryMessagesResponseBodyBizMessages = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.sub_code = sub_code
        self.message = message
        self.logs_id = logs_id
        self.biz_messages = biz_messages

    def validate(self):
        if self.biz_messages:
            self.biz_messages.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.message is not None:
            result['Message'] = self.message
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.biz_messages is not None:
            result['BizMessages'] = self.biz_messages.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('BizMessages') is not None:
            temp_model = QueryMessagesResponseBodyBizMessages()
            self.biz_messages = temp_model.from_map(m['BizMessages'])
        return self


class QueryMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMessagesResponseBody = None,
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
            temp_model = QueryMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMovieCommentsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        movie_id: int = None,
        page_number: int = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.movie_id = movie_id
        self.page_number = page_number
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.movie_id is not None:
            result['MovieId'] = self.movie_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('MovieId') is not None:
            self.movie_id = m.get('MovieId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryMovieCommentsResponseBodyCommentListComment(TeaModel):
    def __init__(
        self,
        remark: int = None,
        favor_count: int = None,
        subject: str = None,
        movie_id: int = None,
        nick_name: str = None,
        content: str = None,
        id: int = None,
        comment_time: str = None,
    ):
        self.remark = remark
        self.favor_count = favor_count
        self.subject = subject
        self.movie_id = movie_id
        self.nick_name = nick_name
        self.content = content
        self.id = id
        self.comment_time = comment_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.favor_count is not None:
            result['FavorCount'] = self.favor_count
        if self.subject is not None:
            result['Subject'] = self.subject
        if self.movie_id is not None:
            result['MovieId'] = self.movie_id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.comment_time is not None:
            result['CommentTime'] = self.comment_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('FavorCount') is not None:
            self.favor_count = m.get('FavorCount')
        if m.get('Subject') is not None:
            self.subject = m.get('Subject')
        if m.get('MovieId') is not None:
            self.movie_id = m.get('MovieId')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CommentTime') is not None:
            self.comment_time = m.get('CommentTime')
        return self


class QueryMovieCommentsResponseBodyCommentList(TeaModel):
    def __init__(
        self,
        comment: List[QueryMovieCommentsResponseBodyCommentListComment] = None,
    ):
        self.comment = comment

    def validate(self):
        if self.comment:
            for k in self.comment:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Comment'] = []
        if self.comment is not None:
            for k in self.comment:
                result['Comment'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.comment = []
        if m.get('Comment') is not None:
            for k in m.get('Comment'):
                temp_model = QueryMovieCommentsResponseBodyCommentListComment()
                self.comment.append(temp_model.from_map(k))
        return self


class QueryMovieCommentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        logs_id: str = None,
        count: int = None,
        comment_list: QueryMovieCommentsResponseBodyCommentList = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.logs_id = logs_id
        self.count = count
        self.comment_list = comment_list

    def validate(self):
        if self.comment_list:
            self.comment_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.count is not None:
            result['Count'] = self.count
        if self.comment_list is not None:
            result['CommentList'] = self.comment_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CommentList') is not None:
            temp_model = QueryMovieCommentsResponseBodyCommentList()
            self.comment_list = temp_model.from_map(m['CommentList'])
        return self


class QueryMovieCommentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMovieCommentsResponseBody = None,
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
            temp_model = QueryMovieCommentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMovieSchedulesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        cinema_id: int = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.cinema_id = cinema_id
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.cinema_id is not None:
            result['CinemaId'] = self.cinema_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CinemaId') is not None:
            self.cinema_id = m.get('CinemaId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryMovieSchedulesResponseBodySchedulesSchedule(TeaModel):
    def __init__(
        self,
        movie_version: str = None,
        session_ending_time: str = None,
        max_can_buy: int = None,
        movie_id: int = None,
        schedule_area: str = None,
        hall_name: str = None,
        is_expired: bool = None,
        session_starting_time: str = None,
        price: int = None,
        section_id: str = None,
        release_date: str = None,
        cinema_id: int = None,
        service_fee: int = None,
        id: int = None,
    ):
        self.movie_version = movie_version
        self.session_ending_time = session_ending_time
        self.max_can_buy = max_can_buy
        self.movie_id = movie_id
        self.schedule_area = schedule_area
        self.hall_name = hall_name
        self.is_expired = is_expired
        self.session_starting_time = session_starting_time
        self.price = price
        self.section_id = section_id
        self.release_date = release_date
        self.cinema_id = cinema_id
        self.service_fee = service_fee
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.movie_version is not None:
            result['MovieVersion'] = self.movie_version
        if self.session_ending_time is not None:
            result['SessionEndingTime'] = self.session_ending_time
        if self.max_can_buy is not None:
            result['MaxCanBuy'] = self.max_can_buy
        if self.movie_id is not None:
            result['MovieId'] = self.movie_id
        if self.schedule_area is not None:
            result['ScheduleArea'] = self.schedule_area
        if self.hall_name is not None:
            result['HallName'] = self.hall_name
        if self.is_expired is not None:
            result['IsExpired'] = self.is_expired
        if self.session_starting_time is not None:
            result['SessionStartingTime'] = self.session_starting_time
        if self.price is not None:
            result['Price'] = self.price
        if self.section_id is not None:
            result['SectionId'] = self.section_id
        if self.release_date is not None:
            result['ReleaseDate'] = self.release_date
        if self.cinema_id is not None:
            result['CinemaId'] = self.cinema_id
        if self.service_fee is not None:
            result['ServiceFee'] = self.service_fee
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MovieVersion') is not None:
            self.movie_version = m.get('MovieVersion')
        if m.get('SessionEndingTime') is not None:
            self.session_ending_time = m.get('SessionEndingTime')
        if m.get('MaxCanBuy') is not None:
            self.max_can_buy = m.get('MaxCanBuy')
        if m.get('MovieId') is not None:
            self.movie_id = m.get('MovieId')
        if m.get('ScheduleArea') is not None:
            self.schedule_area = m.get('ScheduleArea')
        if m.get('HallName') is not None:
            self.hall_name = m.get('HallName')
        if m.get('IsExpired') is not None:
            self.is_expired = m.get('IsExpired')
        if m.get('SessionStartingTime') is not None:
            self.session_starting_time = m.get('SessionStartingTime')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('SectionId') is not None:
            self.section_id = m.get('SectionId')
        if m.get('ReleaseDate') is not None:
            self.release_date = m.get('ReleaseDate')
        if m.get('CinemaId') is not None:
            self.cinema_id = m.get('CinemaId')
        if m.get('ServiceFee') is not None:
            self.service_fee = m.get('ServiceFee')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryMovieSchedulesResponseBodySchedules(TeaModel):
    def __init__(
        self,
        schedule: List[QueryMovieSchedulesResponseBodySchedulesSchedule] = None,
    ):
        self.schedule = schedule

    def validate(self):
        if self.schedule:
            for k in self.schedule:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Schedule'] = []
        if self.schedule is not None:
            for k in self.schedule:
                result['Schedule'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.schedule = []
        if m.get('Schedule') is not None:
            for k in m.get('Schedule'):
                temp_model = QueryMovieSchedulesResponseBodySchedulesSchedule()
                self.schedule.append(temp_model.from_map(k))
        return self


class QueryMovieSchedulesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        logs_id: str = None,
        schedules: QueryMovieSchedulesResponseBodySchedules = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.logs_id = logs_id
        self.schedules = schedules

    def validate(self):
        if self.schedules:
            self.schedules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.schedules is not None:
            result['Schedules'] = self.schedules.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Schedules') is not None:
            temp_model = QueryMovieSchedulesResponseBodySchedules()
            self.schedules = temp_model.from_map(m['Schedules'])
        return self


class QueryMovieSchedulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMovieSchedulesResponseBody = None,
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
            temp_model = QueryMovieSchedulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMovieSeatsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        schedule_id: int = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.schedule_id = schedule_id
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryMovieSeatsResponseBodySeatMapSeatsSeat(TeaModel):
    def __init__(
        self,
        status: int = None,
        flag: int = None,
        ext_id: str = None,
        row_name: str = None,
        top_px: int = None,
        area: str = None,
        name: str = None,
        left_px: int = None,
        column: int = None,
        row: int = None,
    ):
        self.status = status
        self.flag = flag
        self.ext_id = ext_id
        self.row_name = row_name
        self.top_px = top_px
        self.area = area
        self.name = name
        self.left_px = left_px
        self.column = column
        self.row = row

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.ext_id is not None:
            result['ExtId'] = self.ext_id
        if self.row_name is not None:
            result['RowName'] = self.row_name
        if self.top_px is not None:
            result['TopPx'] = self.top_px
        if self.area is not None:
            result['Area'] = self.area
        if self.name is not None:
            result['Name'] = self.name
        if self.left_px is not None:
            result['LeftPx'] = self.left_px
        if self.column is not None:
            result['Column'] = self.column
        if self.row is not None:
            result['Row'] = self.row
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('ExtId') is not None:
            self.ext_id = m.get('ExtId')
        if m.get('RowName') is not None:
            self.row_name = m.get('RowName')
        if m.get('TopPx') is not None:
            self.top_px = m.get('TopPx')
        if m.get('Area') is not None:
            self.area = m.get('Area')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LeftPx') is not None:
            self.left_px = m.get('LeftPx')
        if m.get('Column') is not None:
            self.column = m.get('Column')
        if m.get('Row') is not None:
            self.row = m.get('Row')
        return self


class QueryMovieSeatsResponseBodySeatMapSeats(TeaModel):
    def __init__(
        self,
        seat: List[QueryMovieSeatsResponseBodySeatMapSeatsSeat] = None,
    ):
        self.seat = seat

    def validate(self):
        if self.seat:
            for k in self.seat:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Seat'] = []
        if self.seat is not None:
            for k in self.seat:
                result['Seat'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.seat = []
        if m.get('Seat') is not None:
            for k in m.get('Seat'):
                temp_model = QueryMovieSeatsResponseBodySeatMapSeatsSeat()
                self.seat.append(temp_model.from_map(k))
        return self


class QueryMovieSeatsResponseBodySeatMap(TeaModel):
    def __init__(
        self,
        max_can_buy: int = None,
        tip_message: str = None,
        max_row: int = None,
        min_column: int = None,
        min_top_px: int = None,
        notice: str = None,
        max_column: int = None,
        regular: bool = None,
        max_top_px: int = None,
        max_left_px: int = None,
        sold_count: int = None,
        min_row: int = None,
        seat_count: int = None,
        min_left_px: int = None,
        seats: QueryMovieSeatsResponseBodySeatMapSeats = None,
    ):
        self.max_can_buy = max_can_buy
        self.tip_message = tip_message
        self.max_row = max_row
        self.min_column = min_column
        self.min_top_px = min_top_px
        self.notice = notice
        self.max_column = max_column
        self.regular = regular
        self.max_top_px = max_top_px
        self.max_left_px = max_left_px
        self.sold_count = sold_count
        self.min_row = min_row
        self.seat_count = seat_count
        self.min_left_px = min_left_px
        self.seats = seats

    def validate(self):
        if self.seats:
            self.seats.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_can_buy is not None:
            result['MaxCanBuy'] = self.max_can_buy
        if self.tip_message is not None:
            result['TipMessage'] = self.tip_message
        if self.max_row is not None:
            result['MaxRow'] = self.max_row
        if self.min_column is not None:
            result['MinColumn'] = self.min_column
        if self.min_top_px is not None:
            result['MinTopPx'] = self.min_top_px
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.max_column is not None:
            result['MaxColumn'] = self.max_column
        if self.regular is not None:
            result['Regular'] = self.regular
        if self.max_top_px is not None:
            result['MaxTopPx'] = self.max_top_px
        if self.max_left_px is not None:
            result['MaxLeftPx'] = self.max_left_px
        if self.sold_count is not None:
            result['SoldCount'] = self.sold_count
        if self.min_row is not None:
            result['MinRow'] = self.min_row
        if self.seat_count is not None:
            result['SeatCount'] = self.seat_count
        if self.min_left_px is not None:
            result['MinLeftPx'] = self.min_left_px
        if self.seats is not None:
            result['Seats'] = self.seats.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCanBuy') is not None:
            self.max_can_buy = m.get('MaxCanBuy')
        if m.get('TipMessage') is not None:
            self.tip_message = m.get('TipMessage')
        if m.get('MaxRow') is not None:
            self.max_row = m.get('MaxRow')
        if m.get('MinColumn') is not None:
            self.min_column = m.get('MinColumn')
        if m.get('MinTopPx') is not None:
            self.min_top_px = m.get('MinTopPx')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('MaxColumn') is not None:
            self.max_column = m.get('MaxColumn')
        if m.get('Regular') is not None:
            self.regular = m.get('Regular')
        if m.get('MaxTopPx') is not None:
            self.max_top_px = m.get('MaxTopPx')
        if m.get('MaxLeftPx') is not None:
            self.max_left_px = m.get('MaxLeftPx')
        if m.get('SoldCount') is not None:
            self.sold_count = m.get('SoldCount')
        if m.get('MinRow') is not None:
            self.min_row = m.get('MinRow')
        if m.get('SeatCount') is not None:
            self.seat_count = m.get('SeatCount')
        if m.get('MinLeftPx') is not None:
            self.min_left_px = m.get('MinLeftPx')
        if m.get('Seats') is not None:
            temp_model = QueryMovieSeatsResponseBodySeatMapSeats()
            self.seats = temp_model.from_map(m['Seats'])
        return self


class QueryMovieSeatsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        logs_id: str = None,
        seat_map: QueryMovieSeatsResponseBodySeatMap = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.logs_id = logs_id
        self.seat_map = seat_map

    def validate(self):
        if self.seat_map:
            self.seat_map.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.seat_map is not None:
            result['SeatMap'] = self.seat_map.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('SeatMap') is not None:
            temp_model = QueryMovieSeatsResponseBodySeatMap()
            self.seat_map = temp_model.from_map(m['SeatMap'])
        return self


class QueryMovieSeatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMovieSeatsResponseBody = None,
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
            temp_model = QueryMovieSeatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMovieTicketsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        order_id: str = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.order_id = order_id
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryMovieTicketsResponseBodyMovieTicket(TeaModel):
    def __init__(
        self,
        status: str = None,
        tb_order_id: str = None,
        ticket_contents: str = None,
        return_message: str = None,
    ):
        self.status = status
        self.tb_order_id = tb_order_id
        self.ticket_contents = ticket_contents
        self.return_message = return_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.tb_order_id is not None:
            result['TbOrderId'] = self.tb_order_id
        if self.ticket_contents is not None:
            result['TicketContents'] = self.ticket_contents
        if self.return_message is not None:
            result['ReturnMessage'] = self.return_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TbOrderId') is not None:
            self.tb_order_id = m.get('TbOrderId')
        if m.get('TicketContents') is not None:
            self.ticket_contents = m.get('TicketContents')
        if m.get('ReturnMessage') is not None:
            self.return_message = m.get('ReturnMessage')
        return self


class QueryMovieTicketsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        sub_code: str = None,
        message: str = None,
        logs_id: str = None,
        movie_ticket: QueryMovieTicketsResponseBodyMovieTicket = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.sub_code = sub_code
        self.message = message
        self.logs_id = logs_id
        self.movie_ticket = movie_ticket

    def validate(self):
        if self.movie_ticket:
            self.movie_ticket.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.message is not None:
            result['Message'] = self.message
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.movie_ticket is not None:
            result['MovieTicket'] = self.movie_ticket.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('MovieTicket') is not None:
            temp_model = QueryMovieTicketsResponseBodyMovieTicket()
            self.movie_ticket = temp_model.from_map(m['MovieTicket'])
        return self


class QueryMovieTicketsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryMovieTicketsResponseBody = None,
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
            temp_model = QueryMovieTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderAndPaymentListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        page_size: int = None,
        page_number: int = None,
        filter_option: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.page_size = page_size
        self.page_number = page_number
        self.filter_option = filter_option
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.filter_option is not None:
            result['FilterOption'] = self.filter_option
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('FilterOption') is not None:
            self.filter_option = m.get('FilterOption')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class QueryOrderAndPaymentListResponseBodyPostFee(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
    ):
        self.fund_amount = fund_amount
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListFundStructureModelsFundStructureModels(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
    ):
        self.fund_amount = fund_amount
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListFundStructureModels(TeaModel):
    def __init__(
        self,
        fund_structure_models: List[QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListFundStructureModelsFundStructureModels] = None,
    ):
        self.fund_structure_models = fund_structure_models

    def validate(self):
        if self.fund_structure_models:
            for k in self.fund_structure_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FundStructureModels'] = []
        if self.fund_structure_models is not None:
            for k in self.fund_structure_models:
                result['FundStructureModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fund_structure_models = []
        if m.get('FundStructureModels') is not None:
            for k in m.get('FundStructureModels'):
                temp_model = QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListFundStructureModelsFundStructureModels()
                self.fund_structure_models.append(temp_model.from_map(k))
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceListItemPriceList(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
    ):
        self.fund_amount = fund_amount
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceList(TeaModel):
    def __init__(
        self,
        item_price_list: List[QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceListItemPriceList] = None,
    ):
        self.item_price_list = item_price_list

    def validate(self):
        if self.item_price_list:
            for k in self.item_price_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemPriceList'] = []
        if self.item_price_list is not None:
            for k in self.item_price_list:
                result['ItemPriceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_price_list = []
        if m.get('ItemPriceList') is not None:
            for k in m.get('ItemPriceList'):
                temp_model = QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceListItemPriceList()
                self.item_price_list.append(temp_model.from_map(k))
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
        enable_status: int = None,
        item_title: str = None,
        order_status: int = None,
        sku_name: str = None,
        lm_item_id: str = None,
        sku_id: int = None,
        number: int = None,
        tb_order_id: int = None,
        item_pic: str = None,
        item_id: int = None,
        item_price_list: QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceList = None,
    ):
        self.lm_order_id = lm_order_id
        self.enable_status = enable_status
        self.item_title = item_title
        self.order_status = order_status
        self.sku_name = sku_name
        self.lm_item_id = lm_item_id
        self.sku_id = sku_id
        self.number = number
        self.tb_order_id = tb_order_id
        self.item_pic = item_pic
        self.item_id = item_id
        self.item_price_list = item_price_list

    def validate(self):
        if self.item_price_list:
            self.item_price_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.number is not None:
            result['Number'] = self.number
        if self.tb_order_id is not None:
            result['TbOrderId'] = self.tb_order_id
        if self.item_pic is not None:
            result['ItemPic'] = self.item_pic
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_price_list is not None:
            result['ItemPriceList'] = self.item_price_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('TbOrderId') is not None:
            self.tb_order_id = m.get('TbOrderId')
        if m.get('ItemPic') is not None:
            self.item_pic = m.get('ItemPic')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemPriceList') is not None:
            temp_model = QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceList()
            self.item_price_list = temp_model.from_map(m['ItemPriceList'])
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderList(TeaModel):
    def __init__(
        self,
        sub_order_list: List[QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderList] = None,
    ):
        self.sub_order_list = sub_order_list

    def validate(self):
        if self.sub_order_list:
            for k in self.sub_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubOrderList'] = []
        if self.sub_order_list is not None:
            for k in self.sub_order_list:
                result['SubOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_order_list = []
        if m.get('SubOrderList') is not None:
            for k in m.get('SubOrderList'):
                temp_model = QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderList()
                self.sub_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListPostFee(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
    ):
        self.fund_amount = fund_amount
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
        enable_status: int = None,
        ext_json: str = None,
        order_status: int = None,
        lm_payment_id: str = None,
        shop_name: str = None,
        tb_order_id: int = None,
        order_amount: int = None,
        logistics_status: int = None,
        create_date: str = None,
        fund_structure_models: QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListFundStructureModels = None,
        sub_order_list: QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderList = None,
        post_fee: QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListPostFee = None,
    ):
        self.lm_order_id = lm_order_id
        self.enable_status = enable_status
        self.ext_json = ext_json
        self.order_status = order_status
        self.lm_payment_id = lm_payment_id
        self.shop_name = shop_name
        self.tb_order_id = tb_order_id
        self.order_amount = order_amount
        self.logistics_status = logistics_status
        self.create_date = create_date
        self.fund_structure_models = fund_structure_models
        self.sub_order_list = sub_order_list
        self.post_fee = post_fee

    def validate(self):
        if self.fund_structure_models:
            self.fund_structure_models.validate()
        if self.sub_order_list:
            self.sub_order_list.validate()
        if self.post_fee:
            self.post_fee.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.lm_payment_id is not None:
            result['LmPaymentId'] = self.lm_payment_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.tb_order_id is not None:
            result['TbOrderId'] = self.tb_order_id
        if self.order_amount is not None:
            result['OrderAmount'] = self.order_amount
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.fund_structure_models is not None:
            result['FundStructureModels'] = self.fund_structure_models.to_map()
        if self.sub_order_list is not None:
            result['SubOrderList'] = self.sub_order_list.to_map()
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('LmPaymentId') is not None:
            self.lm_payment_id = m.get('LmPaymentId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('TbOrderId') is not None:
            self.tb_order_id = m.get('TbOrderId')
        if m.get('OrderAmount') is not None:
            self.order_amount = m.get('OrderAmount')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FundStructureModels') is not None:
            temp_model = QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListFundStructureModels()
            self.fund_structure_models = temp_model.from_map(m['FundStructureModels'])
        if m.get('SubOrderList') is not None:
            temp_model = QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListSubOrderList()
            self.sub_order_list = temp_model.from_map(m['SubOrderList'])
        if m.get('PostFee') is not None:
            temp_model = QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderListPostFee()
            self.post_fee = temp_model.from_map(m['PostFee'])
        return self


class QueryOrderAndPaymentListResponseBodyLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_list: List[QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderList] = None,
    ):
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.lm_order_list:
            for k in self.lm_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmOrderList'] = []
        if self.lm_order_list is not None:
            for k in self.lm_order_list:
                result['LmOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_order_list = []
        if m.get('LmOrderList') is not None:
            for k in m.get('LmOrderList'):
                temp_model = QueryOrderAndPaymentListResponseBodyLmOrderListLmOrderList()
                self.lm_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderAndPaymentListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        post_fee: QueryOrderAndPaymentListResponseBodyPostFee = None,
        lm_order_list: QueryOrderAndPaymentListResponseBodyLmOrderList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.post_fee = post_fee
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.post_fee:
            self.post_fee.validate()
        if self.lm_order_list:
            self.lm_order_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee.to_map()
        if self.lm_order_list is not None:
            result['LmOrderList'] = self.lm_order_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PostFee') is not None:
            temp_model = QueryOrderAndPaymentListResponseBodyPostFee()
            self.post_fee = temp_model.from_map(m['PostFee'])
        if m.get('LmOrderList') is not None:
            temp_model = QueryOrderAndPaymentListResponseBodyLmOrderList()
            self.lm_order_list = temp_model.from_map(m['LmOrderList'])
        return self


class QueryOrderAndPaymentListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderAndPaymentListResponseBody = None,
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
            temp_model = QueryOrderAndPaymentListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderCommissionRateRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        lm_order_id: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.lm_order_id = lm_order_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfoRateConfigConfigs(TeaModel):
    def __init__(
        self,
        value_unit: str = None,
        value: int = None,
    ):
        self.value_unit = value_unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value_unit is not None:
            result['ValueUnit'] = self.value_unit
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ValueUnit') is not None:
            self.value_unit = m.get('ValueUnit')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfoRateConfig(TeaModel):
    def __init__(
        self,
        configs: List[QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfoRateConfigConfigs] = None,
    ):
        self.configs = configs

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfoRateConfigConfigs()
                self.configs.append(temp_model.from_map(k))
        return self


class QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfo(TeaModel):
    def __init__(
        self,
        rate_type: str = None,
        rate_config: QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfoRateConfig = None,
    ):
        self.rate_type = rate_type
        self.rate_config = rate_config

    def validate(self):
        if self.rate_config:
            self.rate_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate_type is not None:
            result['RateType'] = self.rate_type
        if self.rate_config is not None:
            result['RateConfig'] = self.rate_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RateType') is not None:
            self.rate_type = m.get('RateType')
        if m.get('RateConfig') is not None:
            temp_model = QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfoRateConfig()
            self.rate_config = temp_model.from_map(m['RateConfig'])
        return self


class QueryOrderCommissionRateResponseBodyCommissionModels(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
        commission_info: QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfo = None,
    ):
        self.lm_order_id = lm_order_id
        self.commission_info = commission_info

    def validate(self):
        if self.commission_info:
            self.commission_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.commission_info is not None:
            result['CommissionInfo'] = self.commission_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('CommissionInfo') is not None:
            temp_model = QueryOrderCommissionRateResponseBodyCommissionModelsCommissionInfo()
            self.commission_info = temp_model.from_map(m['CommissionInfo'])
        return self


class QueryOrderCommissionRateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        commission_models: List[QueryOrderCommissionRateResponseBodyCommissionModels] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.commission_models = commission_models

    def validate(self):
        if self.commission_models:
            for k in self.commission_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['CommissionModels'] = []
        if self.commission_models is not None:
            for k in self.commission_models:
                result['CommissionModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.commission_models = []
        if m.get('CommissionModels') is not None:
            for k in m.get('CommissionModels'):
                temp_model = QueryOrderCommissionRateResponseBodyCommissionModels()
                self.commission_models.append(temp_model.from_map(k))
        return self


class QueryOrderCommissionRateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderCommissionRateResponseBody = None,
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
            temp_model = QueryOrderCommissionRateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderDetailInnerRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        filter_option: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.filter_option = filter_option
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.filter_option is not None:
            result['FilterOption'] = self.filter_option
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('FilterOption') is not None:
            self.filter_option = m.get('FilterOption')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        return self


class QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrderItemPriceListItemPrice(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        tb_order_id: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
        tb_sub_order_id: int = None,
    ):
        self.fund_amount = fund_amount
        self.tb_order_id = tb_order_id
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money
        self.tb_sub_order_id = tb_sub_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.tb_order_id is not None:
            result['TbOrderId'] = self.tb_order_id
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        if self.tb_sub_order_id is not None:
            result['TbSubOrderId'] = self.tb_sub_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('TbOrderId') is not None:
            self.tb_order_id = m.get('TbOrderId')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        if m.get('TbSubOrderId') is not None:
            self.tb_sub_order_id = m.get('TbSubOrderId')
        return self


class QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrderItemPriceList(TeaModel):
    def __init__(
        self,
        item_price: List[QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrderItemPriceListItemPrice] = None,
    ):
        self.item_price = item_price

    def validate(self):
        if self.item_price:
            for k in self.item_price:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemPrice'] = []
        if self.item_price is not None:
            for k in self.item_price:
                result['ItemPrice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_price = []
        if m.get('ItemPrice') is not None:
            for k in m.get('ItemPrice'):
                temp_model = QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrderItemPriceListItemPrice()
                self.item_price.append(temp_model.from_map(k))
        return self


class QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrder(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
        item_price_info: str = None,
        item_title: str = None,
        tb_sub_order_id: int = None,
        lm_item_id: str = None,
        total_payment_info: str = None,
        item_pic: str = None,
        item_id: int = None,
        channel_code: str = None,
        pay_status: int = None,
        sku_name: str = None,
        number: int = None,
        sku_id: int = None,
        item_price_list: QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrderItemPriceList = None,
    ):
        self.lm_order_id = lm_order_id
        self.item_price_info = item_price_info
        self.item_title = item_title
        self.tb_sub_order_id = tb_sub_order_id
        self.lm_item_id = lm_item_id
        self.total_payment_info = total_payment_info
        self.item_pic = item_pic
        self.item_id = item_id
        self.channel_code = channel_code
        self.pay_status = pay_status
        self.sku_name = sku_name
        self.number = number
        self.sku_id = sku_id
        self.item_price_list = item_price_list

    def validate(self):
        if self.item_price_list:
            self.item_price_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.item_price_info is not None:
            result['ItemPriceInfo'] = self.item_price_info
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.tb_sub_order_id is not None:
            result['TbSubOrderId'] = self.tb_sub_order_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.total_payment_info is not None:
            result['TotalPaymentInfo'] = self.total_payment_info
        if self.item_pic is not None:
            result['ItemPic'] = self.item_pic
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.number is not None:
            result['Number'] = self.number
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.item_price_list is not None:
            result['ItemPriceList'] = self.item_price_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('ItemPriceInfo') is not None:
            self.item_price_info = m.get('ItemPriceInfo')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('TbSubOrderId') is not None:
            self.tb_sub_order_id = m.get('TbSubOrderId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('TotalPaymentInfo') is not None:
            self.total_payment_info = m.get('TotalPaymentInfo')
        if m.get('ItemPic') is not None:
            self.item_pic = m.get('ItemPic')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('ItemPriceList') is not None:
            temp_model = QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrderItemPriceList()
            self.item_price_list = temp_model.from_map(m['ItemPriceList'])
        return self


class QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderList(TeaModel):
    def __init__(
        self,
        sub_item_order: List[QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrder] = None,
    ):
        self.sub_item_order = sub_item_order

    def validate(self):
        if self.sub_item_order:
            for k in self.sub_item_order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubItemOrder'] = []
        if self.sub_item_order is not None:
            for k in self.sub_item_order:
                result['SubItemOrder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_item_order = []
        if m.get('SubItemOrder') is not None:
            for k in m.get('SubItemOrder'):
                temp_model = QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderListSubItemOrder()
                self.sub_item_order.append(temp_model.from_map(k))
        return self


class QueryOrderDetailInnerResponseBodyModelOrderFundStructureModelsFundStructure(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        lm_order_id: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
        tb_sub_order_id: int = None,
    ):
        self.fund_amount = fund_amount
        self.lm_order_id = lm_order_id
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money
        self.tb_sub_order_id = tb_sub_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        if self.tb_sub_order_id is not None:
            result['TbSubOrderId'] = self.tb_sub_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        if m.get('TbSubOrderId') is not None:
            self.tb_sub_order_id = m.get('TbSubOrderId')
        return self


class QueryOrderDetailInnerResponseBodyModelOrderFundStructureModels(TeaModel):
    def __init__(
        self,
        fund_structure: List[QueryOrderDetailInnerResponseBodyModelOrderFundStructureModelsFundStructure] = None,
    ):
        self.fund_structure = fund_structure

    def validate(self):
        if self.fund_structure:
            for k in self.fund_structure:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FundStructure'] = []
        if self.fund_structure is not None:
            for k in self.fund_structure:
                result['FundStructure'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fund_structure = []
        if m.get('FundStructure') is not None:
            for k in m.get('FundStructure'):
                temp_model = QueryOrderDetailInnerResponseBodyModelOrderFundStructureModelsFundStructure()
                self.fund_structure.append(temp_model.from_map(k))
        return self


class QueryOrderDetailInnerResponseBodyModelOrderPostFee(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        lm_order_id: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
        tb_sub_order_id: int = None,
    ):
        self.fund_amount = fund_amount
        self.lm_order_id = lm_order_id
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money
        self.tb_sub_order_id = tb_sub_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        if self.tb_sub_order_id is not None:
            result['TbSubOrderId'] = self.tb_sub_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        if m.get('TbSubOrderId') is not None:
            self.tb_sub_order_id = m.get('TbSubOrderId')
        return self


class QueryOrderDetailInnerResponseBodyModelOrder(TeaModel):
    def __init__(
        self,
        eticket: bool = None,
        create_date: str = None,
        logistics_comp_name: str = None,
        channel_code: str = None,
        logistics_mobile_phone: str = None,
        res_ext_info: str = None,
        enable_status: int = None,
        channel_biz_type: str = None,
        shipping: str = None,
        order_pay_info: str = None,
        logistics_status_desc: str = None,
        tb_order_id: str = None,
        logistics_status: int = None,
        lm_order_id: int = None,
        seller_id: int = None,
        shop_name: str = None,
        order_amount: int = None,
        ext_info: Dict[str, Any] = None,
        end_time: int = None,
        pay_status: int = None,
        logistics_no: str = None,
        logistics_user_name: str = None,
        logistics_address: str = None,
        pay_water_status: int = None,
        refund_status: int = None,
        seller_nick: str = None,
        channel_order_id: str = None,
        sub_item_order_list: QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderList = None,
        fund_structure_models: QueryOrderDetailInnerResponseBodyModelOrderFundStructureModels = None,
        post_fee: QueryOrderDetailInnerResponseBodyModelOrderPostFee = None,
    ):
        self.eticket = eticket
        self.create_date = create_date
        self.logistics_comp_name = logistics_comp_name
        self.channel_code = channel_code
        self.logistics_mobile_phone = logistics_mobile_phone
        self.res_ext_info = res_ext_info
        self.enable_status = enable_status
        self.channel_biz_type = channel_biz_type
        self.shipping = shipping
        self.order_pay_info = order_pay_info
        self.logistics_status_desc = logistics_status_desc
        self.tb_order_id = tb_order_id
        self.logistics_status = logistics_status
        self.lm_order_id = lm_order_id
        self.seller_id = seller_id
        self.shop_name = shop_name
        self.order_amount = order_amount
        self.ext_info = ext_info
        self.end_time = end_time
        self.pay_status = pay_status
        self.logistics_no = logistics_no
        self.logistics_user_name = logistics_user_name
        self.logistics_address = logistics_address
        self.pay_water_status = pay_water_status
        self.refund_status = refund_status
        self.seller_nick = seller_nick
        self.channel_order_id = channel_order_id
        self.sub_item_order_list = sub_item_order_list
        self.fund_structure_models = fund_structure_models
        self.post_fee = post_fee

    def validate(self):
        if self.sub_item_order_list:
            self.sub_item_order_list.validate()
        if self.fund_structure_models:
            self.fund_structure_models.validate()
        if self.post_fee:
            self.post_fee.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eticket is not None:
            result['Eticket'] = self.eticket
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.logistics_comp_name is not None:
            result['LogisticsCompName'] = self.logistics_comp_name
        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code
        if self.logistics_mobile_phone is not None:
            result['LogisticsMobilePhone'] = self.logistics_mobile_phone
        if self.res_ext_info is not None:
            result['ResExtInfo'] = self.res_ext_info
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
        if self.channel_biz_type is not None:
            result['ChannelBizType'] = self.channel_biz_type
        if self.shipping is not None:
            result['Shipping'] = self.shipping
        if self.order_pay_info is not None:
            result['OrderPayInfo'] = self.order_pay_info
        if self.logistics_status_desc is not None:
            result['LogisticsStatusDesc'] = self.logistics_status_desc
        if self.tb_order_id is not None:
            result['TbOrderId'] = self.tb_order_id
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.order_amount is not None:
            result['OrderAmount'] = self.order_amount
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.logistics_user_name is not None:
            result['LogisticsUserName'] = self.logistics_user_name
        if self.logistics_address is not None:
            result['LogisticsAddress'] = self.logistics_address
        if self.pay_water_status is not None:
            result['PayWaterStatus'] = self.pay_water_status
        if self.refund_status is not None:
            result['RefundStatus'] = self.refund_status
        if self.seller_nick is not None:
            result['SellerNick'] = self.seller_nick
        if self.channel_order_id is not None:
            result['ChannelOrderId'] = self.channel_order_id
        if self.sub_item_order_list is not None:
            result['SubItemOrderList'] = self.sub_item_order_list.to_map()
        if self.fund_structure_models is not None:
            result['FundStructureModels'] = self.fund_structure_models.to_map()
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Eticket') is not None:
            self.eticket = m.get('Eticket')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('LogisticsCompName') is not None:
            self.logistics_comp_name = m.get('LogisticsCompName')
        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')
        if m.get('LogisticsMobilePhone') is not None:
            self.logistics_mobile_phone = m.get('LogisticsMobilePhone')
        if m.get('ResExtInfo') is not None:
            self.res_ext_info = m.get('ResExtInfo')
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('ChannelBizType') is not None:
            self.channel_biz_type = m.get('ChannelBizType')
        if m.get('Shipping') is not None:
            self.shipping = m.get('Shipping')
        if m.get('OrderPayInfo') is not None:
            self.order_pay_info = m.get('OrderPayInfo')
        if m.get('LogisticsStatusDesc') is not None:
            self.logistics_status_desc = m.get('LogisticsStatusDesc')
        if m.get('TbOrderId') is not None:
            self.tb_order_id = m.get('TbOrderId')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('OrderAmount') is not None:
            self.order_amount = m.get('OrderAmount')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('LogisticsUserName') is not None:
            self.logistics_user_name = m.get('LogisticsUserName')
        if m.get('LogisticsAddress') is not None:
            self.logistics_address = m.get('LogisticsAddress')
        if m.get('PayWaterStatus') is not None:
            self.pay_water_status = m.get('PayWaterStatus')
        if m.get('RefundStatus') is not None:
            self.refund_status = m.get('RefundStatus')
        if m.get('SellerNick') is not None:
            self.seller_nick = m.get('SellerNick')
        if m.get('ChannelOrderId') is not None:
            self.channel_order_id = m.get('ChannelOrderId')
        if m.get('SubItemOrderList') is not None:
            temp_model = QueryOrderDetailInnerResponseBodyModelOrderSubItemOrderList()
            self.sub_item_order_list = temp_model.from_map(m['SubItemOrderList'])
        if m.get('FundStructureModels') is not None:
            temp_model = QueryOrderDetailInnerResponseBodyModelOrderFundStructureModels()
            self.fund_structure_models = temp_model.from_map(m['FundStructureModels'])
        if m.get('PostFee') is not None:
            temp_model = QueryOrderDetailInnerResponseBodyModelOrderPostFee()
            self.post_fee = temp_model.from_map(m['PostFee'])
        return self


class QueryOrderDetailInnerResponseBodyModel(TeaModel):
    def __init__(
        self,
        order: QueryOrderDetailInnerResponseBodyModelOrder = None,
    ):
        self.order = order

    def validate(self):
        if self.order:
            self.order.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['order'] = self.order.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order') is not None:
            temp_model = QueryOrderDetailInnerResponseBodyModelOrder()
            self.order = temp_model.from_map(m['order'])
        return self


class QueryOrderDetailInnerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        model: QueryOrderDetailInnerResponseBodyModel = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Model') is not None:
            temp_model = QueryOrderDetailInnerResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class QueryOrderDetailInnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderDetailInnerResponseBody = None,
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
            temp_model = QueryOrderDetailInnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderIdByPayIdRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        payment_id: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.payment_id = payment_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.payment_id is not None:
            result['PaymentId'] = self.payment_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('PaymentId') is not None:
            self.payment_id = m.get('PaymentId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class QueryOrderIdByPayIdResponseBodyLmOrderIdsLmOrderIds(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
    ):
        self.lm_order_id = lm_order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        return self


class QueryOrderIdByPayIdResponseBodyLmOrderIds(TeaModel):
    def __init__(
        self,
        lm_order_ids: List[QueryOrderIdByPayIdResponseBodyLmOrderIdsLmOrderIds] = None,
    ):
        self.lm_order_ids = lm_order_ids

    def validate(self):
        if self.lm_order_ids:
            for k in self.lm_order_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmOrderIds'] = []
        if self.lm_order_ids is not None:
            for k in self.lm_order_ids:
                result['LmOrderIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_order_ids = []
        if m.get('LmOrderIds') is not None:
            for k in m.get('LmOrderIds'):
                temp_model = QueryOrderIdByPayIdResponseBodyLmOrderIdsLmOrderIds()
                self.lm_order_ids.append(temp_model.from_map(k))
        return self


class QueryOrderIdByPayIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        lm_order_ids: QueryOrderIdByPayIdResponseBodyLmOrderIds = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.lm_order_ids = lm_order_ids

    def validate(self):
        if self.lm_order_ids:
            self.lm_order_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.lm_order_ids is not None:
            result['LmOrderIds'] = self.lm_order_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LmOrderIds') is not None:
            temp_model = QueryOrderIdByPayIdResponseBodyLmOrderIds()
            self.lm_order_ids = temp_model.from_map(m['LmOrderIds'])
        return self


class QueryOrderIdByPayIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderIdByPayIdResponseBody = None,
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
            temp_model = QueryOrderIdByPayIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderInfoAfterSaleRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        channel_user_id: str = None,
        lm_order_id: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.channel_user_id = channel_user_id
        self.lm_order_id = lm_order_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.channel_user_id is not None:
            result['ChannelUserId'] = self.channel_user_id
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ChannelUserId') is not None:
            self.channel_user_id = m.get('ChannelUserId')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class QueryOrderInfoAfterSaleResponseBodyModelLogisticsListLogistics(TeaModel):
    def __init__(
        self,
        logistics_company_code: str = None,
        logistics_no: str = None,
        logistics_status: str = None,
        logistics_company_name: str = None,
    ):
        self.logistics_company_code = logistics_company_code
        self.logistics_no = logistics_no
        self.logistics_status = logistics_status
        self.logistics_company_name = logistics_company_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logistics_company_code is not None:
            result['LogisticsCompanyCode'] = self.logistics_company_code
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.logistics_company_name is not None:
            result['LogisticsCompanyName'] = self.logistics_company_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogisticsCompanyCode') is not None:
            self.logistics_company_code = m.get('LogisticsCompanyCode')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('LogisticsCompanyName') is not None:
            self.logistics_company_name = m.get('LogisticsCompanyName')
        return self


class QueryOrderInfoAfterSaleResponseBodyModelLogisticsList(TeaModel):
    def __init__(
        self,
        logistics: List[QueryOrderInfoAfterSaleResponseBodyModelLogisticsListLogistics] = None,
    ):
        self.logistics = logistics

    def validate(self):
        if self.logistics:
            for k in self.logistics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Logistics'] = []
        if self.logistics is not None:
            for k in self.logistics:
                result['Logistics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logistics = []
        if m.get('Logistics') is not None:
            for k in m.get('Logistics'):
                temp_model = QueryOrderInfoAfterSaleResponseBodyModelLogisticsListLogistics()
                self.logistics.append(temp_model.from_map(k))
        return self


class QueryOrderInfoAfterSaleResponseBodyModel(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
        shop_service_telephone: str = None,
        refund_amount: int = None,
        xiaomi_code: str = None,
        shop_name: str = None,
        create_date: str = None,
        refund_rate: str = None,
        ext_json: str = None,
        order_status: str = None,
        refund_points: int = None,
        tb_order_id: int = None,
        points: int = None,
        refund_status: str = None,
        points_amount: int = None,
        cash_amount: str = None,
        logistics_list: QueryOrderInfoAfterSaleResponseBodyModelLogisticsList = None,
    ):
        self.lm_order_id = lm_order_id
        self.shop_service_telephone = shop_service_telephone
        self.refund_amount = refund_amount
        self.xiaomi_code = xiaomi_code
        self.shop_name = shop_name
        self.create_date = create_date
        self.refund_rate = refund_rate
        self.ext_json = ext_json
        self.order_status = order_status
        self.refund_points = refund_points
        self.tb_order_id = tb_order_id
        self.points = points
        self.refund_status = refund_status
        self.points_amount = points_amount
        self.cash_amount = cash_amount
        self.logistics_list = logistics_list

    def validate(self):
        if self.logistics_list:
            self.logistics_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.shop_service_telephone is not None:
            result['ShopServiceTelephone'] = self.shop_service_telephone
        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount
        if self.xiaomi_code is not None:
            result['XiaomiCode'] = self.xiaomi_code
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.refund_rate is not None:
            result['RefundRate'] = self.refund_rate
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.refund_points is not None:
            result['RefundPoints'] = self.refund_points
        if self.tb_order_id is not None:
            result['TbOrderId'] = self.tb_order_id
        if self.points is not None:
            result['Points'] = self.points
        if self.refund_status is not None:
            result['RefundStatus'] = self.refund_status
        if self.points_amount is not None:
            result['PointsAmount'] = self.points_amount
        if self.cash_amount is not None:
            result['CashAmount'] = self.cash_amount
        if self.logistics_list is not None:
            result['LogisticsList'] = self.logistics_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('ShopServiceTelephone') is not None:
            self.shop_service_telephone = m.get('ShopServiceTelephone')
        if m.get('RefundAmount') is not None:
            self.refund_amount = m.get('RefundAmount')
        if m.get('XiaomiCode') is not None:
            self.xiaomi_code = m.get('XiaomiCode')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('RefundRate') is not None:
            self.refund_rate = m.get('RefundRate')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('RefundPoints') is not None:
            self.refund_points = m.get('RefundPoints')
        if m.get('TbOrderId') is not None:
            self.tb_order_id = m.get('TbOrderId')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('RefundStatus') is not None:
            self.refund_status = m.get('RefundStatus')
        if m.get('PointsAmount') is not None:
            self.points_amount = m.get('PointsAmount')
        if m.get('CashAmount') is not None:
            self.cash_amount = m.get('CashAmount')
        if m.get('LogisticsList') is not None:
            temp_model = QueryOrderInfoAfterSaleResponseBodyModelLogisticsList()
            self.logistics_list = temp_model.from_map(m['LogisticsList'])
        return self


class QueryOrderInfoAfterSaleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        model: QueryOrderInfoAfterSaleResponseBodyModel = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Model') is not None:
            temp_model = QueryOrderInfoAfterSaleResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class QueryOrderInfoAfterSaleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderInfoAfterSaleResponseBody = None,
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
            temp_model = QueryOrderInfoAfterSaleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderItemInfoByPaymentIdForAiZhanYouRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        payment_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.payment_id = payment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.payment_id is not None:
            result['PaymentId'] = self.payment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('PaymentId') is not None:
            self.payment_id = m.get('PaymentId')
        return self


class QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBodyLmOrderListLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
        item_name: str = None,
        sku_name: str = None,
        sku_id: int = None,
        lm_item_id: str = None,
        item_id: int = None,
    ):
        self.lm_order_id = lm_order_id
        self.item_name = item_name
        self.sku_name = sku_name
        self.sku_id = sku_id
        self.lm_item_id = lm_item_id
        self.item_id = item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBodyLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_list: List[QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBodyLmOrderListLmOrderList] = None,
    ):
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.lm_order_list:
            for k in self.lm_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmOrderList'] = []
        if self.lm_order_list is not None:
            for k in self.lm_order_list:
                result['LmOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_order_list = []
        if m.get('LmOrderList') is not None:
            for k in m.get('LmOrderList'):
                temp_model = QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBodyLmOrderListLmOrderList()
                self.lm_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        lm_order_list: QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBodyLmOrderList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.lm_order_list:
            self.lm_order_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.lm_order_list is not None:
            result['LmOrderList'] = self.lm_order_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LmOrderList') is not None:
            temp_model = QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBodyLmOrderList()
            self.lm_order_list = temp_model.from_map(m['LmOrderList'])
        return self


class QueryOrderItemInfoByPaymentIdForAiZhanYouResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBody = None,
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
            temp_model = QueryOrderItemInfoByPaymentIdForAiZhanYouResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderListRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        page_size: int = None,
        page_number: int = None,
        filter_option: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.page_size = page_size
        self.page_number = page_number
        self.filter_option = filter_option
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.filter_option is not None:
            result['FilterOption'] = self.filter_option
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('FilterOption') is not None:
            self.filter_option = m.get('FilterOption')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class QueryOrderListResponseBodyPostFee(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
    ):
        self.fund_amount = fund_amount
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderListResponseBodyLmOrderListLmOrderListFundStructureModelsFundStructureModels(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
    ):
        self.fund_amount = fund_amount
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderListResponseBodyLmOrderListLmOrderListFundStructureModels(TeaModel):
    def __init__(
        self,
        fund_structure_models: List[QueryOrderListResponseBodyLmOrderListLmOrderListFundStructureModelsFundStructureModels] = None,
    ):
        self.fund_structure_models = fund_structure_models

    def validate(self):
        if self.fund_structure_models:
            for k in self.fund_structure_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FundStructureModels'] = []
        if self.fund_structure_models is not None:
            for k in self.fund_structure_models:
                result['FundStructureModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fund_structure_models = []
        if m.get('FundStructureModels') is not None:
            for k in m.get('FundStructureModels'):
                temp_model = QueryOrderListResponseBodyLmOrderListLmOrderListFundStructureModelsFundStructureModels()
                self.fund_structure_models.append(temp_model.from_map(k))
        return self


class QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceListItemPriceList(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
    ):
        self.fund_amount = fund_amount
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceList(TeaModel):
    def __init__(
        self,
        item_price_list: List[QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceListItemPriceList] = None,
    ):
        self.item_price_list = item_price_list

    def validate(self):
        if self.item_price_list:
            for k in self.item_price_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemPriceList'] = []
        if self.item_price_list is not None:
            for k in self.item_price_list:
                result['ItemPriceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_price_list = []
        if m.get('ItemPriceList') is not None:
            for k in m.get('ItemPriceList'):
                temp_model = QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceListItemPriceList()
                self.item_price_list.append(temp_model.from_map(k))
        return self


class QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
        enable_status: int = None,
        item_title: str = None,
        order_status: int = None,
        sku_name: str = None,
        lm_item_id: str = None,
        sku_id: int = None,
        number: int = None,
        tb_order_id: int = None,
        item_pic: str = None,
        item_id: int = None,
        item_price_list: QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceList = None,
    ):
        self.lm_order_id = lm_order_id
        self.enable_status = enable_status
        self.item_title = item_title
        self.order_status = order_status
        self.sku_name = sku_name
        self.lm_item_id = lm_item_id
        self.sku_id = sku_id
        self.number = number
        self.tb_order_id = tb_order_id
        self.item_pic = item_pic
        self.item_id = item_id
        self.item_price_list = item_price_list

    def validate(self):
        if self.item_price_list:
            self.item_price_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.number is not None:
            result['Number'] = self.number
        if self.tb_order_id is not None:
            result['TbOrderId'] = self.tb_order_id
        if self.item_pic is not None:
            result['ItemPic'] = self.item_pic
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_price_list is not None:
            result['ItemPriceList'] = self.item_price_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('TbOrderId') is not None:
            self.tb_order_id = m.get('TbOrderId')
        if m.get('ItemPic') is not None:
            self.item_pic = m.get('ItemPic')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemPriceList') is not None:
            temp_model = QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderListItemPriceList()
            self.item_price_list = temp_model.from_map(m['ItemPriceList'])
        return self


class QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderList(TeaModel):
    def __init__(
        self,
        sub_order_list: List[QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderList] = None,
    ):
        self.sub_order_list = sub_order_list

    def validate(self):
        if self.sub_order_list:
            for k in self.sub_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubOrderList'] = []
        if self.sub_order_list is not None:
            for k in self.sub_order_list:
                result['SubOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_order_list = []
        if m.get('SubOrderList') is not None:
            for k in m.get('SubOrderList'):
                temp_model = QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderListSubOrderList()
                self.sub_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderListResponseBodyLmOrderListLmOrderListPostFee(TeaModel):
    def __init__(
        self,
        fund_amount: int = None,
        fund_type: str = None,
        fund_amount_money: int = None,
    ):
        self.fund_amount = fund_amount
        self.fund_type = fund_type
        self.fund_amount_money = fund_amount_money

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_amount is not None:
            result['FundAmount'] = self.fund_amount
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.fund_amount_money is not None:
            result['FundAmountMoney'] = self.fund_amount_money
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundAmount') is not None:
            self.fund_amount = m.get('FundAmount')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('FundAmountMoney') is not None:
            self.fund_amount_money = m.get('FundAmountMoney')
        return self


class QueryOrderListResponseBodyLmOrderListLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_id: int = None,
        enable_status: int = None,
        ext_json: str = None,
        order_status: int = None,
        shop_name: str = None,
        tb_order_id: int = None,
        order_amount: int = None,
        logistics_status: int = None,
        create_date: str = None,
        fund_structure_models: QueryOrderListResponseBodyLmOrderListLmOrderListFundStructureModels = None,
        sub_order_list: QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderList = None,
        post_fee: QueryOrderListResponseBodyLmOrderListLmOrderListPostFee = None,
    ):
        self.lm_order_id = lm_order_id
        self.enable_status = enable_status
        self.ext_json = ext_json
        self.order_status = order_status
        self.shop_name = shop_name
        self.tb_order_id = tb_order_id
        self.order_amount = order_amount
        self.logistics_status = logistics_status
        self.create_date = create_date
        self.fund_structure_models = fund_structure_models
        self.sub_order_list = sub_order_list
        self.post_fee = post_fee

    def validate(self):
        if self.fund_structure_models:
            self.fund_structure_models.validate()
        if self.sub_order_list:
            self.sub_order_list.validate()
        if self.post_fee:
            self.post_fee.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.tb_order_id is not None:
            result['TbOrderId'] = self.tb_order_id
        if self.order_amount is not None:
            result['OrderAmount'] = self.order_amount
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.fund_structure_models is not None:
            result['FundStructureModels'] = self.fund_structure_models.to_map()
        if self.sub_order_list is not None:
            result['SubOrderList'] = self.sub_order_list.to_map()
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('TbOrderId') is not None:
            self.tb_order_id = m.get('TbOrderId')
        if m.get('OrderAmount') is not None:
            self.order_amount = m.get('OrderAmount')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('FundStructureModels') is not None:
            temp_model = QueryOrderListResponseBodyLmOrderListLmOrderListFundStructureModels()
            self.fund_structure_models = temp_model.from_map(m['FundStructureModels'])
        if m.get('SubOrderList') is not None:
            temp_model = QueryOrderListResponseBodyLmOrderListLmOrderListSubOrderList()
            self.sub_order_list = temp_model.from_map(m['SubOrderList'])
        if m.get('PostFee') is not None:
            temp_model = QueryOrderListResponseBodyLmOrderListLmOrderListPostFee()
            self.post_fee = temp_model.from_map(m['PostFee'])
        return self


class QueryOrderListResponseBodyLmOrderList(TeaModel):
    def __init__(
        self,
        lm_order_list: List[QueryOrderListResponseBodyLmOrderListLmOrderList] = None,
    ):
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.lm_order_list:
            for k in self.lm_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmOrderList'] = []
        if self.lm_order_list is not None:
            for k in self.lm_order_list:
                result['LmOrderList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_order_list = []
        if m.get('LmOrderList') is not None:
            for k in m.get('LmOrderList'):
                temp_model = QueryOrderListResponseBodyLmOrderListLmOrderList()
                self.lm_order_list.append(temp_model.from_map(k))
        return self


class QueryOrderListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        post_fee: QueryOrderListResponseBodyPostFee = None,
        lm_order_list: QueryOrderListResponseBodyLmOrderList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.post_fee = post_fee
        self.lm_order_list = lm_order_list

    def validate(self):
        if self.post_fee:
            self.post_fee.validate()
        if self.lm_order_list:
            self.lm_order_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee.to_map()
        if self.lm_order_list is not None:
            result['LmOrderList'] = self.lm_order_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PostFee') is not None:
            temp_model = QueryOrderListResponseBodyPostFee()
            self.post_fee = temp_model.from_map(m['PostFee'])
        if m.get('LmOrderList') is not None:
            temp_model = QueryOrderListResponseBodyLmOrderList()
            self.lm_order_list = temp_model.from_map(m['LmOrderList'])
        return self


class QueryOrderListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderListResponseBody = None,
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
            temp_model = QueryOrderListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderLogisticsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        lm_order_id: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.lm_order_id = lm_order_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class QueryOrderLogisticsResponseBodyOrderLogisticsLogisticsDetailListLogisticsDetailList(TeaModel):
    def __init__(
        self,
        ocurr_time_str: str = None,
        standerd_desc: str = None,
        status_icon: str = None,
    ):
        self.ocurr_time_str = ocurr_time_str
        self.standerd_desc = standerd_desc
        self.status_icon = status_icon

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ocurr_time_str is not None:
            result['OcurrTimeStr'] = self.ocurr_time_str
        if self.standerd_desc is not None:
            result['StanderdDesc'] = self.standerd_desc
        if self.status_icon is not None:
            result['StatusIcon'] = self.status_icon
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OcurrTimeStr') is not None:
            self.ocurr_time_str = m.get('OcurrTimeStr')
        if m.get('StanderdDesc') is not None:
            self.standerd_desc = m.get('StanderdDesc')
        if m.get('StatusIcon') is not None:
            self.status_icon = m.get('StatusIcon')
        return self


class QueryOrderLogisticsResponseBodyOrderLogisticsLogisticsDetailList(TeaModel):
    def __init__(
        self,
        logistics_detail_list: List[QueryOrderLogisticsResponseBodyOrderLogisticsLogisticsDetailListLogisticsDetailList] = None,
    ):
        self.logistics_detail_list = logistics_detail_list

    def validate(self):
        if self.logistics_detail_list:
            for k in self.logistics_detail_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogisticsDetailList'] = []
        if self.logistics_detail_list is not None:
            for k in self.logistics_detail_list:
                result['LogisticsDetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logistics_detail_list = []
        if m.get('LogisticsDetailList') is not None:
            for k in m.get('LogisticsDetailList'):
                temp_model = QueryOrderLogisticsResponseBodyOrderLogisticsLogisticsDetailListLogisticsDetailList()
                self.logistics_detail_list.append(temp_model.from_map(k))
        return self


class QueryOrderLogisticsResponseBodyOrderLogisticsReceiver(TeaModel):
    def __init__(
        self,
        address: str = None,
        name: str = None,
        phone_number: str = None,
        zip_code: str = None,
    ):
        self.address = address
        self.name = name
        self.phone_number = phone_number
        self.zip_code = zip_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.zip_code is not None:
            result['ZipCode'] = self.zip_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ZipCode') is not None:
            self.zip_code = m.get('ZipCode')
        return self


class QueryOrderLogisticsResponseBodyOrderLogisticsFetcher(TeaModel):
    def __init__(
        self,
        address: str = None,
        name: str = None,
        phone_number: str = None,
        zip_code: str = None,
    ):
        self.address = address
        self.name = name
        self.phone_number = phone_number
        self.zip_code = zip_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.name is not None:
            result['Name'] = self.name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.zip_code is not None:
            result['ZipCode'] = self.zip_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ZipCode') is not None:
            self.zip_code = m.get('ZipCode')
        return self


class QueryOrderLogisticsResponseBodyOrderLogistics(TeaModel):
    def __init__(
        self,
        logistics_company_code: str = None,
        logistics_company_name: str = None,
        data_provider: str = None,
        data_provider_title: str = None,
        logistics_detail_list: QueryOrderLogisticsResponseBodyOrderLogisticsLogisticsDetailList = None,
        receiver: QueryOrderLogisticsResponseBodyOrderLogisticsReceiver = None,
        fetcher: QueryOrderLogisticsResponseBodyOrderLogisticsFetcher = None,
    ):
        self.logistics_company_code = logistics_company_code
        self.logistics_company_name = logistics_company_name
        self.data_provider = data_provider
        self.data_provider_title = data_provider_title
        self.logistics_detail_list = logistics_detail_list
        self.receiver = receiver
        self.fetcher = fetcher

    def validate(self):
        if self.logistics_detail_list:
            self.logistics_detail_list.validate()
        if self.receiver:
            self.receiver.validate()
        if self.fetcher:
            self.fetcher.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logistics_company_code is not None:
            result['LogisticsCompanyCode'] = self.logistics_company_code
        if self.logistics_company_name is not None:
            result['LogisticsCompanyName'] = self.logistics_company_name
        if self.data_provider is not None:
            result['DataProvider'] = self.data_provider
        if self.data_provider_title is not None:
            result['DataProviderTitle'] = self.data_provider_title
        if self.logistics_detail_list is not None:
            result['LogisticsDetailList'] = self.logistics_detail_list.to_map()
        if self.receiver is not None:
            result['Receiver'] = self.receiver.to_map()
        if self.fetcher is not None:
            result['Fetcher'] = self.fetcher.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogisticsCompanyCode') is not None:
            self.logistics_company_code = m.get('LogisticsCompanyCode')
        if m.get('LogisticsCompanyName') is not None:
            self.logistics_company_name = m.get('LogisticsCompanyName')
        if m.get('DataProvider') is not None:
            self.data_provider = m.get('DataProvider')
        if m.get('DataProviderTitle') is not None:
            self.data_provider_title = m.get('DataProviderTitle')
        if m.get('LogisticsDetailList') is not None:
            temp_model = QueryOrderLogisticsResponseBodyOrderLogisticsLogisticsDetailList()
            self.logistics_detail_list = temp_model.from_map(m['LogisticsDetailList'])
        if m.get('Receiver') is not None:
            temp_model = QueryOrderLogisticsResponseBodyOrderLogisticsReceiver()
            self.receiver = temp_model.from_map(m['Receiver'])
        if m.get('Fetcher') is not None:
            temp_model = QueryOrderLogisticsResponseBodyOrderLogisticsFetcher()
            self.fetcher = temp_model.from_map(m['Fetcher'])
        return self


class QueryOrderLogisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        order_logistics: QueryOrderLogisticsResponseBodyOrderLogistics = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.order_logistics = order_logistics

    def validate(self):
        if self.order_logistics:
            self.order_logistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_logistics is not None:
            result['OrderLogistics'] = self.order_logistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderLogistics') is not None:
            temp_model = QueryOrderLogisticsResponseBodyOrderLogistics()
            self.order_logistics = temp_model.from_map(m['OrderLogistics'])
        return self


class QueryOrderLogisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryOrderLogisticsResponseBody = None,
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
            temp_model = QueryOrderLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRefundApplicationDetailRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        sub_lm_order_id: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.sub_lm_order_id = sub_lm_order_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class QueryRefundApplicationDetailResponseBodyRefundApplicationDetailMaxRefundFeeData(TeaModel):
    def __init__(
        self,
        max_refund_fee: int = None,
        min_refund_fee: int = None,
    ):
        self.max_refund_fee = max_refund_fee
        self.min_refund_fee = min_refund_fee

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_refund_fee is not None:
            result['MaxRefundFee'] = self.max_refund_fee
        if self.min_refund_fee is not None:
            result['MinRefundFee'] = self.min_refund_fee
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRefundFee') is not None:
            self.max_refund_fee = m.get('MaxRefundFee')
        if m.get('MinRefundFee') is not None:
            self.min_refund_fee = m.get('MinRefundFee')
        return self


class QueryRefundApplicationDetailResponseBodyRefundApplicationDetailApplyReasonText(TeaModel):
    def __init__(
        self,
        reason_tips: str = None,
        reason_text_id: int = None,
    ):
        self.reason_tips = reason_tips
        self.reason_text_id = reason_text_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason_tips is not None:
            result['ReasonTips'] = self.reason_tips
        if self.reason_text_id is not None:
            result['ReasonTextId'] = self.reason_text_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonTips') is not None:
            self.reason_tips = m.get('ReasonTips')
        if m.get('ReasonTextId') is not None:
            self.reason_text_id = m.get('ReasonTextId')
        return self


class QueryRefundApplicationDetailResponseBodyRefundApplicationDetail(TeaModel):
    def __init__(
        self,
        dispute_type: int = None,
        lm_order_id: str = None,
        refunder_name: str = None,
        seller_agree_msg: str = None,
        return_good_logistics_status: int = None,
        dispute_desc: str = None,
        refunder_address: str = None,
        return_good_count: int = None,
        dispute_id: int = None,
        dispute_end_time: str = None,
        order_logistics_status: int = None,
        biz_claim_type: int = None,
        real_refund_fee: int = None,
        refund_fee: int = None,
        seller_refuse_agreement_message: str = None,
        dispute_create_time: str = None,
        refunder_tel: str = None,
        seller_refuse_reason: str = None,
        sub_lm_order_id: str = None,
        apply_dispute_desc: str = None,
        dispute_status: int = None,
        refunder_zip_code: str = None,
        max_refund_fee_data: QueryRefundApplicationDetailResponseBodyRefundApplicationDetailMaxRefundFeeData = None,
        apply_reason_text: QueryRefundApplicationDetailResponseBodyRefundApplicationDetailApplyReasonText = None,
    ):
        self.dispute_type = dispute_type
        self.lm_order_id = lm_order_id
        self.refunder_name = refunder_name
        self.seller_agree_msg = seller_agree_msg
        self.return_good_logistics_status = return_good_logistics_status
        self.dispute_desc = dispute_desc
        self.refunder_address = refunder_address
        self.return_good_count = return_good_count
        self.dispute_id = dispute_id
        self.dispute_end_time = dispute_end_time
        self.order_logistics_status = order_logistics_status
        self.biz_claim_type = biz_claim_type
        self.real_refund_fee = real_refund_fee
        self.refund_fee = refund_fee
        self.seller_refuse_agreement_message = seller_refuse_agreement_message
        self.dispute_create_time = dispute_create_time
        self.refunder_tel = refunder_tel
        self.seller_refuse_reason = seller_refuse_reason
        self.sub_lm_order_id = sub_lm_order_id
        self.apply_dispute_desc = apply_dispute_desc
        self.dispute_status = dispute_status
        self.refunder_zip_code = refunder_zip_code
        self.max_refund_fee_data = max_refund_fee_data
        self.apply_reason_text = apply_reason_text

    def validate(self):
        if self.max_refund_fee_data:
            self.max_refund_fee_data.validate()
        if self.apply_reason_text:
            self.apply_reason_text.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dispute_type is not None:
            result['DisputeType'] = self.dispute_type
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.refunder_name is not None:
            result['RefunderName'] = self.refunder_name
        if self.seller_agree_msg is not None:
            result['SellerAgreeMsg'] = self.seller_agree_msg
        if self.return_good_logistics_status is not None:
            result['ReturnGoodLogisticsStatus'] = self.return_good_logistics_status
        if self.dispute_desc is not None:
            result['DisputeDesc'] = self.dispute_desc
        if self.refunder_address is not None:
            result['RefunderAddress'] = self.refunder_address
        if self.return_good_count is not None:
            result['ReturnGoodCount'] = self.return_good_count
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.dispute_end_time is not None:
            result['DisputeEndTime'] = self.dispute_end_time
        if self.order_logistics_status is not None:
            result['OrderLogisticsStatus'] = self.order_logistics_status
        if self.biz_claim_type is not None:
            result['BizClaimType'] = self.biz_claim_type
        if self.real_refund_fee is not None:
            result['RealRefundFee'] = self.real_refund_fee
        if self.refund_fee is not None:
            result['RefundFee'] = self.refund_fee
        if self.seller_refuse_agreement_message is not None:
            result['SellerRefuseAgreementMessage'] = self.seller_refuse_agreement_message
        if self.dispute_create_time is not None:
            result['DisputeCreateTime'] = self.dispute_create_time
        if self.refunder_tel is not None:
            result['RefunderTel'] = self.refunder_tel
        if self.seller_refuse_reason is not None:
            result['SellerRefuseReason'] = self.seller_refuse_reason
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.apply_dispute_desc is not None:
            result['ApplyDisputeDesc'] = self.apply_dispute_desc
        if self.dispute_status is not None:
            result['DisputeStatus'] = self.dispute_status
        if self.refunder_zip_code is not None:
            result['RefunderZipCode'] = self.refunder_zip_code
        if self.max_refund_fee_data is not None:
            result['MaxRefundFeeData'] = self.max_refund_fee_data.to_map()
        if self.apply_reason_text is not None:
            result['ApplyReasonText'] = self.apply_reason_text.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisputeType') is not None:
            self.dispute_type = m.get('DisputeType')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('RefunderName') is not None:
            self.refunder_name = m.get('RefunderName')
        if m.get('SellerAgreeMsg') is not None:
            self.seller_agree_msg = m.get('SellerAgreeMsg')
        if m.get('ReturnGoodLogisticsStatus') is not None:
            self.return_good_logistics_status = m.get('ReturnGoodLogisticsStatus')
        if m.get('DisputeDesc') is not None:
            self.dispute_desc = m.get('DisputeDesc')
        if m.get('RefunderAddress') is not None:
            self.refunder_address = m.get('RefunderAddress')
        if m.get('ReturnGoodCount') is not None:
            self.return_good_count = m.get('ReturnGoodCount')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('DisputeEndTime') is not None:
            self.dispute_end_time = m.get('DisputeEndTime')
        if m.get('OrderLogisticsStatus') is not None:
            self.order_logistics_status = m.get('OrderLogisticsStatus')
        if m.get('BizClaimType') is not None:
            self.biz_claim_type = m.get('BizClaimType')
        if m.get('RealRefundFee') is not None:
            self.real_refund_fee = m.get('RealRefundFee')
        if m.get('RefundFee') is not None:
            self.refund_fee = m.get('RefundFee')
        if m.get('SellerRefuseAgreementMessage') is not None:
            self.seller_refuse_agreement_message = m.get('SellerRefuseAgreementMessage')
        if m.get('DisputeCreateTime') is not None:
            self.dispute_create_time = m.get('DisputeCreateTime')
        if m.get('RefunderTel') is not None:
            self.refunder_tel = m.get('RefunderTel')
        if m.get('SellerRefuseReason') is not None:
            self.seller_refuse_reason = m.get('SellerRefuseReason')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('ApplyDisputeDesc') is not None:
            self.apply_dispute_desc = m.get('ApplyDisputeDesc')
        if m.get('DisputeStatus') is not None:
            self.dispute_status = m.get('DisputeStatus')
        if m.get('RefunderZipCode') is not None:
            self.refunder_zip_code = m.get('RefunderZipCode')
        if m.get('MaxRefundFeeData') is not None:
            temp_model = QueryRefundApplicationDetailResponseBodyRefundApplicationDetailMaxRefundFeeData()
            self.max_refund_fee_data = temp_model.from_map(m['MaxRefundFeeData'])
        if m.get('ApplyReasonText') is not None:
            temp_model = QueryRefundApplicationDetailResponseBodyRefundApplicationDetailApplyReasonText()
            self.apply_reason_text = temp_model.from_map(m['ApplyReasonText'])
        return self


class QueryRefundApplicationDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        refund_application_detail: QueryRefundApplicationDetailResponseBodyRefundApplicationDetail = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.refund_application_detail = refund_application_detail

    def validate(self):
        if self.refund_application_detail:
            self.refund_application_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refund_application_detail is not None:
            result['RefundApplicationDetail'] = self.refund_application_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefundApplicationDetail') is not None:
            temp_model = QueryRefundApplicationDetailResponseBodyRefundApplicationDetail()
            self.refund_application_detail = temp_model.from_map(m['RefundApplicationDetail'])
        return self


class QueryRefundApplicationDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryRefundApplicationDetailResponseBody = None,
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
            temp_model = QueryRefundApplicationDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStatementsRequest(TeaModel):
    def __init__(
        self,
        tenant_id: str = None,
        payee_ids: str = None,
        settle_noes: str = None,
        start_time: str = None,
        end_time: str = None,
        page_size: int = None,
        page_number: int = None,
        settle_status: str = None,
        settle_type: str = None,
        ext_info: str = None,
    ):
        self.tenant_id = tenant_id
        self.payee_ids = payee_ids
        self.settle_noes = settle_noes
        self.start_time = start_time
        self.end_time = end_time
        self.page_size = page_size
        self.page_number = page_number
        self.settle_status = settle_status
        self.settle_type = settle_type
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.payee_ids is not None:
            result['PayeeIds'] = self.payee_ids
        if self.settle_noes is not None:
            result['SettleNoes'] = self.settle_noes
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.settle_status is not None:
            result['SettleStatus'] = self.settle_status
        if self.settle_type is not None:
            result['SettleType'] = self.settle_type
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('PayeeIds') is not None:
            self.payee_ids = m.get('PayeeIds')
        if m.get('SettleNoes') is not None:
            self.settle_noes = m.get('SettleNoes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('SettleStatus') is not None:
            self.settle_status = m.get('SettleStatus')
        if m.get('SettleType') is not None:
            self.settle_type = m.get('SettleType')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class QueryStatementsResponseBodyModelStatementList(TeaModel):
    def __init__(
        self,
        payee_account_name: str = None,
        payee_id: str = None,
        payee_account_no: str = None,
        create_date: str = None,
        ext_info: str = None,
        end_time: str = None,
        start_time: str = None,
        settle_no: str = None,
        attributes: str = None,
        settle_status: str = None,
        payee_name: str = None,
        settle_amount: str = None,
        payee_account_id: str = None,
        modified_date: str = None,
        status_message: str = None,
        tenant_id: str = None,
    ):
        self.payee_account_name = payee_account_name
        self.payee_id = payee_id
        self.payee_account_no = payee_account_no
        self.create_date = create_date
        self.ext_info = ext_info
        self.end_time = end_time
        self.start_time = start_time
        self.settle_no = settle_no
        self.attributes = attributes
        self.settle_status = settle_status
        self.payee_name = payee_name
        self.settle_amount = settle_amount
        self.payee_account_id = payee_account_id
        self.modified_date = modified_date
        self.status_message = status_message
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payee_account_name is not None:
            result['PayeeAccountName'] = self.payee_account_name
        if self.payee_id is not None:
            result['PayeeId'] = self.payee_id
        if self.payee_account_no is not None:
            result['PayeeAccountNo'] = self.payee_account_no
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.settle_no is not None:
            result['SettleNo'] = self.settle_no
        if self.attributes is not None:
            result['Attributes'] = self.attributes
        if self.settle_status is not None:
            result['SettleStatus'] = self.settle_status
        if self.payee_name is not None:
            result['PayeeName'] = self.payee_name
        if self.settle_amount is not None:
            result['SettleAmount'] = self.settle_amount
        if self.payee_account_id is not None:
            result['PayeeAccountId'] = self.payee_account_id
        if self.modified_date is not None:
            result['ModifiedDate'] = self.modified_date
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayeeAccountName') is not None:
            self.payee_account_name = m.get('PayeeAccountName')
        if m.get('PayeeId') is not None:
            self.payee_id = m.get('PayeeId')
        if m.get('PayeeAccountNo') is not None:
            self.payee_account_no = m.get('PayeeAccountNo')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SettleNo') is not None:
            self.settle_no = m.get('SettleNo')
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')
        if m.get('SettleStatus') is not None:
            self.settle_status = m.get('SettleStatus')
        if m.get('PayeeName') is not None:
            self.payee_name = m.get('PayeeName')
        if m.get('SettleAmount') is not None:
            self.settle_amount = m.get('SettleAmount')
        if m.get('PayeeAccountId') is not None:
            self.payee_account_id = m.get('PayeeAccountId')
        if m.get('ModifiedDate') is not None:
            self.modified_date = m.get('ModifiedDate')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryStatementsResponseBodyModel(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        statement_list: List[QueryStatementsResponseBodyModelStatementList] = None,
    ):
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.statement_list = statement_list

    def validate(self):
        if self.statement_list:
            for k in self.statement_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['StatementList'] = []
        if self.statement_list is not None:
            for k in self.statement_list:
                result['StatementList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.statement_list = []
        if m.get('StatementList') is not None:
            for k in m.get('StatementList'):
                temp_model = QueryStatementsResponseBodyModelStatementList()
                self.statement_list.append(temp_model.from_map(k))
        return self


class QueryStatementsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: QueryStatementsResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = QueryStatementsResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class QueryStatementsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryStatementsResponseBody = None,
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
            temp_model = QueryStatementsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUnfinishedActivitiesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.biz_id = biz_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2ExtLmActivitySessionModelsLmActivitySessionModel(TeaModel):
    def __init__(
        self,
        sub_biz_code: str = None,
        end_date: str = None,
        display_date: str = None,
        description: str = None,
        lm_session_id: int = None,
        start_date: str = None,
        biz_id: str = None,
        lm_activity_id: int = None,
        name: str = None,
        ext_info: Dict[str, Any] = None,
    ):
        self.sub_biz_code = sub_biz_code
        self.end_date = end_date
        self.display_date = display_date
        self.description = description
        self.lm_session_id = lm_session_id
        self.start_date = start_date
        self.biz_id = biz_id
        self.lm_activity_id = lm_activity_id
        self.name = name
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.display_date is not None:
            result['DisplayDate'] = self.display_date
        if self.description is not None:
            result['Description'] = self.description
        if self.lm_session_id is not None:
            result['LmSessionId'] = self.lm_session_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.name is not None:
            result['Name'] = self.name
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DisplayDate') is not None:
            self.display_date = m.get('DisplayDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LmSessionId') is not None:
            self.lm_session_id = m.get('LmSessionId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2ExtLmActivitySessionModels(TeaModel):
    def __init__(
        self,
        lm_activity_session_model: List[QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2ExtLmActivitySessionModelsLmActivitySessionModel] = None,
    ):
        self.lm_activity_session_model = lm_activity_session_model

    def validate(self):
        if self.lm_activity_session_model:
            for k in self.lm_activity_session_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmActivitySessionModel'] = []
        if self.lm_activity_session_model is not None:
            for k in self.lm_activity_session_model:
                result['LmActivitySessionModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_activity_session_model = []
        if m.get('LmActivitySessionModel') is not None:
            for k in m.get('LmActivitySessionModel'):
                temp_model = QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2ExtLmActivitySessionModelsLmActivitySessionModel()
                self.lm_activity_session_model.append(temp_model.from_map(k))
        return self


class QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2Ext(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        description: str = None,
        start_date: str = None,
        lm_activity_id: int = None,
        biz_id: str = None,
        activity_pic_url: str = None,
        name: str = None,
        lm_activity_session_models: QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2ExtLmActivitySessionModels = None,
    ):
        self.end_date = end_date
        self.description = description
        self.start_date = start_date
        self.lm_activity_id = lm_activity_id
        self.biz_id = biz_id
        self.activity_pic_url = activity_pic_url
        self.name = name
        self.lm_activity_session_models = lm_activity_session_models

    def validate(self):
        if self.lm_activity_session_models:
            self.lm_activity_session_models.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.description is not None:
            result['Description'] = self.description
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.activity_pic_url is not None:
            result['ActivityPicUrl'] = self.activity_pic_url
        if self.name is not None:
            result['Name'] = self.name
        if self.lm_activity_session_models is not None:
            result['LmActivitySessionModels'] = self.lm_activity_session_models.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ActivityPicUrl') is not None:
            self.activity_pic_url = m.get('ActivityPicUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('LmActivitySessionModels') is not None:
            temp_model = QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2ExtLmActivitySessionModels()
            self.lm_activity_session_models = temp_model.from_map(m['LmActivitySessionModels'])
        return self


class QueryUnfinishedActivitiesResponseBodyLmActivityModelExtList(TeaModel):
    def __init__(
        self,
        lm_activity_model_v2ext: List[QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2Ext] = None,
    ):
        self.lm_activity_model_v2ext = lm_activity_model_v2ext

    def validate(self):
        if self.lm_activity_model_v2ext:
            for k in self.lm_activity_model_v2ext:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmActivityModelV2Ext'] = []
        if self.lm_activity_model_v2ext is not None:
            for k in self.lm_activity_model_v2ext:
                result['LmActivityModelV2Ext'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_activity_model_v2ext = []
        if m.get('LmActivityModelV2Ext') is not None:
            for k in m.get('LmActivityModelV2Ext'):
                temp_model = QueryUnfinishedActivitiesResponseBodyLmActivityModelExtListLmActivityModelV2Ext()
                self.lm_activity_model_v2ext.append(temp_model.from_map(k))
        return self


class QueryUnfinishedActivitiesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        total_count: int = None,
        lm_activity_model_ext_list: QueryUnfinishedActivitiesResponseBodyLmActivityModelExtList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.total_count = total_count
        self.lm_activity_model_ext_list = lm_activity_model_ext_list

    def validate(self):
        if self.lm_activity_model_ext_list:
            self.lm_activity_model_ext_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.lm_activity_model_ext_list is not None:
            result['LmActivityModelExtList'] = self.lm_activity_model_ext_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LmActivityModelExtList') is not None:
            temp_model = QueryUnfinishedActivitiesResponseBodyLmActivityModelExtList()
            self.lm_activity_model_ext_list = temp_model.from_map(m['LmActivityModelExtList'])
        return self


class QueryUnfinishedActivitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUnfinishedActivitiesResponseBody = None,
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
            temp_model = QueryUnfinishedActivitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUnfinishedSessionsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        page_number: int = None,
        page_size: int = None,
        query_time: int = None,
    ):
        self.biz_id = biz_id
        self.page_number = page_number
        self.page_size = page_size
        self.query_time = query_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        return self


class QueryUnfinishedSessionsResponseBodyLmActivitySessionModelListLmActivitySessionModel(TeaModel):
    def __init__(
        self,
        sub_biz_code: str = None,
        display_date: str = None,
        end_date: str = None,
        description: str = None,
        lm_session_id: int = None,
        biz_id: str = None,
        lm_activity_id: int = None,
        start_date: str = None,
        name: str = None,
    ):
        self.sub_biz_code = sub_biz_code
        self.display_date = display_date
        self.end_date = end_date
        self.description = description
        self.lm_session_id = lm_session_id
        self.biz_id = biz_id
        self.lm_activity_id = lm_activity_id
        self.start_date = start_date
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.display_date is not None:
            result['DisplayDate'] = self.display_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.description is not None:
            result['Description'] = self.description
        if self.lm_session_id is not None:
            result['LmSessionId'] = self.lm_session_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('DisplayDate') is not None:
            self.display_date = m.get('DisplayDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LmSessionId') is not None:
            self.lm_session_id = m.get('LmSessionId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryUnfinishedSessionsResponseBodyLmActivitySessionModelList(TeaModel):
    def __init__(
        self,
        lm_activity_session_model: List[QueryUnfinishedSessionsResponseBodyLmActivitySessionModelListLmActivitySessionModel] = None,
    ):
        self.lm_activity_session_model = lm_activity_session_model

    def validate(self):
        if self.lm_activity_session_model:
            for k in self.lm_activity_session_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmActivitySessionModel'] = []
        if self.lm_activity_session_model is not None:
            for k in self.lm_activity_session_model:
                result['LmActivitySessionModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_activity_session_model = []
        if m.get('LmActivitySessionModel') is not None:
            for k in m.get('LmActivitySessionModel'):
                temp_model = QueryUnfinishedSessionsResponseBodyLmActivitySessionModelListLmActivitySessionModel()
                self.lm_activity_session_model.append(temp_model.from_map(k))
        return self


class QueryUnfinishedSessionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        lm_activity_session_model_list: QueryUnfinishedSessionsResponseBodyLmActivitySessionModelList = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.lm_activity_session_model_list = lm_activity_session_model_list

    def validate(self):
        if self.lm_activity_session_model_list:
            self.lm_activity_session_model_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.lm_activity_session_model_list is not None:
            result['LmActivitySessionModelList'] = self.lm_activity_session_model_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LmActivitySessionModelList') is not None:
            temp_model = QueryUnfinishedSessionsResponseBodyLmActivitySessionModelList()
            self.lm_activity_session_model_list = temp_model.from_map(m['LmActivitySessionModelList'])
        return self


class QueryUnfinishedSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUnfinishedSessionsResponseBody = None,
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
            temp_model = QueryUnfinishedSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUnfinishedSessions4ItemsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lm_item_ids: Dict[str, Any] = None,
        item_ids: Dict[str, Any] = None,
        query_time: int = None,
    ):
        self.biz_id = biz_id
        self.lm_item_ids = lm_item_ids
        self.item_ids = item_ids
        self.query_time = query_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_item_ids is not None:
            result['LmItemIds'] = self.lm_item_ids
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        return self


class QueryUnfinishedSessions4ItemsShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lm_item_ids_shrink: str = None,
        item_ids_shrink: str = None,
        query_time: int = None,
    ):
        self.biz_id = biz_id
        self.lm_item_ids_shrink = lm_item_ids_shrink
        self.item_ids_shrink = item_ids_shrink
        self.query_time = query_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lm_item_ids_shrink is not None:
            result['LmItemIds'] = self.lm_item_ids_shrink
        if self.item_ids_shrink is not None:
            result['ItemIds'] = self.item_ids_shrink
        if self.query_time is not None:
            result['QueryTime'] = self.query_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LmItemIds') is not None:
            self.lm_item_ids_shrink = m.get('LmItemIds')
        if m.get('ItemIds') is not None:
            self.item_ids_shrink = m.get('ItemIds')
        if m.get('QueryTime') is not None:
            self.query_time = m.get('QueryTime')
        return self


class QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelListLmActivitySessionModelsLmActivitySessionModel(TeaModel):
    def __init__(
        self,
        sub_biz_code: str = None,
        end_date: str = None,
        display_date: str = None,
        lm_session_id: int = None,
        description: str = None,
        start_date: str = None,
        lm_activity_id: int = None,
        biz_id: str = None,
        name: str = None,
        ext_info: Dict[str, Any] = None,
    ):
        self.sub_biz_code = sub_biz_code
        self.end_date = end_date
        self.display_date = display_date
        self.lm_session_id = lm_session_id
        self.description = description
        self.start_date = start_date
        self.lm_activity_id = lm_activity_id
        self.biz_id = biz_id
        self.name = name
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_biz_code is not None:
            result['SubBizCode'] = self.sub_biz_code
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.display_date is not None:
            result['DisplayDate'] = self.display_date
        if self.lm_session_id is not None:
            result['LmSessionId'] = self.lm_session_id
        if self.description is not None:
            result['Description'] = self.description
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.lm_activity_id is not None:
            result['LmActivityId'] = self.lm_activity_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.name is not None:
            result['Name'] = self.name
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubBizCode') is not None:
            self.sub_biz_code = m.get('SubBizCode')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('DisplayDate') is not None:
            self.display_date = m.get('DisplayDate')
        if m.get('LmSessionId') is not None:
            self.lm_session_id = m.get('LmSessionId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('LmActivityId') is not None:
            self.lm_activity_id = m.get('LmActivityId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelListLmActivitySessionModels(TeaModel):
    def __init__(
        self,
        lm_activity_session_model: List[QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelListLmActivitySessionModelsLmActivitySessionModel] = None,
    ):
        self.lm_activity_session_model = lm_activity_session_model

    def validate(self):
        if self.lm_activity_session_model:
            for k in self.lm_activity_session_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmActivitySessionModel'] = []
        if self.lm_activity_session_model is not None:
            for k in self.lm_activity_session_model:
                result['LmActivitySessionModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_activity_session_model = []
        if m.get('LmActivitySessionModel') is not None:
            for k in m.get('LmActivitySessionModel'):
                temp_model = QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelListLmActivitySessionModelsLmActivitySessionModel()
                self.lm_activity_session_model.append(temp_model.from_map(k))
        return self


class QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelList(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        item_id: int = None,
        lm_activity_session_models: QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelListLmActivitySessionModels = None,
    ):
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.lm_activity_session_models = lm_activity_session_models

    def validate(self):
        if self.lm_activity_session_models:
            self.lm_activity_session_models.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.lm_activity_session_models is not None:
            result['LmActivitySessionModels'] = self.lm_activity_session_models.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('LmActivitySessionModels') is not None:
            temp_model = QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelListLmActivitySessionModels()
            self.lm_activity_session_models = temp_model.from_map(m['LmActivitySessionModels'])
        return self


class QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListList(TeaModel):
    def __init__(
        self,
        lm_item_activity_session_model_list: List[QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelList] = None,
    ):
        self.lm_item_activity_session_model_list = lm_item_activity_session_model_list

    def validate(self):
        if self.lm_item_activity_session_model_list:
            for k in self.lm_item_activity_session_model_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmItemActivitySessionModelList'] = []
        if self.lm_item_activity_session_model_list is not None:
            for k in self.lm_item_activity_session_model_list:
                result['LmItemActivitySessionModelList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_item_activity_session_model_list = []
        if m.get('LmItemActivitySessionModelList') is not None:
            for k in m.get('LmItemActivitySessionModelList'):
                temp_model = QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListListLmItemActivitySessionModelList()
                self.lm_item_activity_session_model_list.append(temp_model.from_map(k))
        return self


class QueryUnfinishedSessions4ItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        lm_item_activity_session_model_list_list: QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListList = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.lm_item_activity_session_model_list_list = lm_item_activity_session_model_list_list

    def validate(self):
        if self.lm_item_activity_session_model_list_list:
            self.lm_item_activity_session_model_list_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.lm_item_activity_session_model_list_list is not None:
            result['LmItemActivitySessionModelListList'] = self.lm_item_activity_session_model_list_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LmItemActivitySessionModelListList') is not None:
            temp_model = QueryUnfinishedSessions4ItemsResponseBodyLmItemActivitySessionModelListList()
            self.lm_item_activity_session_model_list_list = temp_model.from_map(m['LmItemActivitySessionModelListList'])
        return self


class QueryUnfinishedSessions4ItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUnfinishedSessions4ItemsResponseBody = None,
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
            temp_model = QueryUnfinishedSessions4ItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUpcomingMoviesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        city_code: int = None,
        ext_json: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.city_code = city_code
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class QueryUpcomingMoviesShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        city_code: int = None,
        ext_json_shrink: str = None,
    ):
        self.biz_id = biz_id
        self.city_code = city_code
        self.ext_json_shrink = ext_json_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.city_code is not None:
            result['CityCode'] = self.city_code
        if self.ext_json_shrink is not None:
            result['ExtJson'] = self.ext_json_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('CityCode') is not None:
            self.city_code = m.get('CityCode')
        if m.get('ExtJson') is not None:
            self.ext_json_shrink = m.get('ExtJson')
        return self


class QueryUpcomingMoviesResponseBodyMoviesMovie(TeaModel):
    def __init__(
        self,
        type: str = None,
        movie_version: str = None,
        background_picture: str = None,
        remark: str = None,
        open_day: str = None,
        highlight: str = None,
        movie_type_list: str = None,
        language: str = None,
        director: str = None,
        open_time: str = None,
        poster: str = None,
        movie_name: str = None,
        description: str = None,
        country: str = None,
        duration: int = None,
        movie_name_en: str = None,
        leading_role: str = None,
        id: int = None,
        trailer_list: str = None,
    ):
        self.type = type
        self.movie_version = movie_version
        self.background_picture = background_picture
        self.remark = remark
        self.open_day = open_day
        self.highlight = highlight
        self.movie_type_list = movie_type_list
        self.language = language
        self.director = director
        self.open_time = open_time
        self.poster = poster
        self.movie_name = movie_name
        self.description = description
        self.country = country
        self.duration = duration
        self.movie_name_en = movie_name_en
        self.leading_role = leading_role
        self.id = id
        self.trailer_list = trailer_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.movie_version is not None:
            result['MovieVersion'] = self.movie_version
        if self.background_picture is not None:
            result['BackgroundPicture'] = self.background_picture
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.open_day is not None:
            result['OpenDay'] = self.open_day
        if self.highlight is not None:
            result['Highlight'] = self.highlight
        if self.movie_type_list is not None:
            result['MovieTypeList'] = self.movie_type_list
        if self.language is not None:
            result['Language'] = self.language
        if self.director is not None:
            result['Director'] = self.director
        if self.open_time is not None:
            result['OpenTime'] = self.open_time
        if self.poster is not None:
            result['Poster'] = self.poster
        if self.movie_name is not None:
            result['MovieName'] = self.movie_name
        if self.description is not None:
            result['Description'] = self.description
        if self.country is not None:
            result['Country'] = self.country
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.movie_name_en is not None:
            result['MovieNameEn'] = self.movie_name_en
        if self.leading_role is not None:
            result['LeadingRole'] = self.leading_role
        if self.id is not None:
            result['Id'] = self.id
        if self.trailer_list is not None:
            result['TrailerList'] = self.trailer_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('MovieVersion') is not None:
            self.movie_version = m.get('MovieVersion')
        if m.get('BackgroundPicture') is not None:
            self.background_picture = m.get('BackgroundPicture')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('OpenDay') is not None:
            self.open_day = m.get('OpenDay')
        if m.get('Highlight') is not None:
            self.highlight = m.get('Highlight')
        if m.get('MovieTypeList') is not None:
            self.movie_type_list = m.get('MovieTypeList')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Director') is not None:
            self.director = m.get('Director')
        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')
        if m.get('Poster') is not None:
            self.poster = m.get('Poster')
        if m.get('MovieName') is not None:
            self.movie_name = m.get('MovieName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('MovieNameEn') is not None:
            self.movie_name_en = m.get('MovieNameEn')
        if m.get('LeadingRole') is not None:
            self.leading_role = m.get('LeadingRole')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TrailerList') is not None:
            self.trailer_list = m.get('TrailerList')
        return self


class QueryUpcomingMoviesResponseBodyMovies(TeaModel):
    def __init__(
        self,
        movie: List[QueryUpcomingMoviesResponseBodyMoviesMovie] = None,
    ):
        self.movie = movie

    def validate(self):
        if self.movie:
            for k in self.movie:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Movie'] = []
        if self.movie is not None:
            for k in self.movie:
                result['Movie'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.movie = []
        if m.get('Movie') is not None:
            for k in m.get('Movie'):
                temp_model = QueryUpcomingMoviesResponseBodyMoviesMovie()
                self.movie.append(temp_model.from_map(k))
        return self


class QueryUpcomingMoviesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        movies: QueryUpcomingMoviesResponseBodyMovies = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.movies = movies

    def validate(self):
        if self.movies:
            self.movies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.movies is not None:
            result['Movies'] = self.movies.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Movies') is not None:
            temp_model = QueryUpcomingMoviesResponseBodyMovies()
            self.movies = temp_model.from_map(m['Movies'])
        return self


class QueryUpcomingMoviesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryUpcomingMoviesResponseBody = None,
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
            temp_model = QueryUpcomingMoviesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWithholdTradeRequest(TeaModel):
    def __init__(
        self,
        trade_no: str = None,
        out_trade_no: str = None,
        merchant_id: str = None,
    ):
        self.trade_no = trade_no
        self.out_trade_no = out_trade_no
        self.merchant_id = merchant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trade_no is not None:
            result['TradeNo'] = self.trade_no
        if self.out_trade_no is not None:
            result['OutTradeNo'] = self.out_trade_no
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TradeNo') is not None:
            self.trade_no = m.get('TradeNo')
        if m.get('OutTradeNo') is not None:
            self.out_trade_no = m.get('OutTradeNo')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        return self


class QueryWithholdTradeResponseBodyQueryWithholdTradeResponse(TeaModel):
    def __init__(
        self,
        settle_status: str = None,
        trade_status: str = None,
        total_amount: str = None,
        trade_no: str = None,
        payment_date: str = None,
        out_trade_no: str = None,
    ):
        self.settle_status = settle_status
        self.trade_status = trade_status
        self.total_amount = total_amount
        self.trade_no = trade_no
        self.payment_date = payment_date
        self.out_trade_no = out_trade_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.settle_status is not None:
            result['SettleStatus'] = self.settle_status
        if self.trade_status is not None:
            result['TradeStatus'] = self.trade_status
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.trade_no is not None:
            result['TradeNo'] = self.trade_no
        if self.payment_date is not None:
            result['PaymentDate'] = self.payment_date
        if self.out_trade_no is not None:
            result['OutTradeNo'] = self.out_trade_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SettleStatus') is not None:
            self.settle_status = m.get('SettleStatus')
        if m.get('TradeStatus') is not None:
            self.trade_status = m.get('TradeStatus')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('TradeNo') is not None:
            self.trade_no = m.get('TradeNo')
        if m.get('PaymentDate') is not None:
            self.payment_date = m.get('PaymentDate')
        if m.get('OutTradeNo') is not None:
            self.out_trade_no = m.get('OutTradeNo')
        return self


class QueryWithholdTradeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        query_withhold_trade_response: QueryWithholdTradeResponseBodyQueryWithholdTradeResponse = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.query_withhold_trade_response = query_withhold_trade_response

    def validate(self):
        if self.query_withhold_trade_response:
            self.query_withhold_trade_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.query_withhold_trade_response is not None:
            result['QueryWithholdTradeResponse'] = self.query_withhold_trade_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('QueryWithholdTradeResponse') is not None:
            temp_model = QueryWithholdTradeResponseBodyQueryWithholdTradeResponse()
            self.query_withhold_trade_response = temp_model.from_map(m['QueryWithholdTradeResponse'])
        return self


class QueryWithholdTradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryWithholdTradeResponseBody = None,
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
            temp_model = QueryWithholdTradeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundOrderRequest(TeaModel):
    def __init__(
        self,
        out_request_no: str = None,
        out_trade_no: str = None,
        trade_no: str = None,
        refund_reason: str = None,
        refund_amount: str = None,
        refund_royalty_parameters: str = None,
        ext_info: str = None,
        merchant_id: str = None,
    ):
        self.out_request_no = out_request_no
        self.out_trade_no = out_trade_no
        self.trade_no = trade_no
        self.refund_reason = refund_reason
        self.refund_amount = refund_amount
        self.refund_royalty_parameters = refund_royalty_parameters
        self.ext_info = ext_info
        self.merchant_id = merchant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        if self.out_trade_no is not None:
            result['OutTradeNo'] = self.out_trade_no
        if self.trade_no is not None:
            result['TradeNo'] = self.trade_no
        if self.refund_reason is not None:
            result['RefundReason'] = self.refund_reason
        if self.refund_amount is not None:
            result['RefundAmount'] = self.refund_amount
        if self.refund_royalty_parameters is not None:
            result['RefundRoyaltyParameters'] = self.refund_royalty_parameters
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        if m.get('OutTradeNo') is not None:
            self.out_trade_no = m.get('OutTradeNo')
        if m.get('TradeNo') is not None:
            self.trade_no = m.get('TradeNo')
        if m.get('RefundReason') is not None:
            self.refund_reason = m.get('RefundReason')
        if m.get('RefundAmount') is not None:
            self.refund_amount = m.get('RefundAmount')
        if m.get('RefundRoyaltyParameters') is not None:
            self.refund_royalty_parameters = m.get('RefundRoyaltyParameters')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        return self


class RefundOrderResponseBodyRefundResponse(TeaModel):
    def __init__(
        self,
        fund_change: str = None,
        gmt_refund_pay: str = None,
        trade_no: str = None,
        out_trade_no: str = None,
        out_request_no: str = None,
    ):
        self.fund_change = fund_change
        self.gmt_refund_pay = gmt_refund_pay
        self.trade_no = trade_no
        self.out_trade_no = out_trade_no
        self.out_request_no = out_request_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fund_change is not None:
            result['FundChange'] = self.fund_change
        if self.gmt_refund_pay is not None:
            result['GmtRefundPay'] = self.gmt_refund_pay
        if self.trade_no is not None:
            result['TradeNo'] = self.trade_no
        if self.out_trade_no is not None:
            result['OutTradeNo'] = self.out_trade_no
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FundChange') is not None:
            self.fund_change = m.get('FundChange')
        if m.get('GmtRefundPay') is not None:
            self.gmt_refund_pay = m.get('GmtRefundPay')
        if m.get('TradeNo') is not None:
            self.trade_no = m.get('TradeNo')
        if m.get('OutTradeNo') is not None:
            self.out_trade_no = m.get('OutTradeNo')
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        return self


class RefundOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        refund_response: RefundOrderResponseBodyRefundResponse = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.refund_response = refund_response

    def validate(self):
        if self.refund_response:
            self.refund_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.refund_response is not None:
            result['RefundResponse'] = self.refund_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RefundResponse') is not None:
            temp_model = RefundOrderResponseBodyRefundResponse()
            self.refund_response = temp_model.from_map(m['RefundResponse'])
        return self


class RefundOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefundOrderResponseBody = None,
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
            temp_model = RefundOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundPointRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        seller_id: str = None,
        lm_order_id: str = None,
        reason: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
    ):
        self.biz_id = biz_id
        self.seller_id = seller_id
        self.lm_order_id = lm_order_id
        self.reason = reason
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        return self


class RefundPointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefundPointResponseBody = None,
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
            temp_model = RefundPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefuseMerchantSyncTaskRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        task_id: str = None,
        seller_nick: str = None,
        time_stamp: int = None,
    ):
        self.biz_id = biz_id
        self.task_id = task_id
        self.seller_nick = seller_nick
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.seller_nick is not None:
            result['SellerNick'] = self.seller_nick
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('SellerNick') is not None:
            self.seller_nick = m.get('SellerNick')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class RefuseMerchantSyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefuseMerchantSyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RefuseMerchantSyncTaskResponseBody = None,
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
            temp_model = RefuseMerchantSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegistAnonymousTbAccountRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        third_party_user_id: str = None,
    ):
        self.biz_id = biz_id
        self.third_party_user_id = third_party_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        return self


class RegistAnonymousTbAccountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegistAnonymousTbAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegistAnonymousTbAccountResponseBody = None,
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
            temp_model = RegistAnonymousTbAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseMovieSeatRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        lock_seat_apply_key: str = None,
        biz_uid: str = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.lock_seat_apply_key = lock_seat_apply_key
        self.biz_uid = biz_uid
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.lock_seat_apply_key is not None:
            result['LockSeatApplyKey'] = self.lock_seat_apply_key
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('LockSeatApplyKey') is not None:
            self.lock_seat_apply_key = m.get('LockSeatApplyKey')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class ReleaseMovieSeatResponseBodyActionResult(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_value: str = None,
        return_message: str = None,
    ):
        self.return_code = return_code
        self.return_value = return_value
        self.return_message = return_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value
        if self.return_message is not None:
            result['ReturnMessage'] = self.return_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')
        if m.get('ReturnMessage') is not None:
            self.return_message = m.get('ReturnMessage')
        return self


class ReleaseMovieSeatResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        logs_id: str = None,
        action_result: ReleaseMovieSeatResponseBodyActionResult = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.logs_id = logs_id
        self.action_result = action_result

    def validate(self):
        if self.action_result:
            self.action_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.action_result is not None:
            result['ActionResult'] = self.action_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('ActionResult') is not None:
            temp_model = ReleaseMovieSeatResponseBodyActionResult()
            self.action_result = temp_model.from_map(m['ActionResult'])
        return self


class ReleaseMovieSeatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseMovieSeatResponseBody = None,
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
            temp_model = ReleaseMovieSeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveAddressRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        third_party_user_id: str = None,
        use_anonymous_tb_account: bool = None,
        address_info: str = None,
    ):
        self.biz_id = biz_id
        self.third_party_user_id = third_party_user_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.address_info = address_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('AddressInfo') is not None:
            self.address_info = m.get('AddressInfo')
        return self


class RemoveAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveAddressResponseBody = None,
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
            temp_model = RemoveAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMessagesRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        message_ids: str = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.message_ids = message_ids
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.message_ids is not None:
            result['MessageIds'] = self.message_ids
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('MessageIds') is not None:
            self.message_ids = m.get('MessageIds')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class RemoveMessagesResponseBodyActionResult(TeaModel):
    def __init__(
        self,
        return_code: str = None,
        return_value: str = None,
        return_message: str = None,
    ):
        self.return_code = return_code
        self.return_value = return_value
        self.return_message = return_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.return_code is not None:
            result['ReturnCode'] = self.return_code
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value
        if self.return_message is not None:
            result['ReturnMessage'] = self.return_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReturnCode') is not None:
            self.return_code = m.get('ReturnCode')
        if m.get('ReturnValue') is not None:
            self.return_value = m.get('ReturnValue')
        if m.get('ReturnMessage') is not None:
            self.return_message = m.get('ReturnMessage')
        return self


class RemoveMessagesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        sub_code: str = None,
        message: str = None,
        logs_id: str = None,
        action_result: RemoveMessagesResponseBodyActionResult = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.sub_code = sub_code
        self.message = message
        self.logs_id = logs_id
        self.action_result = action_result

    def validate(self):
        if self.action_result:
            self.action_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.message is not None:
            result['Message'] = self.message
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.action_result is not None:
            result['ActionResult'] = self.action_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('ActionResult') is not None:
            temp_model = RemoveMessagesResponseBodyActionResult()
            self.action_result = temp_model.from_map(m['ActionResult'])
        return self


class RemoveMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveMessagesResponseBody = None,
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
            temp_model = RemoveMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderH5OrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        buy_order_request_model: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.buy_order_request_model = buy_order_request_model
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.buy_order_request_model is not None:
            result['BuyOrderRequestModel'] = self.buy_order_request_model
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('BuyOrderRequestModel') is not None:
            self.buy_order_request_model = m.get('BuyOrderRequestModel')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class RenderH5OrderResponseBodyModelLmItemInfoList(TeaModel):
    def __init__(
        self,
        tb_shop_name: str = None,
        seller_id: int = None,
        lm_item_id: str = None,
        message: str = None,
        can_sell: bool = None,
        cash: int = None,
        item_id: int = None,
        virtual_item_type: str = None,
        item_name: str = None,
        actual_price: int = None,
        sku_name: str = None,
        sku_id: int = None,
        points: int = None,
        item_url: str = None,
        seller_nick: str = None,
        quantity: int = None,
        features: Dict[str, Any] = None,
        item_pic_url: str = None,
    ):
        self.tb_shop_name = tb_shop_name
        self.seller_id = seller_id
        self.lm_item_id = lm_item_id
        self.message = message
        self.can_sell = can_sell
        self.cash = cash
        self.item_id = item_id
        self.virtual_item_type = virtual_item_type
        self.item_name = item_name
        self.actual_price = actual_price
        self.sku_name = sku_name
        self.sku_id = sku_id
        self.points = points
        self.item_url = item_url
        self.seller_nick = seller_nick
        self.quantity = quantity
        self.features = features
        self.item_pic_url = item_pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tb_shop_name is not None:
            result['TbShopName'] = self.tb_shop_name
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.message is not None:
            result['Message'] = self.message
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.cash is not None:
            result['Cash'] = self.cash
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.virtual_item_type is not None:
            result['VirtualItemType'] = self.virtual_item_type
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.actual_price is not None:
            result['ActualPrice'] = self.actual_price
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.points is not None:
            result['Points'] = self.points
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.seller_nick is not None:
            result['SellerNick'] = self.seller_nick
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.features is not None:
            result['Features'] = self.features
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TbShopName') is not None:
            self.tb_shop_name = m.get('TbShopName')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('Cash') is not None:
            self.cash = m.get('Cash')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('VirtualItemType') is not None:
            self.virtual_item_type = m.get('VirtualItemType')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ActualPrice') is not None:
            self.actual_price = m.get('ActualPrice')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('SellerNick') is not None:
            self.seller_nick = m.get('SellerNick')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Features') is not None:
            self.features = m.get('Features')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        return self


class RenderH5OrderResponseBodyModelDeliveryInfoList(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        post_fee: int = None,
        service_type: int = None,
        id: str = None,
    ):
        self.display_name = display_name
        self.post_fee = post_fee
        self.service_type = service_type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('PostFee') is not None:
            self.post_fee = m.get('PostFee')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RenderH5OrderResponseBodyModelAddressInfoList(TeaModel):
    def __init__(
        self,
        division_code: str = None,
        receiver: str = None,
        address_detail: str = None,
        default: bool = None,
        address_id: int = None,
        receiver_phone: str = None,
    ):
        self.division_code = division_code
        self.receiver = receiver
        self.address_detail = address_detail
        self.default = default
        self.address_id = address_id
        self.receiver_phone = receiver_phone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.division_code is not None:
            result['DivisionCode'] = self.division_code
        if self.receiver is not None:
            result['Receiver'] = self.receiver
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail
        if self.default is not None:
            result['Default'] = self.default
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.receiver_phone is not None:
            result['ReceiverPhone'] = self.receiver_phone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DivisionCode') is not None:
            self.division_code = m.get('DivisionCode')
        if m.get('Receiver') is not None:
            self.receiver = m.get('Receiver')
        if m.get('AddressDetail') is not None:
            self.address_detail = m.get('AddressDetail')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('ReceiverPhone') is not None:
            self.receiver_phone = m.get('ReceiverPhone')
        return self


class RenderH5OrderResponseBodyModelInvoiceInfo(TeaModel):
    def __init__(
        self,
        type: str = None,
        desc: str = None,
    ):
        self.type = type
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class RenderH5OrderResponseBodyModel(TeaModel):
    def __init__(
        self,
        ext_info: Dict[str, Any] = None,
        buyer_current_points: int = None,
        lm_item_info_list: List[RenderH5OrderResponseBodyModelLmItemInfoList] = None,
        delivery_info_list: List[RenderH5OrderResponseBodyModelDeliveryInfoList] = None,
        address_info_list: List[RenderH5OrderResponseBodyModelAddressInfoList] = None,
        invoice_info: RenderH5OrderResponseBodyModelInvoiceInfo = None,
    ):
        self.ext_info = ext_info
        self.buyer_current_points = buyer_current_points
        self.lm_item_info_list = lm_item_info_list
        self.delivery_info_list = delivery_info_list
        self.address_info_list = address_info_list
        self.invoice_info = invoice_info

    def validate(self):
        if self.lm_item_info_list:
            for k in self.lm_item_info_list:
                if k:
                    k.validate()
        if self.delivery_info_list:
            for k in self.delivery_info_list:
                if k:
                    k.validate()
        if self.address_info_list:
            for k in self.address_info_list:
                if k:
                    k.validate()
        if self.invoice_info:
            self.invoice_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.buyer_current_points is not None:
            result['BuyerCurrentPoints'] = self.buyer_current_points
        result['LmItemInfoList'] = []
        if self.lm_item_info_list is not None:
            for k in self.lm_item_info_list:
                result['LmItemInfoList'].append(k.to_map() if k else None)
        result['DeliveryInfoList'] = []
        if self.delivery_info_list is not None:
            for k in self.delivery_info_list:
                result['DeliveryInfoList'].append(k.to_map() if k else None)
        result['AddressInfoList'] = []
        if self.address_info_list is not None:
            for k in self.address_info_list:
                result['AddressInfoList'].append(k.to_map() if k else None)
        if self.invoice_info is not None:
            result['InvoiceInfo'] = self.invoice_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('BuyerCurrentPoints') is not None:
            self.buyer_current_points = m.get('BuyerCurrentPoints')
        self.lm_item_info_list = []
        if m.get('LmItemInfoList') is not None:
            for k in m.get('LmItemInfoList'):
                temp_model = RenderH5OrderResponseBodyModelLmItemInfoList()
                self.lm_item_info_list.append(temp_model.from_map(k))
        self.delivery_info_list = []
        if m.get('DeliveryInfoList') is not None:
            for k in m.get('DeliveryInfoList'):
                temp_model = RenderH5OrderResponseBodyModelDeliveryInfoList()
                self.delivery_info_list.append(temp_model.from_map(k))
        self.address_info_list = []
        if m.get('AddressInfoList') is not None:
            for k in m.get('AddressInfoList'):
                temp_model = RenderH5OrderResponseBodyModelAddressInfoList()
                self.address_info_list.append(temp_model.from_map(k))
        if m.get('InvoiceInfo') is not None:
            temp_model = RenderH5OrderResponseBodyModelInvoiceInfo()
            self.invoice_info = temp_model.from_map(m['InvoiceInfo'])
        return self


class RenderH5OrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: RenderH5OrderResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = RenderH5OrderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class RenderH5OrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenderH5OrderResponseBody = None,
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
            temp_model = RenderH5OrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenderOrderRequestItemList(TeaModel):
    def __init__(
        self,
        sku_id: int = None,
        lm_item_id: str = None,
        item_id: int = None,
        quantity: int = None,
    ):
        self.sku_id = sku_id
        self.lm_item_id = lm_item_id
        self.item_id = item_id
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class RenderOrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        ext_json: str = None,
        delivery_address: str = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        lm_item_id: str = None,
        account_type: str = None,
        item_list: List[RenderOrderRequestItemList] = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.ext_json = ext_json
        self.delivery_address = delivery_address
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.lm_item_id = lm_item_id
        self.account_type = account_type
        self.item_list = item_list

    def validate(self):
        if self.item_list:
            for k in self.item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        result['ItemList'] = []
        if self.item_list is not None:
            for k in self.item_list:
                result['ItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        self.item_list = []
        if m.get('ItemList') is not None:
            for k in m.get('ItemList'):
                temp_model = RenderOrderRequestItemList()
                self.item_list.append(temp_model.from_map(k))
        return self


class RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosLmItemInfosLmItemInfos(TeaModel):
    def __init__(
        self,
        lm_item_id: str = None,
        seller_id: int = None,
        message: str = None,
        item_id: int = None,
        can_sell: bool = None,
        cash: int = None,
        item_name: str = None,
        actual_price: int = None,
        sku_name: str = None,
        sku_id: int = None,
        points: int = None,
        seller_nick: str = None,
        quantity: int = None,
        item_pic_url: str = None,
    ):
        self.lm_item_id = lm_item_id
        self.seller_id = seller_id
        self.message = message
        self.item_id = item_id
        self.can_sell = can_sell
        self.cash = cash
        self.item_name = item_name
        self.actual_price = actual_price
        self.sku_name = sku_name
        self.sku_id = sku_id
        self.points = points
        self.seller_nick = seller_nick
        self.quantity = quantity
        self.item_pic_url = item_pic_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lm_item_id is not None:
            result['LmItemId'] = self.lm_item_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.message is not None:
            result['Message'] = self.message
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.can_sell is not None:
            result['CanSell'] = self.can_sell
        if self.cash is not None:
            result['Cash'] = self.cash
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.actual_price is not None:
            result['ActualPrice'] = self.actual_price
        if self.sku_name is not None:
            result['SkuName'] = self.sku_name
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.points is not None:
            result['Points'] = self.points
        if self.seller_nick is not None:
            result['SellerNick'] = self.seller_nick
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.item_pic_url is not None:
            result['ItemPicUrl'] = self.item_pic_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LmItemId') is not None:
            self.lm_item_id = m.get('LmItemId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('CanSell') is not None:
            self.can_sell = m.get('CanSell')
        if m.get('Cash') is not None:
            self.cash = m.get('Cash')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('ActualPrice') is not None:
            self.actual_price = m.get('ActualPrice')
        if m.get('SkuName') is not None:
            self.sku_name = m.get('SkuName')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('Points') is not None:
            self.points = m.get('Points')
        if m.get('SellerNick') is not None:
            self.seller_nick = m.get('SellerNick')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('ItemPicUrl') is not None:
            self.item_pic_url = m.get('ItemPicUrl')
        return self


class RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosLmItemInfos(TeaModel):
    def __init__(
        self,
        lm_item_infos: List[RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosLmItemInfosLmItemInfos] = None,
    ):
        self.lm_item_infos = lm_item_infos

    def validate(self):
        if self.lm_item_infos:
            for k in self.lm_item_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LmItemInfos'] = []
        if self.lm_item_infos is not None:
            for k in self.lm_item_infos:
                result['LmItemInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.lm_item_infos = []
        if m.get('LmItemInfos') is not None:
            for k in m.get('LmItemInfos'):
                temp_model = RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosLmItemInfosLmItemInfos()
                self.lm_item_infos.append(temp_model.from_map(k))
        return self


class RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosDeliveryInfosDeliveryInfos(TeaModel):
    def __init__(
        self,
        display_name: str = None,
        post_fee: int = None,
        service_type: int = None,
        id: str = None,
    ):
        self.display_name = display_name
        self.post_fee = post_fee
        self.service_type = service_type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.post_fee is not None:
            result['PostFee'] = self.post_fee
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('PostFee') is not None:
            self.post_fee = m.get('PostFee')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosDeliveryInfos(TeaModel):
    def __init__(
        self,
        delivery_infos: List[RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosDeliveryInfosDeliveryInfos] = None,
    ):
        self.delivery_infos = delivery_infos

    def validate(self):
        if self.delivery_infos:
            for k in self.delivery_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeliveryInfos'] = []
        if self.delivery_infos is not None:
            for k in self.delivery_infos:
                result['DeliveryInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_infos = []
        if m.get('DeliveryInfos') is not None:
            for k in m.get('DeliveryInfos'):
                temp_model = RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosDeliveryInfosDeliveryInfos()
                self.delivery_infos.append(temp_model.from_map(k))
        return self


class RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfos(TeaModel):
    def __init__(
        self,
        ext_info: Dict[str, Any] = None,
        lm_item_infos: RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosLmItemInfos = None,
        delivery_infos: RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosDeliveryInfos = None,
    ):
        self.ext_info = ext_info
        self.lm_item_infos = lm_item_infos
        self.delivery_infos = delivery_infos

    def validate(self):
        if self.lm_item_infos:
            self.lm_item_infos.validate()
        if self.delivery_infos:
            self.delivery_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.lm_item_infos is not None:
            result['LmItemInfos'] = self.lm_item_infos.to_map()
        if self.delivery_infos is not None:
            result['DeliveryInfos'] = self.delivery_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('LmItemInfos') is not None:
            temp_model = RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosLmItemInfos()
            self.lm_item_infos = temp_model.from_map(m['LmItemInfos'])
        if m.get('DeliveryInfos') is not None:
            temp_model = RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfosDeliveryInfos()
            self.delivery_infos = temp_model.from_map(m['DeliveryInfos'])
        return self


class RenderOrderResponseBodyModelRenderOrderInfos(TeaModel):
    def __init__(
        self,
        render_order_infos: List[RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfos] = None,
    ):
        self.render_order_infos = render_order_infos

    def validate(self):
        if self.render_order_infos:
            for k in self.render_order_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RenderOrderInfos'] = []
        if self.render_order_infos is not None:
            for k in self.render_order_infos:
                result['RenderOrderInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.render_order_infos = []
        if m.get('RenderOrderInfos') is not None:
            for k in m.get('RenderOrderInfos'):
                temp_model = RenderOrderResponseBodyModelRenderOrderInfosRenderOrderInfos()
                self.render_order_infos.append(temp_model.from_map(k))
        return self


class RenderOrderResponseBodyModel(TeaModel):
    def __init__(
        self,
        render_order_infos: RenderOrderResponseBodyModelRenderOrderInfos = None,
    ):
        self.render_order_infos = render_order_infos

    def validate(self):
        if self.render_order_infos:
            self.render_order_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.render_order_infos is not None:
            result['RenderOrderInfos'] = self.render_order_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderOrderInfos') is not None:
            temp_model = RenderOrderResponseBodyModelRenderOrderInfos()
            self.render_order_infos = temp_model.from_map(m['RenderOrderInfos'])
        return self


class RenderOrderResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: RenderOrderResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = RenderOrderResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class RenderOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenderOrderResponseBody = None,
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
            temp_model = RenderOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RepayForPayUrlRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        lm_order_id: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.lm_order_id = lm_order_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        return self


class RepayForPayUrlResponseBodyModel(TeaModel):
    def __init__(
        self,
        front_url: str = None,
    ):
        self.front_url = front_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.front_url is not None:
            result['FrontUrl'] = self.front_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FrontUrl') is not None:
            self.front_url = m.get('FrontUrl')
        return self


class RepayForPayUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        model: RepayForPayUrlResponseBodyModel = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Model') is not None:
            temp_model = RepayForPayUrlResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class RepayForPayUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RepayForPayUrlResponseBody = None,
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
            temp_model = RepayForPayUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RepayOrderRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        lm_order_id: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.lm_order_id = lm_order_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.lm_order_id is not None:
            result['LmOrderId'] = self.lm_order_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('LmOrderId') is not None:
            self.lm_order_id = m.get('LmOrderId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class RepayOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RepayOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RepayOrderResponseBody = None,
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
            temp_model = RepayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReserveMovieSeatRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        schedule_id: int = None,
        seat_ids: str = None,
        seat_names: str = None,
        biz_uid: str = None,
        mobile: str = None,
        ext_json: str = None,
    ):
        self.biz_id = biz_id
        self.schedule_id = schedule_id
        self.seat_ids = seat_ids
        self.seat_names = seat_names
        self.biz_uid = biz_uid
        self.mobile = mobile
        self.ext_json = ext_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.seat_ids is not None:
            result['SeatIds'] = self.seat_ids
        if self.seat_names is not None:
            result['SeatNames'] = self.seat_names
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('SeatIds') is not None:
            self.seat_ids = m.get('SeatIds')
        if m.get('SeatNames') is not None:
            self.seat_names = m.get('SeatNames')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        return self


class ReserveMovieSeatResponseBodyReservedSeat(TeaModel):
    def __init__(
        self,
        status: str = None,
        reserved_time: int = None,
        apply_key: str = None,
        default_lock_second: int = None,
    ):
        self.status = status
        self.reserved_time = reserved_time
        self.apply_key = apply_key
        self.default_lock_second = default_lock_second

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.reserved_time is not None:
            result['ReservedTime'] = self.reserved_time
        if self.apply_key is not None:
            result['ApplyKey'] = self.apply_key
        if self.default_lock_second is not None:
            result['DefaultLockSecond'] = self.default_lock_second
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ReservedTime') is not None:
            self.reserved_time = m.get('ReservedTime')
        if m.get('ApplyKey') is not None:
            self.apply_key = m.get('ApplyKey')
        if m.get('DefaultLockSecond') is not None:
            self.default_lock_second = m.get('DefaultLockSecond')
        return self


class ReserveMovieSeatResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        logs_id: str = None,
        reserved_seat: ReserveMovieSeatResponseBodyReservedSeat = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.logs_id = logs_id
        self.reserved_seat = reserved_seat

    def validate(self):
        if self.reserved_seat:
            self.reserved_seat.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.reserved_seat is not None:
            result['ReservedSeat'] = self.reserved_seat.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('ReservedSeat') is not None:
            temp_model = ReserveMovieSeatResponseBodyReservedSeat()
            self.reserved_seat = temp_model.from_map(m['ReservedSeat'])
        return self


class ReserveMovieSeatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReserveMovieSeatResponseBody = None,
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
            temp_model = ReserveMovieSeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SettleOrderRequest(TeaModel):
    def __init__(
        self,
        out_request_no: str = None,
        trade_no: str = None,
        royalty_parameters: str = None,
        ext_info: str = None,
        out_trade_no: str = None,
        merchant_id: str = None,
    ):
        self.out_request_no = out_request_no
        self.trade_no = trade_no
        self.royalty_parameters = royalty_parameters
        self.ext_info = ext_info
        self.out_trade_no = out_trade_no
        self.merchant_id = merchant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        if self.trade_no is not None:
            result['TradeNo'] = self.trade_no
        if self.royalty_parameters is not None:
            result['RoyaltyParameters'] = self.royalty_parameters
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.out_trade_no is not None:
            result['OutTradeNo'] = self.out_trade_no
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        if m.get('TradeNo') is not None:
            self.trade_no = m.get('TradeNo')
        if m.get('RoyaltyParameters') is not None:
            self.royalty_parameters = m.get('RoyaltyParameters')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('OutTradeNo') is not None:
            self.out_trade_no = m.get('OutTradeNo')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        return self


class SettleOrderResponseBodyTradeOrderSettleResponse(TeaModel):
    def __init__(
        self,
        trade_no: str = None,
        out_request_no: str = None,
    ):
        self.trade_no = trade_no
        self.out_request_no = out_request_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trade_no is not None:
            result['TradeNo'] = self.trade_no
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TradeNo') is not None:
            self.trade_no = m.get('TradeNo')
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        return self


class SettleOrderResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        trade_order_settle_response: SettleOrderResponseBodyTradeOrderSettleResponse = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.trade_order_settle_response = trade_order_settle_response

    def validate(self):
        if self.trade_order_settle_response:
            self.trade_order_settle_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trade_order_settle_response is not None:
            result['TradeOrderSettleResponse'] = self.trade_order_settle_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TradeOrderSettleResponse') is not None:
            temp_model = SettleOrderResponseBodyTradeOrderSettleResponse()
            self.trade_order_settle_response = temp_model.from_map(m['TradeOrderSettleResponse'])
        return self


class SettleOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SettleOrderResponseBody = None,
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
            temp_model = SettleOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitReturnGoodLogisticsRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        logistics_no: str = None,
        cp_code: str = None,
        sub_lm_order_id: str = None,
        dispute_id: int = None,
        use_anonymous_tb_account: bool = None,
        third_party_user_id: str = None,
        account_type: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.logistics_no = logistics_no
        self.cp_code = cp_code
        self.sub_lm_order_id = sub_lm_order_id
        self.dispute_id = dispute_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.third_party_user_id = third_party_user_id
        self.account_type = account_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.logistics_no is not None:
            result['LogisticsNo'] = self.logistics_no
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.sub_lm_order_id is not None:
            result['SubLmOrderId'] = self.sub_lm_order_id
        if self.dispute_id is not None:
            result['DisputeId'] = self.dispute_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('LogisticsNo') is not None:
            self.logistics_no = m.get('LogisticsNo')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('SubLmOrderId') is not None:
            self.sub_lm_order_id = m.get('SubLmOrderId')
        if m.get('DisputeId') is not None:
            self.dispute_id = m.get('DisputeId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        return self


class SubmitReturnGoodLogisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitReturnGoodLogisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitReturnGoodLogisticsResponseBody = None,
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
            temp_model = SubmitReturnGoodLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncMerchantInfoRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        task_id: str = None,
        seller_nick: str = None,
        item_list: str = None,
        time_stamp: int = None,
    ):
        self.biz_id = biz_id
        self.task_id = task_id
        self.seller_nick = seller_nick
        self.item_list = item_list
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.seller_nick is not None:
            result['SellerNick'] = self.seller_nick
        if self.item_list is not None:
            result['ItemList'] = self.item_list
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('SellerNick') is not None:
            self.seller_nick = m.get('SellerNick')
        if m.get('ItemList') is not None:
            self.item_list = m.get('ItemList')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        return self


class SyncMerchantInfoResponseBodyModel(TeaModel):
    def __init__(
        self,
        status: str = None,
        url: str = None,
        task_id: str = None,
    ):
        self.status = status
        self.url = url
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SyncMerchantInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        model: SyncMerchantInfoResponseBodyModel = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Model') is not None:
            temp_model = SyncMerchantInfoResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class SyncMerchantInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SyncMerchantInfoResponseBody = None,
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
            temp_model = SyncMerchantInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsignWithholdAgreementRequest(TeaModel):
    def __init__(
        self,
        out_request_no: str = None,
        external_agreement_no: str = None,
        merchant_id: str = None,
        agreement_no: str = None,
    ):
        self.out_request_no = out_request_no
        self.external_agreement_no = external_agreement_no
        self.merchant_id = merchant_id
        self.agreement_no = agreement_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        if self.external_agreement_no is not None:
            result['ExternalAgreementNo'] = self.external_agreement_no
        if self.merchant_id is not None:
            result['MerchantId'] = self.merchant_id
        if self.agreement_no is not None:
            result['AgreementNo'] = self.agreement_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        if m.get('ExternalAgreementNo') is not None:
            self.external_agreement_no = m.get('ExternalAgreementNo')
        if m.get('MerchantId') is not None:
            self.merchant_id = m.get('MerchantId')
        if m.get('AgreementNo') is not None:
            self.agreement_no = m.get('AgreementNo')
        return self


class UnsignWithholdAgreementResponseBodyWithholdSignResponse(TeaModel):
    def __init__(
        self,
        out_request_no: str = None,
    ):
        self.out_request_no = out_request_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.out_request_no is not None:
            result['OutRequestNo'] = self.out_request_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutRequestNo') is not None:
            self.out_request_no = m.get('OutRequestNo')
        return self


class UnsignWithholdAgreementResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        withhold_sign_response: UnsignWithholdAgreementResponseBodyWithholdSignResponse = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.withhold_sign_response = withhold_sign_response

    def validate(self):
        if self.withhold_sign_response:
            self.withhold_sign_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.withhold_sign_response is not None:
            result['WithholdSignResponse'] = self.withhold_sign_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WithholdSignResponse') is not None:
            temp_model = UnsignWithholdAgreementResponseBodyWithholdSignResponse()
            self.withhold_sign_response = temp_model.from_map(m['WithholdSignResponse'])
        return self


class UnsignWithholdAgreementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnsignWithholdAgreementResponseBody = None,
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
            temp_model = UnsignWithholdAgreementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAddressRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        third_party_user_id: str = None,
        use_anonymous_tb_account: bool = None,
        address_info: str = None,
    ):
        self.biz_id = biz_id
        self.third_party_user_id = third_party_user_id
        self.use_anonymous_tb_account = use_anonymous_tb_account
        self.address_info = address_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.third_party_user_id is not None:
            result['ThirdPartyUserId'] = self.third_party_user_id
        if self.use_anonymous_tb_account is not None:
            result['UseAnonymousTbAccount'] = self.use_anonymous_tb_account
        if self.address_info is not None:
            result['AddressInfo'] = self.address_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ThirdPartyUserId') is not None:
            self.third_party_user_id = m.get('ThirdPartyUserId')
        if m.get('UseAnonymousTbAccount') is not None:
            self.use_anonymous_tb_account = m.get('UseAnonymousTbAccount')
        if m.get('AddressInfo') is not None:
            self.address_info = m.get('AddressInfo')
        return self


class UpdateAddressResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAddressResponseBody = None,
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
            temp_model = UpdateAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateTaobaoAccountRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_uid: str = None,
        ext_json: str = None,
        tb_user_nick: str = None,
        mobile_no: str = None,
    ):
        self.biz_id = biz_id
        self.biz_uid = biz_uid
        self.ext_json = ext_json
        self.tb_user_nick = tb_user_nick
        self.mobile_no = mobile_no

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.biz_uid is not None:
            result['BizUid'] = self.biz_uid
        if self.ext_json is not None:
            result['ExtJson'] = self.ext_json
        if self.tb_user_nick is not None:
            result['TbUserNick'] = self.tb_user_nick
        if self.mobile_no is not None:
            result['MobileNo'] = self.mobile_no
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BizUid') is not None:
            self.biz_uid = m.get('BizUid')
        if m.get('ExtJson') is not None:
            self.ext_json = m.get('ExtJson')
        if m.get('TbUserNick') is not None:
            self.tb_user_nick = m.get('TbUserNick')
        if m.get('MobileNo') is not None:
            self.mobile_no = m.get('MobileNo')
        return self


class ValidateTaobaoAccountResponseBodyModel(TeaModel):
    def __init__(
        self,
        match: bool = None,
    ):
        self.match = match

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match is not None:
            result['Match'] = self.match
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            self.match = m.get('Match')
        return self


class ValidateTaobaoAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
        sub_message: str = None,
        code: str = None,
        message: str = None,
        sub_code: str = None,
        total_count: int = None,
        logs_id: str = None,
        model: ValidateTaobaoAccountResponseBodyModel = None,
    ):
        self.request_id = request_id
        self.success = success
        self.sub_message = sub_message
        self.code = code
        self.message = message
        self.sub_code = sub_code
        self.total_count = total_count
        self.logs_id = logs_id
        self.model = model

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.sub_message is not None:
            result['SubMessage'] = self.sub_message
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.sub_code is not None:
            result['SubCode'] = self.sub_code
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.logs_id is not None:
            result['LogsId'] = self.logs_id
        if self.model is not None:
            result['Model'] = self.model.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SubMessage') is not None:
            self.sub_message = m.get('SubMessage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('SubCode') is not None:
            self.sub_code = m.get('SubCode')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('LogsId') is not None:
            self.logs_id = m.get('LogsId')
        if m.get('Model') is not None:
            temp_model = ValidateTaobaoAccountResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        return self


class ValidateTaobaoAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ValidateTaobaoAccountResponseBody = None,
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
            temp_model = ValidateTaobaoAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


