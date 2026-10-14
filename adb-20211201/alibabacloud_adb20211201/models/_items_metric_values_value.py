# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ItemsMetricValuesValue(DaraModel):
    def __init__(
        self,
        metric_code: str = None,
        metric_name: str = None,
        primary: bool = None,
        time_2: main_models.ItemsMetricValuesValueTime2 = None,
        avg: main_models.ItemsMetricValuesValueAvg = None,
        sum: main_models.ItemsMetricValuesValueSum = None,
        max: main_models.ItemsMetricValuesValueMax = None,
    ):
        # The primary metric code, which matches the key in `MetricValues` and the `MetricType` request parameter. Valid values:
        # 
        # - `QUERY_COUNT`: the number of query executions.
        # - `CPU_COST`: the CPU consumption.
        # - `SHUFFLE_SIZE`: the shuffle data volume.
        # - `PEAK_MEMORY`: the peak memory consumption.
        # - `SCAN_SIZE`: the scan data volume.
        self.metric_code = metric_code
        # The primary metric name. The mapping is as follows:
        # 
        # - `QUERY_COUNT`: `QueryCount`.
        # - `CPU_COST`: `OperatorCost`.
        # - `SHUFFLE_SIZE`: `ShuffleSize`.
        # - `PEAK_MEMORY`: `PeakMemory`.
        # - `SCAN_SIZE`: `ScanSize`.
        self.metric_name = metric_name
        # Indicates whether this is the primary metric for the current analysis dimension. The current value is true.
        self.primary = primary
        # The aggregated result for Time 2 in the NEW report. This field is returned only for NEW reports.
        self.time_2 = time_2
        # The dual-window comparison of the average value across active query minute buckets for the CHANGED report. This field is returned only for CHANGED reports.
        self.avg = avg
        # The dual-window comparison of the sum of metric values across active query minute buckets for the CHANGED report. This field is returned only for CHANGED reports.
        self.sum = sum
        # The dual-window comparison of the peak value in a single minute bucket for the CHANGED report. This field is returned only for CHANGED reports.
        self.max = max

    def validate(self):
        if self.time_2:
            self.time_2.validate()
        if self.avg:
            self.avg.validate()
        if self.sum:
            self.sum.validate()
        if self.max:
            self.max.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_code is not None:
            result['MetricCode'] = self.metric_code

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.primary is not None:
            result['Primary'] = self.primary

        if self.time_2 is not None:
            result['Time2'] = self.time_2.to_map()

        if self.avg is not None:
            result['Avg'] = self.avg.to_map()

        if self.sum is not None:
            result['Sum'] = self.sum.to_map()

        if self.max is not None:
            result['Max'] = self.max.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricCode') is not None:
            self.metric_code = m.get('MetricCode')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Primary') is not None:
            self.primary = m.get('Primary')

        if m.get('Time2') is not None:
            temp_model = main_models.ItemsMetricValuesValueTime2()
            self.time_2 = temp_model.from_map(m.get('Time2'))

        if m.get('Avg') is not None:
            temp_model = main_models.ItemsMetricValuesValueAvg()
            self.avg = temp_model.from_map(m.get('Avg'))

        if m.get('Sum') is not None:
            temp_model = main_models.ItemsMetricValuesValueSum()
            self.sum = temp_model.from_map(m.get('Sum'))

        if m.get('Max') is not None:
            temp_model = main_models.ItemsMetricValuesValueMax()
            self.max = temp_model.from_map(m.get('Max'))

        return self

class ItemsMetricValuesValueMax(DaraModel):
    def __init__(
        self,
        change_rate_percent: float = None,
        time_1value: float = None,
        time_1display_value: str = None,
        time_2value: float = None,
        time_2display_value: str = None,
    ):
        # The change rate of the peak value in a single minute bucket, calculated as (Time 2 value − Time 1 value) / Time 1 value × 100. A value of 200 indicates a 200% increase. When the Time 1 value is 0, a finite change rate cannot be calculated. This field may not be returned and must not be treated as 0%.
        self.change_rate_percent = change_rate_percent
        # The peak value in a single minute bucket for Time 1. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.time_1value = time_1value
        # The display string of the peak value in a single minute bucket for Time 1, with the unit included.
        self.time_1display_value = time_1display_value
        # The peak value in a single minute bucket for Time 2. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.time_2value = time_2value
        # The display string of the peak value in a single minute bucket for Time 2, with the unit included.
        self.time_2display_value = time_2display_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_rate_percent is not None:
            result['ChangeRatePercent'] = self.change_rate_percent

        if self.time_1value is not None:
            result['Time1Value'] = self.time_1value

        if self.time_1display_value is not None:
            result['Time1DisplayValue'] = self.time_1display_value

        if self.time_2value is not None:
            result['Time2Value'] = self.time_2value

        if self.time_2display_value is not None:
            result['Time2DisplayValue'] = self.time_2display_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeRatePercent') is not None:
            self.change_rate_percent = m.get('ChangeRatePercent')

        if m.get('Time1Value') is not None:
            self.time_1value = m.get('Time1Value')

        if m.get('Time1DisplayValue') is not None:
            self.time_1display_value = m.get('Time1DisplayValue')

        if m.get('Time2Value') is not None:
            self.time_2value = m.get('Time2Value')

        if m.get('Time2DisplayValue') is not None:
            self.time_2display_value = m.get('Time2DisplayValue')

        return self

