# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QuerySavingsPlansDeductLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QuerySavingsPlansDeductLogResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The return data.
        self.data = data
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.QuerySavingsPlansDeductLogResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySavingsPlansDeductLogResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.QuerySavingsPlansDeductLogResponseBodyDataItems] = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The deduction details.
        self.items = items
        # The page number of the returned page.
        self.page_num = page_num
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.QuerySavingsPlansDeductLogResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QuerySavingsPlansDeductLogResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        bill_module: str = None,
        billing_cycle: str = None,
        billing_official_price: str = None,
        deduct_commodity: str = None,
        deduct_fee: str = None,
        deduct_instance_id: str = None,
        deduct_rate: str = None,
        deducted_official_price: str = None,
        discount_rate: str = None,
        end_time: str = None,
        instance_id: str = None,
        instance_spec: str = None,
        instance_type_family: str = None,
        owner_id: int = None,
        region: str = None,
        savings_type: str = None,
        start_time: str = None,
        user_id: int = None,
    ):
        # The billable item for which the fee is deducted.
        self.bill_module = bill_module
        self.billing_cycle = billing_cycle
        self.billing_official_price = billing_official_price
        # The service for which the fee is deducted.
        self.deduct_commodity = deduct_commodity
        # The deducted amount.
        self.deduct_fee = deduct_fee
        # The ID of the instance for which the fee is deducted.
        self.deduct_instance_id = deduct_instance_id
        # The deduction rate.
        self.deduct_rate = deduct_rate
        self.deducted_official_price = deducted_official_price
        # The discount used for the current deduction.
        self.discount_rate = discount_rate
        # The end of the billing cycle for which the fee is deducted.
        self.end_time = end_time
        # The ID of the savings plan instance.
        self.instance_id = instance_id
        self.instance_spec = instance_spec
        self.instance_type_family = instance_type_family
        self.owner_id = owner_id
        self.region = region
        # The type of the savings plan. Valid values:
        # 
        # *   universal: general-purpose
        # *   ecs: ECS compute
        self.savings_type = savings_type
        # The beginning of the billing cycle for which the fee is deducted. The time is in the format of yyyy-MM-dd HH:mm:ss.
        self.start_time = start_time
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bill_module is not None:
            result['BillModule'] = self.bill_module

        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle

        if self.billing_official_price is not None:
            result['BillingOfficialPrice'] = self.billing_official_price

        if self.deduct_commodity is not None:
            result['DeductCommodity'] = self.deduct_commodity

        if self.deduct_fee is not None:
            result['DeductFee'] = self.deduct_fee

        if self.deduct_instance_id is not None:
            result['DeductInstanceId'] = self.deduct_instance_id

        if self.deduct_rate is not None:
            result['DeductRate'] = self.deduct_rate

        if self.deducted_official_price is not None:
            result['DeductedOfficialPrice'] = self.deducted_official_price

        if self.discount_rate is not None:
            result['DiscountRate'] = self.discount_rate

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.savings_type is not None:
            result['SavingsType'] = self.savings_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillModule') is not None:
            self.bill_module = m.get('BillModule')

        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')

        if m.get('BillingOfficialPrice') is not None:
            self.billing_official_price = m.get('BillingOfficialPrice')

        if m.get('DeductCommodity') is not None:
            self.deduct_commodity = m.get('DeductCommodity')

        if m.get('DeductFee') is not None:
            self.deduct_fee = m.get('DeductFee')

        if m.get('DeductInstanceId') is not None:
            self.deduct_instance_id = m.get('DeductInstanceId')

        if m.get('DeductRate') is not None:
            self.deduct_rate = m.get('DeductRate')

        if m.get('DeductedOfficialPrice') is not None:
            self.deducted_official_price = m.get('DeductedOfficialPrice')

        if m.get('DiscountRate') is not None:
            self.discount_rate = m.get('DiscountRate')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SavingsType') is not None:
            self.savings_type = m.get('SavingsType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

