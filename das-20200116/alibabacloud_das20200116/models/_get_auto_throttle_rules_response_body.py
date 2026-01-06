# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_das20200116 import models as main_models
from darabonba.model import DaraModel

class GetAutoThrottleRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetAutoThrottleRulesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        # 
        # >  If the request was successful, **Successful** is returned. If the request failed, an error message that contains information such as an error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
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
            temp_model = main_models.GetAutoThrottleRulesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAutoThrottleRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_auto_throttle_count: int = None,
        enable_auto_throttle_list: List[main_models.GetAutoThrottleRulesResponseBodyDataEnableAutoThrottleList] = None,
        never_enable_auto_throttle_or_released_instance_count: int = None,
        never_enable_auto_throttle_or_released_instance_id_list: List[str] = None,
        total_auto_throttle_rules_count: int = None,
        turn_off_auto_throttle_count: int = None,
        turn_off_auto_throttle_list: List[main_models.GetAutoThrottleRulesResponseBodyDataTurnOffAutoThrottleList] = None,
    ):
        # The number of database instances for which the automatic SQL throttling feature is currently enabled.
        self.enable_auto_throttle_count = enable_auto_throttle_count
        # The database instances for which the automatic SQL throttling feature is currently enabled.
        self.enable_auto_throttle_list = enable_auto_throttle_list
        # The number of database instances that do not exist or for which the automatic SQL throttling feature has never been enabled.
        # 
        # >  If a database instance does not exist, the instance has been released or the specified instance ID is invalid.
        self.never_enable_auto_throttle_or_released_instance_count = never_enable_auto_throttle_or_released_instance_count
        # The number of database instances that do not exist or for which the automatic SQL throttling feature has never been enabled.
        # 
        # >  If a database instance does not exist, the instance has been released or the specified instance ID is invalid.
        self.never_enable_auto_throttle_or_released_instance_id_list = never_enable_auto_throttle_or_released_instance_id_list
        # The number of databases for which the automatic SQL throttling feature has been enabled.
        self.total_auto_throttle_rules_count = total_auto_throttle_rules_count
        # The number of database instances for which the automatic SQL throttling feature was once enabled but is currently disabled.
        self.turn_off_auto_throttle_count = turn_off_auto_throttle_count
        # The database instances for which the automatic SQL throttling feature was once enabled but is currently disabled.
        self.turn_off_auto_throttle_list = turn_off_auto_throttle_list

    def validate(self):
        if self.enable_auto_throttle_list:
            for v1 in self.enable_auto_throttle_list:
                 if v1:
                    v1.validate()
        if self.turn_off_auto_throttle_list:
            for v1 in self.turn_off_auto_throttle_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_auto_throttle_count is not None:
            result['EnableAutoThrottleCount'] = self.enable_auto_throttle_count

        result['EnableAutoThrottleList'] = []
        if self.enable_auto_throttle_list is not None:
            for k1 in self.enable_auto_throttle_list:
                result['EnableAutoThrottleList'].append(k1.to_map() if k1 else None)

        if self.never_enable_auto_throttle_or_released_instance_count is not None:
            result['NeverEnableAutoThrottleOrReleasedInstanceCount'] = self.never_enable_auto_throttle_or_released_instance_count

        if self.never_enable_auto_throttle_or_released_instance_id_list is not None:
            result['NeverEnableAutoThrottleOrReleasedInstanceIdList'] = self.never_enable_auto_throttle_or_released_instance_id_list

        if self.total_auto_throttle_rules_count is not None:
            result['TotalAutoThrottleRulesCount'] = self.total_auto_throttle_rules_count

        if self.turn_off_auto_throttle_count is not None:
            result['TurnOffAutoThrottleCount'] = self.turn_off_auto_throttle_count

        result['TurnOffAutoThrottleList'] = []
        if self.turn_off_auto_throttle_list is not None:
            for k1 in self.turn_off_auto_throttle_list:
                result['TurnOffAutoThrottleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutoThrottleCount') is not None:
            self.enable_auto_throttle_count = m.get('EnableAutoThrottleCount')

        self.enable_auto_throttle_list = []
        if m.get('EnableAutoThrottleList') is not None:
            for k1 in m.get('EnableAutoThrottleList'):
                temp_model = main_models.GetAutoThrottleRulesResponseBodyDataEnableAutoThrottleList()
                self.enable_auto_throttle_list.append(temp_model.from_map(k1))

        if m.get('NeverEnableAutoThrottleOrReleasedInstanceCount') is not None:
            self.never_enable_auto_throttle_or_released_instance_count = m.get('NeverEnableAutoThrottleOrReleasedInstanceCount')

        if m.get('NeverEnableAutoThrottleOrReleasedInstanceIdList') is not None:
            self.never_enable_auto_throttle_or_released_instance_id_list = m.get('NeverEnableAutoThrottleOrReleasedInstanceIdList')

        if m.get('TotalAutoThrottleRulesCount') is not None:
            self.total_auto_throttle_rules_count = m.get('TotalAutoThrottleRulesCount')

        if m.get('TurnOffAutoThrottleCount') is not None:
            self.turn_off_auto_throttle_count = m.get('TurnOffAutoThrottleCount')

        self.turn_off_auto_throttle_list = []
        if m.get('TurnOffAutoThrottleList') is not None:
            for k1 in m.get('TurnOffAutoThrottleList'):
                temp_model = main_models.GetAutoThrottleRulesResponseBodyDataTurnOffAutoThrottleList()
                self.turn_off_auto_throttle_list.append(temp_model.from_map(k1))

        return self

