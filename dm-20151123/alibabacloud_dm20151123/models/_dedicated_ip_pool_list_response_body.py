# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class DedicatedIpPoolListResponseBody(DaraModel):
    def __init__(
        self,
        current_page: str = None,
        has_more: bool = None,
        ip_pools: List[main_models.DedicatedIpPoolListResponseBodyIpPools] = None,
        page_size: str = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # Current page
        self.current_page = current_page
        # Whether there is a next page
        self.has_more = has_more
        # List of IP pools
        self.ip_pools = ip_pools
        # Page size
        self.page_size = page_size
        # Request ID
        self.request_id = request_id
        # Total number of data under the current request conditions
        self.total_counts = total_counts

    def validate(self):
        if self.ip_pools:
            for v1 in self.ip_pools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        result['IpPools'] = []
        if self.ip_pools is not None:
            for k1 in self.ip_pools:
                result['IpPools'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        self.ip_pools = []
        if m.get('IpPools') is not None:
            for k1 in m.get('IpPools'):
                temp_model = main_models.DedicatedIpPoolListResponseBodyIpPools()
                self.ip_pools.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class DedicatedIpPoolListResponseBodyIpPools(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        ip_count: int = None,
        ips: List[main_models.DedicatedIpPoolListResponseBodyIpPoolsIps] = None,
        name: str = None,
    ):
        # Creation time
        self.create_time = create_time
        # IP pool ID
        self.id = id
        # Number of source IP addresses
        self.ip_count = ip_count
        # List of IPs
        self.ips = ips
        # IP pool name
        self.name = name

    def validate(self):
        if self.ips:
            for v1 in self.ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

        result['Ips'] = []
        if self.ips is not None:
            for k1 in self.ips:
                result['Ips'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        self.ips = []
        if m.get('Ips') is not None:
            for k1 in m.get('Ips'):
                temp_model = main_models.DedicatedIpPoolListResponseBodyIpPoolsIps()
                self.ips.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DedicatedIpPoolListResponseBodyIpPoolsIps(DaraModel):
    def __init__(
        self,
        id: str = None,
        ip: str = None,
        zone_id: str = None,
    ):
        # Instance purchase ID
        self.id = id
        # IP address
        self.ip = ip
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

