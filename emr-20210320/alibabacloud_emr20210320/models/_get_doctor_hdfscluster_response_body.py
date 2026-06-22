# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetDoctorHDFSClusterResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDoctorHDFSClusterResponseBodyData = None,
        request_id: str = None,
    ):
        # The HDFS analysis results.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDoctorHDFSClusterResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis: main_models.GetDoctorHDFSClusterResponseBodyDataAnalysis = None,
        metrics: main_models.GetDoctorHDFSClusterResponseBodyDataMetrics = None,
    ):
        # The analysis results.
        self.analysis = analysis
        # The metric information.
        self.metrics = metrics

    def validate(self):
        if self.analysis:
            self.analysis.validate()
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['Analysis'] = self.analysis.to_map()

        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analysis') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('Metrics') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        return self

class GetDoctorHDFSClusterResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        cold_data_day_growth_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsColdDataDayGrowthSize = None,
        cold_data_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsColdDataRatio = None,
        cold_data_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsColdDataSize = None,
        cold_data_size_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsColdDataSizeDayGrowthRatio = None,
        empty_file_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileCount = None,
        empty_file_count_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileCountDayGrowthRatio = None,
        empty_file_day_growth_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileDayGrowthCount = None,
        empty_file_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileRatio = None,
        freeze_data_day_growth_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataDayGrowthSize = None,
        freeze_data_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataRatio = None,
        freeze_data_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataSize = None,
        freeze_data_size_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio = None,
        hot_data_day_growth_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsHotDataDayGrowthSize = None,
        hot_data_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsHotDataRatio = None,
        hot_data_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsHotDataSize = None,
        hot_data_size_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsHotDataSizeDayGrowthRatio = None,
        large_file_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileCount = None,
        large_file_count_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileCountDayGrowthRatio = None,
        large_file_day_growth_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileDayGrowthCount = None,
        large_file_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileRatio = None,
        medium_file_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileCount = None,
        medium_file_count_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileCountDayGrowthRatio = None,
        medium_file_day_growth_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileDayGrowthCount = None,
        medium_file_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileRatio = None,
        small_file_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileCount = None,
        small_file_count_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileCountDayGrowthRatio = None,
        small_file_day_growth_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileDayGrowthCount = None,
        small_file_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileRatio = None,
        tiny_file_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileCount = None,
        tiny_file_count_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileCountDayGrowthRatio = None,
        tiny_file_day_growth_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileDayGrowthCount = None,
        tiny_file_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileRatio = None,
        total_data_day_growth_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataDayGrowthSize = None,
        total_data_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataSize = None,
        total_data_size_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataSizeDayGrowthRatio = None,
        total_file_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileCount = None,
        total_file_count_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileCountDayGrowthRatio = None,
        total_file_day_growth_count: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileDayGrowthCount = None,
        warm_data_day_growth_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataDayGrowthSize = None,
        warm_data_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataRatio = None,
        warm_data_size: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataSize = None,
        warm_data_size_day_growth_ratio: main_models.GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataSizeDayGrowthRatio = None,
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
        # The number of small files. Small files are those with a size greater than or equal to 10 MB and less than 128 MB.
        self.small_file_count = small_file_count
        # The day-to-day growth rate of the number of small files. Small files are those with a size greater than or equal to 10 MB and less than 128 MB.
        self.small_file_count_day_growth_ratio = small_file_count_day_growth_ratio
        # The daily increment of the number of small files. Small files are those with a size greater than or equal to 10 MB and less than 128 MB.
        self.small_file_day_growth_count = small_file_day_growth_count
        # The proportion of small files. Small files are those with a size greater than or equal to 10 MB and less than 128 MB.
        self.small_file_ratio = small_file_ratio
        # The number of very small files. Very small files are those with a size greater than 0 MB and less than 10 MB.
        self.tiny_file_count = tiny_file_count
        # The day-to-day growth rate of the number of very small files. Very small files are those with a size greater than 0 MB and less than 10 MB.
        self.tiny_file_count_day_growth_ratio = tiny_file_count_day_growth_ratio
        # The daily increment of the number of very small files. Very small files are those with a size greater than 0 MB and less than 10 MB.
        self.tiny_file_day_growth_count = tiny_file_day_growth_count
        # The proportion of very small files. Very small files are those with a size greater than 0 MB and less than 10 MB.
        self.tiny_file_ratio = tiny_file_ratio
        # The daily incremental of the total data volume.
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
        if self.small_file_count:
            self.small_file_count.validate()
        if self.small_file_count_day_growth_ratio:
            self.small_file_count_day_growth_ratio.validate()
        if self.small_file_day_growth_count:
            self.small_file_day_growth_count.validate()
        if self.small_file_ratio:
            self.small_file_ratio.validate()
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

        if self.small_file_count is not None:
            result['SmallFileCount'] = self.small_file_count.to_map()

        if self.small_file_count_day_growth_ratio is not None:
            result['SmallFileCountDayGrowthRatio'] = self.small_file_count_day_growth_ratio.to_map()

        if self.small_file_day_growth_count is not None:
            result['SmallFileDayGrowthCount'] = self.small_file_day_growth_count.to_map()

        if self.small_file_ratio is not None:
            result['SmallFileRatio'] = self.small_file_ratio.to_map()

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
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsColdDataDayGrowthSize()
            self.cold_data_day_growth_size = temp_model.from_map(m.get('ColdDataDayGrowthSize'))

        if m.get('ColdDataRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsColdDataRatio()
            self.cold_data_ratio = temp_model.from_map(m.get('ColdDataRatio'))

        if m.get('ColdDataSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsColdDataSize()
            self.cold_data_size = temp_model.from_map(m.get('ColdDataSize'))

        if m.get('ColdDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsColdDataSizeDayGrowthRatio()
            self.cold_data_size_day_growth_ratio = temp_model.from_map(m.get('ColdDataSizeDayGrowthRatio'))

        if m.get('EmptyFileCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileCount()
            self.empty_file_count = temp_model.from_map(m.get('EmptyFileCount'))

        if m.get('EmptyFileCountDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileCountDayGrowthRatio()
            self.empty_file_count_day_growth_ratio = temp_model.from_map(m.get('EmptyFileCountDayGrowthRatio'))

        if m.get('EmptyFileDayGrowthCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileDayGrowthCount()
            self.empty_file_day_growth_count = temp_model.from_map(m.get('EmptyFileDayGrowthCount'))

        if m.get('EmptyFileRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileRatio()
            self.empty_file_ratio = temp_model.from_map(m.get('EmptyFileRatio'))

        if m.get('FreezeDataDayGrowthSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataDayGrowthSize()
            self.freeze_data_day_growth_size = temp_model.from_map(m.get('FreezeDataDayGrowthSize'))

        if m.get('FreezeDataRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataRatio()
            self.freeze_data_ratio = temp_model.from_map(m.get('FreezeDataRatio'))

        if m.get('FreezeDataSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataSize()
            self.freeze_data_size = temp_model.from_map(m.get('FreezeDataSize'))

        if m.get('FreezeDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio()
            self.freeze_data_size_day_growth_ratio = temp_model.from_map(m.get('FreezeDataSizeDayGrowthRatio'))

        if m.get('HotDataDayGrowthSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsHotDataDayGrowthSize()
            self.hot_data_day_growth_size = temp_model.from_map(m.get('HotDataDayGrowthSize'))

        if m.get('HotDataRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsHotDataRatio()
            self.hot_data_ratio = temp_model.from_map(m.get('HotDataRatio'))

        if m.get('HotDataSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsHotDataSize()
            self.hot_data_size = temp_model.from_map(m.get('HotDataSize'))

        if m.get('HotDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsHotDataSizeDayGrowthRatio()
            self.hot_data_size_day_growth_ratio = temp_model.from_map(m.get('HotDataSizeDayGrowthRatio'))

        if m.get('LargeFileCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileCount()
            self.large_file_count = temp_model.from_map(m.get('LargeFileCount'))

        if m.get('LargeFileCountDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileCountDayGrowthRatio()
            self.large_file_count_day_growth_ratio = temp_model.from_map(m.get('LargeFileCountDayGrowthRatio'))

        if m.get('LargeFileDayGrowthCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileDayGrowthCount()
            self.large_file_day_growth_count = temp_model.from_map(m.get('LargeFileDayGrowthCount'))

        if m.get('LargeFileRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileRatio()
            self.large_file_ratio = temp_model.from_map(m.get('LargeFileRatio'))

        if m.get('MediumFileCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileCount()
            self.medium_file_count = temp_model.from_map(m.get('MediumFileCount'))

        if m.get('MediumFileCountDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileCountDayGrowthRatio()
            self.medium_file_count_day_growth_ratio = temp_model.from_map(m.get('MediumFileCountDayGrowthRatio'))

        if m.get('MediumFileDayGrowthCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileDayGrowthCount()
            self.medium_file_day_growth_count = temp_model.from_map(m.get('MediumFileDayGrowthCount'))

        if m.get('MediumFileRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileRatio()
            self.medium_file_ratio = temp_model.from_map(m.get('MediumFileRatio'))

        if m.get('SmallFileCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileCount()
            self.small_file_count = temp_model.from_map(m.get('SmallFileCount'))

        if m.get('SmallFileCountDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileCountDayGrowthRatio()
            self.small_file_count_day_growth_ratio = temp_model.from_map(m.get('SmallFileCountDayGrowthRatio'))

        if m.get('SmallFileDayGrowthCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileDayGrowthCount()
            self.small_file_day_growth_count = temp_model.from_map(m.get('SmallFileDayGrowthCount'))

        if m.get('SmallFileRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileRatio()
            self.small_file_ratio = temp_model.from_map(m.get('SmallFileRatio'))

        if m.get('TinyFileCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileCount()
            self.tiny_file_count = temp_model.from_map(m.get('TinyFileCount'))

        if m.get('TinyFileCountDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileCountDayGrowthRatio()
            self.tiny_file_count_day_growth_ratio = temp_model.from_map(m.get('TinyFileCountDayGrowthRatio'))

        if m.get('TinyFileDayGrowthCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileDayGrowthCount()
            self.tiny_file_day_growth_count = temp_model.from_map(m.get('TinyFileDayGrowthCount'))

        if m.get('TinyFileRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileRatio()
            self.tiny_file_ratio = temp_model.from_map(m.get('TinyFileRatio'))

        if m.get('TotalDataDayGrowthSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataDayGrowthSize()
            self.total_data_day_growth_size = temp_model.from_map(m.get('TotalDataDayGrowthSize'))

        if m.get('TotalDataSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataSize()
            self.total_data_size = temp_model.from_map(m.get('TotalDataSize'))

        if m.get('TotalDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataSizeDayGrowthRatio()
            self.total_data_size_day_growth_ratio = temp_model.from_map(m.get('TotalDataSizeDayGrowthRatio'))

        if m.get('TotalFileCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileCount()
            self.total_file_count = temp_model.from_map(m.get('TotalFileCount'))

        if m.get('TotalFileCountDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileCountDayGrowthRatio()
            self.total_file_count_day_growth_ratio = temp_model.from_map(m.get('TotalFileCountDayGrowthRatio'))

        if m.get('TotalFileDayGrowthCount') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileDayGrowthCount()
            self.total_file_day_growth_count = temp_model.from_map(m.get('TotalFileDayGrowthCount'))

        if m.get('WarmDataDayGrowthSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataDayGrowthSize()
            self.warm_data_day_growth_size = temp_model.from_map(m.get('WarmDataDayGrowthSize'))

        if m.get('WarmDataRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataRatio()
            self.warm_data_ratio = temp_model.from_map(m.get('WarmDataRatio'))

        if m.get('WarmDataSize') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataSize()
            self.warm_data_size = temp_model.from_map(m.get('WarmDataSize'))

        if m.get('WarmDataSizeDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataSizeDayGrowthRatio()
            self.warm_data_size_day_growth_ratio = temp_model.from_map(m.get('WarmDataSizeDayGrowthRatio'))

        return self

class GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataSizeDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsWarmDataDayGrowthSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileDayGrowthCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileCountDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTotalFileCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataSizeDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTotalDataDayGrowthSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileDayGrowthCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileCountDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsTinyFileCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileDayGrowthCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileCountDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsSmallFileCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileDayGrowthCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileCountDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsMediumFileCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileDayGrowthCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileCountDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsLargeFileCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsHotDataSizeDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsHotDataSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsHotDataRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsHotDataDayGrowthSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataSizeDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsFreezeDataDayGrowthSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileDayGrowthCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileCountDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsEmptyFileCount(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsColdDataSizeDayGrowthRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsColdDataSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsColdDataRatio(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataMetricsColdDataDayGrowthSize(DaraModel):
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

class GetDoctorHDFSClusterResponseBodyDataAnalysis(DaraModel):
    def __init__(
        self,
        hdfs_score: int = None,
    ):
        # The overall score of HDFS storage resources.
        self.hdfs_score = hdfs_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hdfs_score is not None:
            result['HdfsScore'] = self.hdfs_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HdfsScore') is not None:
            self.hdfs_score = m.get('HdfsScore')

        return self

