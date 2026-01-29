# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceUsageDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeResourceUsageDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            temp_model = main_models.DescribeResourceUsageDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeResourceUsageDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeResourceUsageDetailResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The data entries.
        self.items = items
        # The number of entries returned on the current page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The total number of entries returned.
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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeResourceUsageDetailResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeResourceUsageDetailResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        capacity_unit: str = None,
        currency: str = None,
        deduct_quantity: float = None,
        end_time: str = None,
        image_type: str = None,
        instance_spec: str = None,
        postpaid_cost: str = None,
        potential_saved_cost: str = None,
        quantity: int = None,
        region: str = None,
        region_no: str = None,
        reservation_cost: str = None,
        resource_instance_id: str = None,
        saved_cost: str = None,
        start_time: str = None,
        status: str = None,
        status_name: str = None,
        total_quantity: float = None,
        usage_percentage: float = None,
        user_id: str = None,
        user_name: str = None,
        zone: str = None,
        zone_name: str = None,
    ):
        # The unit that is used to measure the resources that are deducted.
        self.capacity_unit = capacity_unit
        # The type of the currency.
        self.currency = currency
        # The amount of the deducted resources.
        self.deduct_quantity = deduct_quantity
        # The end of the time range in which the usage details were queried.
        self.end_time = end_time
        # The operating system.
        self.image_type = image_type
        # The instance type.
        self.instance_spec = instance_spec
        # The equivalent of pay-as-you-go costs.
        self.postpaid_cost = postpaid_cost
        # The potential net savings.
        self.potential_saved_cost = potential_saved_cost
        # The number of deduction plans.
        self.quantity = quantity
        # The region.
        self.region = region
        # The code of the region.
        self.region_no = region_no
        # The fee of the deduction plan.
        self.reservation_cost = reservation_cost
        # The ID of the deduction plan.
        self.resource_instance_id = resource_instance_id
        # The net savings.
        self.saved_cost = saved_cost
        # The beginning of the time range in which the usage details were queried.
        self.start_time = start_time
        # The status of the deduction plan.
        self.status = status
        # The name of the status.
        self.status_name = status_name
        # The total capacity of the deduction plan.
        self.total_quantity = total_quantity
        # The usage rate of the deduction plan.
        self.usage_percentage = usage_percentage
        # The account ID.
        self.user_id = user_id
        # The username of the account.
        self.user_name = user_name
        # The zone.
        self.zone = zone
        # The code of the zone.
        self.zone_name = zone_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_unit is not None:
            result['CapacityUnit'] = self.capacity_unit

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deduct_quantity is not None:
            result['DeductQuantity'] = self.deduct_quantity

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.postpaid_cost is not None:
            result['PostpaidCost'] = self.postpaid_cost

        if self.potential_saved_cost is not None:
            result['PotentialSavedCost'] = self.potential_saved_cost

        if self.quantity is not None:
            result['Quantity'] = self.quantity

        if self.region is not None:
            result['Region'] = self.region

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.reservation_cost is not None:
            result['ReservationCost'] = self.reservation_cost

        if self.resource_instance_id is not None:
            result['ResourceInstanceId'] = self.resource_instance_id

        if self.saved_cost is not None:
            result['SavedCost'] = self.saved_cost

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_name is not None:
            result['StatusName'] = self.status_name

        if self.total_quantity is not None:
            result['TotalQuantity'] = self.total_quantity

        if self.usage_percentage is not None:
            result['UsagePercentage'] = self.usage_percentage

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.zone is not None:
            result['Zone'] = self.zone

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityUnit') is not None:
            self.capacity_unit = m.get('CapacityUnit')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductQuantity') is not None:
            self.deduct_quantity = m.get('DeductQuantity')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('PostpaidCost') is not None:
            self.postpaid_cost = m.get('PostpaidCost')

        if m.get('PotentialSavedCost') is not None:
            self.potential_saved_cost = m.get('PotentialSavedCost')

        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('ReservationCost') is not None:
            self.reservation_cost = m.get('ReservationCost')

        if m.get('ResourceInstanceId') is not None:
            self.resource_instance_id = m.get('ResourceInstanceId')

        if m.get('SavedCost') is not None:
            self.saved_cost = m.get('SavedCost')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusName') is not None:
            self.status_name = m.get('StatusName')

        if m.get('TotalQuantity') is not None:
            self.total_quantity = m.get('TotalQuantity')

        if m.get('UsagePercentage') is not None:
            self.usage_percentage = m.get('UsagePercentage')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

