# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class ListVpcInfoByInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpc_infos: List[main_models.ListVpcInfoByInstanceResponseBodyVpcInfos] = None,
    ):
        self.instance_name = instance_name
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vpc_infos = vpc_infos

    def validate(self):
        if self.vpc_infos:
            for v1 in self.vpc_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VpcInfos'] = []
        if self.vpc_infos is not None:
            for k1 in self.vpc_infos:
                result['VpcInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vpc_infos = []
        if m.get('VpcInfos') is not None:
            for k1 in m.get('VpcInfos'):
                temp_model = main_models.ListVpcInfoByInstanceResponseBodyVpcInfos()
                self.vpc_infos.append(temp_model.from_map(k1))

        return self

class ListVpcInfoByInstanceResponseBodyVpcInfos(DaraModel):
    def __init__(
        self,
        domain: str = None,
        endpoint: str = None,
        instance_vpc_name: str = None,
        region_no: str = None,
        vpc_id: str = None,
    ):
        self.domain = domain
        self.endpoint = endpoint
        self.instance_vpc_name = instance_vpc_name
        self.region_no = region_no
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.instance_vpc_name is not None:
            result['InstanceVpcName'] = self.instance_vpc_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('InstanceVpcName') is not None:
            self.instance_vpc_name = m.get('InstanceVpcName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

