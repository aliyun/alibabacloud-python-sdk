# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CommodityValueResultOrder(TeaModel):
    def __init__(
        self,
        currency: str = None,
        trade_amount: str = None,
        discount_amount: str = None,
        original_amount: str = None,
    ):
        # 货币代码。
        self.currency = currency
        # 优惠后。
        self.trade_amount = trade_amount
        # 抵扣金额。
        self.discount_amount = discount_amount
        # 优惠前。
        self.original_amount = original_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        return self


class CommodityValueResultSubOrdersSubOrderModuleInstanceModuleAttrs(TeaModel):
    def __init__(
        self,
        type: int = None,
        name: str = None,
        code: str = None,
        value: str = None,
        unit: str = None,
    ):
        # 属性类型，可选值：
        # 
        # 1. 1：商品属性 
        # 2. 2：规格属性 
        # 3. 3：模块属性 
        # 4. 4：外部参数（备用）
        self.type = type
        # Name
        self.name = name
        # Module attr code
        self.code = code
        # Value
        self.value = value
        # Unit
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class CommodityValueResultSubOrdersSubOrderModuleInstance(TeaModel):
    def __init__(
        self,
        module_id: int = None,
        module_name: str = None,
        module_code: str = None,
        total_product_fee: float = None,
        discount_fee: float = None,
        pay_fee: float = None,
        price_unit: str = None,
        is_pricing_module: bool = None,
        need_order_pay: bool = None,
        price_type: str = None,
        module_attrs: List[CommodityValueResultSubOrdersSubOrderModuleInstanceModuleAttrs] = None,
    ):
        # 模块ID。
        self.module_id = module_id
        # 模块名称。
        self.module_name = module_name
        # 模块代码。
        self.module_code = module_code
        # 产品原价（元）。
        self.total_product_fee = total_product_fee
        # 折扣费用（元）。
        self.discount_fee = discount_fee
        # 实付金额（元）。
        self.pay_fee = pay_fee
        # 价格单位。
        self.price_unit = price_unit
        # 是否计价项。
        self.is_pricing_module = is_pricing_module
        # 在订单中是否需要支付。
        self.need_order_pay = need_order_pay
        # 定价类型。
        self.price_type = price_type
        # 模块属性。
        self.module_attrs = module_attrs

    def validate(self):
        if self.module_attrs:
            for k in self.module_attrs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.total_product_fee is not None:
            result['TotalProductFee'] = self.total_product_fee
        if self.discount_fee is not None:
            result['DiscountFee'] = self.discount_fee
        if self.pay_fee is not None:
            result['PayFee'] = self.pay_fee
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.is_pricing_module is not None:
            result['IsPricingModule'] = self.is_pricing_module
        if self.need_order_pay is not None:
            result['NeedOrderPay'] = self.need_order_pay
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        result['ModuleAttrs'] = []
        if self.module_attrs is not None:
            for k in self.module_attrs:
                result['ModuleAttrs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('TotalProductFee') is not None:
            self.total_product_fee = m.get('TotalProductFee')
        if m.get('DiscountFee') is not None:
            self.discount_fee = m.get('DiscountFee')
        if m.get('PayFee') is not None:
            self.pay_fee = m.get('PayFee')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('IsPricingModule') is not None:
            self.is_pricing_module = m.get('IsPricingModule')
        if m.get('NeedOrderPay') is not None:
            self.need_order_pay = m.get('NeedOrderPay')
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        self.module_attrs = []
        if m.get('ModuleAttrs') is not None:
            for k in m.get('ModuleAttrs'):
                temp_model = CommodityValueResultSubOrdersSubOrderModuleInstanceModuleAttrs()
                self.module_attrs.append(temp_model.from_map(k))
        return self


class CommodityValueResultSubOrdersSubOrder(TeaModel):
    def __init__(
        self,
        module_instance: List[CommodityValueResultSubOrdersSubOrderModuleInstance] = None,
    ):
        # 模块（实例）信息。
        self.module_instance = module_instance

    def validate(self):
        if self.module_instance:
            for k in self.module_instance:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ModuleInstance'] = []
        if self.module_instance is not None:
            for k in self.module_instance:
                result['ModuleInstance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_instance = []
        if m.get('ModuleInstance') is not None:
            for k in m.get('ModuleInstance'):
                temp_model = CommodityValueResultSubOrdersSubOrderModuleInstance()
                self.module_instance.append(temp_model.from_map(k))
        return self


class CommodityValueResultSubOrders(TeaModel):
    def __init__(
        self,
        sub_order: List[CommodityValueResultSubOrdersSubOrder] = None,
    ):
        # 订单子项。
        self.sub_order = sub_order

    def validate(self):
        if self.sub_order:
            for k in self.sub_order:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubOrder'] = []
        if self.sub_order is not None:
            for k in self.sub_order:
                result['SubOrder'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_order = []
        if m.get('SubOrder') is not None:
            for k in m.get('SubOrder'):
                temp_model = CommodityValueResultSubOrdersSubOrder()
                self.sub_order.append(temp_model.from_map(k))
        return self


class CommodityValueResultCoupons(TeaModel):
    def __init__(
        self,
        can_prom_fee: float = None,
        coupon_desc: str = None,
        coupon_name: str = None,
        coupon_option_no: str = None,
        selected: bool = None,
    ):
        # 可支付金额。
        self.can_prom_fee = can_prom_fee
        # Coupon Description
        self.coupon_desc = coupon_desc
        # Coupon Name
        self.coupon_name = coupon_name
        # Coupon OptionNo
        self.coupon_option_no = coupon_option_no
        # 是否选中。
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_prom_fee is not None:
            result['CanPromFee'] = self.can_prom_fee
        if self.coupon_desc is not None:
            result['CouponDesc'] = self.coupon_desc
        if self.coupon_name is not None:
            result['CouponName'] = self.coupon_name
        if self.coupon_option_no is not None:
            result['CouponOptionNo'] = self.coupon_option_no
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanPromFee') is not None:
            self.can_prom_fee = m.get('CanPromFee')
        if m.get('CouponDesc') is not None:
            self.coupon_desc = m.get('CouponDesc')
        if m.get('CouponName') is not None:
            self.coupon_name = m.get('CouponName')
        if m.get('CouponOptionNo') is not None:
            self.coupon_option_no = m.get('CouponOptionNo')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class CommodityValueResult(TeaModel):
    def __init__(
        self,
        order: CommodityValueResultOrder = None,
        inquiry_type: str = None,
        sub_orders: CommodityValueResultSubOrders = None,
        coupons: List[CommodityValueResultCoupons] = None,
    ):
        # 订单信息。
        self.order = order
        # 询价类型，可选值：
        # 1. Buy：新购询价。
        # 2. ModificationBuy：变配询价。
        self.inquiry_type = inquiry_type
        # 订单子项。
        self.sub_orders = sub_orders
        # 优惠券。
        self.coupons = coupons

    def validate(self):
        if self.order:
            self.order.validate()
        if self.sub_orders:
            self.sub_orders.validate()
        if self.coupons:
            for k in self.coupons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order.to_map()
        if self.inquiry_type is not None:
            result['InquiryType'] = self.inquiry_type
        if self.sub_orders is not None:
            result['SubOrders'] = self.sub_orders.to_map()
        result['Coupons'] = []
        if self.coupons is not None:
            for k in self.coupons:
                result['Coupons'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            temp_model = CommodityValueResultOrder()
            self.order = temp_model.from_map(m['Order'])
        if m.get('InquiryType') is not None:
            self.inquiry_type = m.get('InquiryType')
        if m.get('SubOrders') is not None:
            temp_model = CommodityValueResultSubOrders()
            self.sub_orders = temp_model.from_map(m['SubOrders'])
        self.coupons = []
        if m.get('Coupons') is not None:
            for k in m.get('Coupons'):
                temp_model = CommodityValueResultCoupons()
                self.coupons.append(temp_model.from_map(k))
        return self


class CommodityValue(TeaModel):
    def __init__(
        self,
        result: CommodityValueResult = None,
    ):
        # Result模型。
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Result') is not None:
            temp_model = CommodityValueResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CancelServiceUsageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        need_delete: bool = None,
        service_id: str = None,
    ):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to delete the application.
        # 
        # >  After you delete the application, you must re-enter the application information the next time you submit an application.
        self.need_delete = need_delete
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.need_delete is not None:
            result['NeedDelete'] = self.need_delete
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NeedDelete') is not None:
            self.need_delete = m.get('NeedDelete')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class CancelServiceUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class CancelServiceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelServiceUsageResponseBody = None,
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
            temp_model = CancelServiceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        new_resource_group_id: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the new resource group.
        # 
        # You can view resource group IDs in the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups) .
        self.new_resource_group_id = new_resource_group_id
        # The region ID.
        self.region_id = region_id
        # The ID of the cloud resource that you want to move to a new resource group.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   service: service
        # *   serviceinstance: service instance
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckServiceDeployableRequest(TeaModel):
    def __init__(
        self,
        post_paid_amount: str = None,
        pre_paid_amount: str = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        trial_type: str = None,
    ):
        # Total amount of postpaid.
        self.post_paid_amount = post_paid_amount
        # Total amount of prepayment.
        self.pre_paid_amount = pre_paid_amount
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        self.service_version = service_version
        # The trial type of the service instance. Valid values:
        # 
        # *   **Trial**: Trials are supported.
        # *   **NotTrial**: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_paid_amount is not None:
            result['PostPaidAmount'] = self.post_paid_amount
        if self.pre_paid_amount is not None:
            result['PrePaidAmount'] = self.pre_paid_amount
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostPaidAmount') is not None:
            self.post_paid_amount = m.get('PostPaidAmount')
        if m.get('PrePaidAmount') is not None:
            self.pre_paid_amount = m.get('PrePaidAmount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class CheckServiceDeployableResponseBodyCheckResults(TeaModel):
    def __init__(
        self,
        message: str = None,
        type: str = None,
        value: str = None,
    ):
        # Returns a hint message for the result.
        self.message = message
        # Check type, invalid values:
        # 
        # - Balance ：Account balance.
        # 
        # - Quota:  Account quota.
        self.type = type
        # Inspection result.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CheckServiceDeployableResponseBody(TeaModel):
    def __init__(
        self,
        check_results: List[CheckServiceDeployableResponseBodyCheckResults] = None,
        request_id: str = None,
    ):
        # Inspection result.
        self.check_results = check_results
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.check_results:
            for k in self.check_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CheckResults'] = []
        if self.check_results is not None:
            for k in self.check_results:
                result['CheckResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_results = []
        if m.get('CheckResults') is not None:
            for k in m.get('CheckResults'):
                temp_model = CheckServiceDeployableResponseBodyCheckResults()
                self.check_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckServiceDeployableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckServiceDeployableResponseBody = None,
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
            temp_model = CheckServiceDeployableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ContinueDeployServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        option: List[str] = None,
        parameters: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   true: performs a dry run for the request, but does not create a service instance.
        # *   false: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # The options that the system adopts when the system continues to create the service instance.
        self.option = option
        # The parameters configured for the service instance.
        self.parameters = parameters
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.option is not None:
            result['Option'] = self.option
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Option') is not None:
            self.option = m.get('Option')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ContinueDeployServiceInstanceResponseBodyDryRunResult(TeaModel):
    def __init__(
        self,
        parameters_allowed_to_be_modified: List[str] = None,
        parameters_conditionally_allowed_to_be_modified: List[str] = None,
        parameters_not_allowed_to_be_modified: List[str] = None,
    ):
        # The parameters that can be modified. The operation that is performed to modify the parameters does not cause a validation error.
        # 
        # > This parameter is returned only if DryRun is set to true.
        self.parameters_allowed_to_be_modified = parameters_allowed_to_be_modified
        # The parameters that can be modified under specific conditions. The new values of the parameters determine whether the operation that is performed to modify the parameters causes a validation error.
        # 
        # > This parameter is returned only if DryRun is set to true.
        self.parameters_conditionally_allowed_to_be_modified = parameters_conditionally_allowed_to_be_modified
        # The parameters that cannot be modified. The operation that is performed to modify the parameters causes a validation error.
        # 
        # > This parameter is returned only if DryRun is set to true.
        self.parameters_not_allowed_to_be_modified = parameters_not_allowed_to_be_modified

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters_allowed_to_be_modified is not None:
            result['ParametersAllowedToBeModified'] = self.parameters_allowed_to_be_modified
        if self.parameters_conditionally_allowed_to_be_modified is not None:
            result['ParametersConditionallyAllowedToBeModified'] = self.parameters_conditionally_allowed_to_be_modified
        if self.parameters_not_allowed_to_be_modified is not None:
            result['ParametersNotAllowedToBeModified'] = self.parameters_not_allowed_to_be_modified
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParametersAllowedToBeModified') is not None:
            self.parameters_allowed_to_be_modified = m.get('ParametersAllowedToBeModified')
        if m.get('ParametersConditionallyAllowedToBeModified') is not None:
            self.parameters_conditionally_allowed_to_be_modified = m.get('ParametersConditionallyAllowedToBeModified')
        if m.get('ParametersNotAllowedToBeModified') is not None:
            self.parameters_not_allowed_to_be_modified = m.get('ParametersNotAllowedToBeModified')
        return self


class ContinueDeployServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dry_run_result: ContinueDeployServiceInstanceResponseBodyDryRunResult = None,
        request_id: str = None,
        service_instance_id: str = None,
    ):
        # The dry run result.
        self.dry_run_result = dry_run_result
        # The request ID.
        self.request_id = request_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.dry_run_result:
            self.dry_run_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run_result is not None:
            result['DryRunResult'] = self.dry_run_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRunResult') is not None:
            temp_model = ContinueDeployServiceInstanceResponseBodyDryRunResult()
            self.dry_run_result = temp_model.from_map(m['DryRunResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ContinueDeployServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ContinueDeployServiceInstanceResponseBody = None,
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
            temp_model = ContinueDeployServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceInstanceRequestCommodity(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        coupon_id: str = None,
        pay_period: int = None,
        pay_period_unit: str = None,
    ):
        # Specifies whether to automatically complete the payment. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the service instance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_renew = auto_renew
        # The coupon ID.
        self.coupon_id = coupon_id
        # The subscription duration.
        self.pay_period = pay_period
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**\
        # *   **Month**\
        # *   **Day**\
        self.pay_period_unit = pay_period_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.pay_period is not None:
            result['PayPeriod'] = self.pay_period
        if self.pay_period_unit is not None:
            result['PayPeriodUnit'] = self.pay_period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')
        if m.get('PayPeriodUnit') is not None:
            self.pay_period_unit = m.get('PayPeriodUnit')
        return self


class CreateServiceInstanceRequestOperationMetadata(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        extra_info: str = None,
        resources: str = None,
        service_instance_id: str = None,
        start_time: str = None,
    ):
        # The operation end time.
        self.end_time = end_time
        # The additional information.
        self.extra_info = extra_info
        # Imported resource.
        self.resources = resources
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The operation start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateServiceInstanceRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class CreateServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: CreateServiceInstanceRequestCommodity = None,
        contact_group: str = None,
        dry_run: bool = None,
        enable_instance_ops: bool = None,
        enable_user_prometheus: bool = None,
        name: str = None,
        operation_metadata: CreateServiceInstanceRequestOperationMetadata = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        resource_auto_pay: bool = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_code: str = None,
        specification_name: str = None,
        tag: List[CreateServiceInstanceRequestTag] = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the order placed in Alibaba Cloud Marketplace. You do not need to specify this parameter if the service is not published in Alibaba Cloud Marketplace or uses the pay-as-you-go billing method.
        self.commodity = commodity
        # The alert contact group.
        self.contact_group = contact_group
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   **true**: performs a dry run for the request, but does not create a service instance.
        # *   **false**: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # Specifies whether the service instance supports the hosted O\\&M feature. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_instance_ops = enable_instance_ops
        # Specifies whether to enable the Prometheus monitoring feature. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_user_prometheus = enable_user_prometheus
        # The serviceInstance name.
        self.name = name
        # The operation metadata.
        self.operation_metadata = operation_metadata
        # The parameters that the customer specifies to deploy the service instance.
        # 
        # >  If region information is required to create a service instance, you must specify the region ID in the value of Parameters.
        self.parameters = parameters
        # The region ID. Valid values:
        # 
        # *   cn-hangzhou: China (Hangzhou).
        # *   ap-southeast-1: Singapore.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to automatically deduct the resource fees from the account balance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.resource_auto_pay = resource_auto_pay
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # Specification code.
        self.specification_code = specification_code
        # The package name.
        self.specification_name = specification_name
        # The tags.
        self.tag = tag
        # The name of the template.
        self.template_name = template_name
        # The trial type of the service instance. Valid values:
        # 
        # *   **Trial**: Trials are supported.
        # *   **NotTrial**: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_auto_pay is not None:
            result['ResourceAutoPay'] = self.resource_auto_pay
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            temp_model = CreateServiceInstanceRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationMetadata') is not None:
            temp_model = CreateServiceInstanceRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m['OperationMetadata'])
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceAutoPay') is not None:
            self.resource_auto_pay = m.get('ResourceAutoPay')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateServiceInstanceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class CreateServiceInstanceShrinkRequestCommodity(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        coupon_id: str = None,
        pay_period: int = None,
        pay_period_unit: str = None,
    ):
        # Specifies whether to automatically complete the payment. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal for the service instance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_renew = auto_renew
        # The coupon ID.
        self.coupon_id = coupon_id
        # The subscription duration.
        self.pay_period = pay_period
        # The unit of the subscription duration. Valid values:
        # 
        # *   **Year**\
        # *   **Month**\
        # *   **Day**\
        self.pay_period_unit = pay_period_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.pay_period is not None:
            result['PayPeriod'] = self.pay_period
        if self.pay_period_unit is not None:
            result['PayPeriodUnit'] = self.pay_period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')
        if m.get('PayPeriodUnit') is not None:
            self.pay_period_unit = m.get('PayPeriodUnit')
        return self


class CreateServiceInstanceShrinkRequestOperationMetadata(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        extra_info: str = None,
        resources: str = None,
        service_instance_id: str = None,
        start_time: str = None,
    ):
        # The operation end time.
        self.end_time = end_time
        # The additional information.
        self.extra_info = extra_info
        # Imported resource.
        self.resources = resources
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The operation start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateServiceInstanceShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class CreateServiceInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: CreateServiceInstanceShrinkRequestCommodity = None,
        contact_group: str = None,
        dry_run: bool = None,
        enable_instance_ops: bool = None,
        enable_user_prometheus: bool = None,
        name: str = None,
        operation_metadata: CreateServiceInstanceShrinkRequestOperationMetadata = None,
        parameters_shrink: str = None,
        region_id: str = None,
        resource_auto_pay: bool = None,
        resource_group_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_code: str = None,
        specification_name: str = None,
        tag: List[CreateServiceInstanceShrinkRequestTag] = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the order placed in Alibaba Cloud Marketplace. You do not need to specify this parameter if the service is not published in Alibaba Cloud Marketplace or uses the pay-as-you-go billing method.
        self.commodity = commodity
        # The alert contact group.
        self.contact_group = contact_group
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   **true**: performs a dry run for the request, but does not create a service instance.
        # *   **false**: performs a dry run for the request, and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # Specifies whether the service instance supports the hosted O\\&M feature. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_instance_ops = enable_instance_ops
        # Specifies whether to enable the Prometheus monitoring feature. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.enable_user_prometheus = enable_user_prometheus
        # The serviceInstance name.
        self.name = name
        # The operation metadata.
        self.operation_metadata = operation_metadata
        # The parameters that the customer specifies to deploy the service instance.
        # 
        # >  If region information is required to create a service instance, you must specify the region ID in the value of Parameters.
        self.parameters_shrink = parameters_shrink
        # The region ID. Valid values:
        # 
        # *   cn-hangzhou: China (Hangzhou).
        # *   ap-southeast-1: Singapore.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to automatically deduct the resource fees from the account balance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.resource_auto_pay = resource_auto_pay
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # Specification code.
        self.specification_code = specification_code
        # The package name.
        self.specification_name = specification_name
        # The tags.
        self.tag = tag
        # The name of the template.
        self.template_name = template_name
        # The trial type of the service instance. Valid values:
        # 
        # *   **Trial**: Trials are supported.
        # *   **NotTrial**: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.operation_metadata:
            self.operation_metadata.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.contact_group is not None:
            result['ContactGroup'] = self.contact_group
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.name is not None:
            result['Name'] = self.name
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata.to_map()
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_auto_pay is not None:
            result['ResourceAutoPay'] = self.resource_auto_pay
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            temp_model = CreateServiceInstanceShrinkRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('ContactGroup') is not None:
            self.contact_group = m.get('ContactGroup')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperationMetadata') is not None:
            temp_model = CreateServiceInstanceShrinkRequestOperationMetadata()
            self.operation_metadata = temp_model.from_map(m['OperationMetadata'])
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceAutoPay') is not None:
            self.resource_auto_pay = m.get('ResourceAutoPay')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateServiceInstanceShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class CreateServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        market_instance_id: str = None,
        order_id: str = None,
        request_id: str = None,
        service_instance_id: str = None,
        status: str = None,
    ):
        # The MartketInstance ID.
        self.market_instance_id = market_instance_id
        # The order ID.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The status of the service instance. Valid values:
        # 
        # *   **Created**\
        # *   **Deploying**\
        # *   **DeployedFailed**\
        # *   **Deployed**\
        # *   **Upgrading**\
        # *   **Deleting**\
        # *   **Deleted**\
        # *   **DeletedFailed**\
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceInstanceResponseBody = None,
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
            temp_model = CreateServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceUsageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        service_id: str = None,
        user_information: Dict[str, str] = None,
    ):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The application information.
        self.user_information = user_information

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_information is not None:
            result['UserInformation'] = self.user_information
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserInformation') is not None:
            self.user_information = m.get('UserInformation')
        return self


class CreateServiceUsageShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        service_id: str = None,
        user_information_shrink: str = None,
    ):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The application information.
        self.user_information_shrink = user_information_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_information_shrink is not None:
            result['UserInformation'] = self.user_information_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserInformation') is not None:
            self.user_information_shrink = m.get('UserInformation')
        return self


class CreateServiceUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class CreateServiceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceUsageResponseBody = None,
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
            temp_model = CreateServiceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the service instances.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class DeleteServiceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteServiceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceInstancesResponseBody = None,
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
            temp_model = DeleteServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # Ensures idempotency of the request. Generate a unique value for this parameter from your client to ensure it is unique across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters.
        self.client_token = client_token
        # Region ID. Allowed values:
        # 
        # - cn-hangzhou: East China 1 (Hangzhou).
        # 
        # - ap-southeast-1: Singapore.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class DeployServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeployServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployServiceInstanceResponseBody = None,
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
            temp_model = DeployServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The region endpoint.
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The available regions.
        self.regions = regions
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GenerateServicePolicyRequest(TeaModel):
    def __init__(
        self,
        operation_types: List[str] = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The type of operation N for which you want to generate the policy information.
        # 
        # Valid values:
        # 
        # *   CreateServiceInstance: creates a serviceInstance by calling the CreateServiceInstance operation.
        # *   UpdateServiceInstance: updates a serviceInstance by calling the UpdateServiceInstance operation.
        # *   DeleteServiceInstance: deletes a serviceInstance by calling the DeleteServiceInstance operation.
        # 
        # >  The default value is the combination of all valid values.
        self.operation_types = operation_types
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service version.
        self.service_version = service_version
        # The name of the template.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_types is not None:
            result['OperationTypes'] = self.operation_types
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperationTypes') is not None:
            self.operation_types = m.get('OperationTypes')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class GenerateServicePolicyResponseBodyMissingPolicy(TeaModel):
    def __init__(
        self,
        action: List[str] = None,
        resource: str = None,
        service_name: str = None,
    ):
        # Operations on specific resources.
        self.action = action
        # The specific objects authorized. An asterisk (*) denotes all resources.
        self.resource = resource
        # The name of the service.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class GenerateServicePolicyResponseBody(TeaModel):
    def __init__(
        self,
        missing_policy: List[GenerateServicePolicyResponseBodyMissingPolicy] = None,
        policy: str = None,
        request_id: str = None,
    ):
        # The policies that are missing.
        self.missing_policy = missing_policy
        # The RAM policy.
        self.policy = policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.missing_policy:
            for k in self.missing_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MissingPolicy'] = []
        if self.missing_policy is not None:
            for k in self.missing_policy:
                result['MissingPolicy'].append(k.to_map() if k else None)
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.missing_policy = []
        if m.get('MissingPolicy') is not None:
            for k in m.get('MissingPolicy'):
                temp_model = GenerateServicePolicyResponseBodyMissingPolicy()
                self.missing_policy.append(temp_model.from_map(k))
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GenerateServicePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateServicePolicyResponseBody = None,
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
            temp_model = GenerateServicePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_name: str = None,
        service_version: str = None,
        show_details: List[str] = None,
    ):
        # Region Id.
        self.region_id = region_id
        # The service ID.
        self.service_id = service_id
        # The service instance id.
        self.service_instance_id = service_instance_id
        # The service name.
        self.service_name = service_name
        # The service version.
        self.service_version = service_version
        # Whether to disclose service details.
        self.show_details = show_details

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.show_details is not None:
            result['ShowDetails'] = self.show_details
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('ShowDetails') is not None:
            self.show_details = m.get('ShowDetails')
        return self


class GetServiceResponseBodyCommodityCssMetadataComponentsMappings(TeaModel):
    def __init__(
        self,
        mappings: Dict[str, str] = None,
        template_name: str = None,
    ):
        # The mappings.
        self.mappings = mappings
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mappings is not None:
            result['Mappings'] = self.mappings
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mappings') is not None:
            self.mappings = m.get('Mappings')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceResponseBodyCommodityCssMetadata(TeaModel):
    def __init__(
        self,
        components_mappings: List[GetServiceResponseBodyCommodityCssMetadataComponentsMappings] = None,
    ):
        # The mapping information about the billing items.
        self.components_mappings = components_mappings

    def validate(self):
        if self.components_mappings:
            for k in self.components_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentsMappings'] = []
        if self.components_mappings is not None:
            for k in self.components_mappings:
                result['ComponentsMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.components_mappings = []
        if m.get('ComponentsMappings') is not None:
            for k in m.get('ComponentsMappings'):
                temp_model = GetServiceResponseBodyCommodityCssMetadataComponentsMappings()
                self.components_mappings.append(temp_model.from_map(k))
        return self


class GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings(TeaModel):
    def __init__(
        self,
        specification_code: str = None,
        specification_name: str = None,
        template_name: str = None,
    ):
        # The specification code of the service in Alibaba Cloud Marketplace.
        self.specification_code = specification_code
        # The package name.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.specification_code is not None:
            result['SpecificationCode'] = self.specification_code
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpecificationCode') is not None:
            self.specification_code = m.get('SpecificationCode')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceResponseBodyCommodityMarketplaceMetadata(TeaModel):
    def __init__(
        self,
        specification_mappings: List[GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings] = None,
    ):
        # The mappings between the service specifications and the template or package.
        self.specification_mappings = specification_mappings

    def validate(self):
        if self.specification_mappings:
            for k in self.specification_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SpecificationMappings'] = []
        if self.specification_mappings is not None:
            for k in self.specification_mappings:
                result['SpecificationMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.specification_mappings = []
        if m.get('SpecificationMappings') is not None:
            for k in m.get('SpecificationMappings'):
                temp_model = GetServiceResponseBodyCommodityMarketplaceMetadataSpecificationMappings()
                self.specification_mappings.append(temp_model.from_map(k))
        return self


class GetServiceResponseBodyCommoditySpecifications(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        times: List[str] = None,
    ):
        # The commodity code.
        self.code = code
        # The specification name.
        self.name = name
        # The subscription duration. Unit: week or year.
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.times is not None:
            result['Times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Times') is not None:
            self.times = m.get('Times')
        return self


class GetServiceResponseBodyCommodity(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        css_metadata: GetServiceResponseBodyCommodityCssMetadata = None,
        deploy_page: str = None,
        marketplace_metadata: GetServiceResponseBodyCommodityMarketplaceMetadata = None,
        order_time: Dict[str, List[str]] = None,
        saas_boost_metadata: str = None,
        specifications: List[GetServiceResponseBodyCommoditySpecifications] = None,
        type: str = None,
    ):
        # The billing method of the service. Valid values:
        # 
        # *   **PREPAY** (default): subscription.
        # *   **POSTPAY**: pay-as-you-go.
        self.charge_type = charge_type
        # The commodity code of the service in Alibaba Cloud Marketplace.
        self.commodity_code = commodity_code
        # The configuration metadata related to Lingxiao.
        self.css_metadata = css_metadata
        # The deploy page.
        self.deploy_page = deploy_page
        # The metadata of Alibaba Cloud Marketplace.
        self.marketplace_metadata = marketplace_metadata
        # The order time.
        self.order_time = order_time
        # The configuration metadata related to Saas Boost.
        self.saas_boost_metadata = saas_boost_metadata
        # The specification details of the service in Alibaba Cloud Marketplace.
        self.specifications = specifications
        # The service type. Valid values:
        # 
        # *   marketplace: Alibaba Cloud Marketplace.
        # *   Css: Lingxiao.
        self.type = type

    def validate(self):
        if self.css_metadata:
            self.css_metadata.validate()
        if self.marketplace_metadata:
            self.marketplace_metadata.validate()
        if self.specifications:
            for k in self.specifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.css_metadata is not None:
            result['CssMetadata'] = self.css_metadata.to_map()
        if self.deploy_page is not None:
            result['DeployPage'] = self.deploy_page
        if self.marketplace_metadata is not None:
            result['MarketplaceMetadata'] = self.marketplace_metadata.to_map()
        if self.order_time is not None:
            result['OrderTime'] = self.order_time
        if self.saas_boost_metadata is not None:
            result['SaasBoostMetadata'] = self.saas_boost_metadata
        result['Specifications'] = []
        if self.specifications is not None:
            for k in self.specifications:
                result['Specifications'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CssMetadata') is not None:
            temp_model = GetServiceResponseBodyCommodityCssMetadata()
            self.css_metadata = temp_model.from_map(m['CssMetadata'])
        if m.get('DeployPage') is not None:
            self.deploy_page = m.get('DeployPage')
        if m.get('MarketplaceMetadata') is not None:
            temp_model = GetServiceResponseBodyCommodityMarketplaceMetadata()
            self.marketplace_metadata = temp_model.from_map(m['MarketplaceMetadata'])
        if m.get('OrderTime') is not None:
            self.order_time = m.get('OrderTime')
        if m.get('SaasBoostMetadata') is not None:
            self.saas_boost_metadata = m.get('SaasBoostMetadata')
        self.specifications = []
        if m.get('Specifications') is not None:
            for k in m.get('Specifications'):
                temp_model = GetServiceResponseBodyCommoditySpecifications()
                self.specifications.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetServiceResponseBodyComplianceMetadata(TeaModel):
    def __init__(
        self,
        compliance_packs: List[str] = None,
    ):
        self.compliance_packs = compliance_packs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_packs is not None:
            result['CompliancePacks'] = self.compliance_packs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePacks') is not None:
            self.compliance_packs = m.get('CompliancePacks')
        return self


class GetServiceResponseBodyInstanceRoleInfos(TeaModel):
    def __init__(
        self,
        policy_document: str = None,
        principals: List[str] = None,
        role_name: str = None,
        template_name: str = None,
    ):
        # The content of the policy.
        self.policy_document = policy_document
        # The information of the RAM entity.
        self.principals = principals
        # The ram role name.
        self.role_name = role_name
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.principals is not None:
            result['Principals'] = self.principals
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('Principals') is not None:
            self.principals = m.get('Principals')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceResponseBodyServiceDocumentInfos(TeaModel):
    def __init__(
        self,
        document_url: str = None,
        locale: str = None,
        template_name: str = None,
    ):
        # The URL that is used to access the document.
        self.document_url = document_url
        # The language that you use for the query. Valid values: zh-CN and en-US.
        self.locale = locale
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.document_url is not None:
            result['DocumentUrl'] = self.document_url
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocumentUrl') is not None:
            self.document_url = m.get('DocumentUrl')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class GetServiceResponseBodyServiceInfosAgreements(TeaModel):
    def __init__(
        self,
        name: str = None,
        url: str = None,
    ):
        # The agreement name.
        self.name = name
        # The agreement URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetServiceResponseBodyServiceInfosSoftwares(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        # The name of the Software.
        self.name = name
        # The version of the software.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetServiceResponseBodyServiceInfos(TeaModel):
    def __init__(
        self,
        agreements: List[GetServiceResponseBodyServiceInfosAgreements] = None,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
        softwares: List[GetServiceResponseBodyServiceInfosSoftwares] = None,
    ):
        # The agreement information about the service.
        self.agreements = agreements
        # The URL of the service icon.
        self.image = image
        # The language of the service. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.locale = locale
        # The service name.
        self.name = name
        # The description of the service.
        self.short_description = short_description
        # The list of the software in the service.
        self.softwares = softwares

    def validate(self):
        if self.agreements:
            for k in self.agreements:
                if k:
                    k.validate()
        if self.softwares:
            for k in self.softwares:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Agreements'] = []
        if self.agreements is not None:
            for k in self.agreements:
                result['Agreements'].append(k.to_map() if k else None)
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        result['Softwares'] = []
        if self.softwares is not None:
            for k in self.softwares:
                result['Softwares'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agreements = []
        if m.get('Agreements') is not None:
            for k in m.get('Agreements'):
                temp_model = GetServiceResponseBodyServiceInfosAgreements()
                self.agreements.append(temp_model.from_map(k))
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        self.softwares = []
        if m.get('Softwares') is not None:
            for k in m.get('Softwares'):
                temp_model = GetServiceResponseBodyServiceInfosSoftwares()
                self.softwares.append(temp_model.from_map(k))
        return self


class GetServiceResponseBodySupportContacts(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of contact information.
        self.type = type
        # The value of contact information.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetServiceResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        alarm_metadata: str = None,
        categories: str = None,
        commodity: GetServiceResponseBodyCommodity = None,
        compliance_metadata: GetServiceResponseBodyComplianceMetadata = None,
        deploy_from: str = None,
        deploy_metadata: str = None,
        deploy_type: str = None,
        duration: int = None,
        instance_role_infos: List[GetServiceResponseBodyInstanceRoleInfos] = None,
        is_support_operated: bool = None,
        license_metadata: str = None,
        log_metadata: str = None,
        operation_metadata: str = None,
        permission: str = None,
        policy_names: str = None,
        publish_time: str = None,
        request_id: str = None,
        service_document_infos: List[GetServiceResponseBodyServiceDocumentInfos] = None,
        service_id: str = None,
        service_infos: List[GetServiceResponseBodyServiceInfos] = None,
        service_product_url: str = None,
        service_type: str = None,
        share_type: str = None,
        status: str = None,
        supplier_desc: str = None,
        supplier_logo: str = None,
        supplier_name: str = None,
        supplier_uid: int = None,
        supplier_url: str = None,
        support_contacts: List[GetServiceResponseBodySupportContacts] = None,
        tags: List[GetServiceResponseBodyTags] = None,
        tenant_type: str = None,
        trial_duration: int = None,
        trial_type: str = None,
        version: str = None,
        version_name: str = None,
    ):
        # The alert configurations of the service.
        # 
        # >  This parameter takes effect only when you specify an alert policy for **PolicyNames**.
        self.alarm_metadata = alarm_metadata
        # The categories of the Flow.
        self.categories = categories
        # The information about the order placed in Alibaba Cloud Marketplace.
        self.commodity = commodity
        self.compliance_metadata = compliance_metadata
        # Service deployment approach, Valid values：
        # 
        # - NoWhere
        # - Marketplace
        # - ComputeNest
        self.deploy_from = deploy_from
        # The storage configurations of the service. The format in which the deployment information of a service is stored varies based on the deployment type of the service. In this case, the deployment information is stored in the JSON string format.
        self.deploy_metadata = deploy_metadata
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        self.deploy_type = deploy_type
        # The duration for which hosted O\\&M is implemented. Unit: seconds.
        self.duration = duration
        # Information about the ram role created in the service template.
        self.instance_role_infos = instance_role_infos
        # Indicates whether the hosted O\\&M feature is enabled for the service. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is returned if you set **ServiceType** to **private**.
        self.is_support_operated = is_support_operated
        # The license metadata.
        self.license_metadata = license_metadata
        # The logging configurations.
        self.log_metadata = log_metadata
        # The operation metadata.
        self.operation_metadata = operation_metadata
        # The permissions on the service. Valid values:
        # 
        # *   Deployable: Permissions to deploy the service.
        # *   Accessible: Permissions to access the service.
        self.permission = permission
        # The policy name. The name can be up to 128 characters in length. Separate multiple names with commas (,). Only hosted O\\&M policies are supported.
        self.policy_names = policy_names
        # The time when the service was published.
        self.publish_time = publish_time
        # The request ID.
        self.request_id = request_id
        # Service document information.
        self.service_document_infos = service_document_infos
        # The service ID.
        self.service_id = service_id
        # The information about the service.
        self.service_infos = service_infos
        # The URL of the service page.
        self.service_product_url = service_product_url
        # The type of the service. Valid values:
        # 
        # - private: The service is a private service and is deployed within the account of a customer.
        # - managed: The service is a fully managed service and is deployed within the account of a service provider.
        # - operation: The service is a hosted O&M service.
        self.service_type = service_type
        # The permission type of the deployment URL. Valid values:
        # 
        # *   Public: All users can go to the URL to create a service instance or a trial service instance.
        # *   Restricted: Only users in the whitelist can go to the URL to create a service instance or a trial service instance.
        # *   OnlyFormalRestricted: Only users in the whitelist can go to the URL to create a service instance.
        # *   OnlyTrailRestricted: Only users in the whitelist can go to the URL to create a trial service instance.
        # *   Hidden: Users not in the whitelist cannot see the service details page when they go to the URL and cannot request deployment permissions.
        self.share_type = share_type
        # The deploy status of the service. Valid values:
        # - Draft
        # - Beta
        # - Submitted
        # - Approved
        # - Launching
        # - Online
        # - Offline
        # - Creating
        self.status = status
        # The description of service provider.
        self.supplier_desc = supplier_desc
        # The Logo of service provider.
        self.supplier_logo = supplier_logo
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The Alibaba Cloud account ID of the service provider.
        self.supplier_uid = supplier_uid
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # Contact information of the service provider
        self.support_contacts = support_contacts
        # The tags.
        self.tags = tags
        # The type of the tenant. Valid values:
        # 
        # *   SingleTenant
        # *   MultiTenant
        self.tenant_type = tenant_type
        # The trial duration. Unit: day. The maximum trial duration cannot exceed 30 days.
        self.trial_duration = trial_duration
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type
        # The service version.
        self.version = version
        # The version name.
        self.version_name = version_name

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.compliance_metadata:
            self.compliance_metadata.validate()
        if self.instance_role_infos:
            for k in self.instance_role_infos:
                if k:
                    k.validate()
        if self.service_document_infos:
            for k in self.service_document_infos:
                if k:
                    k.validate()
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()
        if self.support_contacts:
            for k in self.support_contacts:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_metadata is not None:
            result['AlarmMetadata'] = self.alarm_metadata
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.compliance_metadata is not None:
            result['ComplianceMetadata'] = self.compliance_metadata.to_map()
        if self.deploy_from is not None:
            result['DeployFrom'] = self.deploy_from
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.duration is not None:
            result['Duration'] = self.duration
        result['InstanceRoleInfos'] = []
        if self.instance_role_infos is not None:
            for k in self.instance_role_infos:
                result['InstanceRoleInfos'].append(k.to_map() if k else None)
        if self.is_support_operated is not None:
            result['IsSupportOperated'] = self.is_support_operated
        if self.license_metadata is not None:
            result['LicenseMetadata'] = self.license_metadata
        if self.log_metadata is not None:
            result['LogMetadata'] = self.log_metadata
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.policy_names is not None:
            result['PolicyNames'] = self.policy_names
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceDocumentInfos'] = []
        if self.service_document_infos is not None:
            for k in self.service_document_infos:
                result['ServiceDocumentInfos'].append(k.to_map() if k else None)
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_product_url is not None:
            result['ServiceProductUrl'] = self.service_product_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.share_type is not None:
            result['ShareType'] = self.share_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_desc is not None:
            result['SupplierDesc'] = self.supplier_desc
        if self.supplier_logo is not None:
            result['SupplierLogo'] = self.supplier_logo
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        result['SupportContacts'] = []
        if self.support_contacts is not None:
            for k in self.support_contacts:
                result['SupportContacts'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type
        if self.trial_duration is not None:
            result['TrialDuration'] = self.trial_duration
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmMetadata') is not None:
            self.alarm_metadata = m.get('AlarmMetadata')
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Commodity') is not None:
            temp_model = GetServiceResponseBodyCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('ComplianceMetadata') is not None:
            temp_model = GetServiceResponseBodyComplianceMetadata()
            self.compliance_metadata = temp_model.from_map(m['ComplianceMetadata'])
        if m.get('DeployFrom') is not None:
            self.deploy_from = m.get('DeployFrom')
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.instance_role_infos = []
        if m.get('InstanceRoleInfos') is not None:
            for k in m.get('InstanceRoleInfos'):
                temp_model = GetServiceResponseBodyInstanceRoleInfos()
                self.instance_role_infos.append(temp_model.from_map(k))
        if m.get('IsSupportOperated') is not None:
            self.is_support_operated = m.get('IsSupportOperated')
        if m.get('LicenseMetadata') is not None:
            self.license_metadata = m.get('LicenseMetadata')
        if m.get('LogMetadata') is not None:
            self.log_metadata = m.get('LogMetadata')
        if m.get('OperationMetadata') is not None:
            self.operation_metadata = m.get('OperationMetadata')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('PolicyNames') is not None:
            self.policy_names = m.get('PolicyNames')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_document_infos = []
        if m.get('ServiceDocumentInfos') is not None:
            for k in m.get('ServiceDocumentInfos'):
                temp_model = GetServiceResponseBodyServiceDocumentInfos()
                self.service_document_infos.append(temp_model.from_map(k))
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceResponseBodyServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ShareType') is not None:
            self.share_type = m.get('ShareType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierDesc') is not None:
            self.supplier_desc = m.get('SupplierDesc')
        if m.get('SupplierLogo') is not None:
            self.supplier_logo = m.get('SupplierLogo')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        self.support_contacts = []
        if m.get('SupportContacts') is not None:
            for k in m.get('SupportContacts'):
                temp_model = GetServiceResponseBodySupportContacts()
                self.support_contacts.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetServiceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')
        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceResponseBody = None,
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceEstimateCostRequestCommodity(TeaModel):
    def __init__(
        self,
        coupon_id: str = None,
        pay_period: int = None,
        pay_period_unit: str = None,
    ):
        # 优惠券ID
        self.coupon_id = coupon_id
        # The subscription duration.
        self.pay_period = pay_period
        # The unit of the subscription duration. Valid values:
        # 
        # *   Year
        # *   Month
        # *   Day
        self.pay_period_unit = pay_period_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.pay_period is not None:
            result['PayPeriod'] = self.pay_period
        if self.pay_period_unit is not None:
            result['PayPeriodUnit'] = self.pay_period_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('PayPeriod') is not None:
            self.pay_period = m.get('PayPeriod')
        if m.get('PayPeriodUnit') is not None:
            self.pay_period_unit = m.get('PayPeriodUnit')
        return self


class GetServiceEstimateCostRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: GetServiceEstimateCostRequestCommodity = None,
        operation_name: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the subscription duration.
        self.commodity = commodity
        # The name of the configuration change operation.
        self.operation_name = operation_name
        # The parameters that are specified to deploy the service instance.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # The name of the package specification.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        if self.commodity:
            self.commodity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            temp_model = GetServiceEstimateCostRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class GetServiceEstimateCostShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity_shrink: str = None,
        operation_name: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the subscription duration.
        self.commodity_shrink = commodity_shrink
        # The name of the configuration change operation.
        self.operation_name = operation_name
        # The parameters that are specified to deploy the service instance.
        self.parameters_shrink = parameters_shrink
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # The name of the package specification.
        self.specification_name = specification_name
        # The template name.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_shrink is not None:
            result['Commodity'] = self.commodity_shrink
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            self.commodity_shrink = m.get('Commodity')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class GetServiceEstimateCostResponseBody(TeaModel):
    def __init__(
        self,
        commodity: Dict[str, CommodityValue] = None,
        request_id: str = None,
        resources: Dict[str, Any] = None,
    ):
        # The estimated price.
        self.commodity = commodity
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resources = resources

    def validate(self):
        if self.commodity:
            for v in self.commodity.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Commodity'] = {}
        if self.commodity is not None:
            for k, v in self.commodity.items():
                result['Commodity'][k] = v.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodity = {}
        if m.get('Commodity') is not None:
            for k, v in m.get('Commodity').items():
                temp_model = CommodityValue()
                self.commodity[k] = temp_model.from_map(v)
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class GetServiceEstimateCostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceEstimateCostResponseBody = None,
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
            temp_model = GetServiceEstimateCostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        market_instance_id: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The MarketInstance ID.
        self.market_instance_id = market_instance_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service instance ID.
        # 
        # >  You must specify either `ServiceInstanceId` or `MarketInstanceId`. Otherwise, the operation fails.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs(TeaModel):
    def __init__(
        self,
        connect_bandwidth: int = None,
        domain_name: str = None,
        endpoint_ips: List[str] = None,
        ingress_endpoint_status: str = None,
        network_service_status: str = None,
        region_id: str = None,
        security_groups: List[str] = None,
        v_switches: List[str] = None,
        vpc_id: str = None,
    ):
        # The bandwidth limit for the private connection established based on the private network interconnection mode of Compute Nest.
        self.connect_bandwidth = connect_bandwidth
        # The domain name.
        self.domain_name = domain_name
        # The IP addresses of the endpoints of the private connections.
        self.endpoint_ips = endpoint_ips
        # The state of the ingress endpoint. Valid values:
        # 
        # *   Ready: The ingress endpoint is connected.
        # *   Pending: The ingress endpoint is being connected.
        # *   Failed: The ingress endpoint fails to be connected.
        # *   Deleted: The ingress endpoint is deleted.
        # *   Deleting: The ingress endpoint is being deleted.
        self.ingress_endpoint_status = ingress_endpoint_status
        # The state of the network service. Valid values:
        # 
        # *   Ready: The network service is connected.
        # *   Pending: The network service is being connected.
        # *   Failed: The network service fails to be connected.
        # *   Deleted: The network service is deleted.
        # *   Deleting: The network service is being deleted.
        self.network_service_status = network_service_status
        # The region ID of the VPC to which the endpoint of the private connection established based on the private network interconnection mode of Compute Nest belongs.
        self.region_id = region_id
        # The names of the security groups.
        self.security_groups = security_groups
        # The names of the vSwitches.
        self.v_switches = v_switches
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.endpoint_ips is not None:
            result['EndpointIps'] = self.endpoint_ips
        if self.ingress_endpoint_status is not None:
            result['IngressEndpointStatus'] = self.ingress_endpoint_status
        if self.network_service_status is not None:
            result['NetworkServiceStatus'] = self.network_service_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_groups is not None:
            result['SecurityGroups'] = self.security_groups
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EndpointIps') is not None:
            self.endpoint_ips = m.get('EndpointIps')
        if m.get('IngressEndpointStatus') is not None:
            self.ingress_endpoint_status = m.get('IngressEndpointStatus')
        if m.get('NetworkServiceStatus') is not None:
            self.network_service_status = m.get('NetworkServiceStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroups') is not None:
            self.security_groups = m.get('SecurityGroups')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections(TeaModel):
    def __init__(
        self,
        connection_configs: List[GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs] = None,
        endpoint_id: str = None,
        private_zone_id: str = None,
        private_zone_name: str = None,
        region_id: str = None,
    ):
        # The network configurations, which are mainly used for private connections.
        self.connection_configs = connection_configs
        # The endpoint ID of the private connection.
        self.endpoint_id = endpoint_id
        # The ID of the private zone of the custom private domain name.
        self.private_zone_id = private_zone_id
        # The custom domain name.
        self.private_zone_name = private_zone_name
        # The region ID of the endpoint of the PrivateLink connection.
        self.region_id = region_id

    def validate(self):
        if self.connection_configs:
            for k in self.connection_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionConfigs'] = []
        if self.connection_configs is not None:
            for k in self.connection_configs:
                result['ConnectionConfigs'].append(k.to_map() if k else None)
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.private_zone_id is not None:
            result['PrivateZoneId'] = self.private_zone_id
        if self.private_zone_name is not None:
            result['PrivateZoneName'] = self.private_zone_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_configs = []
        if m.get('ConnectionConfigs') is not None:
            for k in m.get('ConnectionConfigs'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnectionsConnectionConfigs()
                self.connection_configs.append(temp_model.from_map(k))
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('PrivateZoneId') is not None:
            self.private_zone_id = m.get('PrivateZoneId')
        if m.get('PrivateZoneName') is not None:
            self.private_zone_name = m.get('PrivateZoneName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
    ):
        # The endpoint ID of the reverse private connection.
        self.endpoint_id = endpoint_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        return self


class GetServiceInstanceResponseBodyNetworkConfig(TeaModel):
    def __init__(
        self,
        endpoint_id: str = None,
        private_vpc_connections: List[GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections] = None,
        private_zone_id: str = None,
        reverse_private_vpc_connections: List[GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections] = None,
    ):
        # The ID of the endpoint for the private connection.
        # 
        # >  This parameter is discontinued.
        self.endpoint_id = endpoint_id
        # The information about private connections.
        self.private_vpc_connections = private_vpc_connections
        # The PrivateZone ID.
        self.private_zone_id = private_zone_id
        # The information about the reverse private connection.
        self.reverse_private_vpc_connections = reverse_private_vpc_connections

    def validate(self):
        if self.private_vpc_connections:
            for k in self.private_vpc_connections:
                if k:
                    k.validate()
        if self.reverse_private_vpc_connections:
            for k in self.reverse_private_vpc_connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        result['PrivateVpcConnections'] = []
        if self.private_vpc_connections is not None:
            for k in self.private_vpc_connections:
                result['PrivateVpcConnections'].append(k.to_map() if k else None)
        if self.private_zone_id is not None:
            result['PrivateZoneId'] = self.private_zone_id
        result['ReversePrivateVpcConnections'] = []
        if self.reverse_private_vpc_connections is not None:
            for k in self.reverse_private_vpc_connections:
                result['ReversePrivateVpcConnections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        self.private_vpc_connections = []
        if m.get('PrivateVpcConnections') is not None:
            for k in m.get('PrivateVpcConnections'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigPrivateVpcConnections()
                self.private_vpc_connections.append(temp_model.from_map(k))
        if m.get('PrivateZoneId') is not None:
            self.private_zone_id = m.get('PrivateZoneId')
        self.reverse_private_vpc_connections = []
        if m.get('ReversePrivateVpcConnections') is not None:
            for k in m.get('ReversePrivateVpcConnections'):
                temp_model = GetServiceInstanceResponseBodyNetworkConfigReversePrivateVpcConnections()
                self.reverse_private_vpc_connections.append(temp_model.from_map(k))
        return self


class GetServiceInstanceResponseBodyServiceServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        # The URL of the service icon.
        self.image = image
        # The language of the service instance.
        self.locale = locale
        # The name of the service.
        self.name = name
        # The description of the service.
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class GetServiceInstanceResponseBodyServiceUpgradableServiceInfos(TeaModel):
    def __init__(
        self,
        version: str = None,
        version_name: str = None,
    ):
        # The service version.
        self.version = version
        # The version name.
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetServiceInstanceResponseBodyService(TeaModel):
    def __init__(
        self,
        deploy_metadata: str = None,
        deploy_type: str = None,
        operation_metadata: str = None,
        publish_time: str = None,
        service_doc_url: str = None,
        service_id: str = None,
        service_infos: List[GetServiceInstanceResponseBodyServiceServiceInfos] = None,
        service_product_url: str = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        upgradable_service_infos: List[GetServiceInstanceResponseBodyServiceUpgradableServiceInfos] = None,
        upgradable_service_versions: List[str] = None,
        upgrade_metadata: str = None,
        version: str = None,
        version_name: str = None,
    ):
        # The storage configurations of the service. The format in which the deployment information of a service is stored varies based on the deployment type of the service. In this case, the deployment information is stored in the JSON string format.
        self.deploy_metadata = deploy_metadata
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        # *   ack: The service is deployed by using Container Service for Kubernetes (ACK).
        # *   spi: The service is deployed by calling a service provider interface (SPI).
        # *   operation: The service is deployed by using a hosted O\\&M service.
        self.deploy_type = deploy_type
        # Operation info.
        self.operation_metadata = operation_metadata
        # The time when the service version was published.
        self.publish_time = publish_time
        # The URL of the service documentation.
        self.service_doc_url = service_doc_url
        # The service ID.
        self.service_id = service_id
        # The information about the service.
        self.service_infos = service_infos
        # The URL of the service page.
        self.service_product_url = service_product_url
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        self.service_type = service_type
        # The status of the service. Valid values:
        # 
        # *   Draft
        # *   Submited
        # *   Approved
        # *   Online
        # *   Offline
        # *   Deleted
        # *   Launching
        # *   Beta
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # The service versions that can be updated.
        self.upgradable_service_infos = upgradable_service_infos
        # The service version that can be updated.
        self.upgradable_service_versions = upgradable_service_versions
        # The metadata about the upgrade.
        self.upgrade_metadata = upgrade_metadata
        # The service version.
        self.version = version
        # The custom version name defined by the service provider.
        self.version_name = version_name

    def validate(self):
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()
        if self.upgradable_service_infos:
            for k in self.upgradable_service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deploy_metadata is not None:
            result['DeployMetadata'] = self.deploy_metadata
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.operation_metadata is not None:
            result['OperationMetadata'] = self.operation_metadata
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_doc_url is not None:
            result['ServiceDocUrl'] = self.service_doc_url
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_product_url is not None:
            result['ServiceProductUrl'] = self.service_product_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        result['UpgradableServiceInfos'] = []
        if self.upgradable_service_infos is not None:
            for k in self.upgradable_service_infos:
                result['UpgradableServiceInfos'].append(k.to_map() if k else None)
        if self.upgradable_service_versions is not None:
            result['UpgradableServiceVersions'] = self.upgradable_service_versions
        if self.upgrade_metadata is not None:
            result['UpgradeMetadata'] = self.upgrade_metadata
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeployMetadata') is not None:
            self.deploy_metadata = m.get('DeployMetadata')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('OperationMetadata') is not None:
            self.operation_metadata = m.get('OperationMetadata')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceDocUrl') is not None:
            self.service_doc_url = m.get('ServiceDocUrl')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = GetServiceInstanceResponseBodyServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        self.upgradable_service_infos = []
        if m.get('UpgradableServiceInfos') is not None:
            for k in m.get('UpgradableServiceInfos'):
                temp_model = GetServiceInstanceResponseBodyServiceUpgradableServiceInfos()
                self.upgradable_service_infos.append(temp_model.from_map(k))
        if m.get('UpgradableServiceVersions') is not None:
            self.upgradable_service_versions = m.get('UpgradableServiceVersions')
        if m.get('UpgradeMetadata') is not None:
            self.upgrade_metadata = m.get('UpgradeMetadata')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class GetServiceInstanceResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class GetServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        biz_status: str = None,
        components: str = None,
        create_time: str = None,
        enable_instance_ops: bool = None,
        enable_user_prometheus: bool = None,
        end_time: str = None,
        grafana_dash_board_url: str = None,
        is_operated: bool = None,
        license_end_time: str = None,
        market_instance_id: str = None,
        name: str = None,
        network_config: GetServiceInstanceResponseBodyNetworkConfig = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        outputs: str = None,
        parameters: str = None,
        pay_type: str = None,
        predefined_parameter_name: str = None,
        progress: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        resources: str = None,
        service: GetServiceInstanceResponseBodyService = None,
        service_instance_id: str = None,
        service_type: str = None,
        source: str = None,
        status: str = None,
        status_detail: str = None,
        supplier_uid: int = None,
        support_trial_to_private: bool = None,
        tags: List[GetServiceInstanceResponseBodyTags] = None,
        template_name: str = None,
        update_time: str = None,
        user_id: int = None,
    ):
        # The business state of the service instance. Valid values:
        # 
        # *   Normal
        # *   Renewing
        # *   RenewFailed
        # *   Expired
        self.biz_status = biz_status
        # Cloud Marketplace additional billing items.
        self.components = components
        # The time when the serviceInstance was created.
        self.create_time = create_time
        # Indicates whether the service instance supports the operation feature. Valid values:
        # 
        # *   true
        # *   false
        self.enable_instance_ops = enable_instance_ops
        # Whether to enable Prometheus monitoring.
        self.enable_user_prometheus = enable_user_prometheus
        # The expiration time of service instance.
        self.end_time = end_time
        # The URL of the Grafana dashboard.
        self.grafana_dash_board_url = grafana_dash_board_url
        # Indicates whether the hosted O\\&M feature is enabled for the service instance. Valid values:
        # 
        # *   true
        # *   false
        self.is_operated = is_operated
        # The expiration time of licence.
        self.license_end_time = license_end_time
        # The market Instance ID.
        self.market_instance_id = market_instance_id
        # The name of the service instance.
        self.name = name
        # The network configurations.
        # 
        # >  This parameter is discontinued.
        self.network_config = network_config
        # The serviceInstance  to be operated.
        self.operated_service_instance_id = operated_service_instance_id
        # The operation end time.
        self.operation_end_time = operation_end_time
        # The operation start time.
        self.operation_start_time = operation_start_time
        # The outputs returned from creating the service instance.
        # 
        # *   If the service is deployed by using a ROS template, all output fields of the template are returned.
        # *   If the service is deployed by calling an SPI operation, the output fields of the service provider and for the Compute Nest additional features are returned.
        self.outputs = outputs
        # The parameters configured for the service instance.
        self.parameters = parameters
        # The billing method of the instance for market. Valid values:
        # 
        # *   Permanent: Permanent purchase
        # *   Subscription: Subscription.
        # *   PayAsYouGo: Pay-as-you-go.
        # *   CustomFixTime: Merchant custom fixed duration.
        self.pay_type = pay_type
        # The package name.
        self.predefined_parameter_name = predefined_parameter_name
        # The deployment progress of the service instance. Unit: percentage.
        self.progress = progress
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resources.
        self.resources = resources
        # The information about the cloud service.
        self.service = service
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The type of the service. Valid values:
        # 
        # - private: The service is a private service and is deployed within the account of a customer.
        # - managed: The service is a fully managed service and is deployed within the account of a service provider.
        # - operation: The service is a hosted O&M service.
        self.service_type = service_type
        # The source of the serviceInstance. Valid values:
        # - User
        # - Market
        # - Supplier
        self.source = source
        # The deploy status of the serviceInstance. Valid values:
        # - Created
        # - Deploying
        # - DeployedFailed
        # - Deployed
        # - Upgrading
        # - Deleting
        # - Deleted
        # - DeletedFailed
        self.status = status
        # The description of the deployment state of the service instance.
        self.status_detail = status_detail
        # The Alibaba Cloud account ID of the service provider.
        self.supplier_uid = supplier_uid
        self.support_trial_to_private = support_trial_to_private
        # The tags.
        self.tags = tags
        # The template name.
        self.template_name = template_name
        # The time when the serviceInstance  was last updated.
        self.update_time = update_time
        # The AliUid of the user.
        self.user_id = user_id

    def validate(self):
        if self.network_config:
            self.network_config.validate()
        if self.service:
            self.service.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.components is not None:
            result['Components'] = self.components
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.grafana_dash_board_url is not None:
            result['GrafanaDashBoardUrl'] = self.grafana_dash_board_url
        if self.is_operated is not None:
            result['IsOperated'] = self.is_operated
        if self.license_end_time is not None:
            result['LicenseEndTime'] = self.license_end_time
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.network_config is not None:
            result['NetworkConfig'] = self.network_config.to_map()
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.predefined_parameter_name is not None:
            result['PredefinedParameterName'] = self.predefined_parameter_name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid
        if self.support_trial_to_private is not None:
            result['SupportTrialToPrivate'] = self.support_trial_to_private
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GrafanaDashBoardUrl') is not None:
            self.grafana_dash_board_url = m.get('GrafanaDashBoardUrl')
        if m.get('IsOperated') is not None:
            self.is_operated = m.get('IsOperated')
        if m.get('LicenseEndTime') is not None:
            self.license_end_time = m.get('LicenseEndTime')
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkConfig') is not None:
            temp_model = GetServiceInstanceResponseBodyNetworkConfig()
            self.network_config = temp_model.from_map(m['NetworkConfig'])
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PredefinedParameterName') is not None:
            self.predefined_parameter_name = m.get('PredefinedParameterName')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Service') is not None:
            temp_model = GetServiceInstanceResponseBodyService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')
        if m.get('SupportTrialToPrivate') is not None:
            self.support_trial_to_private = m.get('SupportTrialToPrivate')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetServiceInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceInstanceResponseBody = None,
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
            temp_model = GetServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceInstanceSubscriptionEstimateCostRequestResourcePeriod(TeaModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        resource_arn: str = None,
    ):
        # Renewal duration. The unit is specified by PeriodUnit.
        self.period = period
        # The time unit for the resource renewal duration, which is the unit of the Period parameter. Valid values: Month, Year. Default value: Month.
        self.period_unit = period_unit
        # Resource ARN (Aliyun Resource Name).
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        return self


class GetServiceInstanceSubscriptionEstimateCostRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        order_type: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_period: List[GetServiceInstanceSubscriptionEstimateCostRequestResourcePeriod] = None,
        service_instance_id: str = None,
    ):
        # Ensures idempotence of the request. Generate a parameter value from your client to ensure its uniqueness across different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters.
        self.client_token = client_token
        # Order type. Possible value: Renewal.
        # 
        # This parameter is required.
        self.order_type = order_type
        # The renewal duration for all prepaid resources of the service instance. The unit is specified by PeriodUnit.
        self.period = period
        # The time unit for the renewal duration of all prepaid resources of the service instance, which is the unit of the Period parameter. Valid values: Month, Year. Default value: Month.
        self.period_unit = period_unit
        # Region ID.
        self.region_id = region_id
        # Resource renewal configuration.
        self.resource_period = resource_period
        # Service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.resource_period:
            for k in self.resource_period:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ResourcePeriod'] = []
        if self.resource_period is not None:
            for k in self.resource_period:
                result['ResourcePeriod'].append(k.to_map() if k else None)
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource_period = []
        if m.get('ResourcePeriod') is not None:
            for k in m.get('ResourcePeriod'):
                temp_model = GetServiceInstanceSubscriptionEstimateCostRequestResourcePeriod()
                self.resource_period.append(temp_model.from_map(k))
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesDetailInfos(TeaModel):
    def __init__(
        self,
        discount_amount: float = None,
        original_amount: float = None,
        resource: str = None,
        trade_amount: float = None,
    ):
        # Discount amount.
        self.discount_amount = discount_amount
        # Original price.
        self.original_amount = original_amount
        # Pricing module identifier.
        self.resource = resource
        # Discounted price.
        self.trade_amount = trade_amount

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesRules(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        rule_desc_id: int = None,
    ):
        # Promotion description.
        self.description = description
        # Promotion name.
        self.name = name
        # Promotion ID.
        self.rule_desc_id = rule_desc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')
        return self


class GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePrices(TeaModel):
    def __init__(
        self,
        currency: str = None,
        detail_infos: List[GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesDetailInfos] = None,
        discount_amount: float = None,
        original_amount: float = None,
        period: int = None,
        period_unit: str = None,
        resource_arn: str = None,
        rules: List[GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesRules] = None,
        trade_amount: float = None,
    ):
        # Currency. Valid values:
        # - CNY: Chinese Yuan.
        # - USD: US Dollar.
        # - JPY: Japanese Yen.
        self.currency = currency
        # The price details of the pricing module.
        self.detail_infos = detail_infos
        # Discount.
        self.discount_amount = discount_amount
        # Original price.
        self.original_amount = original_amount
        # Renewal duration. The unit is specified by PeriodUnit.
        self.period = period
        # The time unit for the renewal duration, which is the unit of the Period parameter. Valid values: Month, Year. Default value: Month.
        self.period_unit = period_unit
        # Resource ARN (Aliyun Resource Name).
        self.resource_arn = resource_arn
        # Promotion details.
        self.rules = rules
        # Discounted price.
        self.trade_amount = trade_amount

    def validate(self):
        if self.detail_infos:
            for k in self.detail_infos:
                if k:
                    k.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        result['DetailInfos'] = []
        if self.detail_infos is not None:
            for k in self.detail_infos:
                result['DetailInfos'].append(k.to_map() if k else None)
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        self.detail_infos = []
        if m.get('DetailInfos') is not None:
            for k in m.get('DetailInfos'):
                temp_model = GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesDetailInfos()
                self.detail_infos.append(temp_model.from_map(k))
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePricesRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class GetServiceInstanceSubscriptionEstimateCostResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_prices: List[GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePrices] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # List of resource price information.
        self.resource_prices = resource_prices

    def validate(self):
        if self.resource_prices:
            for k in self.resource_prices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourcePrices'] = []
        if self.resource_prices is not None:
            for k in self.resource_prices:
                result['ResourcePrices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_prices = []
        if m.get('ResourcePrices') is not None:
            for k in m.get('ResourcePrices'):
                temp_model = GetServiceInstanceSubscriptionEstimateCostResponseBodyResourcePrices()
                self.resource_prices.append(temp_model.from_map(k))
        return self


class GetServiceInstanceSubscriptionEstimateCostResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceInstanceSubscriptionEstimateCostResponseBody = None,
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
            temp_model = GetServiceInstanceSubscriptionEstimateCostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceProvisionsRequest(TeaModel):
    def __init__(
        self,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The parameters configured for the service instance.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The version of the service.
        self.service_version = service_version
        # The template name.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class GetServiceProvisionsShrinkRequest(TeaModel):
    def __init__(
        self,
        parameters_shrink: str = None,
        region_id: str = None,
        service_id: str = None,
        service_version: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The parameters configured for the service instance.
        self.parameters_shrink = parameters_shrink
        # The region ID.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The version of the service.
        self.service_version = service_version
        # The template name.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class GetServiceProvisionsResponseBodyServiceProvisionsCommodityProvisions(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        enable_url: str = None,
        status: str = None,
    ):
        self.commodity_code = commodity_code
        self.enable_url = enable_url
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.enable_url is not None:
            result['EnableURL'] = self.enable_url
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('EnableURL') is not None:
            self.enable_url = m.get('EnableURL')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_product_id: str = None,
        api_type: str = None,
        parameters: Dict[str, Any] = None,
    ):
        # The name of the API operation.
        self.api_name = api_name
        # The ID of the Alibaba Cloud service to which the API operation belongs.
        self.api_product_id = api_product_id
        # The type of the API operation. Valid values:
        # 
        # *   Open: public
        # *   Inner: private
        self.api_type = api_type
        # The ROS parameters of the cluster.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['ApiName'] = self.api_name
        if self.api_product_id is not None:
            result['ApiProductId'] = self.api_product_id
        if self.api_type is not None:
            result['ApiType'] = self.api_type
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')
        if m.get('ApiProductId') is not None:
            self.api_product_id = m.get('ApiProductId')
        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles(TeaModel):
    def __init__(
        self,
        api_for_creation: GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation = None,
        created: bool = None,
        function: str = None,
        role_name: str = None,
    ):
        # The information about the API operation that is used to create the RAM role.
        self.api_for_creation = api_for_creation
        # Indicates whether the RAM role is created. Valid values:
        # 
        # *   true
        # *   false
        self.created = created
        # The purpose for which the RAM role is used. Default value: Default. A value of Default indicates that the RAM role is the default role of the service.
        self.function = function
        # The name of the role.
        self.role_name = role_name

    def validate(self):
        if self.api_for_creation:
            self.api_for_creation.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_for_creation is not None:
            result['ApiForCreation'] = self.api_for_creation.to_map()
        if self.created is not None:
            result['Created'] = self.created
        if self.function is not None:
            result['Function'] = self.function
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiForCreation') is not None:
            temp_model = GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRolesApiForCreation()
            self.api_for_creation = temp_model.from_map(m['ApiForCreation'])
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('Function') is not None:
            self.function = m.get('Function')
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision(TeaModel):
    def __init__(
        self,
        authorization_url: str = None,
        roles: List[GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles] = None,
    ):
        # The authorization URL of the RAM role.
        # 
        # > This parameter is returned if Created is set to false.
        self.authorization_url = authorization_url
        # The RAM roles of the service.
        self.roles = roles

    def validate(self):
        if self.roles:
            for k in self.roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_url is not None:
            result['AuthorizationURL'] = self.authorization_url
        result['Roles'] = []
        if self.roles is not None:
            for k in self.roles:
                result['Roles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationURL') is not None:
            self.authorization_url = m.get('AuthorizationURL')
        self.roles = []
        if m.get('Roles') is not None:
            for k in m.get('Roles'):
                temp_model = GetServiceProvisionsResponseBodyServiceProvisionsRoleProvisionRoles()
                self.roles.append(temp_model.from_map(k))
        return self


class GetServiceProvisionsResponseBodyServiceProvisions(TeaModel):
    def __init__(
        self,
        auto_enable_service: bool = None,
        commodity_provisions: List[GetServiceProvisionsResponseBodyServiceProvisionsCommodityProvisions] = None,
        enable_url: str = None,
        role_provision: GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision = None,
        service_name: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        # Indicates whether automatic activation for the service is defined in the template. Valid values:
        # 
        # *   true: Automatic activation for the service is defined in the template.
        # *   false: Manual activation for the service is defined in the template.
        self.auto_enable_service = auto_enable_service
        self.commodity_provisions = commodity_provisions
        # The URL that points to the activation page of the service.
        # 
        # > This parameter is returned if Status is set to Disabled.
        self.enable_url = enable_url
        # The information about the RAM roles of the service. If this parameter is empty, no RAM role is associated with the service.
        self.role_provision = role_provision
        # The service name.
        self.service_name = service_name
        # The activation status of the service. Valid values:
        # 
        # *   Enabled: The service is activated.
        # *   Disabled: The service is not activated.
        # *   Unknown: The activation status of the service is unknown.
        self.status = status
        # The reason why the service is in the Disabled or Unknown state.
        # 
        # > This parameter is returned if Status is set to Disabled or Unknown.
        self.status_reason = status_reason

    def validate(self):
        if self.commodity_provisions:
            for k in self.commodity_provisions:
                if k:
                    k.validate()
        if self.role_provision:
            self.role_provision.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_enable_service is not None:
            result['AutoEnableService'] = self.auto_enable_service
        result['CommodityProvisions'] = []
        if self.commodity_provisions is not None:
            for k in self.commodity_provisions:
                result['CommodityProvisions'].append(k.to_map() if k else None)
        if self.enable_url is not None:
            result['EnableURL'] = self.enable_url
        if self.role_provision is not None:
            result['RoleProvision'] = self.role_provision.to_map()
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoEnableService') is not None:
            self.auto_enable_service = m.get('AutoEnableService')
        self.commodity_provisions = []
        if m.get('CommodityProvisions') is not None:
            for k in m.get('CommodityProvisions'):
                temp_model = GetServiceProvisionsResponseBodyServiceProvisionsCommodityProvisions()
                self.commodity_provisions.append(temp_model.from_map(k))
        if m.get('EnableURL') is not None:
            self.enable_url = m.get('EnableURL')
        if m.get('RoleProvision') is not None:
            temp_model = GetServiceProvisionsResponseBodyServiceProvisionsRoleProvision()
            self.role_provision = temp_model.from_map(m['RoleProvision'])
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')
        return self


class GetServiceProvisionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_provisions: List[GetServiceProvisionsResponseBodyServiceProvisions] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the services.
        self.service_provisions = service_provisions

    def validate(self):
        if self.service_provisions:
            for k in self.service_provisions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceProvisions'] = []
        if self.service_provisions is not None:
            for k in self.service_provisions:
                result['ServiceProvisions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_provisions = []
        if m.get('ServiceProvisions') is not None:
            for k in m.get('ServiceProvisions'):
                temp_model = GetServiceProvisionsResponseBodyServiceProvisions()
                self.service_provisions.append(temp_model.from_map(k))
        return self


class GetServiceProvisionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceProvisionsResponseBody = None,
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
            temp_model = GetServiceProvisionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceTemplateParameterConstraintsRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        # The name of the parameter. If you do not specify Parameters, the parameters and values in the template are used.
        # 
        # >  Parameters is an optional parameter. ParameterKey is required if you specify Parameters.
        self.parameter_key = parameter_key
        # The parameter value that is defined in the template.
        # 
        # >  Parameters is an optional parameter. ParameterValue is required if you specify Parameters.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetServiceTemplateParameterConstraintsRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        deploy_region_id: str = None,
        enable_private_vpc_connection: bool = None,
        parameters: List[GetServiceTemplateParameterConstraintsRequestParameters] = None,
        region_id: str = None,
        service_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
        specification_name: str = None,
        template_name: str = None,
        trial_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID of the service instance.
        # 
        # This parameter is required.
        self.deploy_region_id = deploy_region_id
        # Specifies whether to enable the private connection. Valid values:
        # 
        # *   true
        # *   false
        self.enable_private_vpc_connection = enable_private_vpc_connection
        # The configuration parameters of the service instance.
        self.parameters = parameters
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The service version.
        self.service_version = service_version
        # The name of the specification package.
        self.specification_name = specification_name
        # The template name.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deploy_region_id is not None:
            result['DeployRegionId'] = self.deploy_region_id
        if self.enable_private_vpc_connection is not None:
            result['EnablePrivateVpcConnection'] = self.enable_private_vpc_connection
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.specification_name is not None:
            result['SpecificationName'] = self.specification_name
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeployRegionId') is not None:
            self.deploy_region_id = m.get('DeployRegionId')
        if m.get('EnablePrivateVpcConnection') is not None:
            self.enable_private_vpc_connection = m.get('EnablePrivateVpcConnection')
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetServiceTemplateParameterConstraintsRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('SpecificationName') is not None:
            self.specification_name = m.get('SpecificationName')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        return self


class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints(TeaModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        property_name: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The valid values of the parameter.
        self.allowed_values = allowed_values
        # The property name.
        self.property_name = property_name
        # The name of the resource that is defined in the template.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.property_name is not None:
            result['PropertyName'] = self.property_name
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('PropertyName') is not None:
            self.property_name = m.get('PropertyName')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        # The error message.
        self.error_message = error_message
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints(TeaModel):
    def __init__(
        self,
        allowed_values: List[str] = None,
        association_parameter_names: List[str] = None,
        behavior: str = None,
        behavior_reason: str = None,
        original_constraints: List[GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints] = None,
        parameter_key: str = None,
        query_errors: List[GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors] = None,
        type: str = None,
    ):
        # The valid values of the parameter.
        self.allowed_values = allowed_values
        # The names of the associated parameters.
        self.association_parameter_names = association_parameter_names
        # The behavior of the parameter. Valid values:
        # 
        # *   NoLimit: No limit is imposed on the value of this parameter.
        # *   NotSupport: The value of this parameter cannot be queried.
        # *   QueryError: This parameter failed to be queried.
        # 
        # >  If AllowedValues is not returned, Behavior and BehaviorReason are returned, which indicate the behavior of the parameter and the reason for the behavior.
        self.behavior = behavior
        # The reason why the behavior of the parameter is returned.
        self.behavior_reason = behavior_reason
        # The original constraint information.
        self.original_constraints = original_constraints
        # The name of the parameter.
        self.parameter_key = parameter_key
        # The error details that are returned if the request fails.
        self.query_errors = query_errors
        # The data type of the parameter.
        self.type = type

    def validate(self):
        if self.original_constraints:
            for k in self.original_constraints:
                if k:
                    k.validate()
        if self.query_errors:
            for k in self.query_errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        if self.association_parameter_names is not None:
            result['AssociationParameterNames'] = self.association_parameter_names
        if self.behavior is not None:
            result['Behavior'] = self.behavior
        if self.behavior_reason is not None:
            result['BehaviorReason'] = self.behavior_reason
        result['OriginalConstraints'] = []
        if self.original_constraints is not None:
            for k in self.original_constraints:
                result['OriginalConstraints'].append(k.to_map() if k else None)
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        result['QueryErrors'] = []
        if self.query_errors is not None:
            for k in self.query_errors:
                result['QueryErrors'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        if m.get('AssociationParameterNames') is not None:
            self.association_parameter_names = m.get('AssociationParameterNames')
        if m.get('Behavior') is not None:
            self.behavior = m.get('Behavior')
        if m.get('BehaviorReason') is not None:
            self.behavior_reason = m.get('BehaviorReason')
        self.original_constraints = []
        if m.get('OriginalConstraints') is not None:
            for k in m.get('OriginalConstraints'):
                temp_model = GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsOriginalConstraints()
                self.original_constraints.append(temp_model.from_map(k))
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        self.query_errors = []
        if m.get('QueryErrors') is not None:
            for k in m.get('QueryErrors'):
                temp_model = GetServiceTemplateParameterConstraintsResponseBodyParameterConstraintsQueryErrors()
                self.query_errors.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetServiceTemplateParameterConstraintsResponseBody(TeaModel):
    def __init__(
        self,
        family_constraints: List[str] = None,
        parameter_constraints: List[GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints] = None,
        request_id: str = None,
    ):
        # The package family constraints.
        self.family_constraints = family_constraints
        # The constraints on the parameters.
        self.parameter_constraints = parameter_constraints
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameter_constraints:
            for k in self.parameter_constraints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.family_constraints is not None:
            result['FamilyConstraints'] = self.family_constraints
        result['ParameterConstraints'] = []
        if self.parameter_constraints is not None:
            for k in self.parameter_constraints:
                result['ParameterConstraints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FamilyConstraints') is not None:
            self.family_constraints = m.get('FamilyConstraints')
        self.parameter_constraints = []
        if m.get('ParameterConstraints') is not None:
            for k in m.get('ParameterConstraints'):
                temp_model = GetServiceTemplateParameterConstraintsResponseBodyParameterConstraints()
                self.parameter_constraints.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetServiceTemplateParameterConstraintsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceTemplateParameterConstraintsResponseBody = None,
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
            temp_model = GetServiceTemplateParameterConstraintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserInformationRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetUserInformationResponseBodyDeliverySettings(TeaModel):
    def __init__(
        self,
        actiontrail_delivery_to_oss_enabled: bool = None,
        oss_bucket_name: str = None,
        oss_enabled: bool = None,
        oss_expiration_days: int = None,
        oss_path: str = None,
    ):
        # Indicates whether screencast delivery to OSS is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.actiontrail_delivery_to_oss_enabled = actiontrail_delivery_to_oss_enabled
        # The name of the OSS bucket.
        self.oss_bucket_name = oss_bucket_name
        # Indicates whether screencast delivery to Object Storage Service (OSS) is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.oss_enabled = oss_enabled
        # The number of days for which the screencasts are saved.
        self.oss_expiration_days = oss_expiration_days
        # The OSS path.
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actiontrail_delivery_to_oss_enabled is not None:
            result['ActiontrailDeliveryToOssEnabled'] = self.actiontrail_delivery_to_oss_enabled
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_enabled is not None:
            result['OssEnabled'] = self.oss_enabled
        if self.oss_expiration_days is not None:
            result['OssExpirationDays'] = self.oss_expiration_days
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiontrailDeliveryToOssEnabled') is not None:
            self.actiontrail_delivery_to_oss_enabled = m.get('ActiontrailDeliveryToOssEnabled')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssEnabled') is not None:
            self.oss_enabled = m.get('OssEnabled')
        if m.get('OssExpirationDays') is not None:
            self.oss_expiration_days = m.get('OssExpirationDays')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class GetUserInformationResponseBody(TeaModel):
    def __init__(
        self,
        delivery_settings: GetUserInformationResponseBodyDeliverySettings = None,
        request_id: str = None,
    ):
        # The delivery settings.
        self.delivery_settings = delivery_settings
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.delivery_settings:
            self.delivery_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_settings is not None:
            result['DeliverySettings'] = self.delivery_settings.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverySettings') is not None:
            temp_model = GetUserInformationResponseBodyDeliverySettings()
            self.delivery_settings = temp_model.from_map(m['DeliverySettings'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserInformationResponseBody = None,
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
            temp_model = GetUserInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPoliciesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # Page size.
        self.max_results = max_results
        # Token for the next query, an empty nextToken indicates there is no next page.
        self.next_token = next_token
        # Region ID.
        self.region_id = region_id

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListPoliciesResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # Permission policy description.
        self.description = description
        # Policy content.
        self.policy_document = policy_document
        # Permission policy name.
        self.policy_name = policy_name
        # Permission policy type.
        # 
        # - Custom: Custom policy.
        # - System: System policy.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')
        return self


class ListPoliciesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policies: List[ListPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
    ):
        # 分页大小。
        self.max_results = max_results
        # Next Token
        self.next_token = next_token
        # Permission policy list
        self.policies = policies
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.policies:
            for k in self.policies:
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
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPoliciesResponseBody = None,
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
            temp_model = ListPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceCategoriesResponseBody(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
        request_id: str = None,
    ):
        # The category list of the service.
        self.categories = categories
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListServiceCategoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceCategoriesResponseBody = None,
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
            temp_model = ListServiceCategoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstanceBillRequest(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        billing_date: str = None,
        granularity: str = None,
        max_results: int = None,
        next_token: str = None,
        service_instance_id: str = None,
    ):
        # The billing cycle. Format: YYYY-MM.
        # 
        # This parameter is required.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only if the **Granularity** parameter is set to DAILY. Format: YYYY-MM-DD.
        self.billing_date = billing_date
        # The granularity at which bills are queried. Valid values:
        # 
        # *   MONTHLY: queries bills by month. The data queried is consistent with the data that is displayed for the specified billing cycle on the Billing Details tab of the Bill Details page in User Center.
        # *   DAILY: queries bills by day. The data queried is consistent with the data that is displayed for the specified day on the Billing Details tab of the Bill Details page in User Center.
        # 
        # You must set the **BillingDate** parameter before you can set the Granularity parameter to DAILY.
        self.granularity = granularity
        # The number of entries page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The service instance ID.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ListServiceInstanceBillResponseBodyItem(TeaModel):
    def __init__(
        self,
        billing_cycle: str = None,
        billing_date: str = None,
        billing_item: str = None,
        billing_item_code: str = None,
        currency: str = None,
        deducted_by_resource_package: str = None,
        instance_id: str = None,
        invoice_discount: str = None,
        list_price: str = None,
        list_price_unit: str = None,
        pretax_amount: str = None,
        pretax_gross_amount: str = None,
        product_code: str = None,
        product_detail: str = None,
        product_name: str = None,
        split_billing_cycle: str = None,
        subscription_type: str = None,
        usage: str = None,
        usage_unit: str = None,
    ):
        # The billing cycle. Format: YYYY-MM.
        self.billing_cycle = billing_cycle
        # The billing date. This parameter is required only if the **Granularity** parameter is set to DAILY. Format: YYYY-MM-DD.
        self.billing_date = billing_date
        # The billable item.
        self.billing_item = billing_item
        # The code of the billable item.
        self.billing_item_code = billing_item_code
        # The currency unit.
        # 
        # *   China site: **CNY**.
        # *   International site: **USD**.
        self.currency = currency
        # The amount deducted with resource plans.
        self.deducted_by_resource_package = deducted_by_resource_package
        # The ID of the instance.
        self.instance_id = instance_id
        # The discount amount.
        self.invoice_discount = invoice_discount
        # The unit price.
        self.list_price = list_price
        # The unit of the unit price.
        self.list_price_unit = list_price_unit
        # The pretax amount.
        self.pretax_amount = pretax_amount
        # The pretax gross amount.
        self.pretax_gross_amount = pretax_gross_amount
        # The code of the service.
        self.product_code = product_code
        # The specific service resource.
        self.product_detail = product_detail
        # The name of the cloud service or the name of the service-linked role with which the cloud service is associated.
        self.product_name = product_name
        # The billing cycle in which the bill is split.
        self.split_billing_cycle = split_billing_cycle
        # The billing method. Valid values:
        # 
        # *   Subscription: the subscription billing method.
        # *   PayAsYouGo: the pay-as-you-go billing method.
        self.subscription_type = subscription_type
        # The amount of resource usage.
        self.usage = usage
        # The unit of usage.
        self.usage_unit = usage_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item
        if self.billing_item_code is not None:
            result['BillingItemCode'] = self.billing_item_code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.list_price is not None:
            result['ListPrice'] = self.list_price
        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.split_billing_cycle is not None:
            result['SplitBillingCycle'] = self.split_billing_cycle
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')
        if m.get('BillingItemCode') is not None:
            self.billing_item_code = m.get('BillingItemCode')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')
        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('SplitBillingCycle') is not None:
            self.split_billing_cycle = m.get('SplitBillingCycle')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        return self


class ListServiceInstanceBillResponseBody(TeaModel):
    def __init__(
        self,
        item: List[ListServiceInstanceBillResponseBodyItem] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The billing information of the backup schedule.
        self.item = item
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = ListServiceInstanceBillResponseBodyItem()
                self.item.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceInstanceBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceInstanceBillResponseBody = None,
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
            temp_model = ListServiceInstanceBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstanceLogsRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter. You can specify one or more filters. Valid values:
        # 
        # *   StartTime: the start time of the log event.
        # *   EndTime: the end time of the ActionTrail event.
        # *   EventName: the name of the ActionTrail event.
        # *   ResourceName: the name of the ActionTrail resource.
        # *   ApplicationGroupName: the name of the application group.
        self.name = name
        # The parameter value N of the filter. Valid values of N: 1 to 10.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceInstanceLogsRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListServiceInstanceLogsRequestFilter] = None,
        log_source: str = None,
        logstore: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
        sort_order: str = None,
    ):
        # The filters.
        self.filter = filter
        # The log source. When this field is empty, query logs with the source set to computeNest and ros. Valid values:
        # 
        # computeNest : logs of the deployment and upgrade of the service instance.
        # application: logs generated by the application.
        # actionTrail: logs generated by ActionTrail.
        # compliancePack: Logs originating from the compliance package.
        # ros: Logs originating from ROS.
        # meteringData：Logs originating from the pay-as-you-go model.
        self.log_source = log_source
        # The Logstore. You must specify this parameter if you set LogSource to application.
        self.logstore = logstore
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The region ID. Valid values:
        # 
        # *   cn-hangzhou: China (Hangzhou).
        # *   ap-southeast-1: Singapore.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id
        # The order in which you want to sort the results. Valid values:
        # 
        # *   Ascending
        # *   (Default) Descending
        self.sort_order = sort_order

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.log_source is not None:
            result['LogSource'] = self.log_source
        if self.logstore is not None:
            result['Logstore'] = self.logstore
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceInstanceLogsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListServiceInstanceLogsResponseBodyServiceInstancesLogs(TeaModel):
    def __init__(
        self,
        compliance_pack_type: str = None,
        compliance_rule_name: str = None,
        content: str = None,
        log_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
        source: str = None,
        status: str = None,
        timestamp: str = None,
    ):
        # Compliance package risk types. For example, data security checks within a VPC, such as VpcDataRisk
        self.compliance_pack_type = compliance_pack_type
        # Specific risk rule names for the compliance package. For example, ECS instance migration out of VPC - ecs-move-out-vpc.
        self.compliance_rule_name = compliance_rule_name
        # The log content.
        self.content = content
        # The log type. Valid values:
        # 
        # *   serviceInstance: log generated by the service instance.
        # *   resource: log generated by ROS resources.
        self.log_type = log_type
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The log source. Valid values:
        # 
        # computeNest : logs of the deployment and upgrade of the service instance.
        # application: logs generated by the application.
        # actionTrail: logs generated by ActionTrail.
        # compliancePack: Logs originating from the compliance package.
        # ros: Logs originating from ROS.
        # meteringData：Logs originating from the pay-as-you-go model.
        self.source = source
        # The state of the service instance. Valid values:
        # 
        # *   Creating: The service instance is being created.
        # *   Created: The service instance is created.
        # *   Deploying: The service instance is being deployed.
        # *   Deployed: The service instance is deployed.
        # *   DeployedFailed: The service instance failed to be deployed.
        # *   Expired: The service instance expired.
        # *   ExtendSuccess: The service instance is renewed.
        # *   Upgrading: The service instance is being updated.
        # *   UpgradeSuccess: The service instance is updated.
        self.status = status
        # The timestamp of the service instance log.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compliance_pack_type is not None:
            result['CompliancePackType'] = self.compliance_pack_type
        if self.compliance_rule_name is not None:
            result['ComplianceRuleName'] = self.compliance_rule_name
        if self.content is not None:
            result['Content'] = self.content
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackType') is not None:
            self.compliance_pack_type = m.get('CompliancePackType')
        if m.get('ComplianceRuleName') is not None:
            self.compliance_rule_name = m.get('ComplianceRuleName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class ListServiceInstanceLogsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_instances_logs: List[ListServiceInstanceLogsResponseBodyServiceInstancesLogs] = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The logs of the service instance.
        self.service_instances_logs = service_instances_logs

    def validate(self):
        if self.service_instances_logs:
            for k in self.service_instances_logs:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceInstancesLogs'] = []
        if self.service_instances_logs is not None:
            for k in self.service_instances_logs:
                result['ServiceInstancesLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_instances_logs = []
        if m.get('ServiceInstancesLogs') is not None:
            for k in m.get('ServiceInstancesLogs'):
                temp_model = ListServiceInstanceLogsResponseBodyServiceInstancesLogs()
                self.service_instances_logs.append(temp_model.from_map(k))
        return self


class ListServiceInstanceLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceInstanceLogsResponseBody = None,
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
            temp_model = ListServiceInstanceLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstanceResourcesRequestFilters(TeaModel):
    def __init__(
        self,
        name: str = None,
        values: List[str] = None,
    ):
        # Vaild values:
        # - ExpireTimeStart
        # - ExpireTimeEnd
        # - PayType
        # - ResourceARN
        self.name = name
        # The value of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListServiceInstanceResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class ListServiceInstanceResourcesRequest(TeaModel):
    def __init__(
        self,
        filters: List[ListServiceInstanceResourcesRequestFilters] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
        service_instance_resource_type: str = None,
        tag: List[ListServiceInstanceResourcesRequestTag] = None,
    ):
        # The filter conditions. Vaild values:
        # 
        # - ExpireTimeStart：
        # Query start time for Subscription resource expiration.
        # <notice>Notice Note: Only supports querying service instances on private deployments.>Notice: 
        # 
        # - ExpireTimeEnd：Query end time for Subscription resource expiration.
        # <notice>Notice Note: Only supports querying service instances on private deployments.>Notice: 
        # 
        # - PayType：The billing method of the read-only instance. 
        # <notice>Notice Note: Only supports querying service instances on private deployments.<notice> 
        # 
        #    Valid values:
        # 
        #    - PayAsYouGo
        # 
        #    - Subscription
        # 
        # - ResourceARN：The Alibaba Cloud Resource Name (ARN) of a resource.
        self.filters = filters
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If **NextToken** is not returned, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The region ID. Valid values:
        # 
        # *   cn-hangzhou: China (Hangzhou).
        # *   ap-southeast-1: Singapore.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id
        # Service Instance resource type，include AliyunResource and ContainerResource.
        self.service_instance_resource_type = service_instance_resource_type
        # The tag key and value.
        self.tag = tag

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_instance_resource_type is not None:
            result['ServiceInstanceResourceType'] = self.service_instance_resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListServiceInstanceResourcesRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceInstanceResourceType') is not None:
            self.service_instance_resource_type = m.get('ServiceInstanceResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServiceInstanceResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServiceInstanceResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expire_time: str = None,
        pay_type: str = None,
        product_code: str = None,
        product_type: str = None,
        renew_status: str = None,
        renewal_period: int = None,
        renewal_period_unit: str = None,
        resource_arn: str = None,
        status: str = None,
    ):
        # The time when the resource was created.
        self.create_time = create_time
        # The time when the resource expires.
        self.expire_time = expire_time
        # The billing method. Valid values:
        # 
        # *   Subscription
        # *   PayAsYouGo
        self.pay_type = pay_type
        # The code of the cloud service.
        self.product_code = product_code
        # The type of the cloud service.
        self.product_type = product_type
        # The renewal state. Valid values:
        # 
        # *   AutoRenewal
        # *   ManualRenewal
        # *   NotRenewal
        self.renew_status = renew_status
        # The renewal period.
        self.renewal_period = renewal_period
        # The unit of the renewal period. Valid values:
        # 
        # *   Month
        # *   Year
        self.renewal_period_unit = renewal_period_unit
        # The ARN of the resource.
        self.resource_arn = resource_arn
        # The state of the resource. Valid values:
        # 
        # *   running
        # *   waiting
        # *   terminated
        # 
        # >  This parameter is returned only for containers.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        if self.renewal_period is not None:
            result['RenewalPeriod'] = self.renewal_period
        if self.renewal_period_unit is not None:
            result['RenewalPeriodUnit'] = self.renewal_period_unit
        if self.resource_arn is not None:
            result['ResourceARN'] = self.resource_arn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        if m.get('RenewalPeriod') is not None:
            self.renewal_period = m.get('RenewalPeriod')
        if m.get('RenewalPeriodUnit') is not None:
            self.renewal_period_unit = m.get('RenewalPeriodUnit')
        if m.get('ResourceARN') is not None:
            self.resource_arn = m.get('ResourceARN')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListServiceInstanceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[ListServiceInstanceResourcesResponseBodyResources] = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for k in self.resources:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListServiceInstanceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListServiceInstanceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceInstanceResourcesResponseBody = None,
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
            temp_model = ListServiceInstanceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstanceUpgradeHistoryRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class ListServiceInstanceUpgradeHistoryResponseBodyUpgradeHistory(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        from_version: str = None,
        results: str = None,
        start_time: str = None,
        status: str = None,
        to_version: str = None,
        type: str = None,
        upgrade_history_id: str = None,
    ):
        # The time when the update ended.
        self.end_time = end_time
        # The version before the upgrade.
        self.from_version = from_version
        # The upgrade result.
        self.results = results
        # The time when the update started.
        self.start_time = start_time
        # The state of the update. Valid values:
        # 
        # *   upgrading: The service instance is being upgraded.
        # *   UpgradeSuccessful: The service instance is upgraded.
        # *   UpgradeFailed: The service instance failed to be upgraded.
        self.status = status
        # The version after the upgrade.
        self.to_version = to_version
        # The update type.
        self.type = type
        # The ID of the upgrade record.
        self.upgrade_history_id = upgrade_history_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.from_version is not None:
            result['FromVersion'] = self.from_version
        if self.results is not None:
            result['Results'] = self.results
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.to_version is not None:
            result['ToVersion'] = self.to_version
        if self.type is not None:
            result['Type'] = self.type
        if self.upgrade_history_id is not None:
            result['UpgradeHistoryId'] = self.upgrade_history_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FromVersion') is not None:
            self.from_version = m.get('FromVersion')
        if m.get('Results') is not None:
            self.results = m.get('Results')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ToVersion') is not None:
            self.to_version = m.get('ToVersion')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpgradeHistoryId') is not None:
            self.upgrade_history_id = m.get('UpgradeHistoryId')
        return self


class ListServiceInstanceUpgradeHistoryResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        upgrade_history: List[ListServiceInstanceUpgradeHistoryResponseBodyUpgradeHistory] = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The upgrade history.
        self.upgrade_history = upgrade_history

    def validate(self):
        if self.upgrade_history:
            for k in self.upgrade_history:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UpgradeHistory'] = []
        if self.upgrade_history is not None:
            for k in self.upgrade_history:
                result['UpgradeHistory'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.upgrade_history = []
        if m.get('UpgradeHistory') is not None:
            for k in m.get('UpgradeHistory'):
                temp_model = ListServiceInstanceUpgradeHistoryResponseBodyUpgradeHistory()
                self.upgrade_history.append(temp_model.from_map(k))
        return self


class ListServiceInstanceUpgradeHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceInstanceUpgradeHistoryResponseBody = None,
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
            temp_model = ListServiceInstanceUpgradeHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceInstancesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter. You can specify one or more parameter names to query services. Valid values:
        # 
        # - Name：Query by service name.
        # - ServiceInstanceName：Query by service  instance name.
        # - ServiceInstanceId：Query by service  instance ID.
        # - ServiceId：Query by service ID.
        # - Version：Query by service version.
        # - Status：Query by service status.
        # - DeployType: Query by service deployType.
        # - ServiceType：Query by service deployType.
        self.name = name
        # The parameter values of the filter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class ListServiceInstancesRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListServiceInstancesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[ListServiceInstancesRequestTag] = None,
    ):
        # The filter.
        self.filter = filter
        # The number of entries page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tag key and value.
        self.tag = tag

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceInstancesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServiceInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServiceInstancesResponseBodyServiceInstancesServiceCommodity(TeaModel):
    def __init__(
        self,
        saas_boost_metadata: str = None,
        type: str = None,
    ):
        # The configuration metadata related to SaaS Boost.
        self.saas_boost_metadata = saas_boost_metadata
        # The platform type. Valid values:
        # 
        # *   marketplace: Alibaba Cloud Marketplace.
        # *   Css: Lingxiao.
        # *   SaasBoost: SaaS Boost.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.saas_boost_metadata is not None:
            result['SaasBoostMetadata'] = self.saas_boost_metadata
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SaasBoostMetadata') is not None:
            self.saas_boost_metadata = m.get('SaasBoostMetadata')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
    ):
        # The URL of the service icon.
        self.image = image
        # The language of the service instance.
        self.locale = locale
        # The name of the service.
        self.name = name
        # The description of the service.
        self.short_description = short_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        return self


class ListServiceInstancesResponseBodyServiceInstancesService(TeaModel):
    def __init__(
        self,
        commodity: ListServiceInstancesResponseBodyServiceInstancesServiceCommodity = None,
        deploy_type: str = None,
        publish_time: str = None,
        service_id: str = None,
        service_infos: List[ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos] = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_url: str = None,
        version: str = None,
        version_name: str = None,
    ):
        # The commodity details.
        self.commodity = commodity
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        # *   ack: The service is deployed by using Alibaba Cloud Container Service for Kubernetes (ACK).
        # *   spi: The service is deployed by calling the Service Provider Interface (SPI).
        # *   operation: The service is deployed by using a hosted O\\&M service.
        self.deploy_type = deploy_type
        # The time when the service was published.
        self.publish_time = publish_time
        # The service ID.
        self.service_id = service_id
        # The information about the service.
        self.service_infos = service_infos
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        self.service_type = service_type
        # The service state.
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # The service version.
        self.version = version
        # The custom version name defined by the service provider.
        self.version_name = version_name

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commodity') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesServiceCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesServiceServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        return self


class ListServiceInstancesResponseBodyServiceInstancesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class ListServiceInstancesResponseBodyServiceInstances(TeaModel):
    def __init__(
        self,
        biz_status: str = None,
        create_time: str = None,
        enable_instance_ops: bool = None,
        end_time: str = None,
        market_instance_id: str = None,
        name: str = None,
        operated_service_instance_id: str = None,
        operation_end_time: str = None,
        operation_start_time: str = None,
        order_id: str = None,
        outputs: str = None,
        parameters: str = None,
        pay_type: str = None,
        progress: int = None,
        resource_group_id: str = None,
        resources: str = None,
        service: ListServiceInstancesResponseBodyServiceInstancesService = None,
        service_instance_id: str = None,
        service_type: str = None,
        source: str = None,
        status: str = None,
        status_detail: str = None,
        support_trial_to_private: bool = None,
        tags: List[ListServiceInstancesResponseBodyServiceInstancesTags] = None,
        template_name: str = None,
        update_time: str = None,
    ):
        # The business state of the service instance. Valid values:
        # 
        # *   Normal
        # *   Renewing
        # *   RenewFailed
        # *   Expired
        self.biz_status = biz_status
        # The time when the service instance was created.
        self.create_time = create_time
        # Indicates whether the service instance supports the hosted O\\&M feature. Valid values:
        # 
        # *   true
        # *   false
        self.enable_instance_ops = enable_instance_ops
        # The time when the service instance expires.
        self.end_time = end_time
        # The ID of the Alibaba Cloud Marketplace instance.
        self.market_instance_id = market_instance_id
        # The name of the service instance.
        self.name = name
        # The ID of the managed service instance.
        self.operated_service_instance_id = operated_service_instance_id
        # The end of the time range during which hosted O\\&M is implemented.
        self.operation_end_time = operation_end_time
        # The beginning of the time range during which hosted O\\&M is implemented.
        self.operation_start_time = operation_start_time
        # The order ID.
        self.order_id = order_id
        # The information returned after the service instance is created.
        self.outputs = outputs
        # The parameters of the service instance.
        self.parameters = parameters
        # The billing method. Valid values:
        # 
        # *   Permanent: Once you purchase the service, you can use it permanently.
        # *   Subscription: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a subscription basis.
        # *   PayAsYouGo: You purchase the service from Alibaba Cloud Marketplace and are charged for the service on a pay-as-you-go basis.
        # *   CustomFixTime: You are charged for the service based on a custom duration fixed by the service provider.
        self.pay_type = pay_type
        # The deployment progress of the service instance, in percentage.
        self.progress = progress
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resources.
        self.resources = resources
        # The services.
        self.service = service
        # The service instance ID.
        self.service_instance_id = service_instance_id
        # The type of the service. Valid values:
        # 
        # *   private: The service is a private service and is deployed within the account of a customer.
        # *   managed: The service is a fully managed service and is deployed within the account of a service provider.
        # *   operation: The service is a hosted O\\&M service.
        # *   poc: The service is a trial service.
        self.service_type = service_type
        # The source from which the service instance is created.
        self.source = source
        # The state of the service instance. Valid values:
        # 
        # *   Created
        # *   Deploying
        # *   DeployedFailed
        # *   Deployed
        # *   Upgrading
        # *   Deleting
        # *   Deleted
        # *   DeletedFailed
        self.status = status
        # The description of the deployment of the service instance.
        self.status_detail = status_detail
        self.support_trial_to_private = support_trial_to_private
        # The custom tags.
        self.tags = tags
        # The template name.
        self.template_name = template_name
        # The time when the service instance was updated.
        self.update_time = update_time

    def validate(self):
        if self.service:
            self.service.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_instance_ops is not None:
            result['EnableInstanceOps'] = self.enable_instance_ops
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.market_instance_id is not None:
            result['MarketInstanceId'] = self.market_instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.operated_service_instance_id is not None:
            result['OperatedServiceInstanceId'] = self.operated_service_instance_id
        if self.operation_end_time is not None:
            result['OperationEndTime'] = self.operation_end_time
        if self.operation_start_time is not None:
            result['OperationStartTime'] = self.operation_start_time
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.outputs is not None:
            result['Outputs'] = self.outputs
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.service is not None:
            result['Service'] = self.service.to_map()
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.status_detail is not None:
            result['StatusDetail'] = self.status_detail
        if self.support_trial_to_private is not None:
            result['SupportTrialToPrivate'] = self.support_trial_to_private
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableInstanceOps') is not None:
            self.enable_instance_ops = m.get('EnableInstanceOps')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MarketInstanceId') is not None:
            self.market_instance_id = m.get('MarketInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OperatedServiceInstanceId') is not None:
            self.operated_service_instance_id = m.get('OperatedServiceInstanceId')
        if m.get('OperationEndTime') is not None:
            self.operation_end_time = m.get('OperationEndTime')
        if m.get('OperationStartTime') is not None:
            self.operation_start_time = m.get('OperationStartTime')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('Service') is not None:
            temp_model = ListServiceInstancesResponseBodyServiceInstancesService()
            self.service = temp_model.from_map(m['Service'])
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusDetail') is not None:
            self.status_detail = m.get('StatusDetail')
        if m.get('SupportTrialToPrivate') is not None:
            self.support_trial_to_private = m.get('SupportTrialToPrivate')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListServiceInstancesResponseBodyServiceInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListServiceInstancesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_instances: List[ListServiceInstancesResponseBodyServiceInstances] = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the service instances.
        self.service_instances = service_instances
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.service_instances:
            for k in self.service_instances:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceInstances'] = []
        if self.service_instances is not None:
            for k in self.service_instances:
                result['ServiceInstances'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_instances = []
        if m.get('ServiceInstances') is not None:
            for k in m.get('ServiceInstances'):
                temp_model = ListServiceInstancesResponseBodyServiceInstances()
                self.service_instances.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceInstancesResponseBody = None,
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
            temp_model = ListServiceInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServiceUsagesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter. You can specify one or more filters. Valid values:
        # 
        # *   ServiceId: the ID of the service.
        # *   ServiceName: the service name.
        # *   Status: the state of the service.
        # *   SupplierName: the name of the service provider.
        self.name = name
        # The parameter values of the filter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServiceUsagesRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListServiceUsagesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The filters.
        self.filter = filter
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServiceUsagesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListServiceUsagesResponseBodyServiceUsages(TeaModel):
    def __init__(
        self,
        comments: str = None,
        create_time: str = None,
        service_id: str = None,
        service_name: str = None,
        status: str = None,
        supplier_name: str = None,
        update_time: str = None,
        user_ali_uid: int = None,
        user_information: Dict[str, str] = None,
    ):
        # The review comment.
        self.comments = comments
        # The time when the application was created.
        self.create_time = create_time
        # The service ID.
        self.service_id = service_id
        # The service name.
        self.service_name = service_name
        # The state of the service application. Valid values:
        # 
        # *   Submitted: The application is submitted for review.
        # *   Approved: The application is approved.
        # *   Rejected: The application is rejected.
        # *   Canceled: The application is canceled.
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The time when the application was updated.
        self.update_time = update_time
        # The ID of the Alibaba Cloud account.
        self.user_ali_uid = user_ali_uid
        # The information about the applicants.
        self.user_information = user_information

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_ali_uid is not None:
            result['UserAliUid'] = self.user_ali_uid
        if self.user_information is not None:
            result['UserInformation'] = self.user_information
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserAliUid') is not None:
            self.user_ali_uid = m.get('UserAliUid')
        if m.get('UserInformation') is not None:
            self.user_information = m.get('UserInformation')
        return self


class ListServiceUsagesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_usages: List[ListServiceUsagesResponseBodyServiceUsages] = None,
        total_count: int = None,
    ):
        # The maximum number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The service applications.
        self.service_usages = service_usages
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.service_usages:
            for k in self.service_usages:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceUsages'] = []
        if self.service_usages is not None:
            for k in self.service_usages:
                result['ServiceUsages'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_usages = []
        if m.get('ServiceUsages') is not None:
            for k in m.get('ServiceUsages'):
                temp_model = ListServiceUsagesResponseBodyServiceUsages()
                self.service_usages.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServiceUsagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServiceUsagesResponseBody = None,
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
            temp_model = ListServiceUsagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServicesRequestFilter(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The parameter name of the filter. You can specify one or more parameter names to query services. Valid values:
        # 
        # *   ServiceId: the ID of the service.
        # *   Name: the name of the service.
        # *   Status: the state of the service.
        # *   SupplierName: the name of the service provider.
        self.name = name
        # A value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListServicesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        filter: List[ListServicesRequestFilter] = None,
        fuzzy_keyword: str = None,
        in_used: bool = None,
        max_results: int = None,
        next_token: str = None,
        order_by_type: str = None,
        region_id: str = None,
        service_access_type: str = None,
        tag: List[ListServicesRequestTag] = None,
    ):
        # The filter.
        self.filter = filter
        # Keyword fuzzy query.
        self.fuzzy_keyword = fuzzy_keyword
        # Whether it is used. Optional values:
        # 
        # 
        # 
        # - false: not being used.
        # 
        # 
        # 
        # - true: already in use.
        self.in_used = in_used
        # The number of entries page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # Service ordering type.
        self.order_by_type = order_by_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Service access type.
        self.service_access_type = service_access_type
        # The tags.
        self.tag = tag

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.fuzzy_keyword is not None:
            result['FuzzyKeyword'] = self.fuzzy_keyword
        if self.in_used is not None:
            result['InUsed'] = self.in_used
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_by_type is not None:
            result['OrderByType'] = self.order_by_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_access_type is not None:
            result['ServiceAccessType'] = self.service_access_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = ListServicesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('FuzzyKeyword') is not None:
            self.fuzzy_keyword = m.get('FuzzyKeyword')
        if m.get('InUsed') is not None:
            self.in_used = m.get('InUsed')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderByType') is not None:
            self.order_by_type = m.get('OrderByType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceAccessType') is not None:
            self.service_access_type = m.get('ServiceAccessType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServicesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListServicesResponseBodyServicesCommodity(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        deploy_page: str = None,
    ):
        # The commodity code.
        self.commodity_code = commodity_code
        # Deploy Page.
        self.deploy_page = deploy_page

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.deploy_page is not None:
            result['DeployPage'] = self.deploy_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('DeployPage') is not None:
            self.deploy_page = m.get('DeployPage')
        return self


class ListServicesResponseBodyServicesServiceInfosSoftwares(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListServicesResponseBodyServicesServiceInfos(TeaModel):
    def __init__(
        self,
        image: str = None,
        locale: str = None,
        name: str = None,
        short_description: str = None,
        softwares: List[ListServicesResponseBodyServicesServiceInfosSoftwares] = None,
    ):
        # The URL of the service icon.
        self.image = image
        # The language of the service. Valid values:
        # 
        # *   zh-CN: Chinese.
        # *   en-US: English.
        self.locale = locale
        # The name of the service.
        self.name = name
        # The description of the service.
        self.short_description = short_description
        self.softwares = softwares

    def validate(self):
        if self.softwares:
            for k in self.softwares:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['Image'] = self.image
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.name is not None:
            result['Name'] = self.name
        if self.short_description is not None:
            result['ShortDescription'] = self.short_description
        result['Softwares'] = []
        if self.softwares is not None:
            for k in self.softwares:
                result['Softwares'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ShortDescription') is not None:
            self.short_description = m.get('ShortDescription')
        self.softwares = []
        if m.get('Softwares') is not None:
            for k in m.get('Softwares'):
                temp_model = ListServicesResponseBodyServicesServiceInfosSoftwares()
                self.softwares.append(temp_model.from_map(k))
        return self


class ListServicesResponseBodyServicesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        # 
        # >  This parameter is required.
        self.key = key
        # The tag value.
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


class ListServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        categories: str = None,
        commodity: ListServicesResponseBodyServicesCommodity = None,
        commodity_code: str = None,
        deploy_from: str = None,
        deploy_type: str = None,
        publish_time: str = None,
        score: int = None,
        service_id: str = None,
        service_infos: List[ListServicesResponseBodyServicesServiceInfos] = None,
        service_product_url: str = None,
        service_type: str = None,
        status: str = None,
        supplier_name: str = None,
        supplier_name_eng: str = None,
        supplier_uid: int = None,
        supplier_url: str = None,
        tags: List[ListServicesResponseBodyServicesTags] = None,
        tenant_type: str = None,
        trial_duration: str = None,
        trial_type: str = None,
        version: str = None,
        version_name: str = None,
        virtual_internet_service: str = None,
    ):
        # The category of the service.
        self.categories = categories
        # The commodity details.
        self.commodity = commodity
        # The commodity code of the service in Alibaba Cloud Marketplace.
        self.commodity_code = commodity_code
        # Service deployment approach. Valid values:
        # - NoWhere
        # 
        # - Marketplace
        # 
        # - ComputeNest
        self.deploy_from = deploy_from
        # The deployment type of the service. Valid values:
        # 
        # *   ros: The service is deployed by using Resource Orchestration Service (ROS).
        # *   terraform: The service is deployed by using Terraform.
        self.deploy_type = deploy_type
        # The time when the service was published.
        self.publish_time = publish_time
        # Service recommendation score.
        self.score = score
        # The service ID.
        self.service_id = service_id
        # The information about the service.
        self.service_infos = service_infos
        # The URL of the service page.
        self.service_product_url = service_product_url
        # The type of the service. Valid values:
        # 
        # - private: The service is a private service and is deployed within the account of a customer.
        # - managed: The service is a fully managed service and is deployed within the account of a service provider.
        # - operation: The service is a hosted O&M service.
        self.service_type = service_type
        # The state of the service. Valid values:
        # 
        # *   Draft: The service is a draft.
        # *   Submitted: The service is submitted for review. You cannot modify services in this state.
        # *   Approved: The service is approved. You cannot modify services in this state. You can publish services in this state.
        # *   Launching: The service is being published.
        # *   Online: The service is published.
        # *   Offline: The service is unpublished.
        self.status = status
        # The name of the service provider.
        self.supplier_name = supplier_name
        # The name of service provider.
        self.supplier_name_eng = supplier_name_eng
        # The Alibaba Cloud account ID of the service provider.
        self.supplier_uid = supplier_uid
        # The URL of the service provider.
        self.supplier_url = supplier_url
        # The tags.
        self.tags = tags
        # The tenant type of the managed service. Valid values:
        # 
        # *   SingleTenant
        # *   MultiTenant
        self.tenant_type = tenant_type
        # The trial duration. Unit: day. The maximum trial duration cannot exceed 30 days.
        self.trial_duration = trial_duration
        # The trial policy. Valid values:
        # 
        # *   Trial: Trials are supported.
        # *   NotTrial: Trials are not supported.
        self.trial_type = trial_type
        # The version of the service.
        self.version = version
        # The custom version name defined by the service provider.
        self.version_name = version_name
        # Indicates whether the service is a virtual Internet service. Valid values:
        # 
        # *   false
        # *   true
        self.virtual_internet_service = virtual_internet_service

    def validate(self):
        if self.commodity:
            self.commodity.validate()
        if self.service_infos:
            for k in self.service_infos:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.deploy_from is not None:
            result['DeployFrom'] = self.deploy_from
        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.score is not None:
            result['Score'] = self.score
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['ServiceInfos'] = []
        if self.service_infos is not None:
            for k in self.service_infos:
                result['ServiceInfos'].append(k.to_map() if k else None)
        if self.service_product_url is not None:
            result['ServiceProductUrl'] = self.service_product_url
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name
        if self.supplier_name_eng is not None:
            result['SupplierNameEng'] = self.supplier_name_eng
        if self.supplier_uid is not None:
            result['SupplierUid'] = self.supplier_uid
        if self.supplier_url is not None:
            result['SupplierUrl'] = self.supplier_url
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tenant_type is not None:
            result['TenantType'] = self.tenant_type
        if self.trial_duration is not None:
            result['TrialDuration'] = self.trial_duration
        if self.trial_type is not None:
            result['TrialType'] = self.trial_type
        if self.version is not None:
            result['Version'] = self.version
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.virtual_internet_service is not None:
            result['VirtualInternetService'] = self.virtual_internet_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        if m.get('Commodity') is not None:
            temp_model = ListServicesResponseBodyServicesCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('DeployFrom') is not None:
            self.deploy_from = m.get('DeployFrom')
        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.service_infos = []
        if m.get('ServiceInfos') is not None:
            for k in m.get('ServiceInfos'):
                temp_model = ListServicesResponseBodyServicesServiceInfos()
                self.service_infos.append(temp_model.from_map(k))
        if m.get('ServiceProductUrl') is not None:
            self.service_product_url = m.get('ServiceProductUrl')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')
        if m.get('SupplierNameEng') is not None:
            self.supplier_name_eng = m.get('SupplierNameEng')
        if m.get('SupplierUid') is not None:
            self.supplier_uid = m.get('SupplierUid')
        if m.get('SupplierUrl') is not None:
            self.supplier_url = m.get('SupplierUrl')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListServicesResponseBodyServicesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TenantType') is not None:
            self.tenant_type = m.get('TenantType')
        if m.get('TrialDuration') is not None:
            self.trial_duration = m.get('TrialDuration')
        if m.get('TrialType') is not None:
            self.trial_type = m.get('TrialType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VirtualInternetService') is not None:
            self.virtual_internet_service = m.get('VirtualInternetService')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[ListServicesResponseBodyServices] = None,
        total_count: int = None,
    ):
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The services.
        self.services = services
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.services:
            for k in self.services:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource type. Valid values:
        # 
        # *   service: service
        # *   serviceinstance: service instance
        # *   artifact: artifact
        # *   dataset: dataset
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        keys: List[str] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Details of the tag keys.
        self.keys = keys
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. You can specify up to 50 resource IDs.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   service: service
        # *   serviceinstance: service instance
        # *   artifact: artifact
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   service: service
        # *   serviceinstance: service instance
        # *   artifact: artifact
        self.resource_type = resource_type
        # The key of the tag.
        self.tag_key = tag_key
        # The values of the tags.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # A list of resources that have tags.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The tag key.
        # 
        # >  This parameter is required.
        # 
        # This parameter is required.
        self.key = key
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource type. Valid values:
        # 
        # *   service: service
        # *   serviceinstance: service instance
        # *   artifact: artifact
        # *   dataset: dataset
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        values: List[str] = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information of the tag values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagValuesResponseBody = None,
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
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewServiceInstanceResourcesRequestResourcePeriod(TeaModel):
    def __init__(
        self,
        period: int = None,
        period_unit: str = None,
        resource_arn: str = None,
    ):
        # The renewal duration for the resource. The unit is specified by PeriodUnit.
        self.period = period
        # The time unit for the renewal duration of the resource, which is the unit for the Period parameter. Valid values: Month, Year. Default value: Month.
        self.period_unit = period_unit
        # Resource ARN (Aliyun Resource Name).
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        return self


class RenewServiceInstanceResourcesRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        period: int = None,
        period_unit: str = None,
        region_id: str = None,
        resource_period: List[RenewServiceInstanceResourcesRequestResourcePeriod] = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The renewal duration for all prepaid resources in the service instance. The unit is specified by PeriodUnit.
        self.period = period
        # The time unit for the renewal duration of all prepaid resources in the service instance, which is the unit for the Period parameter. Valid values: Month, Year. Default value: Month.
        self.period_unit = period_unit
        # Region ID.
        self.region_id = region_id
        # List of resource renewals.
        self.resource_period = resource_period
        # Service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.resource_period:
            for k in self.resource_period:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ResourcePeriod'] = []
        if self.resource_period is not None:
            for k in self.resource_period:
                result['ResourcePeriod'].append(k.to_map() if k else None)
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource_period = []
        if m.get('ResourcePeriod') is not None:
            for k in m.get('ResourcePeriod'):
                temp_model = RenewServiceInstanceResourcesRequestResourcePeriod()
                self.resource_period.append(temp_model.from_map(k))
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class RenewServiceInstanceResourcesResponseBodyFailureDetails(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        resource_arn: str = None,
    ):
        # Error code.
        self.error_code = error_code
        # Error message.
        self.error_message = error_message
        # Resource ARN (Aliyun Resource Name).
        self.resource_arn = resource_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')
        return self


class RenewServiceInstanceResourcesResponseBodyRenewalResult(TeaModel):
    def __init__(
        self,
        failed: int = None,
        succeeded: int = None,
        total_count: int = None,
    ):
        # Number of failed renewals.
        self.failed = failed
        # Number of successfully renewed resources.
        self.succeeded = succeeded
        # Number of renewed resources.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class RenewServiceInstanceResourcesResponseBody(TeaModel):
    def __init__(
        self,
        failure_details: List[RenewServiceInstanceResourcesResponseBodyFailureDetails] = None,
        renewal_result: RenewServiceInstanceResourcesResponseBodyRenewalResult = None,
        request_id: str = None,
    ):
        # Details of failed renewals.
        self.failure_details = failure_details
        # Renewal result.
        self.renewal_result = renewal_result
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.failure_details:
            for k in self.failure_details:
                if k:
                    k.validate()
        if self.renewal_result:
            self.renewal_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailureDetails'] = []
        if self.failure_details is not None:
            for k in self.failure_details:
                result['FailureDetails'].append(k.to_map() if k else None)
        if self.renewal_result is not None:
            result['RenewalResult'] = self.renewal_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failure_details = []
        if m.get('FailureDetails') is not None:
            for k in m.get('FailureDetails'):
                temp_model = RenewServiceInstanceResourcesResponseBodyFailureDetails()
                self.failure_details.append(temp_model.from_map(k))
        if m.get('RenewalResult') is not None:
            temp_model = RenewServiceInstanceResourcesResponseBodyRenewalResult()
            self.renewal_result = temp_model.from_map(m['RenewalResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewServiceInstanceResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewServiceInstanceResourcesResponseBody = None,
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
            temp_model = RenewServiceInstanceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID where the service instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class RestartServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RestartServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartServiceInstanceResponseBody = None,
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
            temp_model = RestartServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID.
        self.region_id = region_id
        # The service instance ID.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class RollbackServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class RollbackServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RollbackServiceInstanceResponseBody = None,
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
            temp_model = RollbackServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The region ID where the service instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class StartServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StartServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartServiceInstanceResponseBody = None,
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
            temp_model = StartServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token
        # The region where the service instance resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class StopServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class StopServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopServiceInstanceResponseBody = None,
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
            temp_model = StopServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. You can specify up to 50 resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   service: service
        # *   serviceinstance: service instance
        # *   artifact: artifact
        # *   dataset: dataset
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag key and value.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnTagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the resource. Valid values:
        # 
        # *   true: All tags are removed from the resource.
        # *   false (default): The specified tags are removed from the resource.
        self.all = all
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource ID.
        # 
        # You can remove tags from up to 50 resources at a time.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   service: service
        # *   serviceinstance: service instance
        # *   artifact: artifact
        # *   dataset: dataset
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys.
        # 
        # You can specify a maximum of 20 tag keys.
        # 
        # > If you set the `All` parameter to `true`, you do not need to specify tag keys.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UnTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UnTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnTagResourcesResponseBody = None,
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
            temp_model = UnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceInstanceAttributesRequest(TeaModel):
    def __init__(
        self,
        enable_operation: bool = None,
        region_id: str = None,
        service_instance_id: str = None,
    ):
        # Specifies whether to authorize the service provider to perform O\\&M operations on the service instance.
        self.enable_operation = enable_operation
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the service instance.
        # 
        # You can call the [ListServiceInstances](https://help.aliyun.com/document_detail/396200.html) operation to obtain the ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_operation is not None:
            result['EnableOperation'] = self.enable_operation
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableOperation') is not None:
            self.enable_operation = m.get('EnableOperation')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class UpdateServiceInstanceAttributesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateServiceInstanceAttributesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceInstanceAttributesResponseBody = None,
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
            temp_model = UpdateServiceInstanceAttributesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceInstanceSpecRequestCommodity(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
    ):
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # *   **true (default)**: automatically completes the payment. You must make sure that your account balance is sufficient.
        # *   **false**: does not automatically complete the payment. An unpaid order is generated. If your account balance is insufficient, you can set AutoPay to false. In this case, an unpaid order is generated. You can complete the payment in the Expenses and Costs console.[](https://rdsnext.console.aliyun.com/dashboard/cn-beijing)
        self.auto_pay = auto_pay

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        return self


class UpdateServiceInstanceSpecRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: UpdateServiceInstanceSpecRequestCommodity = None,
        dry_run: bool = None,
        enable_user_prometheus: bool = None,
        operation_name: str = None,
        parameters: Dict[str, Any] = None,
        predefined_parameters_name: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the order placed in Alibaba Cloud Marketplace. You do not need to specify this parameter if the service is not published in Alibaba Cloud Marketplace or uses the pay-as-you-go billing method.
        self.commodity = commodity
        # Specifies whether to perform only a dry run, without performing the actual request. A dry run includes checks on the permissions and instance state.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run but does not create a service instance.
        # *   false: performs a dry run and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # Specifies whether to enable Prometheus monitoring on the user side.
        # 
        # Valid values:
        # 
        # true
        # 
        # false
        self.enable_user_prometheus = enable_user_prometheus
        # The name of the configuration change operation.
        # 
        # To obtain the names and content of the configuration change operations of the service, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **ModifyParametersConfig** in the value of **OperationMetadata**.
        self.operation_name = operation_name
        # The configuration parameter.
        # 
        # This parameter is available if the service provider set **Method** to **Change Parameter** when configuring configuration change operations.
        # 
        # > 
        # 
        # *   To obtain the parameters of the service that support configuration change, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **ModifyParametersConfig** in the value of **OperationMetadata**.
        # 
        # *   You can also view the parameters of the service that support configuration change in the **configuration change** dialog box in the [Compute Nest console](https://computenest.console.aliyun.com/service/instance/cn-hangzhou).
        # 
        # For example, if the service supports Elastic Compute Service (ECS) instance type upgrade, you must specify an instance type that has higher specifications than the current one.
        self.parameters = parameters
        # The name of the configuration plan.
        # 
        # This parameter is available if the service provider set **Method** to **Change Plan** when configuring configuration change operations.
        # 
        # To obtain the configuration plan names of the service, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **PredefinedParameters** in the value of **DeployMetadata**.
        self.predefined_parameters_name = predefined_parameters_name
        # The ID of the service instance.
        # 
        # You can call the [ListServiceInstances](https://help.aliyun.com/document_detail/396200.html) operation to obtain the ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.commodity:
            self.commodity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.predefined_parameters_name is not None:
            result['PredefinedParametersName'] = self.predefined_parameters_name
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            temp_model = UpdateServiceInstanceSpecRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('PredefinedParametersName') is not None:
            self.predefined_parameters_name = m.get('PredefinedParametersName')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class UpdateServiceInstanceSpecShrinkRequestCommodity(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
    ):
        # Specifies whether to enable automatic payment.
        # 
        # Valid values:
        # 
        # *   **true (default)**: automatically completes the payment. You must make sure that your account balance is sufficient.
        # *   **false**: does not automatically complete the payment. An unpaid order is generated. If your account balance is insufficient, you can set AutoPay to false. In this case, an unpaid order is generated. You can complete the payment in the Expenses and Costs console.[](https://rdsnext.console.aliyun.com/dashboard/cn-beijing)
        self.auto_pay = auto_pay

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        return self


class UpdateServiceInstanceSpecShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity: UpdateServiceInstanceSpecShrinkRequestCommodity = None,
        dry_run: bool = None,
        enable_user_prometheus: bool = None,
        operation_name: str = None,
        parameters_shrink: str = None,
        predefined_parameters_name: str = None,
        service_instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The information about the order placed in Alibaba Cloud Marketplace. You do not need to specify this parameter if the service is not published in Alibaba Cloud Marketplace or uses the pay-as-you-go billing method.
        self.commodity = commodity
        # Specifies whether to perform only a dry run, without performing the actual request. A dry run includes checks on the permissions and instance state.
        # 
        # Valid values:
        # 
        # *   true: performs a dry run but does not create a service instance.
        # *   false: performs a dry run and creates a service instance if the request passes the dry run.
        self.dry_run = dry_run
        # Specifies whether to enable Prometheus monitoring on the user side.
        # 
        # Valid values:
        # 
        # true
        # 
        # false
        self.enable_user_prometheus = enable_user_prometheus
        # The name of the configuration change operation.
        # 
        # To obtain the names and content of the configuration change operations of the service, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **ModifyParametersConfig** in the value of **OperationMetadata**.
        self.operation_name = operation_name
        # The configuration parameter.
        # 
        # This parameter is available if the service provider set **Method** to **Change Parameter** when configuring configuration change operations.
        # 
        # > 
        # 
        # *   To obtain the parameters of the service that support configuration change, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **ModifyParametersConfig** in the value of **OperationMetadata**.
        # 
        # *   You can also view the parameters of the service that support configuration change in the **configuration change** dialog box in the [Compute Nest console](https://computenest.console.aliyun.com/service/instance/cn-hangzhou).
        # 
        # For example, if the service supports Elastic Compute Service (ECS) instance type upgrade, you must specify an instance type that has higher specifications than the current one.
        self.parameters_shrink = parameters_shrink
        # The name of the configuration plan.
        # 
        # This parameter is available if the service provider set **Method** to **Change Plan** when configuring configuration change operations.
        # 
        # To obtain the configuration plan names of the service, you can call the [GetService](https://help.aliyun.com/document_detail/2340828.html) operation. In the response, check the value of **PredefinedParameters** in the value of **DeployMetadata**.
        self.predefined_parameters_name = predefined_parameters_name
        # The ID of the service instance.
        # 
        # You can call the [ListServiceInstances](https://help.aliyun.com/document_detail/396200.html) operation to obtain the ID of the service instance.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id

    def validate(self):
        if self.commodity:
            self.commodity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.enable_user_prometheus is not None:
            result['EnableUserPrometheus'] = self.enable_user_prometheus
        if self.operation_name is not None:
            result['OperationName'] = self.operation_name
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.predefined_parameters_name is not None:
            result['PredefinedParametersName'] = self.predefined_parameters_name
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Commodity') is not None:
            temp_model = UpdateServiceInstanceSpecShrinkRequestCommodity()
            self.commodity = temp_model.from_map(m['Commodity'])
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EnableUserPrometheus') is not None:
            self.enable_user_prometheus = m.get('EnableUserPrometheus')
        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('PredefinedParametersName') is not None:
            self.predefined_parameters_name = m.get('PredefinedParametersName')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        return self


class UpdateServiceInstanceSpecResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        # The order ID.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateServiceInstanceSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceInstanceSpecResponseBody = None,
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
            temp_model = UpdateServiceInstanceSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceUsageRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        service_id: str = None,
        user_information: Dict[str, str] = None,
    ):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The information about the applicant.
        self.user_information = user_information

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_information is not None:
            result['UserInformation'] = self.user_information
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserInformation') is not None:
            self.user_information = m.get('UserInformation')
        return self


class UpdateServiceUsageShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        service_id: str = None,
        user_information_shrink: str = None,
    ):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The service ID.
        # 
        # This parameter is required.
        self.service_id = service_id
        # The information about the applicant.
        self.user_information_shrink = user_information_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_information_shrink is not None:
            result['UserInformation'] = self.user_information_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserInformation') is not None:
            self.user_information_shrink = m.get('UserInformation')
        return self


class UpdateServiceUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateServiceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceUsageResponseBody = None,
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
            temp_model = UpdateServiceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserInformationRequestDeliverySettings(TeaModel):
    def __init__(
        self,
        actiontrail_delivery_to_oss_enabled: bool = None,
        oss_bucket_name: str = None,
        oss_enabled: bool = None,
        oss_expiration_days: int = None,
        oss_path: str = None,
    ):
        # Specifies whether to enable screencast delivery to OSS. Valid values:
        # 
        # *   true
        # *   false
        self.actiontrail_delivery_to_oss_enabled = actiontrail_delivery_to_oss_enabled
        # The name of the OSS bucket.
        self.oss_bucket_name = oss_bucket_name
        # Specifies whether to enable screencast delivery to Object Storage Service (OSS). Valid values:
        # 
        # *   true
        # *   false
        self.oss_enabled = oss_enabled
        # The number of days for which the screencasts are saved.
        self.oss_expiration_days = oss_expiration_days
        # The OSS path.
        self.oss_path = oss_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actiontrail_delivery_to_oss_enabled is not None:
            result['ActiontrailDeliveryToOssEnabled'] = self.actiontrail_delivery_to_oss_enabled
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_enabled is not None:
            result['OssEnabled'] = self.oss_enabled
        if self.oss_expiration_days is not None:
            result['OssExpirationDays'] = self.oss_expiration_days
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiontrailDeliveryToOssEnabled') is not None:
            self.actiontrail_delivery_to_oss_enabled = m.get('ActiontrailDeliveryToOssEnabled')
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssEnabled') is not None:
            self.oss_enabled = m.get('OssEnabled')
        if m.get('OssExpirationDays') is not None:
            self.oss_expiration_days = m.get('OssExpirationDays')
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        return self


class UpdateUserInformationRequest(TeaModel):
    def __init__(
        self,
        delivery_settings: UpdateUserInformationRequestDeliverySettings = None,
        region_id: str = None,
    ):
        # The modified delivery settings.
        self.delivery_settings = delivery_settings
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.delivery_settings:
            self.delivery_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_settings is not None:
            result['DeliverySettings'] = self.delivery_settings.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliverySettings') is not None:
            temp_model = UpdateUserInformationRequestDeliverySettings()
            self.delivery_settings = temp_model.from_map(m['DeliverySettings'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateUserInformationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UpdateUserInformationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserInformationResponseBody = None,
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
            temp_model = UpdateUserInformationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeServiceInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: str = None,
        parameters: Dict[str, Any] = None,
        region_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   **true**: performs a dry run for the request, but does not upgrade service instance.
        # *   **false**: performs a dry run for the request, and upgrade service instance if the request passes the dry run.
        self.dry_run = dry_run
        # The parameters required for the upgrade. This parameter is required if the destination version of the service has new parameters.
        self.parameters = parameters
        # The region ID.
        self.region_id = region_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The destination version.
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class UpgradeServiceInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: str = None,
        parameters_shrink: str = None,
        region_id: str = None,
        service_instance_id: str = None,
        service_version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to perform only a dry run for the request to check information such as the permissions and instance status. Valid values:
        # 
        # *   **true**: performs a dry run for the request, but does not upgrade service instance.
        # *   **false**: performs a dry run for the request, and upgrade service instance if the request passes the dry run.
        self.dry_run = dry_run
        # The parameters required for the upgrade. This parameter is required if the destination version of the service has new parameters.
        self.parameters_shrink = parameters_shrink
        # The region ID.
        self.region_id = region_id
        # The ID of the service instance.
        self.service_instance_id = service_instance_id
        # The destination version.
        self.service_version = service_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class UpgradeServiceInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upgrade_required_parameters: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The parameters required for the upgrade. This parameter is returned only if DryRun is set to true in the request. You can specify the required parameters based on the returned value when you perform an actual request.
        self.upgrade_required_parameters = upgrade_required_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upgrade_required_parameters is not None:
            result['UpgradeRequiredParameters'] = self.upgrade_required_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpgradeRequiredParameters') is not None:
            self.upgrade_required_parameters = m.get('UpgradeRequiredParameters')
        return self


class UpgradeServiceInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeServiceInstanceResponseBody = None,
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
            temp_model = UpgradeServiceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


