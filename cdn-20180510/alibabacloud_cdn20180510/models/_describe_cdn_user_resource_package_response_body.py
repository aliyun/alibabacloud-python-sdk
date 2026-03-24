# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnUserResourcePackageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_package_infos: main_models.DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        self.resource_package_infos = resource_package_infos

    def validate(self):
        if self.resource_package_infos:
            self.resource_package_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_package_infos is not None:
            result['ResourcePackageInfos'] = self.resource_package_infos.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourcePackageInfos') is not None:
            temp_model = main_models.DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m.get('ResourcePackageInfos'))

        return self

class DescribeCdnUserResourcePackageResponseBodyResourcePackageInfos(DaraModel):
    def __init__(
        self,
        resource_package_info: List[main_models.DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo] = None,
    ):
        self.resource_package_info = resource_package_info

    def validate(self):
        if self.resource_package_info:
            for v1 in self.resource_package_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ResourcePackageInfo'] = []
        if self.resource_package_info is not None:
            for k1 in self.resource_package_info:
                result['ResourcePackageInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource_package_info = []
        if m.get('ResourcePackageInfo') is not None:
            for k1 in m.get('ResourcePackageInfo'):
                temp_model = main_models.DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k1))

        return self

class DescribeCdnUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(DaraModel):
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
        self.commodity_code = commodity_code
        self.curr_capacity = curr_capacity
        self.curr_capacity_base_unit = curr_capacity_base_unit
        self.curr_capacity_show_unit = curr_capacity_show_unit
        self.curr_capacity_show_value = curr_capacity_show_value
        self.display_name = display_name
        self.end_time = end_time
        self.init_capacity = init_capacity
        self.init_capacity_base_unit = init_capacity_base_unit
        self.init_capacity_show_unit = init_capacity_show_unit
        self.init_capacity_show_value = init_capacity_show_value
        self.instance_id = instance_id
        self.region = region
        self.start_time = start_time
        self.status = status
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

