# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetDISyncTaskResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDISyncTaskResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned results.
        self.data = data
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   True
        # *   False
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetDISyncTaskResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDISyncTaskResponseBodyData(DaraModel):
    def __init__(
        self,
        alarm_list: List[main_models.GetDISyncTaskResponseBodyDataAlarmList] = None,
        code: str = None,
        message: str = None,
        solution_detail: main_models.GetDISyncTaskResponseBodyDataSolutionDetail = None,
        status: str = None,
    ):
        # The alert rules that are associated with the real-time synchronization task. The value of this parameter is an array.
        self.alarm_list = alarm_list
        # *   If the TaskType parameter is set to DI_REALTIME, the details of the real-time synchronization task are returned.
        # *   If the TaskType parameter is set to DI_SOLUTION, the value null is returned.
        self.code = code
        # The cause of the failure to obtain the details of the real-time synchronization task or data synchronization solution.
        # 
        # If the details of the real-time synchronization task or data synchronization solution are obtained, the value null is returned.
        self.message = message
        # *   If the TaskType parameter is set to DI_REALTIME, the value null is returned.
        # *   If the TaskType parameter is set to DI_SOLUTION, the details of the data synchronization solution are returned.
        self.solution_detail = solution_detail
        # Indicates whether the details of the real-time synchronization task or data synchronization solution are obtained. Valid values:
        # 
        # success: The details are obtained. fail: The details fail to be obtained.
        self.status = status

    def validate(self):
        if self.alarm_list:
            for v1 in self.alarm_list:
                 if v1:
                    v1.validate()
        if self.solution_detail:
            self.solution_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmList'] = []
        if self.alarm_list is not None:
            for k1 in self.alarm_list:
                result['AlarmList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.solution_detail is not None:
            result['SolutionDetail'] = self.solution_detail.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_list = []
        if m.get('AlarmList') is not None:
            for k1 in m.get('AlarmList'):
                temp_model = main_models.GetDISyncTaskResponseBodyDataAlarmList()
                self.alarm_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('SolutionDetail') is not None:
            temp_model = main_models.GetDISyncTaskResponseBodyDataSolutionDetail()
            self.solution_detail = temp_model.from_map(m.get('SolutionDetail'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetDISyncTaskResponseBodyDataSolutionDetail(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        id: int = None,
        name: str = None,
        process_content: str = None,
        process_extra: str = None,
        project_id: int = None,
        source_type: str = None,
        start_time: str = None,
        status: str = None,
        submit_time: str = None,
        type: str = None,
    ):
        # The creator of the data synchronization solution.
        self.creator_name = creator_name
        # The ID of the data synchronization solution.
        self.id = id
        # The name of the data synchronization solution.
        self.name = name
        # The configuration details of the data synchronization solution.
        self.process_content = process_content
        # The additional parameters of the data synchronization solution.
        self.process_extra = process_extra
        # The ID of the project to which the data synchronization solution belongs.
        self.project_id = project_id
        # The type of the source of the data synchronization solution.
        self.source_type = source_type
        # The start time of the data synchronization solution.
        self.start_time = start_time
        # The status of the data synchronization solution. Valid values:
        # 
        # *   0: successful
        # *   1: not running
        # *   2: running
        # *   3: failed
        # *   4: committed
        # *   5: pending manual confirmation
        # *   6: manually confirmed
        # *   7: others
        # *   8: waiting
        # *   9: deleted
        self.status = status
        # The time when the data synchronization solution was committed.
        self.submit_time = submit_time
        # The type of the data synchronization solution.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.process_content is not None:
            result['ProcessContent'] = self.process_content

        if self.process_extra is not None:
            result['ProcessExtra'] = self.process_extra

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProcessContent') is not None:
            self.process_content = m.get('ProcessContent')

        if m.get('ProcessExtra') is not None:
            self.process_extra = m.get('ProcessExtra')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDISyncTaskResponseBodyDataAlarmList(DaraModel):
    def __init__(
        self,
        alarm_rule_list: List[main_models.GetDISyncTaskResponseBodyDataAlarmListAlarmRuleList] = None,
        description: str = None,
        enabled: bool = None,
        id: int = None,
        metric: str = None,
        notify_rule: main_models.GetDISyncTaskResponseBodyDataAlarmListNotifyRule = None,
        rule_name: str = None,
    ):
        # The alert notification settings. The value of this parameter is an array.
        self.alarm_rule_list = alarm_rule_list
        # The description of the alert rule.
        self.description = description
        # Indicates whether the alert rule is enabled.
        self.enabled = enabled
        # The ID of the alert rule.
        self.id = id
        # The alert type. Valid values:
        # 
        # *   taskStatus
        # *   bizDelay
        # *   taskFailoverCount
        # *   ddlUnsupport
        # *   ddlReport
        # *   totalDirtyRecordWriteInLines
        self.metric = metric
        # The settings for alert notification rules. The value of this parameter is an array.
        self.notify_rule = notify_rule
        # The name of the alert rule.
        self.rule_name = rule_name

    def validate(self):
        if self.alarm_rule_list:
            for v1 in self.alarm_rule_list:
                 if v1:
                    v1.validate()
        if self.notify_rule:
            self.notify_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlarmRuleList'] = []
        if self.alarm_rule_list is not None:
            for k1 in self.alarm_rule_list:
                result['AlarmRuleList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.notify_rule is not None:
            result['NotifyRule'] = self.notify_rule.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_rule_list = []
        if m.get('AlarmRuleList') is not None:
            for k1 in m.get('AlarmRuleList'):
                temp_model = main_models.GetDISyncTaskResponseBodyDataAlarmListAlarmRuleList()
                self.alarm_rule_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('NotifyRule') is not None:
            temp_model = main_models.GetDISyncTaskResponseBodyDataAlarmListNotifyRule()
            self.notify_rule = temp_model.from_map(m.get('NotifyRule'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class GetDISyncTaskResponseBodyDataAlarmListNotifyRule(DaraModel):
    def __init__(
        self,
        critical: List[str] = None,
        interval: int = None,
        warning: List[str] = None,
    ):
        # The settings for Critical-level alert notifications.
        self.critical = critical
        # The alert interval. Unit: minutes.
        self.interval = interval
        # The settings for Warning-level alert notifications.
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.critical is not None:
            result['Critical'] = self.critical

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.warning is not None:
            result['Warning'] = self.warning

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            self.critical = m.get('Critical')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('Warning') is not None:
            self.warning = m.get('Warning')

        return self

class GetDISyncTaskResponseBodyDataAlarmListAlarmRuleList(DaraModel):
    def __init__(
        self,
        aggregator: str = None,
        comparator: str = None,
        duration: int = None,
        level: str = None,
        threshold: int = None,
    ):
        # The calculation method of a metric. Valid values:
        # 
        # *   avg
        # *   max
        self.aggregator = aggregator
        # The comparison operator, which indicates the method used to compare a metric with the alert rule.
        # 
        # *   \\"=\\"
        # *   \\"<\\"
        # *   \\">\\"
        self.comparator = comparator
        # The duration that a condition is met before an alert is triggered. Unit: minutes.
        self.duration = duration
        # *   WARNING
        # *   CRITICAL
        self.level = level
        # The threshold for the comparison between a metric and the alert rule.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator is not None:
            result['Aggregator'] = self.aggregator

        if self.comparator is not None:
            result['Comparator'] = self.comparator

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.level is not None:
            result['Level'] = self.level

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aggregator') is not None:
            self.aggregator = m.get('Aggregator')

        if m.get('Comparator') is not None:
            self.comparator = m.get('Comparator')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

