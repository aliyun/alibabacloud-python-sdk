# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetSaasDataUnitUsageResponseBody(DaraModel):
    def __init__(
        self,
        distribution: List[main_models.GetSaasDataUnitUsageResponseBodyDistribution] = None,
        end_time: str = None,
        request_id: str = None,
        service_id: str = None,
        start_time: str = None,
        summary: main_models.GetSaasDataUnitUsageResponseBodySummary = None,
        time_series: List[main_models.GetSaasDataUnitUsageResponseBodyTimeSeries] = None,
        warnings: List[main_models.GetSaasDataUnitUsageResponseBodyWarnings] = None,
    ):
        # The business distribution. The items are sorted in descending order of DataUnit. Items with unknown amounts are placed at the end. Items with the same value are sorted in ascending order of scenario code, project ID, and name. The items are grouped by scenario and project ID. Items without an ID but with a name are grouped by name. Records missing both are grouped as unassociated projects. The sum of all items in the complete result equals the summary. Missing or blank log scenarios are classified as other. Scenarios with values but no configured mapping retain the original values as codes and display names, and are normally included in the total. No empty rows are created for other if there are no records.
        self.distribution = distribution
        # The actual end time of the query.
        self.end_time = end_time
        # The request ID.
        self.request_id = request_id
        # The SaaS service ID.
        self.service_id = service_id
        # The actual start time of the query.
        self.start_time = start_time
        # The usage summary.
        self.summary = summary
        # The time trend. The items are sorted in ascending order of the UTC bucket start time. Zero buckets are padded for complete queries. The value is null for unknown amounts and is not replaced with zero.
        self.time_series = time_series
        # The product notifications.
        self.warnings = warnings

    def validate(self):
        if self.distribution:
            for v1 in self.distribution:
                 if v1:
                    v1.validate()
        if self.summary:
            self.summary.validate()
        if self.time_series:
            for v1 in self.time_series:
                 if v1:
                    v1.validate()
        if self.warnings:
            for v1 in self.warnings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Distribution'] = []
        if self.distribution is not None:
            for k1 in self.distribution:
                result['Distribution'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        result['TimeSeries'] = []
        if self.time_series is not None:
            for k1 in self.time_series:
                result['TimeSeries'].append(k1.to_map() if k1 else None)

        result['Warnings'] = []
        if self.warnings is not None:
            for k1 in self.warnings:
                result['Warnings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.distribution = []
        if m.get('Distribution') is not None:
            for k1 in m.get('Distribution'):
                temp_model = main_models.GetSaasDataUnitUsageResponseBodyDistribution()
                self.distribution.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Summary') is not None:
            temp_model = main_models.GetSaasDataUnitUsageResponseBodySummary()
            self.summary = temp_model.from_map(m.get('Summary'))

        self.time_series = []
        if m.get('TimeSeries') is not None:
            for k1 in m.get('TimeSeries'):
                temp_model = main_models.GetSaasDataUnitUsageResponseBodyTimeSeries()
                self.time_series.append(temp_model.from_map(k1))

        self.warnings = []
        if m.get('Warnings') is not None:
            for k1 in m.get('Warnings'):
                temp_model = main_models.GetSaasDataUnitUsageResponseBodyWarnings()
                self.warnings.append(temp_model.from_map(k1))

        return self

class GetSaasDataUnitUsageResponseBodyWarnings(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The notification code. Valid values include DATA_INCOMPLETE and DATA_UNIT_PENDING.
        self.code = code
        # The notification message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class GetSaasDataUnitUsageResponseBodyTimeSeries(DaraModel):
    def __init__(
        self,
        data_unit: str = None,
        scenes: List[main_models.GetSaasDataUnitUsageResponseBodyTimeSeriesScenes] = None,
        time: str = None,
    ):
        # The exact non-negative decimal string. Floating-point or exponential formats are not used. The value is null when the amount is incomplete.
        self.data_unit = data_unit
        # The scenario usage within the bucket.
        self.scenes = scenes
        # The start time of the UTC bucket.
        self.time = time

    def validate(self):
        if self.scenes:
            for v1 in self.scenes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_unit is not None:
            result['DataUnit'] = self.data_unit

        result['Scenes'] = []
        if self.scenes is not None:
            for k1 in self.scenes:
                result['Scenes'].append(k1.to_map() if k1 else None)

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataUnit') is not None:
            self.data_unit = m.get('DataUnit')

        self.scenes = []
        if m.get('Scenes') is not None:
            for k1 in m.get('Scenes'):
                temp_model = main_models.GetSaasDataUnitUsageResponseBodyTimeSeriesScenes()
                self.scenes.append(temp_model.from_map(k1))

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class GetSaasDataUnitUsageResponseBodyTimeSeriesScenes(DaraModel):
    def __init__(
        self,
        data_unit: str = None,
        project_id: str = None,
        project_name: str = None,
        usage_scene: str = None,
    ):
        # The exact non-negative decimal string. Floating-point or exponential formats are not used. The value is null when the amount is incomplete.
        self.data_unit = data_unit
        # The project attribution at the time of the call. The value is null when missing, which does not affect the total amount.
        self.project_id = project_id
        # The project name. For the same scenario and project ID, the latest non-empty name snapshot within the query range is used. If multiple snapshots exist in the same second, the maximum value in lexicographical order is used. The value is null when missing.
        self.project_name = project_name
        # The business scenario code.
        self.usage_scene = usage_scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_unit is not None:
            result['DataUnit'] = self.data_unit

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.usage_scene is not None:
            result['UsageScene'] = self.usage_scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataUnit') is not None:
            self.data_unit = m.get('DataUnit')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UsageScene') is not None:
            self.usage_scene = m.get('UsageScene')

        return self

class GetSaasDataUnitUsageResponseBodySummary(DaraModel):
    def __init__(
        self,
        data_unit: str = None,
    ):
        # The exact non-negative decimal string. Floating-point or exponential formats are not used. The value is null when the amount is incomplete.
        self.data_unit = data_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_unit is not None:
            result['DataUnit'] = self.data_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataUnit') is not None:
            self.data_unit = m.get('DataUnit')

        return self

class GetSaasDataUnitUsageResponseBodyDistribution(DaraModel):
    def __init__(
        self,
        data_unit: str = None,
        project_id: str = None,
        project_name: str = None,
        usage_scene: str = None,
        usage_scene_name: str = None,
    ):
        # The exact non-negative decimal string. Floating-point or exponential formats are not used. The value is null when the amount is incomplete.
        self.data_unit = data_unit
        # The project attribution at the time of the call. The value is null when missing, which does not affect the total amount.
        self.project_id = project_id
        # The project name. For the same scenario and project ID, the latest non-empty name snapshot within the query range is used. If multiple snapshots exist in the same second, the maximum value in lexicographical order is used. The value is null when missing.
        self.project_name = project_name
        # The business scenario code.
        self.usage_scene = usage_scene
        # The display name of the business scenario. This name is supplemented by a dictionary that maps the original Meta values to Chinese names, and is not an SLS field. UsageScene always retains the original log value. If no Chinese name is available, the original value is used as the name. Blank values are classified as other. Different codes with the same Chinese name are not merged.
        self.usage_scene_name = usage_scene_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_unit is not None:
            result['DataUnit'] = self.data_unit

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.usage_scene is not None:
            result['UsageScene'] = self.usage_scene

        if self.usage_scene_name is not None:
            result['UsageSceneName'] = self.usage_scene_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataUnit') is not None:
            self.data_unit = m.get('DataUnit')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('UsageScene') is not None:
            self.usage_scene = m.get('UsageScene')

        if m.get('UsageSceneName') is not None:
            self.usage_scene_name = m.get('UsageSceneName')

        return self

