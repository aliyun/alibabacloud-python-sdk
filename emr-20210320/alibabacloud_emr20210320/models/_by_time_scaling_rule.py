# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ByTimeScalingRule(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        launch_expiration_time: int = None,
        launch_time: int = None,
        recurrence_type: str = None,
        recurrence_value: str = None,
    ):
        # 重复执行定时任务的结束时间戳。单位为毫秒。
        self.end_time = end_time
        # 定时任务触发操作失败后，在此时间内重试。单位为秒，取值范围：0~3600。
        self.launch_expiration_time = launch_expiration_time
        # 启动时间戳。单位为毫秒。
        # 
        # This parameter is required.
        self.launch_time = launch_time
        # 指定时间规则的执行类型。
        self.recurrence_type = recurrence_type
        # 重复执行定时任务的数值。具体取值取决于 recurrenceType 设置。
        # - recurrenceType 取 MINUTELY 时，只能填一个数值，取值范围：1~1440。
        # - recurrenceType 取 HOURLY 时，只能填一个数值，取值范围：1~24。
        # - recurrenceType 取 DAILY 时，只能填一个数值，取值范围：1~31。
        # - recurrenceType 取 WEEKLY 时，可以填入多个值，填多个值时使用英文逗号（,）分隔。周一到周天分别用MON，TUE，WED，THU，FRI，SAT，SUN代替。 比如 MON,FRI,SUN 代表周一、周五、周天。
        # - recurrenceType 取 MONTHLY 时，格式为A-B或者A,B。A、B的取值范围为1~31，如果使用A-B时B必须大于A。
        self.recurrence_value = recurrence_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.launch_expiration_time is not None:
            result['LaunchExpirationTime'] = self.launch_expiration_time

        if self.launch_time is not None:
            result['LaunchTime'] = self.launch_time

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_value is not None:
            result['RecurrenceValue'] = self.recurrence_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LaunchExpirationTime') is not None:
            self.launch_expiration_time = m.get('LaunchExpirationTime')

        if m.get('LaunchTime') is not None:
            self.launch_time = m.get('LaunchTime')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValue') is not None:
            self.recurrence_value = m.get('RecurrenceValue')

        return self

