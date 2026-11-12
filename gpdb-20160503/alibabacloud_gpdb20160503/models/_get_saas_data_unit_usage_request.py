# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSaasDataUnitUsageRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        region_id: str = None,
        service_id: str = None,
        start_time: str = None,
        time_unit: str = None,
    ):
        # UTC时间，格式yyyy-MM-ddTHH:mm:ssZ，秒必须为00。必须晚于StartTime且不晚于请求时刻，不自动裁剪查询范围。
        # 
        # This parameter is required.
        self.end_time = end_time
        self.region_id = region_id
        # 未删除的SaaS服务实例ID，不接受普通DBInstanceId替代。
        # 
        # This parameter is required.
        self.service_id = service_id
        # UTC时间，格式yyyy-MM-ddTHH:mm:ssZ，秒必须为00。不得早于请求时刻前30天；与EndTime组成左闭右开区间，跨度最多7天。
        # 
        # This parameter is required.
        self.start_time = start_time
        # 支持hour（UTC小时）或day（UTC日），未传默认hour。仅决定趋势汇总方式，不在响应中回显。
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        return self

