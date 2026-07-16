# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorHiveDatabasesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorHiveDatabasesResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The analysis results of Hive databases.
        self.data = data
        # The maximum number of entries that are returned.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = main_models.ListDoctorHiveDatabasesResponseBodyData()
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

class ListDoctorHiveDatabasesResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis: main_models.ListDoctorHiveDatabasesResponseBodyDataAnalysis = None,
        database_name: str = None,
        formats: List[main_models.ListDoctorHiveDatabasesResponseBodyDataFormats] = None,
        metrics: main_models.ListDoctorHiveDatabasesResponseBodyDataMetrics = None,
    ):
        # The analysis results.
        self.analysis = analysis
        # The database name.
        self.database_name = database_name
        # The information from the perspective of storage formats.
        self.formats = formats
        # The metric information.
        self.metrics = metrics

    def validate(self):
        if self.analysis:
            self.analysis.validate()
        if self.formats:
            for v1 in self.formats:
                 if v1:
                    v1.validate()
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['Analysis'] = self.analysis.to_map()

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        result['Formats'] = []
        if self.formats is not None:
            for k1 in self.formats:
                result['Formats'].append(k1.to_map() if k1 else None)

        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analysis') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        self.formats = []
        if m.get('Formats') is not None:
            for k1 in m.get('Formats'):
                temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataFormats()
                self.formats.append(temp_model.from_map(k1))

        if m.get('Metrics') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        return self

class ListDoctorHiveDatabasesResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        cold_data_day_growth_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataDayGrowthSize = None,
        cold_data_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataRatio = None,
        cold_data_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataSize = None,
        cold_data_size_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataSizeDayGrowthRatio = None,
        empty_file_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileCount = None,
        empty_file_count_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileCountDayGrowthRatio = None,
        empty_file_day_growth_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileDayGrowthCount = None,
        empty_file_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileRatio = None,
        freeze_data_day_growth_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataDayGrowthSize = None,
        freeze_data_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataRatio = None,
        freeze_data_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataSize = None,
        freeze_data_size_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio = None,
        hot_data_day_growth_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataDayGrowthSize = None,
        hot_data_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataRatio = None,
        hot_data_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataSize = None,
        hot_data_size_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataSizeDayGrowthRatio = None,
        large_file_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileCount = None,
        large_file_count_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileCountDayGrowthRatio = None,
        large_file_day_growth_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileDayGrowthCount = None,
        large_file_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileRatio = None,
        medium_file_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileCount = None,
        medium_file_count_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileCountDayGrowthRatio = None,
        medium_file_day_growth_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileDayGrowthCount = None,
        medium_file_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileRatio = None,
        partition_num: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsPartitionNum = None,
        small_file_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileCount = None,
        small_file_count_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileCountDayGrowthRatio = None,
        small_file_day_growth_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileDayGrowthCount = None,
        small_file_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileRatio = None,
        table_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTableCount = None,
        tiny_file_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileCount = None,
        tiny_file_count_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileCountDayGrowthRatio = None,
        tiny_file_day_growth_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileDayGrowthCount = None,
        tiny_file_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileRatio = None,
        total_data_day_growth_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataDayGrowthSize = None,
        total_data_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataSize = None,
        total_data_size_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataSizeDayGrowthRatio = None,
        total_file_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileCount = None,
        total_file_count_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileCountDayGrowthRatio = None,
        total_file_day_growth_count: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileDayGrowthCount = None,
        warm_data_day_growth_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataDayGrowthSize = None,
        warm_data_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataRatio = None,
        warm_data_size: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataSize = None,
        warm_data_size_day_growth_ratio: main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataSizeDayGrowthRatio = None,
    ):
        # The daily increment of the amount of cold data. Cold data refers to data that is not accessed for more than 30 days but is accessed in 90 days.
        self.cold_data_day_growth_size = cold_data_day_growth_size
        # The proportion of cold data. Cold data refers to data that is not accessed for more than 30 days but is accessed in 90 days.
        self.cold_data_ratio = cold_data_ratio
        # The amount of cold data. Cold data refers to data that is not accessed for more than 30 days but is accessed in 90 days.
        self.cold_data_size = cold_data_size
        # The day-to-day growth rate of the amount of cold data. Cold data refers to data that is not accessed for more than 30 days but is accessed in 90 days.
        self.cold_data_size_day_growth_ratio = cold_data_size_day_growth_ratio
        # The number of empty files. Empty files are those with a size of 0 MB.
        self.empty_file_count = empty_file_count
        # The day-to-day growth rate of the number of empty files. Empty files are those with a size of 0 MB.
        self.empty_file_count_day_growth_ratio = empty_file_count_day_growth_ratio
        # The daily increment of the number of empty files. Empty files are those with a size of 0 MB.
        self.empty_file_day_growth_count = empty_file_day_growth_count
        # The proportion of empty files. Empty files are those with a size of 0 MB.
        self.empty_file_ratio = empty_file_ratio
        # The daily increment of the amount of very cold data. Very cold data refers to data that is not accessed for more than 90 days.
        self.freeze_data_day_growth_size = freeze_data_day_growth_size
        # The proportion of very cold data. Very cold data refers to data that is not accessed for more than 90 days.
        self.freeze_data_ratio = freeze_data_ratio
        # The amount of very cold data. Very cold data refers to data that is not accessed for more than 90 days.
        self.freeze_data_size = freeze_data_size
        # The day-to-day growth rate of the amount of very cold data. Very cold data refers to data that is not accessed for more than 90 days.
        self.freeze_data_size_day_growth_ratio = freeze_data_size_day_growth_ratio
        # The daily increment of the amount of hot data. Hot data refers to data that is accessed in recent seven days.
        self.hot_data_day_growth_size = hot_data_day_growth_size
        # The proportion of hot data. Hot data refers to data that is accessed in recent seven days.
        self.hot_data_ratio = hot_data_ratio
        # The amount of hot data. Hot data refers to data that is accessed in recent seven days.
        self.hot_data_size = hot_data_size
        # The day-to-day growth rate of the amount of hot data. Hot data refers to data that is accessed in recent seven days.
        self.hot_data_size_day_growth_ratio = hot_data_size_day_growth_ratio
        # The number of large files. Large files are those with a size greater than 1 GB.
        self.large_file_count = large_file_count
        # The day-to-day growth rate of the number of large files. Large files are those with a size greater than 1 GB.
        self.large_file_count_day_growth_ratio = large_file_count_day_growth_ratio
        # The daily increment of the number of large files. Large files are those with a size greater than 1 GB.
        self.large_file_day_growth_count = large_file_day_growth_count
        # The proportion of large files. Large files are those with a size greater than 1 GB.
        self.large_file_ratio = large_file_ratio
        # The number of medium files. Medium files are those with a size greater than or equal to 128 MB and less than or equal to 1 GB.
        self.medium_file_count = medium_file_count
        # The day-to-day growth rate of the number of medium files. Medium files are those with a size greater than or equal to 128 MB and less than or equal to 1 GB.
        self.medium_file_count_day_growth_ratio = medium_file_count_day_growth_ratio
        # The daily increment of the number of medium files. Medium files are those with a size greater than or equal to 128 MB and less than or equal to 1 GB.
        self.medium_file_day_growth_count = medium_file_day_growth_count
        # The proportion of medium files. Medium files are those with a size greater than or equal to 128 MB and less than or equal to 1 GB.
        self.medium_file_ratio = medium_file_ratio
        # The number of partitions.
        self.partition_num = partition_num
        # The number of small files. Small files are those with a size greater than or equal to 10 MB and less than 128 MB.
        self.small_file_count = small_file_count
        # The day-to-day growth rate of the number of small files. Small files are those with a size greater than or equal to 10 MB and less than 128 MB.
        self.small_file_count_day_growth_ratio = small_file_count_day_growth_ratio
        # The daily increment of the number of small files. Small files are those with a size greater than or equal to 10 MB and less than 128 MB.
        self.small_file_day_growth_count = small_file_day_growth_count
        # The proportion of small files. Small files are those with a size greater than or equal to 10 MB and less than 128 MB.
        self.small_file_ratio = small_file_ratio
        # The number of tables.
        self.table_count = table_count
        # The number of very small files. Very small files are those with a size greater than 0 MB and less than 10 MB.
        self.tiny_file_count = tiny_file_count
        # The day-to-day growth rate of the number of very small files. Very small files are those with a size greater than 0 MB and less than 10 MB.
        self.tiny_file_count_day_growth_ratio = tiny_file_count_day_growth_ratio
        # The daily increment of the number of very small files. Very small files are those with a size greater than 0 MB and less than 10 MB.
        self.tiny_file_day_growth_count = tiny_file_day_growth_count
        # The proportion of very small files. Very small files are those with a size greater than 0 MB and less than 10 MB.
        self.tiny_file_ratio = tiny_file_ratio
        # The daily increment of the total data volume.
        self.total_data_day_growth_size = total_data_day_growth_size
        # The total amount of data.
        self.total_data_size = total_data_size
        # The day-to-day growth rate of the total data volume.
        self.total_data_size_day_growth_ratio = total_data_size_day_growth_ratio
        # The total number of files.
        self.total_file_count = total_file_count
        # The day-to-day growth rate of the total number of files.
        self.total_file_count_day_growth_ratio = total_file_count_day_growth_ratio
        # The daily increment of the total number of files.
        self.total_file_day_growth_count = total_file_day_growth_count
        # The daily increment of the amount of warm data. Warm data refers to data that is not accessed for more than 7 days but is accessed in 30 days.
        self.warm_data_day_growth_size = warm_data_day_growth_size
        # The proportion of warm data. Warm data refers to data that is not accessed for more than 7 days but is accessed in 30 days.
        self.warm_data_ratio = warm_data_ratio
        # The amount of warm data. Warm data refers to data that is not accessed for more than 7 days but is accessed in 30 days.
        self.warm_data_size = warm_data_size
        # The day-to-day growth rate of the amount of warm data. Warm data refers to data that is not accessed for more than 7 days but is accessed in 30 days.
        self.warm_data_size_day_growth_ratio = warm_data_size_day_growth_ratio

    def validate(self):
        if self.cold_data_day_growth_size:
            self.cold_data_day_growth_size.validate()
        if self.cold_data_ratio:
            self.cold_data_ratio.validate()
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
        if self.empty_file_ratio:
            self.empty_file_ratio.validate()
        if self.freeze_data_day_growth_size:
            self.freeze_data_day_growth_size.validate()
        if self.freeze_data_ratio:
            self.freeze_data_ratio.validate()
        if self.freeze_data_size:
            self.freeze_data_size.validate()
        if self.freeze_data_size_day_growth_ratio:
            self.freeze_data_size_day_growth_ratio.validate()
        if self.hot_data_day_growth_size:
            self.hot_data_day_growth_size.validate()
        if self.hot_data_ratio:
            self.hot_data_ratio.validate()
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
        if self.large_file_ratio:
            self.large_file_ratio.validate()
        if self.medium_file_count:
            self.medium_file_count.validate()
        if self.medium_file_count_day_growth_ratio:
            self.medium_file_count_day_growth_ratio.validate()
        if self.medium_file_day_growth_count:
            self.medium_file_day_growth_count.validate()
        if self.medium_file_ratio:
            self.medium_file_ratio.validate()
        if self.partition_num:
            self.partition_num.validate()
        if self.small_file_count:
            self.small_file_count.validate()
        if self.small_file_count_day_growth_ratio:
            self.small_file_count_day_growth_ratio.validate()
        if self.small_file_day_growth_count:
            self.small_file_day_growth_count.validate()
        if self.small_file_ratio:
            self.small_file_ratio.validate()
        if self.table_count:
            self.table_count.validate()
        if self.tiny_file_count:
            self.tiny_file_count.validate()
        if self.tiny_file_count_day_growth_ratio:
            self.tiny_file_count_day_growth_ratio.validate()
        if self.tiny_file_day_growth_count:
            self.tiny_file_day_growth_count.validate()
        if self.tiny_file_ratio:
            self.tiny_file_ratio.validate()
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
        if self.warm_data_ratio:
            self.warm_data_ratio.validate()
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

        if self.cold_data_ratio is not None:
            result['ColdDataRatio'] = self.cold_data_ratio.to_map()

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

        if self.empty_file_ratio is not None:
            result['EmptyFileRatio'] = self.empty_file_ratio.to_map()

        if self.freeze_data_day_growth_size is not None:
            result['FreezeDataDayGrowthSize'] = self.freeze_data_day_growth_size.to_map()

        if self.freeze_data_ratio is not None:
            result['FreezeDataRatio'] = self.freeze_data_ratio.to_map()

        if self.freeze_data_size is not None:
            result['FreezeDataSize'] = self.freeze_data_size.to_map()

        if self.freeze_data_size_day_growth_ratio is not None:
            result['FreezeDataSizeDayGrowthRatio'] = self.freeze_data_size_day_growth_ratio.to_map()

        if self.hot_data_day_growth_size is not None:
            result['HotDataDayGrowthSize'] = self.hot_data_day_growth_size.to_map()

        if self.hot_data_ratio is not None:
            result['HotDataRatio'] = self.hot_data_ratio.to_map()

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

        if self.large_file_ratio is not None:
            result['LargeFileRatio'] = self.large_file_ratio.to_map()

        if self.medium_file_count is not None:
            result['MediumFileCount'] = self.medium_file_count.to_map()

        if self.medium_file_count_day_growth_ratio is not None:
            result['MediumFileCountDayGrowthRatio'] = self.medium_file_count_day_growth_ratio.to_map()

        if self.medium_file_day_growth_count is not None:
            result['MediumFileDayGrowthCount'] = self.medium_file_day_growth_count.to_map()

        if self.medium_file_ratio is not None:
            result['MediumFileRatio'] = self.medium_file_ratio.to_map()

        if self.partition_num is not None:
            result['PartitionNum'] = self.partition_num.to_map()

        if self.small_file_count is not None:
            result['SmallFileCount'] = self.small_file_count.to_map()

        if self.small_file_count_day_growth_ratio is not None:
            result['SmallFileCountDayGrowthRatio'] = self.small_file_count_day_growth_ratio.to_map()

        if self.small_file_day_growth_count is not None:
            result['SmallFileDayGrowthCount'] = self.small_file_day_growth_count.to_map()

        if self.small_file_ratio is not None:
            result['SmallFileRatio'] = self.small_file_ratio.to_map()

        if self.table_count is not None:
            result['TableCount'] = self.table_count.to_map()

        if self.tiny_file_count is not None:
            result['TinyFileCount'] = self.tiny_file_count.to_map()

        if self.tiny_file_count_day_growth_ratio is not None:
            result['TinyFileCountDayGrowthRatio'] = self.tiny_file_count_day_growth_ratio.to_map()

        if self.tiny_file_day_growth_count is not None:
            result['TinyFileDayGrowthCount'] = self.tiny_file_day_growth_count.to_map()

        if self.tiny_file_ratio is not None:
            result['TinyFileRatio'] = self.tiny_file_ratio.to_map()

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

        if self.warm_data_ratio is not None:
            result['WarmDataRatio'] = self.warm_data_ratio.to_map()

        if self.warm_data_size is not None:
            result['WarmDataSize'] = self.warm_data_size.to_map()

        if self.warm_data_size_day_growth_ratio is not None:
            result['WarmDataSizeDayGrowthRatio'] = self.warm_data_size_day_growth_ratio.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataDayGrowthSize()
            self.cold_data_day_growth_size = temp_model.from_map(m.get('ColdDataDayGrowthSize'))

        if m.get('ColdDataRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataRatio()
            self.cold_data_ratio = temp_model.from_map(m.get('ColdDataRatio'))

        if m.get('ColdDataSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataSize()
            self.cold_data_size = temp_model.from_map(m.get('ColdDataSize'))

        if m.get('ColdDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataSizeDayGrowthRatio()
            self.cold_data_size_day_growth_ratio = temp_model.from_map(m.get('ColdDataSizeDayGrowthRatio'))

        if m.get('EmptyFileCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileCount()
            self.empty_file_count = temp_model.from_map(m.get('EmptyFileCount'))

        if m.get('EmptyFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileCountDayGrowthRatio()
            self.empty_file_count_day_growth_ratio = temp_model.from_map(m.get('EmptyFileCountDayGrowthRatio'))

        if m.get('EmptyFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileDayGrowthCount()
            self.empty_file_day_growth_count = temp_model.from_map(m.get('EmptyFileDayGrowthCount'))

        if m.get('EmptyFileRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileRatio()
            self.empty_file_ratio = temp_model.from_map(m.get('EmptyFileRatio'))

        if m.get('FreezeDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataDayGrowthSize()
            self.freeze_data_day_growth_size = temp_model.from_map(m.get('FreezeDataDayGrowthSize'))

        if m.get('FreezeDataRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataRatio()
            self.freeze_data_ratio = temp_model.from_map(m.get('FreezeDataRatio'))

        if m.get('FreezeDataSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataSize()
            self.freeze_data_size = temp_model.from_map(m.get('FreezeDataSize'))

        if m.get('FreezeDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio()
            self.freeze_data_size_day_growth_ratio = temp_model.from_map(m.get('FreezeDataSizeDayGrowthRatio'))

        if m.get('HotDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataDayGrowthSize()
            self.hot_data_day_growth_size = temp_model.from_map(m.get('HotDataDayGrowthSize'))

        if m.get('HotDataRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataRatio()
            self.hot_data_ratio = temp_model.from_map(m.get('HotDataRatio'))

        if m.get('HotDataSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataSize()
            self.hot_data_size = temp_model.from_map(m.get('HotDataSize'))

        if m.get('HotDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataSizeDayGrowthRatio()
            self.hot_data_size_day_growth_ratio = temp_model.from_map(m.get('HotDataSizeDayGrowthRatio'))

        if m.get('LargeFileCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileCount()
            self.large_file_count = temp_model.from_map(m.get('LargeFileCount'))

        if m.get('LargeFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileCountDayGrowthRatio()
            self.large_file_count_day_growth_ratio = temp_model.from_map(m.get('LargeFileCountDayGrowthRatio'))

        if m.get('LargeFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileDayGrowthCount()
            self.large_file_day_growth_count = temp_model.from_map(m.get('LargeFileDayGrowthCount'))

        if m.get('LargeFileRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileRatio()
            self.large_file_ratio = temp_model.from_map(m.get('LargeFileRatio'))

        if m.get('MediumFileCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileCount()
            self.medium_file_count = temp_model.from_map(m.get('MediumFileCount'))

        if m.get('MediumFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileCountDayGrowthRatio()
            self.medium_file_count_day_growth_ratio = temp_model.from_map(m.get('MediumFileCountDayGrowthRatio'))

        if m.get('MediumFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileDayGrowthCount()
            self.medium_file_day_growth_count = temp_model.from_map(m.get('MediumFileDayGrowthCount'))

        if m.get('MediumFileRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileRatio()
            self.medium_file_ratio = temp_model.from_map(m.get('MediumFileRatio'))

        if m.get('PartitionNum') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsPartitionNum()
            self.partition_num = temp_model.from_map(m.get('PartitionNum'))

        if m.get('SmallFileCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileCount()
            self.small_file_count = temp_model.from_map(m.get('SmallFileCount'))

        if m.get('SmallFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileCountDayGrowthRatio()
            self.small_file_count_day_growth_ratio = temp_model.from_map(m.get('SmallFileCountDayGrowthRatio'))

        if m.get('SmallFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileDayGrowthCount()
            self.small_file_day_growth_count = temp_model.from_map(m.get('SmallFileDayGrowthCount'))

        if m.get('SmallFileRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileRatio()
            self.small_file_ratio = temp_model.from_map(m.get('SmallFileRatio'))

        if m.get('TableCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTableCount()
            self.table_count = temp_model.from_map(m.get('TableCount'))

        if m.get('TinyFileCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileCount()
            self.tiny_file_count = temp_model.from_map(m.get('TinyFileCount'))

        if m.get('TinyFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileCountDayGrowthRatio()
            self.tiny_file_count_day_growth_ratio = temp_model.from_map(m.get('TinyFileCountDayGrowthRatio'))

        if m.get('TinyFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileDayGrowthCount()
            self.tiny_file_day_growth_count = temp_model.from_map(m.get('TinyFileDayGrowthCount'))

        if m.get('TinyFileRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileRatio()
            self.tiny_file_ratio = temp_model.from_map(m.get('TinyFileRatio'))

        if m.get('TotalDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataDayGrowthSize()
            self.total_data_day_growth_size = temp_model.from_map(m.get('TotalDataDayGrowthSize'))

        if m.get('TotalDataSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataSize()
            self.total_data_size = temp_model.from_map(m.get('TotalDataSize'))

        if m.get('TotalDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataSizeDayGrowthRatio()
            self.total_data_size_day_growth_ratio = temp_model.from_map(m.get('TotalDataSizeDayGrowthRatio'))

        if m.get('TotalFileCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileCount()
            self.total_file_count = temp_model.from_map(m.get('TotalFileCount'))

        if m.get('TotalFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileCountDayGrowthRatio()
            self.total_file_count_day_growth_ratio = temp_model.from_map(m.get('TotalFileCountDayGrowthRatio'))

        if m.get('TotalFileDayGrowthCount') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileDayGrowthCount()
            self.total_file_day_growth_count = temp_model.from_map(m.get('TotalFileDayGrowthCount'))

        if m.get('WarmDataDayGrowthSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataDayGrowthSize()
            self.warm_data_day_growth_size = temp_model.from_map(m.get('WarmDataDayGrowthSize'))

        if m.get('WarmDataRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataRatio()
            self.warm_data_ratio = temp_model.from_map(m.get('WarmDataRatio'))

        if m.get('WarmDataSize') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataSize()
            self.warm_data_size = temp_model.from_map(m.get('WarmDataSize'))

        if m.get('WarmDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataSizeDayGrowthRatio()
            self.warm_data_size_day_growth_ratio = temp_model.from_map(m.get('WarmDataSizeDayGrowthRatio'))

        return self

class ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataSizeDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsWarmDataDayGrowthSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileDayGrowthCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileCountDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTotalFileCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataSizeDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTotalDataDayGrowthSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileDayGrowthCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileCountDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTinyFileCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsTableCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileDayGrowthCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileCountDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsSmallFileCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsPartitionNum(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileDayGrowthCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileCountDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsMediumFileCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileDayGrowthCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileCountDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsLargeFileCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataSizeDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsHotDataDayGrowthSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsFreezeDataDayGrowthSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileDayGrowthCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileCountDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsEmptyFileCount(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataSizeDayGrowthRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataRatio(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataMetricsColdDataDayGrowthSize(DaraModel):
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

class ListDoctorHiveDatabasesResponseBodyDataFormats(DaraModel):
    def __init__(
        self,
        format_day_growth_size: int = None,
        format_name: str = None,
        format_ratio: float = None,
        format_size: int = None,
        format_size_day_growth_ratio: float = None,
        format_size_unit: str = None,
    ):
        # The daily increment of storage format-specific data.
        self.format_day_growth_size = format_day_growth_size
        # The name of the storage format.
        self.format_name = format_name
        # The proportion of data in a specific storage format.
        self.format_ratio = format_ratio
        # The amount of storage format-specific data.
        self.format_size = format_size
        # The day-to-day growth rate of storage format-specific data.
        self.format_size_day_growth_ratio = format_size_day_growth_ratio
        # The unit of the amount of storage format-specific data.
        self.format_size_unit = format_size_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format_day_growth_size is not None:
            result['FormatDayGrowthSize'] = self.format_day_growth_size

        if self.format_name is not None:
            result['FormatName'] = self.format_name

        if self.format_ratio is not None:
            result['FormatRatio'] = self.format_ratio

        if self.format_size is not None:
            result['FormatSize'] = self.format_size

        if self.format_size_day_growth_ratio is not None:
            result['FormatSizeDayGrowthRatio'] = self.format_size_day_growth_ratio

        if self.format_size_unit is not None:
            result['FormatSizeUnit'] = self.format_size_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FormatDayGrowthSize') is not None:
            self.format_day_growth_size = m.get('FormatDayGrowthSize')

        if m.get('FormatName') is not None:
            self.format_name = m.get('FormatName')

        if m.get('FormatRatio') is not None:
            self.format_ratio = m.get('FormatRatio')

        if m.get('FormatSize') is not None:
            self.format_size = m.get('FormatSize')

        if m.get('FormatSizeDayGrowthRatio') is not None:
            self.format_size_day_growth_ratio = m.get('FormatSizeDayGrowthRatio')

        if m.get('FormatSizeUnit') is not None:
            self.format_size_unit = m.get('FormatSizeUnit')

        return self

class ListDoctorHiveDatabasesResponseBodyDataAnalysis(DaraModel):
    def __init__(
        self,
        hive_distribution_score: int = None,
        hive_format_score: int = None,
        hive_frequency_score: int = None,
        hive_score: int = None,
    ):
        # The score for the distribution of files of different sizes stored in the Hive database.
        self.hive_distribution_score = hive_distribution_score
        # The score for the distribution of files stored in different formats in the Hive database.
        self.hive_format_score = hive_format_score
        # The score for the access frequency of the Hive database.
        self.hive_frequency_score = hive_frequency_score
        # The overall score of the Hive database.
        self.hive_score = hive_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hive_distribution_score is not None:
            result['HiveDistributionScore'] = self.hive_distribution_score

        if self.hive_format_score is not None:
            result['HiveFormatScore'] = self.hive_format_score

        if self.hive_frequency_score is not None:
            result['HiveFrequencyScore'] = self.hive_frequency_score

        if self.hive_score is not None:
            result['HiveScore'] = self.hive_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HiveDistributionScore') is not None:
            self.hive_distribution_score = m.get('HiveDistributionScore')

        if m.get('HiveFormatScore') is not None:
            self.hive_format_score = m.get('HiveFormatScore')

        if m.get('HiveFrequencyScore') is not None:
            self.hive_frequency_score = m.get('HiveFrequencyScore')

        if m.get('HiveScore') is not None:
            self.hive_score = m.get('HiveScore')

        return self

