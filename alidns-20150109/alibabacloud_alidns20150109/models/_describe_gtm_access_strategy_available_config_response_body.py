# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeGtmAccessStrategyAvailableConfigResponseBody(DaraModel):
    def __init__(
        self,
        addr_pools: main_models.DescribeGtmAccessStrategyAvailableConfigResponseBodyAddrPools = None,
        lines: main_models.DescribeGtmAccessStrategyAvailableConfigResponseBodyLines = None,
        request_id: str = None,
        suggest_set_default_line: bool = None,
    ):
        # The address pools.
        self.addr_pools = addr_pools
        # The Domain Name System (DNS) request sources.
        self.lines = lines
        # The request ID.
        self.request_id = request_id
        # Indicates whether the global line is recommended.
        self.suggest_set_default_line = suggest_set_default_line

    def validate(self):
        if self.addr_pools:
            self.addr_pools.validate()
        if self.lines:
            self.lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_pools is not None:
            result['AddrPools'] = self.addr_pools.to_map()

        if self.lines is not None:
            result['Lines'] = self.lines.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.suggest_set_default_line is not None:
            result['SuggestSetDefaultLine'] = self.suggest_set_default_line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPools') is not None:
            temp_model = main_models.DescribeGtmAccessStrategyAvailableConfigResponseBodyAddrPools()
            self.addr_pools = temp_model.from_map(m.get('AddrPools'))

        if m.get('Lines') is not None:
            temp_model = main_models.DescribeGtmAccessStrategyAvailableConfigResponseBodyLines()
            self.lines = temp_model.from_map(m.get('Lines'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SuggestSetDefaultLine') is not None:
            self.suggest_set_default_line = m.get('SuggestSetDefaultLine')

        return self

class DescribeGtmAccessStrategyAvailableConfigResponseBodyLines(DaraModel):
    def __init__(
        self,
        line: List[main_models.DescribeGtmAccessStrategyAvailableConfigResponseBodyLinesLine] = None,
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
                temp_model = main_models.DescribeGtmAccessStrategyAvailableConfigResponseBodyLinesLine()
                self.line.append(temp_model.from_map(k1))

        return self

class DescribeGtmAccessStrategyAvailableConfigResponseBodyLinesLine(DaraModel):
    def __init__(
        self,
        father_code: str = None,
        group_code: str = None,
        group_name: str = None,
        line_code: str = None,
        line_name: str = None,
        status: str = None,
    ):
        # The code of the parent line. No value is returned if no parent line exists.
        self.father_code = father_code
        # The group number of the DNS request source.
        self.group_code = group_code
        # The group name of the DNS request source.
        self.group_name = group_name
        # The code of the DNS request source.
        self.line_code = line_code
        # The name of the DNS request source.
        self.line_name = line_name
        # The state of the line. Valid values:
        # 
        # *   **FORBIDDEN**: The line is unavailable.
        # *   **OPTIONAL**: The line is available.
        self.status = status

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

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeGtmAccessStrategyAvailableConfigResponseBodyAddrPools(DaraModel):
    def __init__(
        self,
        addr_pool: List[main_models.DescribeGtmAccessStrategyAvailableConfigResponseBodyAddrPoolsAddrPool] = None,
    ):
        self.addr_pool = addr_pool

    def validate(self):
        if self.addr_pool:
            for v1 in self.addr_pool:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddrPool'] = []
        if self.addr_pool is not None:
            for k1 in self.addr_pool:
                result['AddrPool'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addr_pool = []
        if m.get('AddrPool') is not None:
            for k1 in m.get('AddrPool'):
                temp_model = main_models.DescribeGtmAccessStrategyAvailableConfigResponseBodyAddrPoolsAddrPool()
                self.addr_pool.append(temp_model.from_map(k1))

        return self

class DescribeGtmAccessStrategyAvailableConfigResponseBodyAddrPoolsAddrPool(DaraModel):
    def __init__(
        self,
        addr_pool_id: str = None,
        addr_pool_name: str = None,
    ):
        # The ID of the address pool.
        self.addr_pool_id = addr_pool_id
        # The name of the address pool.
        self.addr_pool_name = addr_pool_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addr_pool_id is not None:
            result['AddrPoolId'] = self.addr_pool_id

        if self.addr_pool_name is not None:
            result['AddrPoolName'] = self.addr_pool_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddrPoolId') is not None:
            self.addr_pool_id = m.get('AddrPoolId')

        if m.get('AddrPoolName') is not None:
            self.addr_pool_name = m.get('AddrPoolName')

        return self

