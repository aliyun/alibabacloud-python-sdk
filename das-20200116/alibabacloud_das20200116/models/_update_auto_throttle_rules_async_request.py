# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAutoThrottleRulesAsyncRequest(DaraModel):
    def __init__(
        self,
        abnormal_duration: float = None,
        active_sessions: int = None,
        allow_throttle_end_time: str = None,
        allow_throttle_start_time: str = None,
        auto_kill_session: bool = None,
        console_context: str = None,
        cpu_session_relation: str = None,
        cpu_usage: float = None,
        instance_ids: str = None,
        max_throttle_time: float = None,
        result_id: str = None,
    ):
        # The duration threshold for triggering automatic SQL throttling. Set this parameter to an integer that is greater than or equal to 2. Unit: minutes.
        # 
        # This parameter is required.
        self.abnormal_duration = abnormal_duration
        # The threshold for the number of active sessions.
        # 
        # *   If this parameter and CpuUsage are in the **OR** relationship, set this parameter to an integer that is greater than or equal to 16.
        # *   If this parameter and CpuUsage are in the **AND** relationship, set this parameter to an integer that is greater than or equal to 2.
        # 
        # This parameter is required.
        self.active_sessions = active_sessions
        # The end time of the throttling window. The time must be in UTC.
        # 
        # This parameter is required.
        self.allow_throttle_end_time = allow_throttle_end_time
        # The start time of the throttling window. The time must be in UTC.
        # 
        # This parameter is required.
        self.allow_throttle_start_time = allow_throttle_start_time
        # Specifies whether to terminate abnormal SQL statements in execution at the same time. Valid values:
        # 
        # >  Abnormal SQL statements use the same template as the SQL statements to be throttled.
        # 
        # *   **true**
        # *   **false**
        # 
        # This parameter is required.
        self.auto_kill_session = auto_kill_session
        # The reserved parameter.
        self.console_context = console_context
        # The logical relationship between the CPU utilization threshold and the maximum number of active sessions. Valid values:
        # 
        # *   **AND**
        # *   **OR**
        # 
        # This parameter is required.
        self.cpu_session_relation = cpu_session_relation
        # The threshold for CPU utilization. Valid values: 70% to 100%.
        # 
        # This parameter is required.
        self.cpu_usage = cpu_usage
        # The database instance IDs.
        # 
        # >  Set this parameter to a JSON array that consists of multiple instance IDs. Separate instance IDs with commas (,). Example: `[\\"Instance ID1\\", \\"Instance ID2\\"]`.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The maximum throttling duration. Set this parameter to a positive integer. Unit: minutes.
        # 
        # This parameter is required.
        self.max_throttle_time = max_throttle_time
        # The ID of the asynchronous request.
        # 
        # >  You can leave this parameter empty when you call the operation to initiate the request for the first time, and use the value of this parameter contained in the response to the first request for subsequent requests.
        self.result_id = result_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_duration is not None:
            result['AbnormalDuration'] = self.abnormal_duration

        if self.active_sessions is not None:
            result['ActiveSessions'] = self.active_sessions

        if self.allow_throttle_end_time is not None:
            result['AllowThrottleEndTime'] = self.allow_throttle_end_time

        if self.allow_throttle_start_time is not None:
            result['AllowThrottleStartTime'] = self.allow_throttle_start_time

        if self.auto_kill_session is not None:
            result['AutoKillSession'] = self.auto_kill_session

        if self.console_context is not None:
            result['ConsoleContext'] = self.console_context

        if self.cpu_session_relation is not None:
            result['CpuSessionRelation'] = self.cpu_session_relation

        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.max_throttle_time is not None:
            result['MaxThrottleTime'] = self.max_throttle_time

        if self.result_id is not None:
            result['ResultId'] = self.result_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalDuration') is not None:
            self.abnormal_duration = m.get('AbnormalDuration')

        if m.get('ActiveSessions') is not None:
            self.active_sessions = m.get('ActiveSessions')

        if m.get('AllowThrottleEndTime') is not None:
            self.allow_throttle_end_time = m.get('AllowThrottleEndTime')

        if m.get('AllowThrottleStartTime') is not None:
            self.allow_throttle_start_time = m.get('AllowThrottleStartTime')

        if m.get('AutoKillSession') is not None:
            self.auto_kill_session = m.get('AutoKillSession')

        if m.get('ConsoleContext') is not None:
            self.console_context = m.get('ConsoleContext')

        if m.get('CpuSessionRelation') is not None:
            self.cpu_session_relation = m.get('CpuSessionRelation')

        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('MaxThrottleTime') is not None:
            self.max_throttle_time = m.get('MaxThrottleTime')

        if m.get('ResultId') is not None:
            self.result_id = m.get('ResultId')

        return self

