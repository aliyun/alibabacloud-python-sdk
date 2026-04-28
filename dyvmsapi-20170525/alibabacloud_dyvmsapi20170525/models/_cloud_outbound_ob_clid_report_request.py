# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudOutboundObClidReportRequest(DaraModel):
    def __init__(
        self,
        area_codes: str = None,
        end_hour: int = None,
        end_time: str = None,
        enterprise_id: int = None,
        limit: int = None,
        start: int = None,
        start_hour: int = None,
        start_time: str = None,
        statistic_method: int = None,
        time_range_type: int = None,
    ):
        # 说明：根据区号查询指定区域的预览外呼被叫号码统计支持按照多个区号进行查询，多个区号之间使用英文逗号","分隔，默认查询账户下所有地区的预览外呼被叫号码统计
        self.area_codes = area_codes
        # 统计时段结束时间；取值：0~23,默认值为24时
        self.end_hour = end_hour
        # 说明：统计日期的结束时间，格式：yyyy-MM-dd
        # 
        # This parameter is required.
        self.end_time = end_time
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 查询条数；取值：最大不能超过1000，默认10
        self.limit = limit
        # 查询起始位置；取值：大于等于0，默认0
        self.start = start
        # 统计时段开始时间；取值：0~23,默认值为0时
        self.start_hour = start_hour
        # 说明：统计日期的开始时间，格式：yyyy-MM-dd
        # 
        # This parameter is required.
        self.start_time = start_time
        # 统计方法；说明：0：分时1：分日2：汇总11：中继群组汇总
        # 
        # This parameter is required.
        self.statistic_method = statistic_method
        # 统计类型；说明：统计报表时间类型，1：日报表2：周报表3：月报表4：自定义时间
        # 
        # This parameter is required.
        self.time_range_type = time_range_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_codes is not None:
            result['AreaCodes'] = self.area_codes

        if self.end_hour is not None:
            result['EndHour'] = self.end_hour

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.start is not None:
            result['Start'] = self.start

        if self.start_hour is not None:
            result['StartHour'] = self.start_hour

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.statistic_method is not None:
            result['StatisticMethod'] = self.statistic_method

        if self.time_range_type is not None:
            result['TimeRangeType'] = self.time_range_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaCodes') is not None:
            self.area_codes = m.get('AreaCodes')

        if m.get('EndHour') is not None:
            self.end_hour = m.get('EndHour')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('StartHour') is not None:
            self.start_hour = m.get('StartHour')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StatisticMethod') is not None:
            self.statistic_method = m.get('StatisticMethod')

        if m.get('TimeRangeType') is not None:
            self.time_range_type = m.get('TimeRangeType')

        return self

