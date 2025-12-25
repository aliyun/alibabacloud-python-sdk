# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetEnterpriseVocAnalysisTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetEnterpriseVocAnalysisTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        statistics_overview: main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverview = None,
        status: str = None,
        usage: main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataUsage = None,
    ):
        self.error_message = error_message
        self.statistics_overview = statistics_overview
        self.status = status
        self.usage = usage

    def validate(self):
        if self.statistics_overview:
            self.statistics_overview.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.statistics_overview is not None:
            result['StatisticsOverview'] = self.statistics_overview.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('StatisticsOverview') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverview()
            self.statistics_overview = temp_model.from_map(m.get('StatisticsOverview'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Usage') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyDataUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverview(DaraModel):
    def __init__(
        self,
        count: int = None,
        filter_dimension_statistics: main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatistics = None,
        tag_dimension_statistics: main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatistics = None,
    ):
        self.count = count
        self.filter_dimension_statistics = filter_dimension_statistics
        self.tag_dimension_statistics = tag_dimension_statistics

    def validate(self):
        if self.filter_dimension_statistics:
            self.filter_dimension_statistics.validate()
        if self.tag_dimension_statistics:
            self.tag_dimension_statistics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.filter_dimension_statistics is not None:
            result['FilterDimensionStatistics'] = self.filter_dimension_statistics.to_map()

        if self.tag_dimension_statistics is not None:
            result['TagDimensionStatistics'] = self.tag_dimension_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FilterDimensionStatistics') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatistics()
            self.filter_dimension_statistics = temp_model.from_map(m.get('FilterDimensionStatistics'))

        if m.get('TagDimensionStatistics') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatistics()
            self.tag_dimension_statistics = temp_model.from_map(m.get('TagDimensionStatistics'))

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatistics(DaraModel):
    def __init__(
        self,
        tag_value_count_statistic: List[main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatisticsTagValueCountStatistic] = None,
    ):
        self.tag_value_count_statistic = tag_value_count_statistic

    def validate(self):
        if self.tag_value_count_statistic:
            for v1 in self.tag_value_count_statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagValueCountStatistic'] = []
        if self.tag_value_count_statistic is not None:
            for k1 in self.tag_value_count_statistic:
                result['TagValueCountStatistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_value_count_statistic = []
        if m.get('TagValueCountStatistic') is not None:
            for k1 in m.get('TagValueCountStatistic'):
                temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatisticsTagValueCountStatistic()
                self.tag_value_count_statistic.append(temp_model.from_map(k1))

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatisticsTagValueCountStatistic(DaraModel):
    def __init__(
        self,
        tag_name: str = None,
        tag_task_type: str = None,
        value_count: int = None,
    ):
        self.tag_name = tag_name
        self.tag_task_type = tag_task_type
        self.value_count = value_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.tag_task_type is not None:
            result['TagTaskType'] = self.tag_task_type

        if self.value_count is not None:
            result['ValueCount'] = self.value_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('TagTaskType') is not None:
            self.tag_task_type = m.get('TagTaskType')

        if m.get('ValueCount') is not None:
            self.value_count = m.get('ValueCount')

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatistics(DaraModel):
    def __init__(
        self,
        tag_value_count_statistic: List[main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatisticsTagValueCountStatistic] = None,
    ):
        self.tag_value_count_statistic = tag_value_count_statistic

    def validate(self):
        if self.tag_value_count_statistic:
            for v1 in self.tag_value_count_statistic:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TagValueCountStatistic'] = []
        if self.tag_value_count_statistic is not None:
            for k1 in self.tag_value_count_statistic:
                result['TagValueCountStatistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_value_count_statistic = []
        if m.get('TagValueCountStatistic') is not None:
            for k1 in m.get('TagValueCountStatistic'):
                temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatisticsTagValueCountStatistic()
                self.tag_value_count_statistic.append(temp_model.from_map(k1))

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatisticsTagValueCountStatistic(DaraModel):
    def __init__(
        self,
        tag_name: str = None,
        tag_task_type: str = None,
        value_count: int = None,
    ):
        self.tag_name = tag_name
        self.tag_task_type = tag_task_type
        self.value_count = value_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.tag_task_type is not None:
            result['TagTaskType'] = self.tag_task_type

        if self.value_count is not None:
            result['ValueCount'] = self.value_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('TagTaskType') is not None:
            self.tag_task_type = m.get('TagTaskType')

        if m.get('ValueCount') is not None:
            self.value_count = m.get('ValueCount')

        return self

