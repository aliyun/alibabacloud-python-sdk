# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class DescribeVsUserResourcePackageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_package_infos: main_models.DescribeVsUserResourcePackageResponseBodyResourcePackageInfos = None,
    ):
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
            temp_model = main_models.DescribeVsUserResourcePackageResponseBodyResourcePackageInfos()
            self.resource_package_infos = temp_model.from_map(m.get('ResourcePackageInfos'))

        return self

class DescribeVsUserResourcePackageResponseBodyResourcePackageInfos(DaraModel):
    def __init__(
        self,
        resource_package_info: List[main_models.DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo] = None,
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
                temp_model = main_models.DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo()
                self.resource_package_info.append(temp_model.from_map(k1))

        return self

class DescribeVsUserResourcePackageResponseBodyResourcePackageInfosResourcePackageInfo(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        curr_capacity: str = None,
        display_name: str = None,
        init_capacity: str = None,
        instance_id: str = None,
        status: str = None,
    ):
        self.commodity_code = commodity_code
        self.curr_capacity = curr_capacity
        self.display_name = display_name
        self.init_capacity = init_capacity
        self.instance_id = instance_id
        self.status = status

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

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

