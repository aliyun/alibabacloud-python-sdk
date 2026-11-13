# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetMetricDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        group_by: List[str] = None,
        metric_names: List[str] = None,
        period: int = None,
        sandbox_id: str = None,
        sandbox_plan: str = None,
        start_time: str = None,
        team_id: str = None,
        template_id: str = None,
        time: str = None,
    ):
        # 时序查询的结束时间，区间不含此时刻。使用 UTC 整秒时间，须晚于 startTime。一次最多查询 7 天。区间须包含至少一个按 period 对齐的时间点，且这些时间点不能晚于当前时间。
        self.end_time = end_time
        # 例如，按 teamID 分组可分别查看各团队的指标。可组合最多 4 个不同的分组键，可用键因指标而异。不填时返回查询范围的整体结果。
        self.group_by = group_by
        # 要查询的指标名称。一次可查询 1～16 个不同的指标。可选指标和查询范围见指标目录。
        # 
        # This parameter is required.
        self.metric_names = metric_names
        # 时序查询的时间间隔，单位为秒。可选 60、300、900、1800、3600、86400。60 对应整分钟，86400 对应每日 UTC 零点。部分统计指标的计算时长随间隔变化。
        # 
        # This parameter is required.
        self.period = period
        # 要查询的沙箱 ID。请同时填写所属的 teamID 和 templateID，并选择支持按沙箱查询的指标。
        self.sandbox_id = sandbox_id
        # 按沙箱版本查询沙箱数量。仅适用于 sandboxCount，可选 eco、std、pro、ent。
        self.sandbox_plan = sandbox_plan
        # 时序查询的开始时间，包含此时刻。请按示例填写 UTC 时间，精确到秒，并同时填写 endTime。
        self.start_time = start_time
        # 要查询的团队 ID。不填时查询当前账号。
        self.team_id = team_id
        # 要查询的模板 ID。请同时填写模板所属的 teamID。
        self.template_id = template_id
        # 查询某一时刻时，只填写 time。请按示例填写当前或过去的 UTC 时间，精确到秒。省略所有时间参数时，查询当前时刻。
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.group_by is not None:
            result['groupBy'] = self.group_by

        if self.metric_names is not None:
            result['metricNames'] = self.metric_names

        if self.period is not None:
            result['period'] = self.period

        if self.sandbox_id is not None:
            result['sandboxID'] = self.sandbox_id

        if self.sandbox_plan is not None:
            result['sandboxPlan'] = self.sandbox_plan

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.team_id is not None:
            result['teamID'] = self.team_id

        if self.template_id is not None:
            result['templateID'] = self.template_id

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')

        if m.get('metricNames') is not None:
            self.metric_names = m.get('metricNames')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('sandboxID') is not None:
            self.sandbox_id = m.get('sandboxID')

        if m.get('sandboxPlan') is not None:
            self.sandbox_plan = m.get('sandboxPlan')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('teamID') is not None:
            self.team_id = m.get('teamID')

        if m.get('templateID') is not None:
            self.template_id = m.get('templateID')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