class ItemsMetricValuesValueSum(DaraModel):
    def __init__(
        self,
        change_rate_percent: float = None,
        time_1value: float = None,
        time_1display_value: str = None,
        time_1ratio_percent: float = None,
        time_2value: float = None,
        time_2display_value: str = None,
        time_2ratio_percent: float = None,
    ):
        # The change rate of the sum of metric values across active query minute buckets, calculated as (Time 2 value − Time 1 value) / Time 1 value × 100. A value of 200 indicates a 200% increase. When the Time 1 value is 0, a finite change rate cannot be calculated. This field may not be returned and must not be treated as 0%.
        self.change_rate_percent = change_rate_percent
        # The sum of metric values across active query minute buckets for Time 1. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.time_1value = time_1value
        # The display string of the sum of metric values across active query minute buckets for Time 1, with the unit included.
        self.time_1display_value = time_1display_value
        # The percentage of this Pattern\\"s Time 1 sum of metric values across active query minute buckets relative to the sum of the corresponding statistics for all results before dimension filtering in the current report. A value of 10 indicates 10%.
        self.time_1ratio_percent = time_1ratio_percent
        # The sum of metric values across active query minute buckets for Time 2. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.time_2value = time_2value
        # The display string of the sum of metric values across active query minute buckets for Time 2, with the unit included.
        self.time_2display_value = time_2display_value
        # The percentage of this Pattern\\"s Time 2 sum of metric values across active query minute buckets relative to the sum of the corresponding statistics for all results before dimension filtering in the current report. A value of 10 indicates 10%.
        self.time_2ratio_percent = time_2ratio_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_rate_percent is not None:
            result['ChangeRatePercent'] = self.change_rate_percent

        if self.time_1value is not None:
            result['Time1Value'] = self.time_1value

        if self.time_1display_value is not None:
            result['Time1DisplayValue'] = self.time_1display_value

        if self.time_1ratio_percent is not None:
            result['Time1RatioPercent'] = self.time_1ratio_percent

        if self.time_2value is not None:
            result['Time2Value'] = self.time_2value

        if self.time_2display_value is not None:
            result['Time2DisplayValue'] = self.time_2display_value

        if self.time_2ratio_percent is not None:
            result['Time2RatioPercent'] = self.time_2ratio_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeRatePercent') is not None:
            self.change_rate_percent = m.get('ChangeRatePercent')

        if m.get('Time1Value') is not None:
            self.time_1value = m.get('Time1Value')

        if m.get('Time1DisplayValue') is not None:
            self.time_1display_value = m.get('Time1DisplayValue')

        if m.get('Time1RatioPercent') is not None:
            self.time_1ratio_percent = m.get('Time1RatioPercent')

        if m.get('Time2Value') is not None:
            self.time_2value = m.get('Time2Value')

        if m.get('Time2DisplayValue') is not None:
            self.time_2display_value = m.get('Time2DisplayValue')

        if m.get('Time2RatioPercent') is not None:
            self.time_2ratio_percent = m.get('Time2RatioPercent')

        return self

