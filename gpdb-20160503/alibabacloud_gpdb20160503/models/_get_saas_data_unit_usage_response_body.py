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
        # 按DataUnit降序，未知金额排末尾，同值按场景码、项目ID和名称升序。按场景和项目ID分组；无ID但有名称按名称分组；两者均缺失的记录为未关联项目。完整结果各项之和等于汇总；缺失或空白的日志场景归other（其他）；有值但未配置映射的场景保留原值作为编码和展示名，正常计入总量；无记录的other不创建空行。
        self.distribution = distribution
        self.end_time = end_time
        self.request_id = request_id
        self.service_id = service_id
        self.start_time = start_time
        self.summary = summary
        # 按UTC桶起点升序。完整查询补齐零桶；未知金额为null，不以零替代。
        self.time_series = time_series
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
        # 包括DATA_INCOMPLETE和DATA_UNIT_PENDING。
        self.code = code
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
        # 精确非负十进制字符串，不使用浮点或指数格式；金额不完整时为null。
        self.data_unit = data_unit
        self.scenes = scenes
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
        # 精确非负十进制字符串，不使用浮点或指数格式；金额不完整时为null。
        self.data_unit = data_unit
        # 调用时的项目归因；缺失时为null，不影响总量。
        self.project_id = project_id
        # 同一场景和项目ID取查询范围内最新非空名称快照，同秒取字典序最大值；缺失为null。
        self.project_name = project_name
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
        # 精确非负十进制字符串，不使用浮点或指数格式；金额不完整时为null。
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
        # 精确非负十进制字符串，不使用浮点或指数格式；金额不完整时为null。
        self.data_unit = data_unit
        # 调用时的项目归因；缺失时为null，不影响总量。
        self.project_id = project_id
        # 同一场景和项目ID取查询范围内最新非空名称快照，同秒取字典序最大值；缺失为null。
        self.project_name = project_name
        self.usage_scene = usage_scene
        # 由Meta原值到中文名的字典补充，不是SLS字段。UsageScene始终保留日志原值；无中文名则名称也用原值；空白归其他。同中文名不同编码不合并。
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

