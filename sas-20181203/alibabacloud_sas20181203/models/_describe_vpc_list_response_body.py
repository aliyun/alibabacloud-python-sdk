# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcListResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        request_id: str = None,
        vpc_list: List[main_models.DescribeVpcListResponseBodyVpcList] = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of VPCs.
        self.vpc_list = vpc_list

    def validate(self):
        if self.vpc_list:
            for v1 in self.vpc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VpcList'] = []
        if self.vpc_list is not None:
            for k1 in self.vpc_list:
                result['VpcList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k1 in m.get('VpcList'):
                temp_model = main_models.DescribeVpcListResponseBodyVpcList()
                self.vpc_list.append(temp_model.from_map(k1))

        return self

class DescribeVpcListResponseBodyVpcList(DaraModel):
    def __init__(
        self,
        ecs_count: int = None,
        instance_desc: str = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The number of Elastic Compute Service (ECS) instances.
        self.ecs_count = ecs_count
        # The information about the virtual private cloud (VPC).
        self.instance_desc = instance_desc
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the VPC.
        self.instance_name = instance_name
        # The region in which the server resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.instance_desc is not None:
            result['InstanceDesc'] = self.instance_desc

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('InstanceDesc') is not None:
            self.instance_desc = m.get('InstanceDesc')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

