# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ListDataDiagnosisReportsResponseBody(DaraModel):
    def __init__(
        self,
        exception_rate: List[main_models.ListDataDiagnosisReportsResponseBodyExceptionRate] = None,
        reports_of_abnormal_behavior: List[List[main_models.ListDataDiagnosisReportsResponseBodyReportsOfAbnormalBehavior]] = None,
        reports_of_base_statistics: List[List[main_models.ListDataDiagnosisReportsResponseBodyReportsOfBaseStatistics]] = None,
        reports_of_change_rate_data: List[List[main_models.ListDataDiagnosisReportsResponseBodyReportsOfChangeRateData]] = None,
        reports_of_join_tables: List[List[main_models.ListDataDiagnosisReportsResponseBodyReportsOfJoinTables]] = None,
        reports_of_preference_statistics_cycle: List[List[main_models.ListDataDiagnosisReportsResponseBodyReportsOfPreferenceStatisticsCycle]] = None,
        request_id: str = None,
        type: str = None,
    ):
        self.exception_rate = exception_rate
        self.reports_of_abnormal_behavior = reports_of_abnormal_behavior
        self.reports_of_base_statistics = reports_of_base_statistics
        self.reports_of_change_rate_data = reports_of_change_rate_data
        self.reports_of_join_tables = reports_of_join_tables
        self.reports_of_preference_statistics_cycle = reports_of_preference_statistics_cycle
        self.request_id = request_id
        self.type = type

    def validate(self):
        if self.exception_rate:
            for v1 in self.exception_rate:
                 if v1:
                    v1.validate()
        if self.reports_of_abnormal_behavior:
            for v1 in self.reports_of_abnormal_behavior:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.reports_of_base_statistics:
            for v1 in self.reports_of_base_statistics:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.reports_of_change_rate_data:
            for v1 in self.reports_of_change_rate_data:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.reports_of_join_tables:
            for v1 in self.reports_of_join_tables:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.reports_of_preference_statistics_cycle:
            for v1 in self.reports_of_preference_statistics_cycle:
                for v2 in v1:
                     if v2:
                        v2.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExceptionRate'] = []
        if self.exception_rate is not None:
            for k1 in self.exception_rate:
                result['ExceptionRate'].append(k1.to_map() if k1 else None)

        result['ReportsOfAbnormalBehavior'] = []
        if self.reports_of_abnormal_behavior is not None:
            for k1 in self.reports_of_abnormal_behavior:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['ReportsOfAbnormalBehavior'].append(l1)

        result['ReportsOfBaseStatistics'] = []
        if self.reports_of_base_statistics is not None:
            for k1 in self.reports_of_base_statistics:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['ReportsOfBaseStatistics'].append(l1)

        result['ReportsOfChangeRateData'] = []
        if self.reports_of_change_rate_data is not None:
            for k1 in self.reports_of_change_rate_data:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['ReportsOfChangeRateData'].append(l1)

        result['ReportsOfJoinTables'] = []
        if self.reports_of_join_tables is not None:
            for k1 in self.reports_of_join_tables:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['ReportsOfJoinTables'].append(l1)

        result['ReportsOfPreferenceStatisticsCycle'] = []
        if self.reports_of_preference_statistics_cycle is not None:
            for k1 in self.reports_of_preference_statistics_cycle:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['ReportsOfPreferenceStatisticsCycle'].append(l1)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exception_rate = []
        if m.get('ExceptionRate') is not None:
            for k1 in m.get('ExceptionRate'):
                temp_model = main_models.ListDataDiagnosisReportsResponseBodyExceptionRate()
                self.exception_rate.append(temp_model.from_map(k1))

        self.reports_of_abnormal_behavior = []
        if m.get('ReportsOfAbnormalBehavior') is not None:
            for k1 in m.get('ReportsOfAbnormalBehavior'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.ListDataDiagnosisReportsResponseBodyReportsOfAbnormalBehavior()
                    l1.append(temp_model.from_map(k2))
                self.reports_of_abnormal_behavior.append(l1)

        self.reports_of_base_statistics = []
        if m.get('ReportsOfBaseStatistics') is not None:
            for k1 in m.get('ReportsOfBaseStatistics'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.ListDataDiagnosisReportsResponseBodyReportsOfBaseStatistics()
                    l1.append(temp_model.from_map(k2))
                self.reports_of_base_statistics.append(l1)

        self.reports_of_change_rate_data = []
        if m.get('ReportsOfChangeRateData') is not None:
            for k1 in m.get('ReportsOfChangeRateData'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.ListDataDiagnosisReportsResponseBodyReportsOfChangeRateData()
                    l1.append(temp_model.from_map(k2))
                self.reports_of_change_rate_data.append(l1)

        self.reports_of_join_tables = []
        if m.get('ReportsOfJoinTables') is not None:
            for k1 in m.get('ReportsOfJoinTables'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.ListDataDiagnosisReportsResponseBodyReportsOfJoinTables()
                    l1.append(temp_model.from_map(k2))
                self.reports_of_join_tables.append(l1)

        self.reports_of_preference_statistics_cycle = []
        if m.get('ReportsOfPreferenceStatisticsCycle') is not None:
            for k1 in m.get('ReportsOfPreferenceStatisticsCycle'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.ListDataDiagnosisReportsResponseBodyReportsOfPreferenceStatisticsCycle()
                    l1.append(temp_model.from_map(k2))
                self.reports_of_preference_statistics_cycle.append(l1)

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListDataDiagnosisReportsResponseBodyReportsOfPreferenceStatisticsCycle(DaraModel):
    def __init__(
        self,
        cycle_remain_rate: str = None,
        single_remain_rate: str = None,
        ds: str = None,
        days: str = None,
        ever_appeared_rate: str = None,
        period: str = None,
        period_remain_rate: str = None,
        period_remain_count: int = None,
        period_internal: int = None,
    ):
        self.cycle_remain_rate = cycle_remain_rate
        self.single_remain_rate = single_remain_rate
        self.ds = ds
        self.days = days
        self.ever_appeared_rate = ever_appeared_rate
        self.period = period
        self.period_remain_rate = period_remain_rate
        self.period_remain_count = period_remain_count
        self.period_internal = period_internal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_remain_rate is not None:
            result['CycleRemainRate'] = self.cycle_remain_rate

        if self.single_remain_rate is not None:
            result['SingleRemainRate'] = self.single_remain_rate

        if self.ds is not None:
            result['Ds'] = self.ds

        if self.days is not None:
            result['Days'] = self.days

        if self.ever_appeared_rate is not None:
            result['EverAppearedRate'] = self.ever_appeared_rate

        if self.period is not None:
            result['Period'] = self.period

        if self.period_remain_rate is not None:
            result['PeriodRemainRate'] = self.period_remain_rate

        if self.period_remain_count is not None:
            result['PeriodRemainCount'] = self.period_remain_count

        if self.period_internal is not None:
            result['PeriodInternal'] = self.period_internal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleRemainRate') is not None:
            self.cycle_remain_rate = m.get('CycleRemainRate')

        if m.get('SingleRemainRate') is not None:
            self.single_remain_rate = m.get('SingleRemainRate')

        if m.get('Ds') is not None:
            self.ds = m.get('Ds')

        if m.get('Days') is not None:
            self.days = m.get('Days')

        if m.get('EverAppearedRate') is not None:
            self.ever_appeared_rate = m.get('EverAppearedRate')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodRemainRate') is not None:
            self.period_remain_rate = m.get('PeriodRemainRate')

        if m.get('PeriodRemainCount') is not None:
            self.period_remain_count = m.get('PeriodRemainCount')

        if m.get('PeriodInternal') is not None:
            self.period_internal = m.get('PeriodInternal')

        return self

class ListDataDiagnosisReportsResponseBodyReportsOfJoinTables(DaraModel):
    def __init__(
        self,
        ds: str = None,
        join_field: str = None,
        left_except_rate: str = None,
        right_except_rate: str = None,
        flag: str = None,
        feature_name: str = None,
        feature_value: str = None,
        percent: str = None,
        quantile: str = None,
        value_count: str = None,
        value_percent: str = None,
        value_quantile: str = None,
    ):
        self.ds = ds
        self.join_field = join_field
        self.left_except_rate = left_except_rate
        self.right_except_rate = right_except_rate
        self.flag = flag
        self.feature_name = feature_name
        self.feature_value = feature_value
        self.percent = percent
        self.quantile = quantile
        self.value_count = value_count
        self.value_percent = value_percent
        self.value_quantile = value_quantile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds is not None:
            result['Ds'] = self.ds

        if self.join_field is not None:
            result['JoinField'] = self.join_field

        if self.left_except_rate is not None:
            result['LeftExceptRate'] = self.left_except_rate

        if self.right_except_rate is not None:
            result['RightExceptRate'] = self.right_except_rate

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_value is not None:
            result['FeatureValue'] = self.feature_value

        if self.percent is not None:
            result['Percent'] = self.percent

        if self.quantile is not None:
            result['Quantile'] = self.quantile

        if self.value_count is not None:
            result['ValueCount'] = self.value_count

        if self.value_percent is not None:
            result['ValuePercent'] = self.value_percent

        if self.value_quantile is not None:
            result['ValueQuantile'] = self.value_quantile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ds') is not None:
            self.ds = m.get('Ds')

        if m.get('JoinField') is not None:
            self.join_field = m.get('JoinField')

        if m.get('LeftExceptRate') is not None:
            self.left_except_rate = m.get('LeftExceptRate')

        if m.get('RightExceptRate') is not None:
            self.right_except_rate = m.get('RightExceptRate')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureValue') is not None:
            self.feature_value = m.get('FeatureValue')

        if m.get('Percent') is not None:
            self.percent = m.get('Percent')

        if m.get('Quantile') is not None:
            self.quantile = m.get('Quantile')

        if m.get('ValueCount') is not None:
            self.value_count = m.get('ValueCount')

        if m.get('ValuePercent') is not None:
            self.value_percent = m.get('ValuePercent')

        if m.get('ValueQuantile') is not None:
            self.value_quantile = m.get('ValueQuantile')

        return self

class ListDataDiagnosisReportsResponseBodyReportsOfChangeRateData(DaraModel):
    def __init__(
        self,
        ds: str = None,
        flag: str = None,
        change_count: str = None,
        change_rate: str = None,
    ):
        self.ds = ds
        self.flag = flag
        self.change_count = change_count
        self.change_rate = change_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds is not None:
            result['Ds'] = self.ds

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.change_count is not None:
            result['ChangeCount'] = self.change_count

        if self.change_rate is not None:
            result['ChangeRate'] = self.change_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ds') is not None:
            self.ds = m.get('Ds')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('ChangeCount') is not None:
            self.change_count = m.get('ChangeCount')

        if m.get('ChangeRate') is not None:
            self.change_rate = m.get('ChangeRate')

        return self

class ListDataDiagnosisReportsResponseBodyReportsOfBaseStatistics(DaraModel):
    def __init__(
        self,
        default_null_count: str = None,
        default_null_rate: str = None,
        ds: str = None,
        feature_name: str = None,
        feature_type: str = None,
        null_count: str = None,
        null_rate: str = None,
        total_count: str = None,
        unique_count: str = None,
        value_max: str = None,
        value_median: str = None,
        value_min: str = None,
        value_quantile_1: str = None,
        value_quantile_5: str = None,
        value_quantile_25: str = None,
        value_quantile_75: str = None,
        value_quantile_95: str = None,
        value_quantile_99: str = None,
        rn: str = None,
        frequency_max: str = None,
        frequency_median: str = None,
        frequency_min: str = None,
        frequency_quantile_1: str = None,
        frequency_quantile_5: str = None,
        frequency_quantile_25: str = None,
        frequency_quantile_75: str = None,
        frequency_quantile_95: str = None,
        frequency_quantile_99: str = None,
        distribution: str = None,
        rank_id: str = None,
        feature_value: str = None,
        value_count: str = None,
        value_percent: str = None,
        value_quantile: str = None,
        feature_frequency: str = None,
        frequency_count: str = None,
        frequency_percent: str = None,
        frequency_quantile: str = None,
    ):
        self.default_null_count = default_null_count
        self.default_null_rate = default_null_rate
        self.ds = ds
        self.feature_name = feature_name
        self.feature_type = feature_type
        self.null_count = null_count
        self.null_rate = null_rate
        self.total_count = total_count
        self.unique_count = unique_count
        self.value_max = value_max
        self.value_median = value_median
        self.value_min = value_min
        self.value_quantile_1 = value_quantile_1
        self.value_quantile_5 = value_quantile_5
        self.value_quantile_25 = value_quantile_25
        self.value_quantile_75 = value_quantile_75
        self.value_quantile_95 = value_quantile_95
        self.value_quantile_99 = value_quantile_99
        self.rn = rn
        self.frequency_max = frequency_max
        self.frequency_median = frequency_median
        self.frequency_min = frequency_min
        self.frequency_quantile_1 = frequency_quantile_1
        self.frequency_quantile_5 = frequency_quantile_5
        self.frequency_quantile_25 = frequency_quantile_25
        self.frequency_quantile_75 = frequency_quantile_75
        self.frequency_quantile_95 = frequency_quantile_95
        self.frequency_quantile_99 = frequency_quantile_99
        self.distribution = distribution
        self.rank_id = rank_id
        self.feature_value = feature_value
        self.value_count = value_count
        self.value_percent = value_percent
        self.value_quantile = value_quantile
        self.feature_frequency = feature_frequency
        self.frequency_count = frequency_count
        self.frequency_percent = frequency_percent
        self.frequency_quantile = frequency_quantile

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_null_count is not None:
            result['DefaultNullCount'] = self.default_null_count

        if self.default_null_rate is not None:
            result['DefaultNullRate'] = self.default_null_rate

        if self.ds is not None:
            result['Ds'] = self.ds

        if self.feature_name is not None:
            result['FeatureName'] = self.feature_name

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.null_count is not None:
            result['NullCount'] = self.null_count

        if self.null_rate is not None:
            result['NullRate'] = self.null_rate

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.unique_count is not None:
            result['UniqueCount'] = self.unique_count

        if self.value_max is not None:
            result['ValueMax'] = self.value_max

        if self.value_median is not None:
            result['ValueMedian'] = self.value_median

        if self.value_min is not None:
            result['ValueMin'] = self.value_min

        if self.value_quantile_1 is not None:
            result['ValueQuantile1'] = self.value_quantile_1

        if self.value_quantile_5 is not None:
            result['ValueQuantile5'] = self.value_quantile_5

        if self.value_quantile_25 is not None:
            result['ValueQuantile25'] = self.value_quantile_25

        if self.value_quantile_75 is not None:
            result['ValueQuantile75'] = self.value_quantile_75

        if self.value_quantile_95 is not None:
            result['ValueQuantile95'] = self.value_quantile_95

        if self.value_quantile_99 is not None:
            result['ValueQuantile99'] = self.value_quantile_99

        if self.rn is not None:
            result['Rn'] = self.rn

        if self.frequency_max is not None:
            result['FrequencyMax'] = self.frequency_max

        if self.frequency_median is not None:
            result['FrequencyMedian'] = self.frequency_median

        if self.frequency_min is not None:
            result['FrequencyMin'] = self.frequency_min

        if self.frequency_quantile_1 is not None:
            result['FrequencyQuantile1'] = self.frequency_quantile_1

        if self.frequency_quantile_5 is not None:
            result['FrequencyQuantile5'] = self.frequency_quantile_5

        if self.frequency_quantile_25 is not None:
            result['FrequencyQuantile25'] = self.frequency_quantile_25

        if self.frequency_quantile_75 is not None:
            result['FrequencyQuantile75'] = self.frequency_quantile_75

        if self.frequency_quantile_95 is not None:
            result['FrequencyQuantile95'] = self.frequency_quantile_95

        if self.frequency_quantile_99 is not None:
            result['FrequencyQuantile99'] = self.frequency_quantile_99

        if self.distribution is not None:
            result['Distribution'] = self.distribution

        if self.rank_id is not None:
            result['RankId'] = self.rank_id

        if self.feature_value is not None:
            result['FeatureValue'] = self.feature_value

        if self.value_count is not None:
            result['ValueCount'] = self.value_count

        if self.value_percent is not None:
            result['ValuePercent'] = self.value_percent

        if self.value_quantile is not None:
            result['ValueQuantile'] = self.value_quantile

        if self.feature_frequency is not None:
            result['FeatureFrequency'] = self.feature_frequency

        if self.frequency_count is not None:
            result['FrequencyCount'] = self.frequency_count

        if self.frequency_percent is not None:
            result['FrequencyPercent'] = self.frequency_percent

        if self.frequency_quantile is not None:
            result['FrequencyQuantile'] = self.frequency_quantile

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultNullCount') is not None:
            self.default_null_count = m.get('DefaultNullCount')

        if m.get('DefaultNullRate') is not None:
            self.default_null_rate = m.get('DefaultNullRate')

        if m.get('Ds') is not None:
            self.ds = m.get('Ds')

        if m.get('FeatureName') is not None:
            self.feature_name = m.get('FeatureName')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('NullCount') is not None:
            self.null_count = m.get('NullCount')

        if m.get('NullRate') is not None:
            self.null_rate = m.get('NullRate')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UniqueCount') is not None:
            self.unique_count = m.get('UniqueCount')

        if m.get('ValueMax') is not None:
            self.value_max = m.get('ValueMax')

        if m.get('ValueMedian') is not None:
            self.value_median = m.get('ValueMedian')

        if m.get('ValueMin') is not None:
            self.value_min = m.get('ValueMin')

        if m.get('ValueQuantile1') is not None:
            self.value_quantile_1 = m.get('ValueQuantile1')

        if m.get('ValueQuantile5') is not None:
            self.value_quantile_5 = m.get('ValueQuantile5')

        if m.get('ValueQuantile25') is not None:
            self.value_quantile_25 = m.get('ValueQuantile25')

        if m.get('ValueQuantile75') is not None:
            self.value_quantile_75 = m.get('ValueQuantile75')

        if m.get('ValueQuantile95') is not None:
            self.value_quantile_95 = m.get('ValueQuantile95')

        if m.get('ValueQuantile99') is not None:
            self.value_quantile_99 = m.get('ValueQuantile99')

        if m.get('Rn') is not None:
            self.rn = m.get('Rn')

        if m.get('FrequencyMax') is not None:
            self.frequency_max = m.get('FrequencyMax')

        if m.get('FrequencyMedian') is not None:
            self.frequency_median = m.get('FrequencyMedian')

        if m.get('FrequencyMin') is not None:
            self.frequency_min = m.get('FrequencyMin')

        if m.get('FrequencyQuantile1') is not None:
            self.frequency_quantile_1 = m.get('FrequencyQuantile1')

        if m.get('FrequencyQuantile5') is not None:
            self.frequency_quantile_5 = m.get('FrequencyQuantile5')

        if m.get('FrequencyQuantile25') is not None:
            self.frequency_quantile_25 = m.get('FrequencyQuantile25')

        if m.get('FrequencyQuantile75') is not None:
            self.frequency_quantile_75 = m.get('FrequencyQuantile75')

        if m.get('FrequencyQuantile95') is not None:
            self.frequency_quantile_95 = m.get('FrequencyQuantile95')

        if m.get('FrequencyQuantile99') is not None:
            self.frequency_quantile_99 = m.get('FrequencyQuantile99')

        if m.get('Distribution') is not None:
            self.distribution = m.get('Distribution')

        if m.get('RankId') is not None:
            self.rank_id = m.get('RankId')

        if m.get('FeatureValue') is not None:
            self.feature_value = m.get('FeatureValue')

        if m.get('ValueCount') is not None:
            self.value_count = m.get('ValueCount')

        if m.get('ValuePercent') is not None:
            self.value_percent = m.get('ValuePercent')

        if m.get('ValueQuantile') is not None:
            self.value_quantile = m.get('ValueQuantile')

        if m.get('FeatureFrequency') is not None:
            self.feature_frequency = m.get('FeatureFrequency')

        if m.get('FrequencyCount') is not None:
            self.frequency_count = m.get('FrequencyCount')

        if m.get('FrequencyPercent') is not None:
            self.frequency_percent = m.get('FrequencyPercent')

        if m.get('FrequencyQuantile') is not None:
            self.frequency_quantile = m.get('FrequencyQuantile')

        return self

class ListDataDiagnosisReportsResponseBodyReportsOfAbnormalBehavior(DaraModel):
    def __init__(
        self,
        ds: str = None,
        rank_id: str = None,
        conversion_rate: str = None,
        conversion_rate_ids: str = None,
        down_stream_count: str = None,
        down_stream_count_ids: str = None,
        granularity: str = None,
        up_stream_count: str = None,
        up_stream_count_ids: str = None,
        distribution: str = None,
        indicator_name: str = None,
        exception_rate: str = None,
    ):
        self.ds = ds
        self.rank_id = rank_id
        self.conversion_rate = conversion_rate
        self.conversion_rate_ids = conversion_rate_ids
        self.down_stream_count = down_stream_count
        self.down_stream_count_ids = down_stream_count_ids
        self.granularity = granularity
        self.up_stream_count = up_stream_count
        self.up_stream_count_ids = up_stream_count_ids
        self.distribution = distribution
        self.indicator_name = indicator_name
        self.exception_rate = exception_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ds is not None:
            result['Ds'] = self.ds

        if self.rank_id is not None:
            result['RankId'] = self.rank_id

        if self.conversion_rate is not None:
            result['ConversionRate'] = self.conversion_rate

        if self.conversion_rate_ids is not None:
            result['ConversionRateIds'] = self.conversion_rate_ids

        if self.down_stream_count is not None:
            result['DownStreamCount'] = self.down_stream_count

        if self.down_stream_count_ids is not None:
            result['DownStreamCountIds'] = self.down_stream_count_ids

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.up_stream_count is not None:
            result['UpStreamCount'] = self.up_stream_count

        if self.up_stream_count_ids is not None:
            result['UpStreamCountIds'] = self.up_stream_count_ids

        if self.distribution is not None:
            result['Distribution'] = self.distribution

        if self.indicator_name is not None:
            result['IndicatorName'] = self.indicator_name

        if self.exception_rate is not None:
            result['ExceptionRate'] = self.exception_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ds') is not None:
            self.ds = m.get('Ds')

        if m.get('RankId') is not None:
            self.rank_id = m.get('RankId')

        if m.get('ConversionRate') is not None:
            self.conversion_rate = m.get('ConversionRate')

        if m.get('ConversionRateIds') is not None:
            self.conversion_rate_ids = m.get('ConversionRateIds')

        if m.get('DownStreamCount') is not None:
            self.down_stream_count = m.get('DownStreamCount')

        if m.get('DownStreamCountIds') is not None:
            self.down_stream_count_ids = m.get('DownStreamCountIds')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('UpStreamCount') is not None:
            self.up_stream_count = m.get('UpStreamCount')

        if m.get('UpStreamCountIds') is not None:
            self.up_stream_count_ids = m.get('UpStreamCountIds')

        if m.get('Distribution') is not None:
            self.distribution = m.get('Distribution')

        if m.get('IndicatorName') is not None:
            self.indicator_name = m.get('IndicatorName')

        if m.get('ExceptionRate') is not None:
            self.exception_rate = m.get('ExceptionRate')

        return self

class ListDataDiagnosisReportsResponseBodyExceptionRate(DaraModel):
    def __init__(
        self,
        group: str = None,
        message: str = None,
        type: str = None,
    ):
        self.group = group
        self.message = message
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['Group'] = self.group

        if self.message is not None:
            result['Message'] = self.message

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

