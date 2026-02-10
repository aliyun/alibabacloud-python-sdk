# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVulTargetStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        target_stats: List[main_models.DescribeVulTargetStatisticsResponseBodyTargetStats] = None,
        total_count: int = None,
    ):
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # An array that consists of the configurations of the vulnerability scan feature.
        self.target_stats = target_stats
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.target_stats:
            for v1 in self.target_stats:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TargetStats'] = []
        if self.target_stats is not None:
            for k1 in self.target_stats:
                result['TargetStats'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.target_stats = []
        if m.get('TargetStats') is not None:
            for k1 in m.get('TargetStats'):
                temp_model = main_models.DescribeVulTargetStatisticsResponseBodyTargetStats()
                self.target_stats.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVulTargetStatisticsResponseBodyTargetStats(DaraModel):
    def __init__(
        self,
        targets: List[main_models.DescribeVulTargetStatisticsResponseBodyTargetStatsTargets] = None,
        total_count: int = None,
        uuid_count: int = None,
        vul_type: str = None,
    ):
        # An array that consists of available servers.
        self.targets = targets
        # The total number of servers.
        self.total_count = total_count
        # The number of servers to which the configurations are applied.
        self.uuid_count = uuid_count
        # The type of the vulnerability. Valid values:
        # 
        # *   cve: Linux software vulnerabilities
        # *   sys: Windows system vulnerabilities
        # *   cms: Web-CMS vulnerabilities
        # *   emg: urgent vulnerabilities
        self.vul_type = vul_type

    def validate(self):
        if self.targets:
            for v1 in self.targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Targets'] = []
        if self.targets is not None:
            for k1 in self.targets:
                result['Targets'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.uuid_count is not None:
            result['UuidCount'] = self.uuid_count

        if self.vul_type is not None:
            result['VulType'] = self.vul_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.targets = []
        if m.get('Targets') is not None:
            for k1 in m.get('Targets'):
                temp_model = main_models.DescribeVulTargetStatisticsResponseBodyTargetStatsTargets()
                self.targets.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UuidCount') is not None:
            self.uuid_count = m.get('UuidCount')

        if m.get('VulType') is not None:
            self.vul_type = m.get('VulType')

        return self

class DescribeVulTargetStatisticsResponseBodyTargetStatsTargets(DaraModel):
    def __init__(
        self,
        flag: str = None,
        target: str = None,
        target_type: str = None,
    ):
        # Indicates whether the configurations are applied to the server. Valid values:
        # 
        # *   **add**: yes
        # *   **del**: no
        self.flag = flag
        # The group ID or UUID of the server to which the configurations are applied.
        self.target = target
        # The condition by which the configurations are applied to the server. Valid values:
        # 
        # *   **uuid**: the UUID of the server
        # *   **groupId**: the ID of the server group
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flag is not None:
            result['Flag'] = self.flag

        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

