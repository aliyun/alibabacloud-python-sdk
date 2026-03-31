# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeHybridCloudGroupsResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.DescribeHybridCloudGroupsResponseBodyGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The node groups.
        self.groups = groups
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.DescribeHybridCloudGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeHybridCloudGroupsResponseBodyGroups(DaraModel):
    def __init__(
        self,
        back_source_mark: str = None,
        continents_value: int = None,
        group_id: int = None,
        group_name: str = None,
        group_type: str = None,
        load_balance_ip: str = None,
        location_id: int = None,
        operator_value: int = None,
        ports: str = None,
        region_code_value: int = None,
        remark: str = None,
    ):
        # The back-to-origin mark of the protected cluster. The value is in the {ISP name}-{Continent name}-{City name}-{Back-to-origin identifier} format. The back-to-origin identifier is optional.
        # 
        # >  For more information about ISP names, continent names, city names, and back-to-origin identifiers, see the following sections.
        self.back_source_mark = back_source_mark
        # The continent code of the protected cluster.
        # 
        # >  For more information about continent codes, see Continent codes in this topic.
        self.continents_value = continents_value
        # The ID of the node group.
        self.group_id = group_id
        # The name of the node group.
        self.group_name = group_name
        # The type of the node group. Valid values:
        # 
        # *   **protect**
        # *   **control**
        # *   **storage**
        # *   **controlStorage**
        self.group_type = group_type
        # The IP address of the server used for load balancing.
        self.load_balance_ip = load_balance_ip
        # The ID of the protection node.
        self.location_id = location_id
        # The ISP code of the protected cluster.
        # 
        # >  For more information about ISP codes, see ISP codes in this topic.
        self.operator_value = operator_value
        # The port that is used by the hybrid cloud cluster. The value of this parameter is a string. If multiple ports are returned, the value is in the **port1,port2,port3** format.
        self.ports = ports
        # The city code of the protected cluster.
        # 
        # >  For more information about city codes, see City codes in this topic.
        self.region_code_value = region_code_value
        # The description of the node group.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.back_source_mark is not None:
            result['BackSourceMark'] = self.back_source_mark

        if self.continents_value is not None:
            result['ContinentsValue'] = self.continents_value

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.load_balance_ip is not None:
            result['LoadBalanceIp'] = self.load_balance_ip

        if self.location_id is not None:
            result['LocationId'] = self.location_id

        if self.operator_value is not None:
            result['OperatorValue'] = self.operator_value

        if self.ports is not None:
            result['Ports'] = self.ports

        if self.region_code_value is not None:
            result['RegionCodeValue'] = self.region_code_value

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackSourceMark') is not None:
            self.back_source_mark = m.get('BackSourceMark')

        if m.get('ContinentsValue') is not None:
            self.continents_value = m.get('ContinentsValue')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('LoadBalanceIp') is not None:
            self.load_balance_ip = m.get('LoadBalanceIp')

        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

        if m.get('OperatorValue') is not None:
            self.operator_value = m.get('OperatorValue')

        if m.get('Ports') is not None:
            self.ports = m.get('Ports')

        if m.get('RegionCodeValue') is not None:
            self.region_code_value = m.get('RegionCodeValue')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

