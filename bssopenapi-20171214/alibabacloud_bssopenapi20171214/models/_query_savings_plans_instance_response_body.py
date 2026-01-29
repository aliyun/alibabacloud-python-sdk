# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QuerySavingsPlansInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QuerySavingsPlansInstanceResponseBodyData = None,
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
            temp_model = main_models.QuerySavingsPlansInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySavingsPlansInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.QuerySavingsPlansInstanceResponseBodyDataItems] = None,
        page_num: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The details about the instances.
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
                temp_model = main_models.QuerySavingsPlansInstanceResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QuerySavingsPlansInstanceResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        allocation_status: str = None,
        commodity_code: str = None,
        currency: str = None,
        current_pool_value: str = None,
        cycle: str = None,
        deduct_cycle_type: str = None,
        end_time: str = None,
        end_timestamp: int = None,
        instance_family: str = None,
        instance_id: str = None,
        last_bill_total_usage: str = None,
        last_bill_utilization: str = None,
        pay_mode: str = None,
        pool_value: str = None,
        prepay_fee: str = None,
        region: str = None,
        rest_pool_value: str = None,
        savings_type: str = None,
        start_time: str = None,
        start_timestamp: int = None,
        status: str = None,
        tags: List[main_models.QuerySavingsPlansInstanceResponseBodyDataItemsTags] = None,
        total_save: str = None,
        utilization: str = None,
    ):
        # The allocation status. Valid values:
        # 
        # *   unallocated
        # *   allocated
        # *   beAllocated
        self.allocation_status = allocation_status
        self.commodity_code = commodity_code
        # The currency. Valid values: CNY and USD.
        self.currency = currency
        self.current_pool_value = current_pool_value
        self.cycle = cycle
        self.deduct_cycle_type = deduct_cycle_type
        # The time when the instance expires. The time is in the format of yyyy-MM-dd HH:mm:ss.
        self.end_time = end_time
        self.end_timestamp = end_timestamp
        # The instance family information. For an instance of the Elastic Compute Service (ECS) compute type, the value indicates the ECS instance family or the ECS instance family package.
        self.instance_family = instance_family
        # The ID of the savings plan instance.
        self.instance_id = instance_id
        self.last_bill_total_usage = last_bill_total_usage
        self.last_bill_utilization = last_bill_utilization
        # The payment type. Valid values:
        # 
        # *   total: All Upfront
        # *   half: Partial Upfront
        # *   zero: No Upfront
        self.pay_mode = pay_mode
        # The commitment.
        self.pool_value = pool_value
        # The prepaid amount.
        self.prepay_fee = prepay_fee
        # The region.
        self.region = region
        self.rest_pool_value = rest_pool_value
        # The type of the savings plan. Valid values:
        # 
        # *   universal: general-purpose
        # *   ecs: ECS compute
        self.savings_type = savings_type
        # The time when the instance takes effect. The time is in the format of yyyy-MM-dd HH:mm:ss.
        self.start_time = start_time
        self.start_timestamp = start_timestamp
        # The status of the instance. Valid values:
        # 
        # *   NORMAL: normal
        # *   LIMIT: stopped due to overdue payment
        # *   RELEASE: released
        self.status = status
        # The details about the tags.
        self.tags = tags
        # The total amount that is saved.
        self.total_save = total_save
        # The total usage.
        self.utilization = utilization

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_status is not None:
            result['AllocationStatus'] = self.allocation_status

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.current_pool_value is not None:
            result['CurrentPoolValue'] = self.current_pool_value

        if self.cycle is not None:
            result['Cycle'] = self.cycle

        if self.deduct_cycle_type is not None:
            result['DeductCycleType'] = self.deduct_cycle_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.instance_family is not None:
            result['InstanceFamily'] = self.instance_family

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_bill_total_usage is not None:
            result['LastBillTotalUsage'] = self.last_bill_total_usage

        if self.last_bill_utilization is not None:
            result['LastBillUtilization'] = self.last_bill_utilization

        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode

        if self.pool_value is not None:
            result['PoolValue'] = self.pool_value

        if self.prepay_fee is not None:
            result['PrepayFee'] = self.prepay_fee

        if self.region is not None:
            result['Region'] = self.region

        if self.rest_pool_value is not None:
            result['RestPoolValue'] = self.rest_pool_value

        if self.savings_type is not None:
            result['SavingsType'] = self.savings_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.total_save is not None:
            result['TotalSave'] = self.total_save

        if self.utilization is not None:
            result['Utilization'] = self.utilization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStatus') is not None:
            self.allocation_status = m.get('AllocationStatus')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('CurrentPoolValue') is not None:
            self.current_pool_value = m.get('CurrentPoolValue')

        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        if m.get('DeductCycleType') is not None:
            self.deduct_cycle_type = m.get('DeductCycleType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('InstanceFamily') is not None:
            self.instance_family = m.get('InstanceFamily')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastBillTotalUsage') is not None:
            self.last_bill_total_usage = m.get('LastBillTotalUsage')

        if m.get('LastBillUtilization') is not None:
            self.last_bill_utilization = m.get('LastBillUtilization')

        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')

        if m.get('PoolValue') is not None:
            self.pool_value = m.get('PoolValue')

        if m.get('PrepayFee') is not None:
            self.prepay_fee = m.get('PrepayFee')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RestPoolValue') is not None:
            self.rest_pool_value = m.get('RestPoolValue')

        if m.get('SavingsType') is not None:
            self.savings_type = m.get('SavingsType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.QuerySavingsPlansInstanceResponseBodyDataItemsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TotalSave') is not None:
            self.total_save = m.get('TotalSave')

        if m.get('Utilization') is not None:
            self.utilization = m.get('Utilization')

        return self

class QuerySavingsPlansInstanceResponseBodyDataItemsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

