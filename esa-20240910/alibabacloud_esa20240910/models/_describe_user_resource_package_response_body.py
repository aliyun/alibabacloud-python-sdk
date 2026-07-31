# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class DescribeUserResourcePackageResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        resource_package_infos: List[main_models.DescribeUserResourcePackageResponseBodyResourcePackageInfos] = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The array of ResourcePackageInfo objects.
        self.resource_package_infos = resource_package_infos
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.resource_package_infos:
            for v1 in self.resource_package_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResourcePackageInfos'] = []
        if self.resource_package_infos is not None:
            for k1 in self.resource_package_infos:
                result['ResourcePackageInfos'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resource_package_infos = []
        if m.get('ResourcePackageInfos') is not None:
            for k1 in m.get('ResourcePackageInfos'):
                temp_model = main_models.DescribeUserResourcePackageResponseBodyResourcePackageInfos()
                self.resource_package_infos.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeUserResourcePackageResponseBodyResourcePackageInfos(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        curr_capacity: str = None,
        curr_capacity_base_unit: str = None,
        curr_capacity_show_unit: str = None,
        curr_capacity_show_value: str = None,
        display_name: str = None,
        end_time: str = None,
        init_capacity: str = None,
        init_capacity_base_unit: str = None,
        init_capacity_show_unit: str = None,
        init_capacity_show_value: str = None,
        instance_id: str = None,
        region: str = None,
        start_time: str = None,
        status: str = None,
        template_name: str = None,
    ):
        # The commodity code of the resource plan.
        self.commodity_code = commodity_code
        # The current remaining capacity of the instance.
        # - Unit for traffic plans: bytes.
        # 
        # - Unit for request plans: count.
        self.curr_capacity = curr_capacity
        # The base unit of the current remaining capacity of the instance.
        self.curr_capacity_base_unit = curr_capacity_base_unit
        # The display unit of the current remaining capacity of the instance.
        self.curr_capacity_show_unit = curr_capacity_show_unit
        # The display value of the current remaining capacity of the instance.
        self.curr_capacity_show_value = curr_capacity_show_value
        # The name of the resource plan.
        self.display_name = display_name
        # The expiration time.
        self.end_time = end_time
        # The total capacity of the resource plan.
        # - Unit for traffic plans: bytes.
        # 
        # - Unit for request plans: count.
        self.init_capacity = init_capacity
        # The base unit of the total capacity of the resource plan.
        self.init_capacity_base_unit = init_capacity_base_unit
        # The display unit of the total capacity of the resource plan.
        self.init_capacity_show_unit = init_capacity_show_unit
        # The display value of the total capacity of the resource plan.
        self.init_capacity_show_value = init_capacity_show_value
        # The resource plan instance ID.
        self.instance_id = instance_id
        # The region.
        self.region = region
        # The effective period.
        self.start_time = start_time
        # The status of the resource plan.
        self.status = status
        # The template name.
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity

        if self.curr_capacity_base_unit is not None:
            result['CurrCapacityBaseUnit'] = self.curr_capacity_base_unit

        if self.curr_capacity_show_unit is not None:
            result['CurrCapacityShowUnit'] = self.curr_capacity_show_unit

        if self.curr_capacity_show_value is not None:
            result['CurrCapacityShowValue'] = self.curr_capacity_show_value

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity

        if self.init_capacity_base_unit is not None:
            result['InitCapacityBaseUnit'] = self.init_capacity_base_unit

        if self.init_capacity_show_unit is not None:
            result['InitCapacityShowUnit'] = self.init_capacity_show_unit

        if self.init_capacity_show_value is not None:
            result['InitCapacityShowValue'] = self.init_capacity_show_value

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')

        if m.get('CurrCapacityBaseUnit') is not None:
            self.curr_capacity_base_unit = m.get('CurrCapacityBaseUnit')

        if m.get('CurrCapacityShowUnit') is not None:
            self.curr_capacity_show_unit = m.get('CurrCapacityShowUnit')

        if m.get('CurrCapacityShowValue') is not None:
            self.curr_capacity_show_value = m.get('CurrCapacityShowValue')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')

        if m.get('InitCapacityBaseUnit') is not None:
            self.init_capacity_base_unit = m.get('InitCapacityBaseUnit')

        if m.get('InitCapacityShowUnit') is not None:
            self.init_capacity_show_unit = m.get('InitCapacityShowUnit')

        if m.get('InitCapacityShowValue') is not None:
            self.init_capacity_show_value = m.get('InitCapacityShowValue')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

