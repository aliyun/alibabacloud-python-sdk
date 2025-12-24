# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeSubnetsResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        subnets: List[main_models.DescribeSubnetsResponseBodySubnets] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.subnets = subnets

    def validate(self):
        if self.subnets:
            for v1 in self.subnets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Subnets'] = []
        if self.subnets is not None:
            for k1 in self.subnets:
                result['Subnets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.subnets = []
        if m.get('Subnets') is not None:
            for k1 in m.get('Subnets'):
                temp_model = main_models.DescribeSubnetsResponseBodySubnets()
                self.subnets.append(temp_model.from_map(k1))

        return self

class DescribeSubnetsResponseBodySubnets(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        name: str = None,
        office_site_id: str = None,
        status: str = None,
        subnet_id: str = None,
        total_eds_count: int = None,
        total_eds_count_for_group: int = None,
        zone_id: str = None,
    ):
        self.cidr_block = cidr_block
        self.name = name
        self.office_site_id = office_site_id
        self.status = status
        self.subnet_id = subnet_id
        self.total_eds_count = total_eds_count
        self.total_eds_count_for_group = total_eds_count_for_group
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.name is not None:
            result['Name'] = self.name

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.status is not None:
            result['Status'] = self.status

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        if self.total_eds_count is not None:
            result['TotalEdsCount'] = self.total_eds_count

        if self.total_eds_count_for_group is not None:
            result['TotalEdsCountForGroup'] = self.total_eds_count_for_group

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        if m.get('TotalEdsCount') is not None:
            self.total_eds_count = m.get('TotalEdsCount')

        if m.get('TotalEdsCountForGroup') is not None:
            self.total_eds_count_for_group = m.get('TotalEdsCountForGroup')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

