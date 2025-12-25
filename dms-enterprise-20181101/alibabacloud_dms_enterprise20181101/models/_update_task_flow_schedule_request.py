# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTaskFlowScheduleRequest(DaraModel):
    def __init__(
        self,
        cron_begin_date: str = None,
        cron_end_date: str = None,
        cron_str: str = None,
        cron_type: str = None,
        dag_id: int = None,
        schedule_param: str = None,
        schedule_switch: bool = None,
        tid: int = None,
        time_zone_id: str = None,
        trigger_type: str = None,
    ):
        # The start of the time range for scheduling.
        self.cron_begin_date = cron_begin_date
        # The end of the time range for scheduling.
        self.cron_end_date = cron_end_date
        # The cron expression for timed scheduling.
        self.cron_str = cron_str
        # The type of the scheduling cycle. Valid values:
        # 
        # *   **MINUTE**: scheduling by minute
        # *   **HOUR**: scheduling by hour
        # *   **DAY**: scheduling by day
        # *   **WEEK**: scheduling by week
        # *   **MONTH**: scheduling by month
        self.cron_type = cron_type
        # The ID of the task flow.
        # 
        # This parameter is required.
        self.dag_id = dag_id
        # The event scheduling configuration. The value of this parameter is a JSON string.
        # 
        # This parameter is required.
        self.schedule_param = schedule_param
        # Specifies whether to enable scheduling. Valid values:
        # 
        # *   **Enable**
        # *   **Disable**
        # 
        # This parameter is required.
        self.schedule_switch = schedule_switch
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, go to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid
        # The time zone. The default time zone is UTC+8 (Asia/Shanghai).
        self.time_zone_id = time_zone_id
        # The mode in which the task flow is triggered. Valid values:
        # 
        # *   **Cron**: The task flow is triggered based on timed scheduling.
        # *   **Event**: The task flow is triggered by events.
        # 
        # This parameter is required.
        self.trigger_type = trigger_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron_begin_date is not None:
            result['CronBeginDate'] = self.cron_begin_date

        if self.cron_end_date is not None:
            result['CronEndDate'] = self.cron_end_date

        if self.cron_str is not None:
            result['CronStr'] = self.cron_str

        if self.cron_type is not None:
            result['CronType'] = self.cron_type

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.schedule_param is not None:
            result['ScheduleParam'] = self.schedule_param

        if self.schedule_switch is not None:
            result['ScheduleSwitch'] = self.schedule_switch

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.time_zone_id is not None:
            result['TimeZoneId'] = self.time_zone_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CronBeginDate') is not None:
            self.cron_begin_date = m.get('CronBeginDate')

        if m.get('CronEndDate') is not None:
            self.cron_end_date = m.get('CronEndDate')

        if m.get('CronStr') is not None:
            self.cron_str = m.get('CronStr')

        if m.get('CronType') is not None:
            self.cron_type = m.get('CronType')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('ScheduleParam') is not None:
            self.schedule_param = m.get('ScheduleParam')

        if m.get('ScheduleSwitch') is not None:
            self.schedule_switch = m.get('ScheduleSwitch')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('TimeZoneId') is not None:
            self.time_zone_id = m.get('TimeZoneId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        return self

