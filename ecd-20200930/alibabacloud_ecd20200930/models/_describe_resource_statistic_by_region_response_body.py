# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceStatisticByRegionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        statistic: main_models.DescribeResourceStatisticByRegionResponseBodyStatistic = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The statistics information.
        self.statistic = statistic

    def validate(self):
        if self.statistic:
            self.statistic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.statistic is not None:
            result['Statistic'] = self.statistic.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Statistic') is not None:
            temp_model = main_models.DescribeResourceStatisticByRegionResponseBodyStatistic()
            self.statistic = temp_model.from_map(m.get('Statistic'))

        return self

class DescribeResourceStatisticByRegionResponseBodyStatistic(DaraModel):
    def __init__(
        self,
        region_statistics: List[main_models.DescribeResourceStatisticByRegionResponseBodyStatisticRegionStatistics] = None,
    ):
        # The statistics by region.
        self.region_statistics = region_statistics

    def validate(self):
        if self.region_statistics:
            for v1 in self.region_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionStatistics'] = []
        if self.region_statistics is not None:
            for k1 in self.region_statistics:
                result['RegionStatistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_statistics = []
        if m.get('RegionStatistics') is not None:
            for k1 in m.get('RegionStatistics'):
                temp_model = main_models.DescribeResourceStatisticByRegionResponseBodyStatisticRegionStatistics()
                self.region_statistics.append(temp_model.from_map(k1))

        return self

class DescribeResourceStatisticByRegionResponseBodyStatisticRegionStatistics(DaraModel):
    def __init__(
        self,
        assigned_end_user_count: int = None,
        connected_end_user_count: int = None,
        desktop_count: int = None,
        desktop_group_count: int = None,
        network_package_count: int = None,
        policy_group_count: int = None,
        region_id: str = None,
    ):
        # The number of assigned users in the current region.
        self.assigned_end_user_count = assigned_end_user_count
        # The number of connected users in the current region.
        self.connected_end_user_count = connected_end_user_count
        # The number of cloud desktops in the current region.
        self.desktop_count = desktop_count
        # The number of shared cloud desktops in the current region.
        self.desktop_group_count = desktop_group_count
        # The number of network packages in the current region.
        self.network_package_count = network_package_count
        # The number of policy groups in the current region.
        self.policy_group_count = policy_group_count
        # The region ID. You can call the [DescribeRegions](https://next.api.aliyun.com/document/ecd/2020-09-30/DescribeRegions) operation to query the regions supported by WUYING Workspace.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assigned_end_user_count is not None:
            result['AssignedEndUserCount'] = self.assigned_end_user_count

        if self.connected_end_user_count is not None:
            result['ConnectedEndUserCount'] = self.connected_end_user_count

        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count

        if self.desktop_group_count is not None:
            result['DesktopGroupCount'] = self.desktop_group_count

        if self.network_package_count is not None:
            result['NetworkPackageCount'] = self.network_package_count

        if self.policy_group_count is not None:
            result['PolicyGroupCount'] = self.policy_group_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignedEndUserCount') is not None:
            self.assigned_end_user_count = m.get('AssignedEndUserCount')

        if m.get('ConnectedEndUserCount') is not None:
            self.connected_end_user_count = m.get('ConnectedEndUserCount')

        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')

        if m.get('DesktopGroupCount') is not None:
            self.desktop_group_count = m.get('DesktopGroupCount')

        if m.get('NetworkPackageCount') is not None:
            self.network_package_count = m.get('NetworkPackageCount')

        if m.get('PolicyGroupCount') is not None:
            self.policy_group_count = m.get('PolicyGroupCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

