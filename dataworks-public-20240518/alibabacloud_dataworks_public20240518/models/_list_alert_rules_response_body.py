# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListAlertRulesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListAlertRulesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAlertRulesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        alert_rules: List[main_models.ListAlertRulesResponseBodyPagingInfoAlertRules] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The rules.
        self.alert_rules = alert_rules
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.alert_rules:
            for v1 in self.alert_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlertRules'] = []
        if self.alert_rules is not None:
            for k1 in self.alert_rules:
                result['AlertRules'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_rules = []
        if m.get('AlertRules') is not None:
            for k1 in m.get('AlertRules'):
                temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRules()
                self.alert_rules.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRules(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        trigger_condition: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerCondition = None,
    ):
        # Indicates whether the rule is enabled.
        self.enabled = enabled
        # The rule ID.
        self.id = id
        # The name of the rule.
        self.name = name
        # The ID of the Alibaba Cloud account used by the owner of the rule.
        self.owner = owner
        # The alert triggering condition.
        self.trigger_condition = trigger_condition

    def validate(self):
        if self.trigger_condition:
            self.trigger_condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.trigger_condition is not None:
            result['TriggerCondition'] = self.trigger_condition.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TriggerCondition') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerCondition()
            self.trigger_condition = temp_model.from_map(m.get('TriggerCondition'))

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerCondition(DaraModel):
    def __init__(
        self,
        extension: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtension = None,
        target: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionTarget = None,
        type: str = None,
    ):
        # The extended information about the rule. This parameter is required for specific types of alerts.
        self.extension = extension
        # The monitored objects.
        self.target = target
        # The alert type. Valid values:
        # 
        # *   Finished: An instance is successfully run.
        # *   UnFinished: An instance does not finish running before a specified point in time.
        # *   Error: An error occurs on an instance.
        # *   CycleUnfinished: An instance does not finish running as expected within a specific cycle.
        # *   Timeout: An instance times out.
        # *   InstanceTransferComplete: An instance is generated by the auto triggered node.
        # *   InstanceTransferFluctuate: The number of generated instances fluctuates.
        # *   ExhaustedError: An error persists after an instance is automatically rerun.
        # *   InstanceKeyword: An instance with errors contains specified keywords.
        # *   InstanceErrorCount: The number of instances on which an error occurs reaches a specified threshold.
        # *   InstanceErrorPercentage: The proportion of instances on which an error occurs in the workspace to the total number of instances reaches a specified threshold.
        # *   ResourceGroupPercentage: The usage rate of the resource group reaches a specified threshold.
        # *   ResourceGroupWaitCount: The number of instances that are waiting for resources in the resource group reaches a specified threshold.
        self.type = type

    def validate(self):
        if self.extension:
            self.extension.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extension is not None:
            result['Extension'] = self.extension.to_map()

        if self.target is not None:
            result['Target'] = self.target.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extension') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtension()
            self.extension = temp_model.from_map(m.get('Extension'))

        if m.get('Target') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionTarget()
            self.target = temp_model.from_map(m.get('Target'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionTarget(DaraModel):
    def __init__(
        self,
        allow_tasks: List[int] = None,
        ids: List[int] = None,
        type: str = None,
    ):
        # The nodes that are not to be monitored.
        self.allow_tasks = allow_tasks
        # The IDs of monitored objects.
        self.ids = ids
        # The type of the monitored objects. Valid values:
        # 
        # *   Task: node
        # *   Baseline: baseline
        # *   Project: workspace
        # *   BizProcess: workflow
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_tasks is not None:
            result['AllowTasks'] = self.allow_tasks

        if self.ids is not None:
            result['Ids'] = self.ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowTasks') is not None:
            self.allow_tasks = m.get('AllowTasks')

        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtension(DaraModel):
    def __init__(
        self,
        cycle_unfinished: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionCycleUnfinished = None,
        error: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionError = None,
        instance_error_count: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceErrorCount = None,
        instance_error_percentage: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceErrorPercentage = None,
        instance_transfer_fluctuate: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceTransferFluctuate = None,
        timeout: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionTimeout = None,
        un_finished: main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionUnFinished = None,
    ):
        # The configuration for an alert of the CycleUnfinished type.
        self.cycle_unfinished = cycle_unfinished
        # The configuration for an alert of the Error type.
        self.error = error
        # The configuration for an alert of the InstanceErrorCount type.
        self.instance_error_count = instance_error_count
        # The configuration for an alert of the InstanceErrorPercentage type.
        self.instance_error_percentage = instance_error_percentage
        # The configuration for an alert of the InstanceTransferFluctuate type.
        self.instance_transfer_fluctuate = instance_transfer_fluctuate
        # The configuration for an alert of the Timeout type.
        self.timeout = timeout
        # The configuration for an alert of the UnFinished type.
        self.un_finished = un_finished

    def validate(self):
        if self.cycle_unfinished:
            self.cycle_unfinished.validate()
        if self.error:
            self.error.validate()
        if self.instance_error_count:
            self.instance_error_count.validate()
        if self.instance_error_percentage:
            self.instance_error_percentage.validate()
        if self.instance_transfer_fluctuate:
            self.instance_transfer_fluctuate.validate()
        if self.timeout:
            self.timeout.validate()
        if self.un_finished:
            self.un_finished.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_unfinished is not None:
            result['CycleUnfinished'] = self.cycle_unfinished.to_map()

        if self.error is not None:
            result['Error'] = self.error.to_map()

        if self.instance_error_count is not None:
            result['InstanceErrorCount'] = self.instance_error_count.to_map()

        if self.instance_error_percentage is not None:
            result['InstanceErrorPercentage'] = self.instance_error_percentage.to_map()

        if self.instance_transfer_fluctuate is not None:
            result['InstanceTransferFluctuate'] = self.instance_transfer_fluctuate.to_map()

        if self.timeout is not None:
            result['Timeout'] = self.timeout.to_map()

        if self.un_finished is not None:
            result['UnFinished'] = self.un_finished.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleUnfinished') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionCycleUnfinished()
            self.cycle_unfinished = temp_model.from_map(m.get('CycleUnfinished'))

        if m.get('Error') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionError()
            self.error = temp_model.from_map(m.get('Error'))

        if m.get('InstanceErrorCount') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceErrorCount()
            self.instance_error_count = temp_model.from_map(m.get('InstanceErrorCount'))

        if m.get('InstanceErrorPercentage') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceErrorPercentage()
            self.instance_error_percentage = temp_model.from_map(m.get('InstanceErrorPercentage'))

        if m.get('InstanceTransferFluctuate') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceTransferFluctuate()
            self.instance_transfer_fluctuate = temp_model.from_map(m.get('InstanceTransferFluctuate'))

        if m.get('Timeout') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionTimeout()
            self.timeout = temp_model.from_map(m.get('Timeout'))

        if m.get('UnFinished') is not None:
            temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionUnFinished()
            self.un_finished = temp_model.from_map(m.get('UnFinished'))

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionUnFinished(DaraModel):
    def __init__(
        self,
        un_finished_time: str = None,
    ):
        # The latest completion time of the instance. The period is in the hh:mm format. Valid values of hh: [0,47]. Valid values of mm: [0,59].
        self.un_finished_time = un_finished_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.un_finished_time is not None:
            result['UnFinishedTime'] = self.un_finished_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnFinishedTime') is not None:
            self.un_finished_time = m.get('UnFinishedTime')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionTimeout(DaraModel):
    def __init__(
        self,
        timeout_in_minutes: int = None,
    ):
        # The timeout period. Unit: minutes.
        self.timeout_in_minutes = timeout_in_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timeout_in_minutes is not None:
            result['TimeoutInMinutes'] = self.timeout_in_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimeoutInMinutes') is not None:
            self.timeout_in_minutes = m.get('TimeoutInMinutes')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceTransferFluctuate(DaraModel):
    def __init__(
        self,
        percentage: int = None,
        trend: str = None,
    ):
        # The maximum percentage of fluctuation in the number of auto triggered node instances that are generated in your workspace. Valid values: [1-100].
        self.percentage = percentage
        # The way in which the number of auto triggered node instances that are generated in your workspace fluctuates. Valid values:
        # 
        # *   abs: the absolute value. The number of instances increases or decreases.
        # *   increase: The number of instances increases.
        # *   decrease: The number of instances decreases.
        self.trend = trend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.trend is not None:
            result['Trend'] = self.trend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('Trend') is not None:
            self.trend = m.get('Trend')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceErrorPercentage(DaraModel):
    def __init__(
        self,
        percentage: int = None,
    ):
        # The maximum percentage of instances on which an error occurs in the workspace to the total number of instances. Valid values: [1-100].
        self.percentage = percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionInstanceErrorCount(DaraModel):
    def __init__(
        self,
        count: int = None,
    ):
        # The maximum number of instances on which an error occurs. Valid values: [1,10000].
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionError(DaraModel):
    def __init__(
        self,
        auto_rerun_alert_enabled: bool = None,
        stream_task_ids: List[int] = None,
    ):
        # Indicates whether an alert is triggered if a batch synchronization task is automatically rerun upon a failure.
        self.auto_rerun_alert_enabled = auto_rerun_alert_enabled
        # The IDs of the real-time computing tasks. This parameter is required when you monitor real-time computing tasks.
        self.stream_task_ids = stream_task_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_rerun_alert_enabled is not None:
            result['AutoRerunAlertEnabled'] = self.auto_rerun_alert_enabled

        if self.stream_task_ids is not None:
            result['StreamTaskIds'] = self.stream_task_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRerunAlertEnabled') is not None:
            self.auto_rerun_alert_enabled = m.get('AutoRerunAlertEnabled')

        if m.get('StreamTaskIds') is not None:
            self.stream_task_ids = m.get('StreamTaskIds')

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionCycleUnfinished(DaraModel):
    def __init__(
        self,
        cycle_and_time: List[main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionCycleUnfinishedCycleAndTime] = None,
    ):
        # The configurations of the scheduling cycle and timeout period of the instance.
        self.cycle_and_time = cycle_and_time

    def validate(self):
        if self.cycle_and_time:
            for v1 in self.cycle_and_time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CycleAndTime'] = []
        if self.cycle_and_time is not None:
            for k1 in self.cycle_and_time:
                result['CycleAndTime'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cycle_and_time = []
        if m.get('CycleAndTime') is not None:
            for k1 in m.get('CycleAndTime'):
                temp_model = main_models.ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionCycleUnfinishedCycleAndTime()
                self.cycle_and_time.append(temp_model.from_map(k1))

        return self

class ListAlertRulesResponseBodyPagingInfoAlertRulesTriggerConditionExtensionCycleUnfinishedCycleAndTime(DaraModel):
    def __init__(
        self,
        cycle_id: int = None,
        time: str = None,
    ):
        # The ID of the scheduling cycle of the instance. Valid values: [1,288].
        self.cycle_id = cycle_id
        # The latest completion time of the instance within the scheduling cycle. The time is in the hh:mm format. Valid values of hh: [0,47]. Valid values of mm: [0,59].
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_id is not None:
            result['CycleId'] = self.cycle_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleId') is not None:
            self.cycle_id = m.get('CycleId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

