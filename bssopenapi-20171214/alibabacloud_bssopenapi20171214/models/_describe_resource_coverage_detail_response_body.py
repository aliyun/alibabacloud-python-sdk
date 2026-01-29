# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceCoverageDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeResourceCoverageDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The returned data.
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
            temp_model = main_models.DescribeResourceCoverageDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeResourceCoverageDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeResourceCoverageDetailResponseBodyDataItems] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The data entries.
        self.items = items
        # The number of entries returned on the current page.
        self.max_results = max_results
        # The token of the next page.
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
                temp_model = main_models.DescribeResourceCoverageDetailResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeResourceCoverageDetailResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        capacity_unit: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        coverage_percentage: float = None,
        currency: str = None,
        deduct_quantity: float = None,
        end_time: str = None,
        instance_id: str = None,
        instance_spec: str = None,
        payment_amount: float = None,
        product_code: str = None,
        product_name: str = None,
        region: str = None,
        region_no: str = None,
        start_time: str = None,
        total_quantity: float = None,
        user_id: str = None,
        user_name: str = None,
        zone: str = None,
        zone_name: str = None,
    ):
        # The unit that is used to measure the resources deducted from deduction plans.
        self.capacity_unit = capacity_unit
        # The code of the service.
        self.commodity_code = commodity_code
        # The name and billing method of the service.
        self.commodity_name = commodity_name
        # The coverage rate of a deduction plan.
        self.coverage_percentage = coverage_percentage
        # The currency in which deduction plans were priced.
        self.currency = currency
        # The amount of the resources deducted from a deduction plan.
        self.deduct_quantity = deduct_quantity
        # The end of the time range in which the coverage details were queried.
        self.end_time = end_time
        # The ID of a pay-as-you-go instance.
        self.instance_id = instance_id
        # The specifications of a deduction plan.
        self.instance_spec = instance_spec
        # The amount of the bill.
        self.payment_amount = payment_amount
        # The code of the service.
        self.product_code = product_code
        # The name of the service.
        self.product_name = product_name
        # The region.
        self.region = region
        # The code of the region.
        self.region_no = region_no
        # The beginning of the time range in which the coverage details were queried.
        self.start_time = start_time
        # The total amount of resources consumed.
        self.total_quantity = total_quantity
        # The ID of the account.
        self.user_id = user_id
        # The username of the account.
        self.user_name = user_name
        # The code of the zone.
        self.zone = zone
        # The zone.
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

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.coverage_percentage is not None:
            result['CoveragePercentage'] = self.coverage_percentage

        if self.currency is not None:
            result['Currency'] = self.currency

        if self.deduct_quantity is not None:
            result['DeductQuantity'] = self.deduct_quantity

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec

        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.region is not None:
            result['Region'] = self.region

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.total_quantity is not None:
            result['TotalQuantity'] = self.total_quantity

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

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('CoveragePercentage') is not None:
            self.coverage_percentage = m.get('CoveragePercentage')

        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('DeductQuantity') is not None:
            self.deduct_quantity = m.get('DeductQuantity')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')

        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TotalQuantity') is not None:
            self.total_quantity = m.get('TotalQuantity')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

