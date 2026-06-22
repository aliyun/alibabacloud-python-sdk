# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorHDFSDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorHDFSDirectoriesResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The analytical data for the batch analysis of HDFS directories.
        self.data = data
        # The maximum number of records returned.
        self.max_results = max_results
        # The starting position for the next read.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries that match the request.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDoctorHDFSDirectoriesResponseBodyData(DaraModel):
    def __init__(
        self,
        depth: int = None,
        dir_path: str = None,
        group: str = None,
        metrics: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetrics = None,
        user: str = None,
    ):
        # The directory level.
        self.depth = depth
        # The directory name.
        self.dir_path = dir_path
        # The group of the folder.
        self.group = group
        # The metric information.
        self.metrics = metrics
        # The owner of the directory.
        self.user = user

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.depth is not None:
            result['Depth'] = self.depth

        if self.dir_path is not None:
            result['DirPath'] = self.dir_path

        if self.group is not None:
            result['Group'] = self.group

        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')

        if m.get('DirPath') is not None:
            self.dir_path = m.get('DirPath')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Metrics') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        cold_data_day_growth_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataDayGrowthSize = None,
        cold_data_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataSize = None,
        cold_data_size_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataSizeDayGrowthRatio = None,
        empty_file_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileCount = None,
        empty_file_count_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileCountDayGrowthRatio = None,
        empty_file_day_growth_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileDayGrowthCount = None,
        freeze_data_day_growth_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataDayGrowthSize = None,
        freeze_data_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataSize = None,
        freeze_data_size_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio = None,
        hot_data_day_growth_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataDayGrowthSize = None,
        hot_data_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataSize = None,
        hot_data_size_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataSizeDayGrowthRatio = None,
        large_file_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileCount = None,
        large_file_count_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileCountDayGrowthRatio = None,
        large_file_day_growth_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileDayGrowthCount = None,
        medium_file_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileCount = None,
        medium_file_count_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileCountDayGrowthRatio = None,
        medium_file_day_growth_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileDayGrowthCount = None,
        small_file_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileCount = None,
        small_file_count_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileCountDayGrowthRatio = None,
        small_file_day_growth_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileDayGrowthCount = None,
        tiny_file_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileCount = None,
        tiny_file_count_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileCountDayGrowthRatio = None,
        tiny_file_day_growth_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileDayGrowthCount = None,
        total_data_day_growth_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataDayGrowthSize = None,
        total_data_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataSize = None,
        total_data_size_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataSizeDayGrowthRatio = None,
        total_file_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileCount = None,
        total_file_count_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileCountDayGrowthRatio = None,
        total_file_day_growth_count: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileDayGrowthCount = None,
        warm_data_day_growth_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataDayGrowthSize = None,
        warm_data_size: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataSize = None,
        warm_data_size_day_growth_ratio: main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataSizeDayGrowthRatio = None,
    ):
        # The daily growth in the size of cold data. Cold data is data that was last accessed between 30 and 90 days ago.
        self.cold_data_day_growth_size = cold_data_day_growth_size
        # The size of the cold data. Cold data is data that was last accessed between 30 and 90 days ago.
        self.cold_data_size = cold_data_size
        # The day-over-day growth rate of the cold data size. Cold data refers to data last accessed between 30 and 90 days ago.
        self.cold_data_size_day_growth_ratio = cold_data_size_day_growth_ratio
        # The count of empty files. An empty file is a file with a size of 0 MB.
        self.empty_file_count = empty_file_count
        # The day-over-day growth ratio of the empty file count. An empty file is a file with a size of 0 MB.
        self.empty_file_count_day_growth_ratio = empty_file_count_day_growth_ratio
        # The daily growth in the number of empty files. An empty file has a size of 0 MB.
        self.empty_file_day_growth_count = empty_file_day_growth_count
        # The daily growth in the size of freeze data. Freeze data is data that has not been accessed for 90 days.
        self.freeze_data_day_growth_size = freeze_data_day_growth_size
        # The size of the frozen data. Data is considered frozen if it has not been accessed in the last 90 days.
        self.freeze_data_size = freeze_data_size
        # The daily growth rate of freeze data. Freeze data is data that has not been accessed in 90 days.
        self.freeze_data_size_day_growth_ratio = freeze_data_size_day_growth_ratio
        # The daily increase in hot data size. Hot data is data that has been accessed within the last 7 days.
        self.hot_data_day_growth_size = hot_data_day_growth_size
        # The size of the hot data. Hot data is data accessed within the last 7 days.
        self.hot_data_size = hot_data_size
        # The daily growth rate of the hot data size. Hot data is any data accessed in the past 7 days.
        self.hot_data_size_day_growth_ratio = hot_data_size_day_growth_ratio
        # The number of large files. A large file is a file that is 1 GB or larger.
        self.large_file_count = large_file_count
        # The day-over-day growth ratio of the large file count. A large file is a file that is 1 GB or larger.
        self.large_file_count_day_growth_ratio = large_file_count_day_growth_ratio
        # The daily increase in the number of large files. A large file is a file larger than 1 GB.
        self.large_file_day_growth_count = large_file_day_growth_count
        # The number of files larger than 128 MB and up to 1 GB.
        self.medium_file_count = medium_file_count
        # The day-over-day growth ratio of the number of medium-sized files. A medium-sized file is larger than 128 MB and smaller than 1 GB.
        self.medium_file_count_day_growth_ratio = medium_file_count_day_growth_ratio
        # The daily increase in the number of medium-sized files. A medium-sized file is larger than 128 MB and less than or equal to 1 GB.
        self.medium_file_day_growth_count = medium_file_day_growth_count
        # The number of small files. A small file is a file with a size from 10 MB to 128 MB.
        self.small_file_count = small_file_count
        # The day-over-day growth ratio of the number of small files. A small file has a size greater than 10 MB and less than or equal to 128 MB.
        self.small_file_count_day_growth_ratio = small_file_count_day_growth_ratio
        # The number of new small files added each day. A small file is 10 MB to 128 MB.
        self.small_file_day_growth_count = small_file_day_growth_count
        # The number of tiny files. A tiny file is larger than 0 MB and up to 10 MB in size.
        self.tiny_file_count = tiny_file_count
        # The daily growth rate of tiny files. A tiny file is larger than 0 MB and smaller than 10 MB.
        self.tiny_file_count_day_growth_ratio = tiny_file_count_day_growth_ratio
        # The daily growth in the tiny file count. A tiny file is a file larger than 0 MB and smaller than 10 MB.
        self.tiny_file_day_growth_count = tiny_file_day_growth_count
        # The daily growth in the total data size.
        self.total_data_day_growth_size = total_data_day_growth_size
        # The total data size.
        self.total_data_size = total_data_size
        # The day-over-day growth ratio of the total data size.
        self.total_data_size_day_growth_ratio = total_data_size_day_growth_ratio
        # The total number of files.
        self.total_file_count = total_file_count
        # The day-over-day growth ratio of the total file count.
        self.total_file_count_day_growth_ratio = total_file_count_day_growth_ratio
        # The daily growth in the total file count.
        self.total_file_day_growth_count = total_file_day_growth_count
        # The daily growth in the size of warm data. Warm data is data that has not been accessed in the last 7 days, but has been accessed in the last 30 days.
        self.warm_data_day_growth_size = warm_data_day_growth_size
        # The size of the warm data. Warm data is data that has been accessed within the past 30 days, but not within the past 7 days.
        self.warm_data_size = warm_data_size
        # The day-over-day growth ratio of the warm data size. Warm data has not been accessed in the last 7 days but has been accessed in the last 30 days.
        self.warm_data_size_day_growth_ratio = warm_data_size_day_growth_ratio

    def validate(self):
        if self.cold_data_day_growth_size:
            self.cold_data_day_growth_size.validate()
        if self.cold_data_size:
            self.cold_data_size.validate()
        if self.cold_data_size_day_growth_ratio:
            self.cold_data_size_day_growth_ratio.validate()
        if self.empty_file_count:
            self.empty_file_count.validate()
        if self.empty_file_count_day_growth_ratio:
            self.empty_file_count_day_growth_ratio.validate()
        if self.empty_file_day_growth_count:
            self.empty_file_day_growth_count.validate()
        if self.freeze_data_day_growth_size:
            self.freeze_data_day_growth_size.validate()
        if self.freeze_data_size:
            self.freeze_data_size.validate()
        if self.freeze_data_size_day_growth_ratio:
            self.freeze_data_size_day_growth_ratio.validate()
        if self.hot_data_day_growth_size:
            self.hot_data_day_growth_size.validate()
        if self.hot_data_size:
            self.hot_data_size.validate()
        if self.hot_data_size_day_growth_ratio:
            self.hot_data_size_day_growth_ratio.validate()
        if self.large_file_count:
            self.large_file_count.validate()
        if self.large_file_count_day_growth_ratio:
            self.large_file_count_day_growth_ratio.validate()
        if self.large_file_day_growth_count:
            self.large_file_day_growth_count.validate()
        if self.medium_file_count:
            self.medium_file_count.validate()
        if self.medium_file_count_day_growth_ratio:
            self.medium_file_count_day_growth_ratio.validate()
        if self.medium_file_day_growth_count:
            self.medium_file_day_growth_count.validate()
        if self.small_file_count:
            self.small_file_count.validate()
        if self.small_file_count_day_growth_ratio:
            self.small_file_count_day_growth_ratio.validate()
        if self.small_file_day_growth_count:
            self.small_file_day_growth_count.validate()
        if self.tiny_file_count:
            self.tiny_file_count.validate()
        if self.tiny_file_count_day_growth_ratio:
            self.tiny_file_count_day_growth_ratio.validate()
        if self.tiny_file_day_growth_count:
            self.tiny_file_day_growth_count.validate()
        if self.total_data_day_growth_size:
            self.total_data_day_growth_size.validate()
        if self.total_data_size:
            self.total_data_size.validate()
        if self.total_data_size_day_growth_ratio:
            self.total_data_size_day_growth_ratio.validate()
        if self.total_file_count:
            self.total_file_count.validate()
        if self.total_file_count_day_growth_ratio:
            self.total_file_count_day_growth_ratio.validate()
        if self.total_file_day_growth_count:
            self.total_file_day_growth_count.validate()
        if self.warm_data_day_growth_size:
            self.warm_data_day_growth_size.validate()
        if self.warm_data_size:
            self.warm_data_size.validate()
        if self.warm_data_size_day_growth_ratio:
            self.warm_data_size_day_growth_ratio.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_data_day_growth_size is not None:
            result['ColdDataDayGrowthSize'] = self.cold_data_day_growth_size.to_map()

        if self.cold_data_size is not None:
            result['ColdDataSize'] = self.cold_data_size.to_map()

        if self.cold_data_size_day_growth_ratio is not None:
            result['ColdDataSizeDayGrowthRatio'] = self.cold_data_size_day_growth_ratio.to_map()

        if self.empty_file_count is not None:
            result['EmptyFileCount'] = self.empty_file_count.to_map()

        if self.empty_file_count_day_growth_ratio is not None:
            result['EmptyFileCountDayGrowthRatio'] = self.empty_file_count_day_growth_ratio.to_map()

        if self.empty_file_day_growth_count is not None:
            result['EmptyFileDayGrowthCount'] = self.empty_file_day_growth_count.to_map()

        if self.freeze_data_day_growth_size is not None:
            result['FreezeDataDayGrowthSize'] = self.freeze_data_day_growth_size.to_map()

        if self.freeze_data_size is not None:
            result['FreezeDataSize'] = self.freeze_data_size.to_map()

        if self.freeze_data_size_day_growth_ratio is not None:
            result['FreezeDataSizeDayGrowthRatio'] = self.freeze_data_size_day_growth_ratio.to_map()

        if self.hot_data_day_growth_size is not None:
            result['HotDataDayGrowthSize'] = self.hot_data_day_growth_size.to_map()

        if self.hot_data_size is not None:
            result['HotDataSize'] = self.hot_data_size.to_map()

        if self.hot_data_size_day_growth_ratio is not None:
            result['HotDataSizeDayGrowthRatio'] = self.hot_data_size_day_growth_ratio.to_map()

        if self.large_file_count is not None:
            result['LargeFileCount'] = self.large_file_count.to_map()

        if self.large_file_count_day_growth_ratio is not None:
            result['LargeFileCountDayGrowthRatio'] = self.large_file_count_day_growth_ratio.to_map()

        if self.large_file_day_growth_count is not None:
            result['LargeFileDayGrowthCount'] = self.large_file_day_growth_count.to_map()

        if self.medium_file_count is not None:
            result['MediumFileCount'] = self.medium_file_count.to_map()

        if self.medium_file_count_day_growth_ratio is not None:
            result['MediumFileCountDayGrowthRatio'] = self.medium_file_count_day_growth_ratio.to_map()

        if self.medium_file_day_growth_count is not None:
            result['MediumFileDayGrowthCount'] = self.medium_file_day_growth_count.to_map()

        if self.small_file_count is not None:
            result['SmallFileCount'] = self.small_file_count.to_map()

        if self.small_file_count_day_growth_ratio is not None:
            result['SmallFileCountDayGrowthRatio'] = self.small_file_count_day_growth_ratio.to_map()

        if self.small_file_day_growth_count is not None:
            result['SmallFileDayGrowthCount'] = self.small_file_day_growth_count.to_map()

        if self.tiny_file_count is not None:
            result['TinyFileCount'] = self.tiny_file_count.to_map()

        if self.tiny_file_count_day_growth_ratio is not None:
            result['TinyFileCountDayGrowthRatio'] = self.tiny_file_count_day_growth_ratio.to_map()

        if self.tiny_file_day_growth_count is not None:
            result['TinyFileDayGrowthCount'] = self.tiny_file_day_growth_count.to_map()

        if self.total_data_day_growth_size is not None:
            result['TotalDataDayGrowthSize'] = self.total_data_day_growth_size.to_map()

        if self.total_data_size is not None:
            result['TotalDataSize'] = self.total_data_size.to_map()

        if self.total_data_size_day_growth_ratio is not None:
            result['TotalDataSizeDayGrowthRatio'] = self.total_data_size_day_growth_ratio.to_map()

        if self.total_file_count is not None:
            result['TotalFileCount'] = self.total_file_count.to_map()

        if self.total_file_count_day_growth_ratio is not None:
            result['TotalFileCountDayGrowthRatio'] = self.total_file_count_day_growth_ratio.to_map()

        if self.total_file_day_growth_count is not None:
            result['TotalFileDayGrowthCount'] = self.total_file_day_growth_count.to_map()

        if self.warm_data_day_growth_size is not None:
            result['WarmDataDayGrowthSize'] = self.warm_data_day_growth_size.to_map()

        if self.warm_data_size is not None:
            result['WarmDataSize'] = self.warm_data_size.to_map()

        if self.warm_data_size_day_growth_ratio is not None:
            result['WarmDataSizeDayGrowthRatio'] = self.warm_data_size_day_growth_ratio.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataDayGrowthSize()
            self.cold_data_day_growth_size = temp_model.from_map(m.get('ColdDataDayGrowthSize'))

        if m.get('ColdDataSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataSize()
            self.cold_data_size = temp_model.from_map(m.get('ColdDataSize'))

        if m.get('ColdDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataSizeDayGrowthRatio()
            self.cold_data_size_day_growth_ratio = temp_model.from_map(m.get('ColdDataSizeDayGrowthRatio'))

        if m.get('EmptyFileCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileCount()
            self.empty_file_count = temp_model.from_map(m.get('EmptyFileCount'))

        if m.get('EmptyFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileCountDayGrowthRatio()
            self.empty_file_count_day_growth_ratio = temp_model.from_map(m.get('EmptyFileCountDayGrowthRatio'))

        if m.get('EmptyFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileDayGrowthCount()
            self.empty_file_day_growth_count = temp_model.from_map(m.get('EmptyFileDayGrowthCount'))

        if m.get('FreezeDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataDayGrowthSize()
            self.freeze_data_day_growth_size = temp_model.from_map(m.get('FreezeDataDayGrowthSize'))

        if m.get('FreezeDataSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataSize()
            self.freeze_data_size = temp_model.from_map(m.get('FreezeDataSize'))

        if m.get('FreezeDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio()
            self.freeze_data_size_day_growth_ratio = temp_model.from_map(m.get('FreezeDataSizeDayGrowthRatio'))

        if m.get('HotDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataDayGrowthSize()
            self.hot_data_day_growth_size = temp_model.from_map(m.get('HotDataDayGrowthSize'))

        if m.get('HotDataSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataSize()
            self.hot_data_size = temp_model.from_map(m.get('HotDataSize'))

        if m.get('HotDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataSizeDayGrowthRatio()
            self.hot_data_size_day_growth_ratio = temp_model.from_map(m.get('HotDataSizeDayGrowthRatio'))

        if m.get('LargeFileCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileCount()
            self.large_file_count = temp_model.from_map(m.get('LargeFileCount'))

        if m.get('LargeFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileCountDayGrowthRatio()
            self.large_file_count_day_growth_ratio = temp_model.from_map(m.get('LargeFileCountDayGrowthRatio'))

        if m.get('LargeFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileDayGrowthCount()
            self.large_file_day_growth_count = temp_model.from_map(m.get('LargeFileDayGrowthCount'))

        if m.get('MediumFileCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileCount()
            self.medium_file_count = temp_model.from_map(m.get('MediumFileCount'))

        if m.get('MediumFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileCountDayGrowthRatio()
            self.medium_file_count_day_growth_ratio = temp_model.from_map(m.get('MediumFileCountDayGrowthRatio'))

        if m.get('MediumFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileDayGrowthCount()
            self.medium_file_day_growth_count = temp_model.from_map(m.get('MediumFileDayGrowthCount'))

        if m.get('SmallFileCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileCount()
            self.small_file_count = temp_model.from_map(m.get('SmallFileCount'))

        if m.get('SmallFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileCountDayGrowthRatio()
            self.small_file_count_day_growth_ratio = temp_model.from_map(m.get('SmallFileCountDayGrowthRatio'))

        if m.get('SmallFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileDayGrowthCount()
            self.small_file_day_growth_count = temp_model.from_map(m.get('SmallFileDayGrowthCount'))

        if m.get('TinyFileCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileCount()
            self.tiny_file_count = temp_model.from_map(m.get('TinyFileCount'))

        if m.get('TinyFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileCountDayGrowthRatio()
            self.tiny_file_count_day_growth_ratio = temp_model.from_map(m.get('TinyFileCountDayGrowthRatio'))

        if m.get('TinyFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileDayGrowthCount()
            self.tiny_file_day_growth_count = temp_model.from_map(m.get('TinyFileDayGrowthCount'))

        if m.get('TotalDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataDayGrowthSize()
            self.total_data_day_growth_size = temp_model.from_map(m.get('TotalDataDayGrowthSize'))

        if m.get('TotalDataSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataSize()
            self.total_data_size = temp_model.from_map(m.get('TotalDataSize'))

        if m.get('TotalDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataSizeDayGrowthRatio()
            self.total_data_size_day_growth_ratio = temp_model.from_map(m.get('TotalDataSizeDayGrowthRatio'))

        if m.get('TotalFileCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileCount()
            self.total_file_count = temp_model.from_map(m.get('TotalFileCount'))

        if m.get('TotalFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileCountDayGrowthRatio()
            self.total_file_count_day_growth_ratio = temp_model.from_map(m.get('TotalFileCountDayGrowthRatio'))

        if m.get('TotalFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileDayGrowthCount()
            self.total_file_day_growth_count = temp_model.from_map(m.get('TotalFileDayGrowthCount'))

        if m.get('WarmDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataDayGrowthSize()
            self.warm_data_day_growth_size = temp_model.from_map(m.get('WarmDataDayGrowthSize'))

        if m.get('WarmDataSize') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataSize()
            self.warm_data_size = temp_model.from_map(m.get('WarmDataSize'))

        if m.get('WarmDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataSizeDayGrowthRatio()
            self.warm_data_size_day_growth_ratio = temp_model.from_map(m.get('WarmDataSizeDayGrowthRatio'))

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataSizeDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsWarmDataDayGrowthSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileDayGrowthCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalFileCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataSizeDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTotalDataDayGrowthSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileDayGrowthCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsTinyFileCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileDayGrowthCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsSmallFileCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileDayGrowthCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsMediumFileCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileDayGrowthCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsLargeFileCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataSizeDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsHotDataDayGrowthSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsFreezeDataDayGrowthSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileDayGrowthCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsEmptyFileCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataSizeDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHDFSDirectoriesResponseBodyDataMetricsColdDataDayGrowthSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

