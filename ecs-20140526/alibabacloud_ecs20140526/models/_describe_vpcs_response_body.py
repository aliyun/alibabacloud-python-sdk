# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpcs: main_models.DescribeVpcsResponseBodyVpcs = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vpcs = vpcs

    def validate(self):
        if self.vpcs:
            self.vpcs.validate()

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vpcs is not None:
            result['Vpcs'] = self.vpcs.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Vpcs') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcs()
            self.vpcs = temp_model.from_map(m.get('Vpcs'))

        return self

class DescribeVpcsResponseBodyVpcs(DaraModel):
    def __init__(
        self,
        vpc: List[main_models.DescribeVpcsResponseBodyVpcsVpc] = None,
    ):
        self.vpc = vpc

    def validate(self):
        if self.vpc:
            for v1 in self.vpc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Vpc'] = []
        if self.vpc is not None:
            for k1 in self.vpc:
                result['Vpc'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vpc = []
        if m.get('Vpc') is not None:
            for k1 in m.get('Vpc'):
                temp_model = main_models.DescribeVpcsResponseBodyVpcsVpc()
                self.vpc.append(temp_model.from_map(k1))

        return self

class DescribeVpcsResponseBodyVpcsVpc(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        creation_time: str = None,
        description: str = None,
        is_default: bool = None,
        region_id: str = None,
        status: str = None,
        user_cidrs: main_models.DescribeVpcsResponseBodyVpcsVpcUserCidrs = None,
        vrouter_id: str = None,
        v_switch_ids: main_models.DescribeVpcsResponseBodyVpcsVpcVSwitchIds = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.creation_time = creation_time
        self.description = description
        self.is_default = is_default
        self.region_id = region_id
        self.status = status
        self.user_cidrs = user_cidrs
        self.vrouter_id = vrouter_id
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        if self.user_cidrs:
            self.user_cidrs.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_cidrs is not None:
            result['UserCidrs'] = self.user_cidrs.to_map()

        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserCidrs') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcUserCidrs()
            self.user_cidrs = temp_model.from_map(m.get('UserCidrs'))

        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.DescribeVpcsResponseBodyVpcsVpcVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcsResponseBodyVpcsVpcVSwitchIds(DaraModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeVpcsResponseBodyVpcsVpcUserCidrs(DaraModel):
    def __init__(
        self,
        user_cidr: List[str] = None,
    ):
        self.user_cidr = user_cidr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_cidr is not None:
            result['UserCidr'] = self.user_cidr

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserCidr') is not None:
            self.user_cidr = m.get('UserCidr')

        return self

