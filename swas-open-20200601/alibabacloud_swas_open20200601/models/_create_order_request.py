# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class CreateOrderRequest(DaraModel):
    def __init__(
        self,
        business_info: main_models.CreateOrderRequestBusinessInfo = None,
        commodity: main_models.CreateOrderRequestCommodity = None,
        coupon_no: str = None,
        from_app: str = None,
        order_type: str = None,
        region_id: str = None,
    ):
        # The additional parameter for business information.
        self.business_info = business_info
        # The order configuration information.
        # 
        # This parameter is required.
        self.commodity = commodity
        # The coupon code. Default value: `youhuiquan_promotion_option_id_for_blank`.
        self.coupon_no = coupon_no
        # The request source. Valid values:
        # - **OpenApi**: The request is sent from OpenAPI.
        # - **mongo_buy**: The request is sent from the console.
        self.from_app = from_app
        # The order type. Valid values:
        # - Buy
        # Default value: Buy.
        self.order_type = order_type
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.business_info:
            self.business_info.validate()
        if self.commodity:
            self.commodity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_info is not None:
            result['BusinessInfo'] = self.business_info.to_map()

        if self.commodity is not None:
            result['Commodity'] = self.commodity.to_map()

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        if self.from_app is not None:
            result['FromApp'] = self.from_app

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessInfo') is not None:
            temp_model = main_models.CreateOrderRequestBusinessInfo()
            self.business_info = temp_model.from_map(m.get('BusinessInfo'))

        if m.get('Commodity') is not None:
            temp_model = main_models.CreateOrderRequestCommodity()
            self.commodity = temp_model.from_map(m.get('Commodity'))

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateOrderRequestCommodity(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        commodity_type: str = None,
        data_disk_size: int = None,
        image_id: str = None,
        instance_ids: List[str] = None,
        pay_type: str = None,
        period: int = None,
        period_unit: str = None,
        plan_id: str = None,
    ):
        # The number of Simple Application Server instances to create. Valid values: 1 to 20. Default value: 1.
        self.amount = amount
        # Specifies whether automatic payment is enabled for the order. Valid values:
        # - **true**: Automatic payment.
        # - **false**: No automatic payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal upon expiration. Valid values:
        # - true: Auto-renewal is enabled.
        # - false: Auto-renewal is disabled.
        # Default value: false.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values:
        # - If PeriodUnit is set to Year: 1, 2, and 3.
        # - If PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # The resource name.
        self.commodity_type = commodity_type
        # The size of the mounted data cloud disk. Unit: GB. Valid values: 0 to 16380. The value must be a multiple of 20. Default value: 0.
        self.data_disk_size = data_disk_size
        # The image ID. You can call the [ListImages](https://help.aliyun.com/document_detail/189313.html) operation to query available image IDs in a specified region.
        self.image_id = image_id
        # The IDs of the Simple Application Server instances.
        self.instance_ids = instance_ids
        # The billing method. Valid values:
        # - Prepaid: subscription.
        self.pay_type = pay_type
        # The subscription period. Valid values: 1 to 20. Default value: 1.
        self.period = period
        # The unit of the subscription period. Valid values:
        # - Month: monthly billing.
        # - Year: yearly billing.
        # Default value: Month.
        self.period_unit = period_unit
        # The plan ID. You can call the [ListPlans](https://help.aliyun.com/document_detail/189314.html) operation to query all plans in a specified region.
        self.plan_id = plan_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        return self

class CreateOrderRequestBusinessInfo(DaraModel):
    def __init__(
        self,
        aliyun_lang: str = None,
        order_source: str = None,
        promotion_options: main_models.CreateOrderRequestBusinessInfoPromotionOptions = None,
        use_coupon: bool = None,
        we_chat_pro_type: str = None,
        lx_channel_cookie_value: str = None,
    ):
        # The language environment. Default value: Chinese.
        self.aliyun_lang = aliyun_lang
        # The order source.
        self.order_source = order_source
        # The promotion option information.
        self.promotion_options = promotion_options
        # Specifies whether to use a voucher. Valid values:
        # - **true**: A voucher is used.
        # - **false**: No voucher is used.
        # Default value: **false**.
        self.use_coupon = use_coupon
        # The WeChat product type.
        self.we_chat_pro_type = we_chat_pro_type
        # The channel cookie value.
        self.lx_channel_cookie_value = lx_channel_cookie_value

    def validate(self):
        if self.promotion_options:
            self.promotion_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_lang is not None:
            result['AliyunLang'] = self.aliyun_lang

        if self.order_source is not None:
            result['OrderSource'] = self.order_source

        if self.promotion_options is not None:
            result['PromotionOptions'] = self.promotion_options.to_map()

        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon

        if self.we_chat_pro_type is not None:
            result['WeChatProType'] = self.we_chat_pro_type

        if self.lx_channel_cookie_value is not None:
            result['lx_channel_cookie_value'] = self.lx_channel_cookie_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunLang') is not None:
            self.aliyun_lang = m.get('AliyunLang')

        if m.get('OrderSource') is not None:
            self.order_source = m.get('OrderSource')

        if m.get('PromotionOptions') is not None:
            temp_model = main_models.CreateOrderRequestBusinessInfoPromotionOptions()
            self.promotion_options = temp_model.from_map(m.get('PromotionOptions'))

        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')

        if m.get('WeChatProType') is not None:
            self.we_chat_pro_type = m.get('WeChatProType')

        if m.get('lx_channel_cookie_value') is not None:
            self.lx_channel_cookie_value = m.get('lx_channel_cookie_value')

        return self

class CreateOrderRequestBusinessInfoPromotionOptions(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        promotion_filter: main_models.CreateOrderRequestBusinessInfoPromotionOptionsPromotionFilter = None,
        promotion_option_code: str = None,
        promotion_option_no: str = None,
    ):
        # The activity ID.
        self.activity_id = activity_id
        # The promotion filter.
        self.promotion_filter = promotion_filter
        # The promotion option code.
        self.promotion_option_code = promotion_option_code
        # The coupon ID.
        self.promotion_option_no = promotion_option_no

    def validate(self):
        if self.promotion_filter:
            self.promotion_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.promotion_filter is not None:
            result['PromotionFilter'] = self.promotion_filter.to_map()

        if self.promotion_option_code is not None:
            result['PromotionOptionCode'] = self.promotion_option_code

        if self.promotion_option_no is not None:
            result['PromotionOptionNo'] = self.promotion_option_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('PromotionFilter') is not None:
            temp_model = main_models.CreateOrderRequestBusinessInfoPromotionOptionsPromotionFilter()
            self.promotion_filter = temp_model.from_map(m.get('PromotionFilter'))

        if m.get('PromotionOptionCode') is not None:
            self.promotion_option_code = m.get('PromotionOptionCode')

        if m.get('PromotionOptionNo') is not None:
            self.promotion_option_no = m.get('PromotionOptionNo')

        return self

class CreateOrderRequestBusinessInfoPromotionOptionsPromotionFilter(DaraModel):
    def __init__(
        self,
        use_coupon: bool = None,
    ):
        # Specifies whether to use a voucher. Valid values:
        # - **true**: A voucher is used.
        # - **false**: No voucher is used.
        # Default value: **false**.
        self.use_coupon = use_coupon

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.use_coupon is not None:
            result['UseCoupon'] = self.use_coupon

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UseCoupon') is not None:
            self.use_coupon = m.get('UseCoupon')

        return self

