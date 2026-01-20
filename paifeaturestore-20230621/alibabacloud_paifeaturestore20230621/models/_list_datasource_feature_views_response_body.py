# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paifeaturestore20230621 import models as main_models
from darabonba.model import DaraModel

class ListDatasourceFeatureViewsResponseBody(DaraModel):
    def __init__(
        self,
        feature_views: List[main_models.ListDatasourceFeatureViewsResponseBodyFeatureViews] = None,
        total_count: int = None,
        total_usage_statistics: main_models.ListDatasourceFeatureViewsResponseBodyTotalUsageStatistics = None,
        request_id: str = None,
    ):
        self.feature_views = feature_views
        self.total_count = total_count
        self.total_usage_statistics = total_usage_statistics
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.feature_views:
            for v1 in self.feature_views:
                 if v1:
                    v1.validate()
        if self.total_usage_statistics:
            self.total_usage_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FeatureViews'] = []
        if self.feature_views is not None:
            for k1 in self.feature_views:
                result['FeatureViews'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_usage_statistics is not None:
            result['TotalUsageStatistics'] = self.total_usage_statistics.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.feature_views = []
        if m.get('FeatureViews') is not None:
            for k1 in m.get('FeatureViews'):
                temp_model = main_models.ListDatasourceFeatureViewsResponseBodyFeatureViews()
                self.feature_views.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalUsageStatistics') is not None:
            temp_model = main_models.ListDatasourceFeatureViewsResponseBodyTotalUsageStatistics()
            self.total_usage_statistics = temp_model.from_map(m.get('TotalUsageStatistics'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListDatasourceFeatureViewsResponseBodyTotalUsageStatistics(DaraModel):
    def __init__(
        self,
        total_disk_usage: float = None,
        total_memory_usage: float = None,
        total_read_write_count: List[main_models.ListDatasourceFeatureViewsResponseBodyTotalUsageStatisticsTotalReadWriteCount] = None,
    ):
        self.total_disk_usage = total_disk_usage
        self.total_memory_usage = total_memory_usage
        self.total_read_write_count = total_read_write_count

    def validate(self):
        if self.total_read_write_count:
            for v1 in self.total_read_write_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_disk_usage is not None:
            result['TotalDiskUsage'] = self.total_disk_usage

        if self.total_memory_usage is not None:
            result['TotalMemoryUsage'] = self.total_memory_usage

        result['TotalReadWriteCount'] = []
        if self.total_read_write_count is not None:
            for k1 in self.total_read_write_count:
                result['TotalReadWriteCount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalDiskUsage') is not None:
            self.total_disk_usage = m.get('TotalDiskUsage')

        if m.get('TotalMemoryUsage') is not None:
            self.total_memory_usage = m.get('TotalMemoryUsage')

        self.total_read_write_count = []
        if m.get('TotalReadWriteCount') is not None:
            for k1 in m.get('TotalReadWriteCount'):
                temp_model = main_models.ListDatasourceFeatureViewsResponseBodyTotalUsageStatisticsTotalReadWriteCount()
                self.total_read_write_count.append(temp_model.from_map(k1))

        return self

class ListDatasourceFeatureViewsResponseBodyTotalUsageStatisticsTotalReadWriteCount(DaraModel):
    def __init__(
        self,
        date: str = None,
        total_read_count: int = None,
        total_write_count: int = None,
    ):
        self.date = date
        self.total_read_count = total_read_count
        self.total_write_count = total_write_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.total_read_count is not None:
            result['TotalReadCount'] = self.total_read_count

        if self.total_write_count is not None:
            result['TotalWriteCount'] = self.total_write_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('TotalReadCount') is not None:
            self.total_read_count = m.get('TotalReadCount')

        if m.get('TotalWriteCount') is not None:
            self.total_write_count = m.get('TotalWriteCount')

        return self

class ListDatasourceFeatureViewsResponseBodyFeatureViews(DaraModel):
    def __init__(
        self,
        config: str = None,
        feature_entity_name: str = None,
        feature_view_id: str = None,
        name: str = None,
        project_name: str = None,
        ttl: int = None,
        type: str = None,
        usage_statistics: main_models.ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatistics = None,
    ):
        self.config = config
        self.feature_entity_name = feature_entity_name
        self.feature_view_id = feature_view_id
        self.name = name
        self.project_name = project_name
        self.ttl = ttl
        self.type = type
        self.usage_statistics = usage_statistics

    def validate(self):
        if self.usage_statistics:
            self.usage_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.feature_entity_name is not None:
            result['FeatureEntityName'] = self.feature_entity_name

        if self.feature_view_id is not None:
            result['FeatureViewId'] = self.feature_view_id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.usage_statistics is not None:
            result['UsageStatistics'] = self.usage_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('FeatureEntityName') is not None:
            self.feature_entity_name = m.get('FeatureEntityName')

        if m.get('FeatureViewId') is not None:
            self.feature_view_id = m.get('FeatureViewId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UsageStatistics') is not None:
            temp_model = main_models.ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatistics()
            self.usage_statistics = temp_model.from_map(m.get('UsageStatistics'))

        return self

class ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatistics(DaraModel):
    def __init__(
        self,
        disk_usage: float = None,
        memory_usage: float = None,
        read_write_count: List[main_models.ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatisticsReadWriteCount] = None,
        row_count: int = None,
    ):
        self.disk_usage = disk_usage
        self.memory_usage = memory_usage
        self.read_write_count = read_write_count
        self.row_count = row_count

    def validate(self):
        if self.read_write_count:
            for v1 in self.read_write_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_usage is not None:
            result['DiskUsage'] = self.disk_usage

        if self.memory_usage is not None:
            result['MemoryUsage'] = self.memory_usage

        result['ReadWriteCount'] = []
        if self.read_write_count is not None:
            for k1 in self.read_write_count:
                result['ReadWriteCount'].append(k1.to_map() if k1 else None)

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskUsage') is not None:
            self.disk_usage = m.get('DiskUsage')

        if m.get('MemoryUsage') is not None:
            self.memory_usage = m.get('MemoryUsage')

        self.read_write_count = []
        if m.get('ReadWriteCount') is not None:
            for k1 in m.get('ReadWriteCount'):
                temp_model = main_models.ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatisticsReadWriteCount()
                self.read_write_count.append(temp_model.from_map(k1))

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        return self

class ListDatasourceFeatureViewsResponseBodyFeatureViewsUsageStatisticsReadWriteCount(DaraModel):
    def __init__(
        self,
        date: str = None,
        read_count: int = None,
        write_count: int = None,
    ):
        self.date = date
        self.read_count = read_count
        self.write_count = write_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.read_count is not None:
            result['ReadCount'] = self.read_count

        if self.write_count is not None:
            result['WriteCount'] = self.write_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')

        if m.get('WriteCount') is not None:
            self.write_count = m.get('WriteCount')

        return self