class GetAutoThrottleRulesResponseBodyDataTurnOffAutoThrottleList(DaraModel):
    def __init__(
        self,
        abnormal_duration: float = None,
        active_sessions: int = None,
        allow_throttle_end_time: str = None,
        allow_throttle_start_time: str = None,
        auto_kill_session: bool = None,
        cpu_session_relation: str = None,
        cpu_usage: float = None,
        instance_id: str = None,
        max_throttle_time: float = None,
        user_id: str = None,
        visible: bool = None,
    ):
        # The maximum period of time during which the automatic SQL throttling feature is triggered. Unit: minutes.
        self.abnormal_duration = abnormal_duration
        # The maximum number of active sessions.
        self.active_sessions = active_sessions
        # The end time of the throttling window. The value of this parameter is in UTC.
        self.allow_throttle_end_time = allow_throttle_end_time
        # The start time of the throttling window. The value of this parameter is in UTC.
        self.allow_throttle_start_time = allow_throttle_start_time
        # Indicates whether abnormal SQL statements in execution are terminated at a time. Valid values:
        # 
        # > Abnormal SQL statements use the same template as the SQL statements that need to be throttled.
        # 
        # * **true**
        # * **false**
        self.auto_kill_session = auto_kill_session
        # The logical relationship between the CPU utilization threshold and the maximum number of active sessions. Valid values:
        # 
        # * **AND**
        # * **OR**
        self.cpu_session_relation = cpu_session_relation
        # The CPU utilization threshold.
        self.cpu_usage = cpu_usage
        # The database instance ID.
        self.instance_id = instance_id
        # The maximum throttling duration. Unit: minutes.
        self.max_throttle_time = max_throttle_time
        # The ID of the Alibaba Cloud account that is used to create the database instance.
        self.user_id = user_id
        # Indicates whether the automatic SQL throttling feature is enabled. Valid values:
        # 
        # * **true**
        # * **false**
        self.visible = visible

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

        if self.cpu_session_relation is not None:
            result['CpuSessionRelation'] = self.cpu_session_relation

        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_throttle_time is not None:
            result['MaxThrottleTime'] = self.max_throttle_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.visible is not None:
            result['Visible'] = self.visible

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

        if m.get('CpuSessionRelation') is not None:
            self.cpu_session_relation = m.get('CpuSessionRelation')

        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxThrottleTime') is not None:
            self.max_throttle_time = m.get('MaxThrottleTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

class GetAutoThrottleRulesResponseBodyDataEnableAutoThrottleList(DaraModel):
    def __init__(
        self,
        abnormal_duration: float = None,
        active_sessions: int = None,
        allow_throttle_end_time: str = None,
        allow_throttle_start_time: str = None,
        auto_kill_session: bool = None,
        cpu_session_relation: str = None,
        cpu_usage: float = None,
        instance_id: str = None,
        max_throttle_time: float = None,
        user_id: str = None,
        visible: bool = None,
    ):
        # The maximum period of time during which an exception occurs when automatic SQL throttling is triggered. Unit: minutes.
        self.abnormal_duration = abnormal_duration
        # The maximum number of active sessions.
        self.active_sessions = active_sessions
        # The end time of the throttling window. The value of this parameter is in UTC.
        self.allow_throttle_end_time = allow_throttle_end_time
        # The start time of the throttling window. The value of this parameter is in UTC.
        self.allow_throttle_start_time = allow_throttle_start_time
        # Indicates whether abnormal SQL statements in execution are terminated at a time. Valid values:
        # 
        # > Abnormal SQL statements use the same template as the SQL statements that need to be throttled.
        # 
        # * **true**
        # * **false**
        self.auto_kill_session = auto_kill_session
        # The logical relationship between the CPU utilization threshold and the maximum number of active sessions. Valid values:
        # 
        # * **AND**
        # * **OR**
        self.cpu_session_relation = cpu_session_relation
        # The CPU utilization threshold.
        self.cpu_usage = cpu_usage
        # The database instance ID.
        self.instance_id = instance_id
        # The maximum throttling duration. Unit: minutes.
        self.max_throttle_time = max_throttle_time
        # The ID of the Alibaba Cloud account that is used to create the database instance.
        self.user_id = user_id
        # Indicates whether the automatic SQL throttling feature is enabled. Valid values:
        # 
        # * **true**
        # * **false**
        self.visible = visible

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

        if self.cpu_session_relation is not None:
            result['CpuSessionRelation'] = self.cpu_session_relation

        if self.cpu_usage is not None:
            result['CpuUsage'] = self.cpu_usage

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_throttle_time is not None:
            result['MaxThrottleTime'] = self.max_throttle_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.visible is not None:
            result['Visible'] = self.visible

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

        if m.get('CpuSessionRelation') is not None:
            self.cpu_session_relation = m.get('CpuSessionRelation')

        if m.get('CpuUsage') is not None:
            self.cpu_usage = m.get('CpuUsage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxThrottleTime') is not None:
            self.max_throttle_time = m.get('MaxThrottleTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

