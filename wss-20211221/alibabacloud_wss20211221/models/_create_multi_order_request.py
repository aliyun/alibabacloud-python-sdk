# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class CreateMultiOrderRequest(DaraModel):
    def __init__(
        self,
        channel_cookie: str = None,
        order_items: List[main_models.CreateMultiOrderRequestOrderItems] = None,
        order_type: str = None,
        properties: Dict[str, str] = None,
        reseller_owner_uid: int = None,
    ):
        # The channel cookie information.
        self.channel_cookie = channel_cookie
        # The product information.
        self.order_items = order_items
        # The order type.
        self.order_type = order_type
        # The extended properties.
        self.properties = properties
        # The UID of the reseller owner.
        self.reseller_owner_uid = reseller_owner_uid

    def validate(self):
        if self.order_items:
            for v1 in self.order_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel_cookie is not None:
            result['ChannelCookie'] = self.channel_cookie

        result['OrderItems'] = []
        if self.order_items is not None:
            for k1 in self.order_items:
                result['OrderItems'].append(k1.to_map() if k1 else None)

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.properties is not None:
            result['Properties'] = self.properties

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelCookie') is not None:
            self.channel_cookie = m.get('ChannelCookie')

        self.order_items = []
        if m.get('OrderItems') is not None:
            for k1 in m.get('OrderItems'):
                temp_model = main_models.CreateMultiOrderRequestOrderItems()
                self.order_items.append(temp_model.from_map(k1))

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Properties') is not None:
            self.properties = m.get('Properties')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        return self

class CreateMultiOrderRequestOrderItems(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_pay: bool = None,
        auto_renew: bool = None,
        buy_change: bool = None,
        components: List[main_models.CreateMultiOrderRequestOrderItemsComponents] = None,
        instance_ids: List[str] = None,
        paid_call_back_url: str = None,
        period: int = None,
        period_unit: str = None,
        promotion_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        # The quantity to purchase.
        self.amount = amount
        # Specifies whether to enable automatic payment.
        self.auto_pay = auto_pay
        # Specifies whether to enable auto-renewal.
        self.auto_renew = auto_renew
        # Specifies whether this is a change purchase.
        self.buy_change = buy_change
        # The product modules.
        self.components = components
        # The list of instance IDs.
        self.instance_ids = instance_ids
        # The callback URL after the payment is completed.
        self.paid_call_back_url = paid_call_back_url
        # The subscription duration. Valid values:
        # 
        # - If PeriodUnit is set to Year: 1, 2, 3, and 5.
        # 
        # - If PeriodUnit is set to Month: 1, 2, 3, and 6.
        self.period = period
        # The unit of the subscription duration for a subscription instance.
        # 
        # > This parameter is required only when the billing method of the instance is subscription. This parameter is case-sensitive. Make sure that the value is spelled correctly.
        self.period_unit = period_unit
        # The promotion ID.
        self.promotion_id = promotion_id
        # The list of resource IDs.
        # > For monthly duration packages, this parameter corresponds to the cloud desktop ID. This parameter is required when OrderType is not set to `create`.
        self.resource_ids = resource_ids
        # The resource type.
        # > This parameter is case-sensitive. Make sure that the value is spelled correctly.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

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

        if self.buy_change is not None:
            result['BuyChange'] = self.buy_change

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.paid_call_back_url is not None:
            result['PaidCallBackUrl'] = self.paid_call_back_url

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('BuyChange') is not None:
            self.buy_change = m.get('BuyChange')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.CreateMultiOrderRequestOrderItemsComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PaidCallBackUrl') is not None:
            self.paid_call_back_url = m.get('PaidCallBackUrl')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self



class CreateMultiOrderRequestOrderItemsComponents(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the module.
        self.key = key
        # The value of the module.
        # 
        # The following section describes the sample values and valid values for each key of the Enterprise Edition monthly duration package:
        # 
        # - RegionId: ap-southeast-1
        # - InstanceType: eds.enterprise_office.4c8g
        # - DurationType (hours): Valid values: 
        #    - 120
        #    - 250
        # - OsType: Valid values: 
        #    - Windows
        #    - Linux
        # - RootDiskSize (GiB): 80
        # - RootDiskCategory: Valid values: 
        #    - cloud_efficiency (ultra cloud disk)
        #    - cloud_auto (ultra-fast cloud disk)
        #    - cloud_essd (enhanced standard SSD. Only specific instance types support this value.)
        # - RootPerformanceLevel: Valid values: 
        #    - PL0
        #    - PL1
        #    - PL2
        #    - PL3
        # - DataDiskSize (GiB): Valid values are the same as those of RootDiskSize.
        # - DataDiskCategory: Valid values are the same as those of RootDiskCategory.
        # - DataPerformanceLevel: Valid values are the same as those of RootPerformanceLevel.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

