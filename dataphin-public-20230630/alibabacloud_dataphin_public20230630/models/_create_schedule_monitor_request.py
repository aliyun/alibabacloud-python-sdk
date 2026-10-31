# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateScheduleMonitorRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateScheduleMonitorRequestCreateCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The request body for creating a scheduling monitoring configuration.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The operator user ID.
        self.op_user_id = op_user_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateScheduleMonitorRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class CreateScheduleMonitorRequestCreateCommand(DaraModel):
    def __init__(
        self,
        monitored_item_config: main_models.CreateScheduleMonitorRequestCreateCommandMonitoredItemConfig = None,
        monitored_rule_config_list: List[main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigList] = None,
    ):
        # The monitored object configuration.
        # 
        # This parameter is required.
        self.monitored_item_config = monitored_item_config
        # The list of monitoring rule configurations. You can configure multiple rules for different alert causes.
        # 
        # This parameter is required.
        self.monitored_rule_config_list = monitored_rule_config_list

    def validate(self):
        if self.monitored_item_config:
            self.monitored_item_config.validate()
        if self.monitored_rule_config_list:
            for v1 in self.monitored_rule_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitored_item_config is not None:
            result['MonitoredItemConfig'] = self.monitored_item_config.to_map()

        result['MonitoredRuleConfigList'] = []
        if self.monitored_rule_config_list is not None:
            for k1 in self.monitored_rule_config_list:
                result['MonitoredRuleConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitoredItemConfig') is not None:
            temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredItemConfig()
            self.monitored_item_config = temp_model.from_map(m.get('MonitoredItemConfig'))

        self.monitored_rule_config_list = []
        if m.get('MonitoredRuleConfigList') is not None:
            for k1 in m.get('MonitoredRuleConfigList'):
                temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigList()
                self.monitored_rule_config_list.append(temp_model.from_map(k1))

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigList(DaraModel):
    def __init__(
        self,
        alert_reason_type: str = None,
        alert_strategy: main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategy = None,
        fixed_elapsed_time: int = None,
        fixed_unfinished_time: str = None,
        unfinished_rule_detail_config: main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfig = None,
    ):
        # The alert cause type. Valid values:
        # - FAILED: The task execution failed.
        # - TIME_OUT: The task execution timed out.
        # - UNFINISHED: The task is not completed.
        # - SUCCESS: The task execution succeeded.
        # - DATA_DELAY: The data is delayed.
        # 
        # This parameter is required.
        self.alert_reason_type = alert_reason_type
        # The alert strategy.
        # 
        # This parameter is required.
        self.alert_strategy = alert_strategy
        # The timeout period in minutes. Specify this parameter only when AlertReasonType is set to TIME_OUT.
        self.fixed_elapsed_time = fixed_elapsed_time
        # The daily time to check for unfinished tasks in HH:mm format. Specify this parameter only when AlertReasonType is set to UNFINISHED.
        self.fixed_unfinished_time = fixed_unfinished_time
        # The detailed configuration for the unfinished rule. Specify this parameter only when AlertReasonType is set to UNFINISHED.
        self.unfinished_rule_detail_config = unfinished_rule_detail_config

    def validate(self):
        if self.alert_strategy:
            self.alert_strategy.validate()
        if self.unfinished_rule_detail_config:
            self.unfinished_rule_detail_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_reason_type is not None:
            result['AlertReasonType'] = self.alert_reason_type

        if self.alert_strategy is not None:
            result['AlertStrategy'] = self.alert_strategy.to_map()

        if self.fixed_elapsed_time is not None:
            result['FixedElapsedTime'] = self.fixed_elapsed_time

        if self.fixed_unfinished_time is not None:
            result['FixedUnfinishedTime'] = self.fixed_unfinished_time

        if self.unfinished_rule_detail_config is not None:
            result['UnfinishedRuleDetailConfig'] = self.unfinished_rule_detail_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertReasonType') is not None:
            self.alert_reason_type = m.get('AlertReasonType')

        if m.get('AlertStrategy') is not None:
            temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategy()
            self.alert_strategy = temp_model.from_map(m.get('AlertStrategy'))

        if m.get('FixedElapsedTime') is not None:
            self.fixed_elapsed_time = m.get('FixedElapsedTime')

        if m.get('FixedUnfinishedTime') is not None:
            self.fixed_unfinished_time = m.get('FixedUnfinishedTime')

        if m.get('UnfinishedRuleDetailConfig') is not None:
            temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfig()
            self.unfinished_rule_detail_config = temp_model.from_map(m.get('UnfinishedRuleDetailConfig'))

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfig(DaraModel):
    def __init__(
        self,
        daily_unfinished_config: main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigDailyUnfinishedConfig = None,
        multi_period_unfinished_config: main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfig = None,
    ):
        # The daily unfinished configuration.
        self.daily_unfinished_config = daily_unfinished_config
        # The multi-period unfinished configuration.
        self.multi_period_unfinished_config = multi_period_unfinished_config

    def validate(self):
        if self.daily_unfinished_config:
            self.daily_unfinished_config.validate()
        if self.multi_period_unfinished_config:
            self.multi_period_unfinished_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.daily_unfinished_config is not None:
            result['DailyUnfinishedConfig'] = self.daily_unfinished_config.to_map()

        if self.multi_period_unfinished_config is not None:
            result['MultiPeriodUnfinishedConfig'] = self.multi_period_unfinished_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyUnfinishedConfig') is not None:
            temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigDailyUnfinishedConfig()
            self.daily_unfinished_config = temp_model.from_map(m.get('DailyUnfinishedConfig'))

        if m.get('MultiPeriodUnfinishedConfig') is not None:
            temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfig()
            self.multi_period_unfinished_config = temp_model.from_map(m.get('MultiPeriodUnfinishedConfig'))

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfig(DaraModel):
    def __init__(
        self,
        custom_period_list: List[main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfigCustomPeriodList] = None,
        interval_after_due_time: int = None,
        interval_unit: str = None,
        monitor_period_type: str = None,
        trigger_rule_type: str = None,
    ):
        # The list of custom monitoring periods. Specify this parameter when MonitorPeriodType is set to CUSTOM.
        self.custom_period_list = custom_period_list
        # The interval time value. This parameter is used together with IntervalUnit.
        self.interval_after_due_time = interval_after_due_time
        # The interval unit. Valid values: SECONDS, MINUTES, and HOURS.
        self.interval_unit = interval_unit
        # The monitoring period type. Valid values: ALL, FIRST, LAST, and CUSTOM.
        self.monitor_period_type = monitor_period_type
        # The trigger rule type. Valid values:
        # - INTERVAL_AFTER_DUE_TIME: Triggered at an interval after the due time.
        # - FIX_TIME: Triggered at a fixed time.
        self.trigger_rule_type = trigger_rule_type

    def validate(self):
        if self.custom_period_list:
            for v1 in self.custom_period_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomPeriodList'] = []
        if self.custom_period_list is not None:
            for k1 in self.custom_period_list:
                result['CustomPeriodList'].append(k1.to_map() if k1 else None)

        if self.interval_after_due_time is not None:
            result['IntervalAfterDueTime'] = self.interval_after_due_time

        if self.interval_unit is not None:
            result['IntervalUnit'] = self.interval_unit

        if self.monitor_period_type is not None:
            result['MonitorPeriodType'] = self.monitor_period_type

        if self.trigger_rule_type is not None:
            result['TriggerRuleType'] = self.trigger_rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_period_list = []
        if m.get('CustomPeriodList') is not None:
            for k1 in m.get('CustomPeriodList'):
                temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfigCustomPeriodList()
                self.custom_period_list.append(temp_model.from_map(k1))

        if m.get('IntervalAfterDueTime') is not None:
            self.interval_after_due_time = m.get('IntervalAfterDueTime')

        if m.get('IntervalUnit') is not None:
            self.interval_unit = m.get('IntervalUnit')

        if m.get('MonitorPeriodType') is not None:
            self.monitor_period_type = m.get('MonitorPeriodType')

        if m.get('TriggerRuleType') is not None:
            self.trigger_rule_type = m.get('TriggerRuleType')

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfigCustomPeriodList(DaraModel):
    def __init__(
        self,
        fixed_unfinished_time: str = None,
        period_num: int = None,
    ):
        # The time to check for unfinished tasks in HH:mm format.
        self.fixed_unfinished_time = fixed_unfinished_time
        # The number of periods.
        self.period_num = period_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fixed_unfinished_time is not None:
            result['FixedUnfinishedTime'] = self.fixed_unfinished_time

        if self.period_num is not None:
            result['PeriodNum'] = self.period_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedUnfinishedTime') is not None:
            self.fixed_unfinished_time = m.get('FixedUnfinishedTime')

        if m.get('PeriodNum') is not None:
            self.period_num = m.get('PeriodNum')

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListUnfinishedRuleDetailConfigDailyUnfinishedConfig(DaraModel):
    def __init__(
        self,
        fixed_unfinished_time: str = None,
    ):
        # The daily time to check for unfinished tasks in HH:mm format.
        self.fixed_unfinished_time = fixed_unfinished_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fixed_unfinished_time is not None:
            result['FixedUnfinishedTime'] = self.fixed_unfinished_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FixedUnfinishedTime') is not None:
            self.fixed_unfinished_time = m.get('FixedUnfinishedTime')

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategy(DaraModel):
    def __init__(
        self,
        alert_frequency: int = None,
        monitored_time_range: main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategyMonitoredTimeRange = None,
        receiver_config_list: List[main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategyReceiverConfigList] = None,
        send_times: int = None,
    ):
        # The alert trigger frequency.
        # 
        # This parameter is required.
        self.alert_frequency = alert_frequency
        # The monitored time range.
        self.monitored_time_range = monitored_time_range
        # The list of recipient configurations.
        # 
        # This parameter is required.
        self.receiver_config_list = receiver_config_list
        # The maximum number of alert notifications to send.
        # 
        # This parameter is required.
        self.send_times = send_times

    def validate(self):
        if self.monitored_time_range:
            self.monitored_time_range.validate()
        if self.receiver_config_list:
            for v1 in self.receiver_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_frequency is not None:
            result['AlertFrequency'] = self.alert_frequency

        if self.monitored_time_range is not None:
            result['MonitoredTimeRange'] = self.monitored_time_range.to_map()

        result['ReceiverConfigList'] = []
        if self.receiver_config_list is not None:
            for k1 in self.receiver_config_list:
                result['ReceiverConfigList'].append(k1.to_map() if k1 else None)

        if self.send_times is not None:
            result['SendTimes'] = self.send_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertFrequency') is not None:
            self.alert_frequency = m.get('AlertFrequency')

        if m.get('MonitoredTimeRange') is not None:
            temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategyMonitoredTimeRange()
            self.monitored_time_range = temp_model.from_map(m.get('MonitoredTimeRange'))

        self.receiver_config_list = []
        if m.get('ReceiverConfigList') is not None:
            for k1 in m.get('ReceiverConfigList'):
                temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategyReceiverConfigList()
                self.receiver_config_list.append(temp_model.from_map(k1))

        if m.get('SendTimes') is not None:
            self.send_times = m.get('SendTimes')

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategyReceiverConfigList(DaraModel):
    def __init__(
        self,
        custom_alert_channel_id_list: List[str] = None,
        on_duty_table_id_list: List[str] = None,
        received_way_list: List[str] = None,
        receiver_type: str = None,
        receiver_user_id_list: List[str] = None,
    ):
        # The list of custom alert channel IDs.
        self.custom_alert_channel_id_list = custom_alert_channel_id_list
        # The list of on-duty table IDs. This parameter is required when ReceiverType is set to ON_DUTY_TABLE.
        self.on_duty_table_id_list = on_duty_table_id_list
        # The list of notification methods. Valid values:
        # - PHONE: Phone call.
        # - MESSAGE: Text message.
        # - EMAIL: Email.
        # - DING_TALK: DingTalk.
        # - FEISHU: Lark.
        # - WECHAT: WeChat.
        # - CUSTOM: Custom channel.
        # 
        # This parameter is required.
        self.received_way_list = received_way_list
        # The recipient type. Valid values:
        # - OWNER: The owner.
        # - USER_CUSTOM: A custom user.
        # - ON_DUTY_TABLE: An on-duty table.
        # 
        # This parameter is required.
        self.receiver_type = receiver_type
        # The list of recipient user IDs. This parameter is required when ReceiverType is set to USER_CUSTOM.
        self.receiver_user_id_list = receiver_user_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_alert_channel_id_list is not None:
            result['CustomAlertChannelIdList'] = self.custom_alert_channel_id_list

        if self.on_duty_table_id_list is not None:
            result['OnDutyTableIdList'] = self.on_duty_table_id_list

        if self.received_way_list is not None:
            result['ReceivedWayList'] = self.received_way_list

        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type

        if self.receiver_user_id_list is not None:
            result['ReceiverUserIdList'] = self.receiver_user_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAlertChannelIdList') is not None:
            self.custom_alert_channel_id_list = m.get('CustomAlertChannelIdList')

        if m.get('OnDutyTableIdList') is not None:
            self.on_duty_table_id_list = m.get('OnDutyTableIdList')

        if m.get('ReceivedWayList') is not None:
            self.received_way_list = m.get('ReceivedWayList')

        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')

        if m.get('ReceiverUserIdList') is not None:
            self.receiver_user_id_list = m.get('ReceiverUserIdList')

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredRuleConfigListAlertStrategyMonitoredTimeRange(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The end time in HH:mm format. Set this parameter to 0 to indicate no limit.
        self.end_time = end_time
        # The start time in HH:mm format. Set this parameter to 0 to indicate no limit.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredItemConfig(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        logical_table_id: int = None,
        logical_table_name: str = None,
        monitored_item_type: str = None,
        monitored_node_range: main_models.CreateScheduleMonitorRequestCreateCommandMonitoredItemConfigMonitoredNodeRange = None,
        node_id: str = None,
        node_name: str = None,
        node_sub_type: str = None,
        ops_owner_id_list: List[str] = None,
        project_id: int = None,
    ):
        # The business unit ID. Specify this parameter when the summary logical table does not have a project ID.
        self.biz_unit_id = biz_unit_id
        # The logical table ID. Specify this parameter when the monitored object type is LOGICAL_FIELD or LOGICAL_TABLE_NODE.
        self.logical_table_id = logical_table_id
        # The name of the logical table.
        self.logical_table_name = logical_table_name
        # The monitored object type. Valid values:
        # - LOGICAL_FIELD: logical field.
        # - OND_ID_NODE: logical table node.
        # - SCHEDULE_PHYSICAL_NODE: physical task with epoch scheduling.
        # - MANUAL_PHYSICAL_NODE: physical task with manual scheduling.
        # - ODM_NODE: source data path task.
        # - LOGICAL_TABLE_NODE: logical table task.
        # - PROJECT: project.
        # 
        # This parameter is required.
        self.monitored_item_type = monitored_item_type
        # The scope of monitored tasks, which serves as the filtering rule for project-level monitoring. Specify this parameter when the monitored object type is PROJECT.
        self.monitored_node_range = monitored_node_range
        # The ID of the monitored task, which is the node ID. This parameter is required when the monitored object type is not PROJECT.
        self.node_id = node_id
        # The name of the monitored task, which is the node name. This parameter is required when the monitored object type is not PROJECT.
        self.node_name = node_name
        # The subtype of the node. This parameter is required when the monitored object type is not PROJECT or LOGICAL_FIELD.
        self.node_sub_type = node_sub_type
        # The list of O&M owner IDs for the node. This serves as the source for the OWNER recipient type.
        self.ops_owner_id_list = ops_owner_id_list
        # The project ID. This parameter is required when the monitored object type is PROJECT. For other types, it specifies the project to which the monitored object belongs.
        self.project_id = project_id

    def validate(self):
        if self.monitored_node_range:
            self.monitored_node_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.logical_table_id is not None:
            result['LogicalTableId'] = self.logical_table_id

        if self.logical_table_name is not None:
            result['LogicalTableName'] = self.logical_table_name

        if self.monitored_item_type is not None:
            result['MonitoredItemType'] = self.monitored_item_type

        if self.monitored_node_range is not None:
            result['MonitoredNodeRange'] = self.monitored_node_range.to_map()

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_sub_type is not None:
            result['NodeSubType'] = self.node_sub_type

        if self.ops_owner_id_list is not None:
            result['OpsOwnerIdList'] = self.ops_owner_id_list

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('LogicalTableId') is not None:
            self.logical_table_id = m.get('LogicalTableId')

        if m.get('LogicalTableName') is not None:
            self.logical_table_name = m.get('LogicalTableName')

        if m.get('MonitoredItemType') is not None:
            self.monitored_item_type = m.get('MonitoredItemType')

        if m.get('MonitoredNodeRange') is not None:
            temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredItemConfigMonitoredNodeRange()
            self.monitored_node_range = temp_model.from_map(m.get('MonitoredNodeRange'))

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeSubType') is not None:
            self.node_sub_type = m.get('NodeSubType')

        if m.get('OpsOwnerIdList') is not None:
            self.ops_owner_id_list = m.get('OpsOwnerIdList')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredItemConfigMonitoredNodeRange(DaraModel):
    def __init__(
        self,
        filter_rule_list: List[main_models.CreateScheduleMonitorRequestCreateCommandMonitoredItemConfigMonitoredNodeRangeFilterRuleList] = None,
    ):
        # The list of filter rules. If this parameter is left empty, all tasks are monitored by default.
        self.filter_rule_list = filter_rule_list

    def validate(self):
        if self.filter_rule_list:
            for v1 in self.filter_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FilterRuleList'] = []
        if self.filter_rule_list is not None:
            for k1 in self.filter_rule_list:
                result['FilterRuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_rule_list = []
        if m.get('FilterRuleList') is not None:
            for k1 in m.get('FilterRuleList'):
                temp_model = main_models.CreateScheduleMonitorRequestCreateCommandMonitoredItemConfigMonitoredNodeRangeFilterRuleList()
                self.filter_rule_list.append(temp_model.from_map(k1))

        return self

class CreateScheduleMonitorRequestCreateCommandMonitoredItemConfigMonitoredNodeRangeFilterRuleList(DaraModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_value_list: List[str] = None,
        is_exclude: bool = None,
    ):
        # The filter key.
        self.filter_key = filter_key
        # The list of filter values. Multiple values are supported.
        self.filter_value_list = filter_value_list
        # Specifies whether to invert the selection.
        self.is_exclude = is_exclude

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key

        if self.filter_value_list is not None:
            result['FilterValueList'] = self.filter_value_list

        if self.is_exclude is not None:
            result['IsExclude'] = self.is_exclude

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')

        if m.get('FilterValueList') is not None:
            self.filter_value_list = m.get('FilterValueList')

        if m.get('IsExclude') is not None:
            self.is_exclude = m.get('IsExclude')

        return self

