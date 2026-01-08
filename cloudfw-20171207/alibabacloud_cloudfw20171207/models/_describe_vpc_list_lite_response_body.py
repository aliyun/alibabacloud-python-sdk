# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcListLiteResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        vpc_list: List[main_models.DescribeVpcListLiteResponseBodyVpcList] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The information about the VPCs.
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['VpcList'] = []
        if self.vpc_list is not None:
            for k1 in self.vpc_list:
                result['VpcList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k1 in m.get('VpcList'):
                temp_model = main_models.DescribeVpcListLiteResponseBodyVpcList()
                self.vpc_list.append(temp_model.from_map(k1))

        return self

class DescribeVpcListLiteResponseBodyVpcList(DaraModel):
    def __init__(
        self,
        region_no: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        # The region ID of the VPC.
        self.region_no = region_no
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The name of the VPC.
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

