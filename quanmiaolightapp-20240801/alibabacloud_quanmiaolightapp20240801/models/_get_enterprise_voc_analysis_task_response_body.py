# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quanmiaolightapp20240801 import models as main_models
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
        # Id of the request
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        model_id: str = None,
        model_name: str = None,
        statistics_overview: main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverview = None,
        status: str = None,
        usage: main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataUsage = None,
    ):
        self.error_message = error_message
        self.model_id = model_id
        self.model_name = model_name
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
            result['errorMessage'] = self.error_message

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.statistics_overview is not None:
            result['statisticsOverview'] = self.statistics_overview.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.usage is not None:
            result['usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('statisticsOverview') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverview()
            self.statistics_overview = temp_model.from_map(m.get('statisticsOverview'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('usage') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataUsage()
            self.usage = temp_model.from_map(m.get('usage'))

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
            result['inputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')

        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')

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
            result['count'] = self.count

        if self.filter_dimension_statistics is not None:
            result['filterDimensionStatistics'] = self.filter_dimension_statistics.to_map()

        if self.tag_dimension_statistics is not None:
            result['tagDimensionStatistics'] = self.tag_dimension_statistics.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('filterDimensionStatistics') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatistics()
            self.filter_dimension_statistics = temp_model.from_map(m.get('filterDimensionStatistics'))

        if m.get('tagDimensionStatistics') is not None:
            temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatistics()
            self.tag_dimension_statistics = temp_model.from_map(m.get('tagDimensionStatistics'))

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
        result['tagValueCountStatistic'] = []
        if self.tag_value_count_statistic is not None:
            for k1 in self.tag_value_count_statistic:
                result['tagValueCountStatistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_value_count_statistic = []
        if m.get('tagValueCountStatistic') is not None:
            for k1 in m.get('tagValueCountStatistic'):
                temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatisticsTagValueCountStatistic()
                self.tag_value_count_statistic.append(temp_model.from_map(k1))

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewTagDimensionStatisticsTagValueCountStatistic(DaraModel):
    def __init__(
        self,
        tag_name: str = None,
        value_count: int = None,
    ):
        self.tag_name = tag_name
        self.value_count = value_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        if self.value_count is not None:
            result['valueCount'] = self.value_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        if m.get('valueCount') is not None:
            self.value_count = m.get('valueCount')

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
        result['tagValueCountStatistic'] = []
        if self.tag_value_count_statistic is not None:
            for k1 in self.tag_value_count_statistic:
                result['tagValueCountStatistic'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_value_count_statistic = []
        if m.get('tagValueCountStatistic') is not None:
            for k1 in m.get('tagValueCountStatistic'):
                temp_model = main_models.GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatisticsTagValueCountStatistic()
                self.tag_value_count_statistic.append(temp_model.from_map(k1))

        return self

class GetEnterpriseVocAnalysisTaskResponseBodyDataStatisticsOverviewFilterDimensionStatisticsTagValueCountStatistic(DaraModel):
    def __init__(
        self,
        tag_name: str = None,
        value_count: int = None,
    ):
        self.tag_name = tag_name
        self.value_count = value_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        if self.value_count is not None:
            result['valueCount'] = self.value_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        if m.get('valueCount') is not None:
            self.value_count = m.get('valueCount')

        return self

