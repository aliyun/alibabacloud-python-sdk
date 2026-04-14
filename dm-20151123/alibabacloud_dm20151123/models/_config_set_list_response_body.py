# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class ConfigSetListResponseBody(DaraModel):
    def __init__(
        self,
        config_sets: List[main_models.ConfigSetListResponseBodyConfigSets] = None,
        current_page: int = None,
        has_more: bool = None,
        page_size: int = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        self.config_sets = config_sets
        self.current_page = current_page
        self.has_more = has_more
        self.page_size = page_size
        self.request_id = request_id
        self.total_counts = total_counts

    def validate(self):
        if self.config_sets:
            for v1 in self.config_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigSets'] = []
        if self.config_sets is not None:
            for k1 in self.config_sets:
                result['ConfigSets'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_sets = []
        if m.get('ConfigSets') is not None:
            for k1 in m.get('ConfigSets'):
                temp_model = main_models.ConfigSetListResponseBodyConfigSets()
                self.config_sets.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ConfigSetListResponseBodyConfigSets(DaraModel):
    def __init__(
        self,
        description: str = None,
        from_addresses: List[str] = None,
        id: str = None,
        ip_pool: main_models.ConfigSetListResponseBodyConfigSetsIpPool = None,
        name: str = None,
    ):
        self.description = description
        self.from_addresses = from_addresses
        self.id = id
        self.ip_pool = ip_pool
        self.name = name

    def validate(self):
        if self.ip_pool:
            self.ip_pool.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.from_addresses is not None:
            result['FromAddresses'] = self.from_addresses

        if self.id is not None:
            result['Id'] = self.id

        if self.ip_pool is not None:
            result['IpPool'] = self.ip_pool.to_map()

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FromAddresses') is not None:
            self.from_addresses = m.get('FromAddresses')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IpPool') is not None:
            temp_model = main_models.ConfigSetListResponseBodyConfigSetsIpPool()
            self.ip_pool = temp_model.from_map(m.get('IpPool'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ConfigSetListResponseBodyConfigSetsIpPool(DaraModel):
    def __init__(
        self,
        ip_pool_id: str = None,
        ip_pool_name: str = None,
    ):
        self.ip_pool_id = ip_pool_id
        self.ip_pool_name = ip_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_pool_id is not None:
            result['IpPoolId'] = self.ip_pool_id

        if self.ip_pool_name is not None:
            result['IpPoolName'] = self.ip_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpPoolId') is not None:
            self.ip_pool_id = m.get('IpPoolId')

        if m.get('IpPoolName') is not None:
            self.ip_pool_name = m.get('IpPoolName')

        return self

