# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class GetBasicStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        global_statistics: main_models.GetBasicStatisticsResponseBodyGlobalStatistics = None,
        message: str = None,
        region_statistics: List[main_models.GetBasicStatisticsResponseBodyRegionStatistics] = None,
        request_id: str = None,
        source_type: str = None,
        success: bool = None,
    ):
        # The HTTP status code. A value of 200 indicates that the request was successful.
        self.code = code
        # The Backup statistics for all regions.
        self.global_statistics = global_statistics
        # The response message. If the request is successful, `successful` is returned. If the request fails, an error message is returned.
        self.message = message
        # The Backup statistics for each region.
        self.region_statistics = region_statistics
        # The Request ID.
        self.request_id = request_id
        # The data source type. The valid value is:
        # 
        # - **ECS_FILE**: ECS File Backup.
        self.source_type = source_type
        # Indicates whether the request was successful.
        # 
        # - true: The request was successful.
        # 
        # - false: The request failed.
        self.success = success

    def validate(self):
        if self.global_statistics:
            self.global_statistics.validate()
        if self.region_statistics:
            for v1 in self.region_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.global_statistics is not None:
            result['GlobalStatistics'] = self.global_statistics.to_map()

        if self.message is not None:
            result['Message'] = self.message

        result['RegionStatistics'] = []
        if self.region_statistics is not None:
            for k1 in self.region_statistics:
                result['RegionStatistics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('GlobalStatistics') is not None:
            temp_model = main_models.GetBasicStatisticsResponseBodyGlobalStatistics()
            self.global_statistics = temp_model.from_map(m.get('GlobalStatistics'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.region_statistics = []
        if m.get('RegionStatistics') is not None:
            for k1 in m.get('RegionStatistics'):
                temp_model = main_models.GetBasicStatisticsResponseBodyRegionStatistics()
                self.region_statistics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetBasicStatisticsResponseBodyRegionStatistics(DaraModel):
    def __init__(
        self,
        protected_data_size: int = None,
        protected_resource_count: int = None,
        region_id: str = None,
    ):
        # The backed-up data size, in bytes.
        # 
        # - When `SourceType` is set to `ECS_FILE`, this parameter represents the total capacity of backed-up Cloud Disks.
        self.protected_data_size = protected_data_size
        # The number of backed-up resources.
        # 
        # - When `SourceType` is set to `ECS_FILE`, this parameter represents the number of backed-up ECS instances.
        self.protected_resource_count = protected_resource_count
        # The Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protected_data_size is not None:
            result['ProtectedDataSize'] = self.protected_data_size

        if self.protected_resource_count is not None:
            result['ProtectedResourceCount'] = self.protected_resource_count

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedDataSize') is not None:
            self.protected_data_size = m.get('ProtectedDataSize')

        if m.get('ProtectedResourceCount') is not None:
            self.protected_resource_count = m.get('ProtectedResourceCount')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class GetBasicStatisticsResponseBodyGlobalStatistics(DaraModel):
    def __init__(
        self,
        protected_data_size: int = None,
        protected_resource_count: int = None,
    ):
        # The backed-up data size, in bytes.
        # 
        # - When `SourceType` is set to `ECS_FILE`, this parameter represents the total capacity of backed-up Cloud Disks.
        self.protected_data_size = protected_data_size
        # The number of backed-up resources.
        # 
        # - When `SourceType` is set to `ECS_FILE`, this parameter represents the number of backed-up ECS instances.
        self.protected_resource_count = protected_resource_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protected_data_size is not None:
            result['ProtectedDataSize'] = self.protected_data_size

        if self.protected_resource_count is not None:
            result['ProtectedResourceCount'] = self.protected_resource_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProtectedDataSize') is not None:
            self.protected_data_size = m.get('ProtectedDataSize')

        if m.get('ProtectedResourceCount') is not None:
            self.protected_resource_count = m.get('ProtectedResourceCount')

        return self