class ItemsMetricValuesValueAvg(DaraModel):
    def __init__(
        self,
        change_rate_percent: float = None,
        time_1value: float = None,
        time_1display_value: str = None,
        time_1ratio_percent: float = None,
        time_2value: float = None,
        time_2display_value: str = None,
        time_2ratio_percent: float = None,
    ):
        # The change rate of the average value across active query minute buckets, calculated as (Time 2 value − Time 1 value) / Time 1 value × 100. A value of 200 indicates a 200% increase. When the Time 1 value is 0, a finite change rate cannot be calculated. This field may not be returned and must not be treated as 0%.
        self.change_rate_percent = change_rate_percent
        # The average value across active query minute buckets for Time 1. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.time_1value = time_1value
        # The display string of the average value across active query minute buckets for Time 1, with the unit included.
        self.time_1display_value = time_1display_value
        # The percentage of this Pattern\\"s Time 1 average value across active query minute buckets relative to the sum of the corresponding statistics for all results before dimension filtering in the current report. A value of 10 indicates 10%.
        self.time_1ratio_percent = time_1ratio_percent
        # The average value across active query minute buckets for Time 2. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.time_2value = time_2value
        # The display string of the average value across active query minute buckets for Time 2, with the unit included.
        self.time_2display_value = time_2display_value
        # The percentage of this Pattern\\"s Time 2 average value across active query minute buckets relative to the sum of the corresponding statistics for all results before dimension filtering in the current report. A value of 10 indicates 10%.
        self.time_2ratio_percent = time_2ratio_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_rate_percent is not None:
            result['ChangeRatePercent'] = self.change_rate_percent

        if self.time_1value is not None:
            result['Time1Value'] = self.time_1value

        if self.time_1display_value is not None:
            result['Time1DisplayValue'] = self.time_1display_value

        if self.time_1ratio_percent is not None:
            result['Time1RatioPercent'] = self.time_1ratio_percent

        if self.time_2value is not None:
            result['Time2Value'] = self.time_2value

        if self.time_2display_value is not None:
            result['Time2DisplayValue'] = self.time_2display_value

        if self.time_2ratio_percent is not None:
            result['Time2RatioPercent'] = self.time_2ratio_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeRatePercent') is not None:
            self.change_rate_percent = m.get('ChangeRatePercent')

        if m.get('Time1Value') is not None:
            self.time_1value = m.get('Time1Value')

        if m.get('Time1DisplayValue') is not None:
            self.time_1display_value = m.get('Time1DisplayValue')

        if m.get('Time1RatioPercent') is not None:
            self.time_1ratio_percent = m.get('Time1RatioPercent')

        if m.get('Time2Value') is not None:
            self.time_2value = m.get('Time2Value')

        if m.get('Time2DisplayValue') is not None:
            self.time_2display_value = m.get('Time2DisplayValue')

        if m.get('Time2RatioPercent') is not None:
            self.time_2ratio_percent = m.get('Time2RatioPercent')

        return self

class ItemsMetricValuesValueTime2(DaraModel):
    def __init__(
        self,
        sum_value: float = None,
        sum_display_value: str = None,
        avg_value: float = None,
        avg_display_value: str = None,
        max_value: float = None,
        max_display_value: str = None,
        sum_ratio_percent: float = None,
        avg_ratio_percent: float = None,
    ):
        # The sum of metric values across active query minute buckets for Time 2. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.sum_value = sum_value
        # The display string of the total sum for Time 2, with the unit included.
        self.sum_display_value = sum_display_value
        # The average value across active query minute buckets for Time 2, calculated as the total sum divided by the number of minute buckets that contain queries for this Pattern. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.avg_value = avg_value
        # The display string of the average value across active query minute buckets for Time 2, with the unit included.
        self.avg_display_value = avg_display_value
        # The maximum metric value in a single minute bucket for Time 2. The unit depends on MetricCode: count for QUERY_COUNT, seconds for CPU_COST, and GB (1 GB = 1024³ bytes) for SHUFFLE_SIZE, PEAK_MEMORY, and SCAN_SIZE.
        self.max_value = max_value
        # The display string of the peak value in a single minute bucket for Time 2, with the unit included.
        self.max_display_value = max_display_value
        # The percentage of this Pattern\\"s Time 2 total sum relative to the total sum of all results before dimension filtering in the current report. A value of 10 indicates 10%.
        self.sum_ratio_percent = sum_ratio_percent
        # The percentage of this Pattern\\"s Time 2 average value relative to the sum of average values across all Patterns before dimension filtering in the current report. A value of 10 indicates 10%.
        self.avg_ratio_percent = avg_ratio_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sum_value is not None:
            result['SumValue'] = self.sum_value

        if self.sum_display_value is not None:
            result['SumDisplayValue'] = self.sum_display_value

        if self.avg_value is not None:
            result['AvgValue'] = self.avg_value

        if self.avg_display_value is not None:
            result['AvgDisplayValue'] = self.avg_display_value

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.max_display_value is not None:
            result['MaxDisplayValue'] = self.max_display_value

        if self.sum_ratio_percent is not None:
            result['SumRatioPercent'] = self.sum_ratio_percent

        if self.avg_ratio_percent is not None:
            result['AvgRatioPercent'] = self.avg_ratio_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SumValue') is not None:
            self.sum_value = m.get('SumValue')

        if m.get('SumDisplayValue') is not None:
            self.sum_display_value = m.get('SumDisplayValue')

        if m.get('AvgValue') is not None:
            self.avg_value = m.get('AvgValue')

        if m.get('AvgDisplayValue') is not None:
            self.avg_display_value = m.get('AvgDisplayValue')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MaxDisplayValue') is not None:
            self.max_display_value = m.get('MaxDisplayValue')

        if m.get('SumRatioPercent') is not None:
            self.sum_ratio_percent = m.get('SumRatioPercent')

        if m.get('AvgRatioPercent') is not None:
            self.avg_ratio_percent = m.get('AvgRatioPercent')

        return self

