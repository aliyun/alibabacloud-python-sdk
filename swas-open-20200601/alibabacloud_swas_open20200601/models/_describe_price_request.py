# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribePriceRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        amount: int = None,
        commodity_type: str = None,
        data_disk_size: int = None,
        instance_id: str = None,
        order_type: str = None,
        pay_type: str = None,
        period: int = None,
        plan_id: str = None,
        price_unit: str = None,
        promotion_options: main_models.DescribePriceRequestPromotionOptions = None,
        region_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # - **zh-CN** (default): Chinese.
        # 
        # - **en-US**: English.
        self.accept_language = accept_language
        # The number of Simple Application Server instances to create. Valid values: 1 to 20.
        # 
        # Default value: 1.
        self.amount = amount
        # The resource type. Valid values:
        # - Server.
        # 
        # This parameter is required.
        self.commodity_type = commodity_type
        # The capacity of the mounted data cloud disk. Unit: GB. Valid values: 0 to 16380. The value must be a multiple of 20.
        self.data_disk_size = data_disk_size
        # The ID of the Simple Application Server instance.
        self.instance_id = instance_id
        # The order type. Valid values:
        # - Buy.
        # 
        # Default value: Buy.
        self.order_type = order_type
        # The billing method of the instance. Valid values:
        # - Prepaid: subscription.
        # 
        # Example: Prepaid.
        self.pay_type = pay_type
        # The billing duration. Valid values:
        # - If the PriceUnit parameter is set to Month: 1 to 9.
        # - If the PriceUnit parameter is set to Year: 1 to 5.
        # 
        # Default value: 1.
        self.period = period
        # The plan ID. You can call the [ListPlans](https://help.aliyun.com/document_detail/189314.html) operation to query all plan information in the specified region.
        self.plan_id = plan_id
        # The pricing unit. Valid values:
        # - Month: the pricing unit for monthly billing.
        # - Year: the pricing unit for yearly billing.
        # 
        # Default value: Month.
        self.price_unit = price_unit
        # The promotion option information.
        self.promotion_options = promotion_options
        # The region ID of the specified Simple Application Server instance. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the list of supported Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.promotion_options:
            self.promotion_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.period is not None:
            result['Period'] = self.period

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit

        if self.promotion_options is not None:
            result['PromotionOptions'] = self.promotion_options.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')

        if m.get('PromotionOptions') is not None:
            temp_model = main_models.DescribePriceRequestPromotionOptions()
            self.promotion_options = temp_model.from_map(m.get('PromotionOptions'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribePriceRequestPromotionOptions(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        coupon_no: str = None,
    ):
        # The activity ID.
        self.activity_id = activity_id
        # The coupon code.
        self.coupon_no = coupon_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.coupon_no is not None:
            result['CouponNo'] = self.coupon_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('CouponNo') is not None:
            self.coupon_no = m.get('CouponNo')

        return self

