# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBody(DaraModel):
    def __init__(
        self,
        domain_addr_pools: main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyDomainAddrPools = None,
        ipv_4addr_pools: main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv4AddrPools = None,
        ipv_6addr_pools: main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv6AddrPools = None,
        lines: main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyLines = None,
        request_id: str = None,
        selected_domain_lines: main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedDomainLines = None,
        selected_ipv_4lines: main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedIpv4Lines = None,
        selected_ipv_6lines: main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedIpv6Lines = None,
        suggest_set_default_line: bool = None,
    ):
        # The available address pools of the domain name type.
        self.domain_addr_pools = domain_addr_pools
        # The available address pools of the IPv4 type.
        self.ipv_4addr_pools = ipv_4addr_pools
        # The available address pools of the IPv6 type.
        self.ipv_6addr_pools = ipv_6addr_pools
        # The source regions.
        self.lines = lines
        # The ID of the request.
        self.request_id = request_id
        self.selected_domain_lines = selected_domain_lines
        self.selected_ipv_4lines = selected_ipv_4lines
        self.selected_ipv_6lines = selected_ipv_6lines
        # Indicates whether we recommend that you set the source region to global.
        self.suggest_set_default_line = suggest_set_default_line

    def validate(self):
        if self.domain_addr_pools:
            self.domain_addr_pools.validate()
        if self.ipv_4addr_pools:
            self.ipv_4addr_pools.validate()
        if self.ipv_6addr_pools:
            self.ipv_6addr_pools.validate()
        if self.lines:
            self.lines.validate()
        if self.selected_domain_lines:
            self.selected_domain_lines.validate()
        if self.selected_ipv_4lines:
            self.selected_ipv_4lines.validate()
        if self.selected_ipv_6lines:
            self.selected_ipv_6lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_addr_pools is not None:
            result['DomainAddrPools'] = self.domain_addr_pools.to_map()

        if self.ipv_4addr_pools is not None:
            result['Ipv4AddrPools'] = self.ipv_4addr_pools.to_map()

        if self.ipv_6addr_pools is not None:
            result['Ipv6AddrPools'] = self.ipv_6addr_pools.to_map()

        if self.lines is not None:
            result['Lines'] = self.lines.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.selected_domain_lines is not None:
            result['SelectedDomainLines'] = self.selected_domain_lines.to_map()

        if self.selected_ipv_4lines is not None:
            result['SelectedIpv4Lines'] = self.selected_ipv_4lines.to_map()

        if self.selected_ipv_6lines is not None:
            result['SelectedIpv6Lines'] = self.selected_ipv_6lines.to_map()

        if self.suggest_set_default_line is not None:
            result['SuggestSetDefaultLine'] = self.suggest_set_default_line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainAddrPools') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyDomainAddrPools()
            self.domain_addr_pools = temp_model.from_map(m.get('DomainAddrPools'))

        if m.get('Ipv4AddrPools') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv4AddrPools()
            self.ipv_4addr_pools = temp_model.from_map(m.get('Ipv4AddrPools'))

        if m.get('Ipv6AddrPools') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv6AddrPools()
            self.ipv_6addr_pools = temp_model.from_map(m.get('Ipv6AddrPools'))

        if m.get('Lines') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyLines()
            self.lines = temp_model.from_map(m.get('Lines'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SelectedDomainLines') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedDomainLines()
            self.selected_domain_lines = temp_model.from_map(m.get('SelectedDomainLines'))

        if m.get('SelectedIpv4Lines') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedIpv4Lines()
            self.selected_ipv_4lines = temp_model.from_map(m.get('SelectedIpv4Lines'))

        if m.get('SelectedIpv6Lines') is not None:
            temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedIpv6Lines()
            self.selected_ipv_6lines = temp_model.from_map(m.get('SelectedIpv6Lines'))

        if m.get('SuggestSetDefaultLine') is not None:
            self.suggest_set_default_line = m.get('SuggestSetDefaultLine')

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedIpv6Lines(DaraModel):
    def __init__(
        self,
        selected_ipv_6line: List[str] = None,
    ):
        self.selected_ipv_6line = selected_ipv_6line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.selected_ipv_6line is not None:
            result['SelectedIpv6Line'] = self.selected_ipv_6line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectedIpv6Line') is not None:
            self.selected_ipv_6line = m.get('SelectedIpv6Line')

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedIpv4Lines(DaraModel):
    def __init__(
        self,
        selected_ipv_4line: List[str] = None,
    ):
        self.selected_ipv_4line = selected_ipv_4line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.selected_ipv_4line is not None:
            result['SelectedIpv4Line'] = self.selected_ipv_4line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectedIpv4Line') is not None:
            self.selected_ipv_4line = m.get('SelectedIpv4Line')

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodySelectedDomainLines(DaraModel):
    def __init__(
        self,
        selected_domain_line: List[str] = None,
    ):
        self.selected_domain_line = selected_domain_line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.selected_domain_line is not None:
            result['SelectedDomainLine'] = self.selected_domain_line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SelectedDomainLine') is not None:
            self.selected_domain_line = m.get('SelectedDomainLine')

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyLines(DaraModel):
    def __init__(
        self,
        line: List[main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyLinesLine] = None,
    ):
        self.line = line

    def validate(self):
        if self.line:
            for v1 in self.line:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Line'] = []
        if self.line is not None:
            for k1 in self.line:
                result['Line'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.line = []
        if m.get('Line') is not None:
            for k1 in m.get('Line'):
                temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyLinesLine()
                self.line.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyLinesLine(DaraModel):
    def __init__(
        self,
        father_code: str = None,
        group_code: str = None,
        group_name: str = None,
        line_code: str = None,
        line_name: str = None,
    ):
        # The parent line code of the source region. Leave it blank if no parent line exists.
        self.father_code = father_code
        # The line name of the source region.
        self.group_code = group_code
        # The name of the source region group.
        self.group_name = group_name
        # The line code of the source region.
        self.line_code = line_code
        # The code of the source region group.
        self.line_name = line_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.father_code is not None:
            result['FatherCode'] = self.father_code

        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.line_name is not None:
            result['LineName'] = self.line_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FatherCode') is not None:
            self.father_code = m.get('FatherCode')

        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('LineName') is not None:
            self.line_name = m.get('LineName')

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv6AddrPools(DaraModel):
    def __init__(
        self,
        ipv_6addr_pool: List[main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv6AddrPoolsIpv6AddrPool] = None,
    ):
        self.ipv_6addr_pool = ipv_6addr_pool

    def validate(self):
        if self.ipv_6addr_pool:
            for v1 in self.ipv_6addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv6AddrPool'] = []
        if self.ipv_6addr_pool is not None:
            for k1 in self.ipv_6addr_pool:
                result['Ipv6AddrPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_6addr_pool = []
        if m.get('Ipv6AddrPool') is not None:
            for k1 in m.get('Ipv6AddrPool'):
                temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv6AddrPoolsIpv6AddrPool()
                self.ipv_6addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv6AddrPoolsIpv6AddrPool(DaraModel):
    def __init__(
        self,
        addr_count: int = None,
        id: str = None,
        name: str = None,
    ):
        # The number of addresses in the address pool.
        self.addr_count = addr_count
        # The ID of the address pool.
        self.id = id
        # The name of the address pool.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv4AddrPools(DaraModel):
    def __init__(
        self,
        ipv_4addr_pool: List[main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv4AddrPoolsIpv4AddrPool] = None,
    ):
        self.ipv_4addr_pool = ipv_4addr_pool

    def validate(self):
        if self.ipv_4addr_pool:
            for v1 in self.ipv_4addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ipv4AddrPool'] = []
        if self.ipv_4addr_pool is not None:
            for k1 in self.ipv_4addr_pool:
                result['Ipv4AddrPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ipv_4addr_pool = []
        if m.get('Ipv4AddrPool') is not None:
            for k1 in m.get('Ipv4AddrPool'):
                temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv4AddrPoolsIpv4AddrPool()
                self.ipv_4addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyIpv4AddrPoolsIpv4AddrPool(DaraModel):
    def __init__(
        self,
        addr_count: int = None,
        id: str = None,
        name: str = None,
    ):
        # The number of addresses in the address pool.
        self.addr_count = addr_count
        # The ID of the address pool.
        self.id = id
        # The name of the address pool.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyDomainAddrPools(DaraModel):
    def __init__(
        self,
        domain_addr_pool: List[main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyDomainAddrPoolsDomainAddrPool] = None,
    ):
        self.domain_addr_pool = domain_addr_pool

    def validate(self):
        if self.domain_addr_pool:
            for v1 in self.domain_addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DomainAddrPool'] = []
        if self.domain_addr_pool is not None:
            for k1 in self.domain_addr_pool:
                result['DomainAddrPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.domain_addr_pool = []
        if m.get('DomainAddrPool') is not None:
            for k1 in m.get('DomainAddrPool'):
                temp_model = main_models.DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyDomainAddrPoolsDomainAddrPool()
                self.domain_addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeDnsGtmAccessStrategyAvailableConfigResponseBodyDomainAddrPoolsDomainAddrPool(DaraModel):
    def __init__(
        self,
        addr_count: int = None,
        id: str = None,
        name: str = None,
    ):
        # The number of addresses in the address pool.
        self.addr_count = addr_count
        # The ID of the address pool.
        self.id = id
        # The name of the address pool.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_count is not None:
            result['AddrCount'] = self.addr_count

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrCount') is not None:
            self.addr_count = m.get('AddrCount')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

