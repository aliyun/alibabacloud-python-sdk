# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkInstanceListResponseBody(DaraModel):
    def __init__(
        self,
        network_instance_list: List[main_models.DescribeNetworkInstanceListResponseBodyNetworkInstanceList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.network_instance_list = network_instance_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.network_instance_list:
            for v1 in self.network_instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkInstanceList'] = []
        if self.network_instance_list is not None:
            for k1 in self.network_instance_list:
                result['NetworkInstanceList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_instance_list = []
        if m.get('NetworkInstanceList') is not None:
            for k1 in m.get('NetworkInstanceList'):
                temp_model = main_models.DescribeNetworkInstanceListResponseBodyNetworkInstanceList()
                self.network_instance_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNetworkInstanceListResponseBodyNetworkInstanceList(DaraModel):
    def __init__(
        self,
        network_instance_id: str = None,
        network_instance_name: str = None,
        network_instance_type: str = None,
        region_no: str = None,
    ):
        self.network_instance_id = network_instance_id
        self.network_instance_name = network_instance_name
        self.network_instance_type = network_instance_type
        self.region_no = region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_instance_id is not None:
            result['NetworkInstanceId'] = self.network_instance_id

        if self.network_instance_name is not None:
            result['NetworkInstanceName'] = self.network_instance_name

        if self.network_instance_type is not None:
            result['NetworkInstanceType'] = self.network_instance_type

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInstanceId') is not None:
            self.network_instance_id = m.get('NetworkInstanceId')

        if m.get('NetworkInstanceName') is not None:
            self.network_instance_name = m.get('NetworkInstanceName')

        if m.get('NetworkInstanceType') is not None:
            self.network_instance_type = m.get('NetworkInstanceType')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        return self

