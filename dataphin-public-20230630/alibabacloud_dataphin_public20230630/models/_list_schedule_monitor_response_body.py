# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListScheduleMonitorResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListScheduleMonitorResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code of the request. A value of OK indicates that the request is successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message of the request.
        self.message = message
        # The paginated result of the scheduling monitoring alert query.
        self.page_result = page_result
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListScheduleMonitorResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        monitor_item_list: List[main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemList] = None,
        total_count: int = None,
    ):
        # The list of monitored objects on the current page.
        self.monitor_item_list = monitor_item_list
        # The total number of monitored objects that meet the conditions.
        self.total_count = total_count

    def validate(self):
        if self.monitor_item_list:
            for v1 in self.monitor_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MonitorItemList'] = []
        if self.monitor_item_list is not None:
            for k1 in self.monitor_item_list:
                result['MonitorItemList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item_list = []
        if m.get('MonitorItemList') is not None:
            for k1 in m.get('MonitorItemList'):
                temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemList()
                self.monitor_item_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemList(DaraModel):
    def __init__(
        self,
        biz_unit: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListBizUnit = None,
        create_time: str = None,
        logic_table: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListLogicTable = None,
        modified_time: str = None,
        monitor_node_range: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitorNodeRange = None,
        monitored_item_id: int = None,
        monitored_rule_list: List[main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleList] = None,
        monitored_task: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredTask = None,
        project_id: int = None,
        project_info: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListProjectInfo = None,
        sub_type: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        # The business segment information.
        self.biz_unit = biz_unit
        # The creation time.
        self.create_time = create_time
        # The logical table information.
        self.logic_table = logic_table
        # The last modification time.
        self.modified_time = modified_time
        # The scope of the monitoring task.
        self.monitor_node_range = monitor_node_range
        # The ID of the monitored object.
        self.monitored_item_id = monitored_item_id
        # The list of monitoring rules.
        self.monitored_rule_list = monitored_rule_list
        # The monitored task information.
        self.monitored_task = monitored_task
        # The project ID.
        self.project_id = project_id
        # The project information.
        self.project_info = project_info
        # The business subtype.
        self.sub_type = sub_type
        # The tenant ID.
        self.tenant_id = tenant_id
        # The monitored object type.
        self.type = type

    def validate(self):
        if self.biz_unit:
            self.biz_unit.validate()
        if self.logic_table:
            self.logic_table.validate()
        if self.monitor_node_range:
            self.monitor_node_range.validate()
        if self.monitored_rule_list:
            for v1 in self.monitored_rule_list:
                 if v1:
                    v1.validate()
        if self.monitored_task:
            self.monitored_task.validate()
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit is not None:
            result['BizUnit'] = self.biz_unit.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.logic_table is not None:
            result['LogicTable'] = self.logic_table.to_map()

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.monitor_node_range is not None:
            result['MonitorNodeRange'] = self.monitor_node_range.to_map()

        if self.monitored_item_id is not None:
            result['MonitoredItemId'] = self.monitored_item_id

        result['MonitoredRuleList'] = []
        if self.monitored_rule_list is not None:
            for k1 in self.monitored_rule_list:
                result['MonitoredRuleList'].append(k1.to_map() if k1 else None)

        if self.monitored_task is not None:
            result['MonitoredTask'] = self.monitored_task.to_map()

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnit') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListBizUnit()
            self.biz_unit = temp_model.from_map(m.get('BizUnit'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('LogicTable') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListLogicTable()
            self.logic_table = temp_model.from_map(m.get('LogicTable'))

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('MonitorNodeRange') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitorNodeRange()
            self.monitor_node_range = temp_model.from_map(m.get('MonitorNodeRange'))

        if m.get('MonitoredItemId') is not None:
            self.monitored_item_id = m.get('MonitoredItemId')

        self.monitored_rule_list = []
        if m.get('MonitoredRuleList') is not None:
            for k1 in m.get('MonitoredRuleList'):
                temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleList()
                self.monitored_rule_list.append(temp_model.from_map(k1))

        if m.get('MonitoredTask') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredTask()
            self.monitored_task = temp_model.from_map(m.get('MonitoredTask'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectInfo') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListProjectInfo()
            self.project_info = temp_model.from_map(m.get('ProjectInfo'))

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListProjectInfo(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The project ID.
        self.id = id
        # The project name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredTask(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        project_name: str = None,
        schedule_period_type: str = None,
    ):
        # The ID of the monitoring task.
        self.id = id
        # The name of the monitoring task.
        self.name = name
        # The name of the project to which the task belongs.
        self.project_name = project_name
        # The schedule period type. Valid values: MINUTELY, HOURLY, DAILY, WEEKLY, MONTHLY, and YEARLY.
        self.schedule_period_type = schedule_period_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.schedule_period_type is not None:
            result['SchedulePeriodType'] = self.schedule_period_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SchedulePeriodType') is not None:
            self.schedule_period_type = m.get('SchedulePeriodType')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleList(DaraModel):
    def __init__(
        self,
        alert_reason: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReason = None,
        alert_strategy: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategy = None,
        create_time: str = None,
        creator: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListCreator = None,
        id: int = None,
        modified_time: str = None,
        modifier: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListModifier = None,
        monitored_item_id: int = None,
        project_id: int = None,
        switch_status: bool = None,
        tenant_id: str = None,
    ):
        # The reason for the alert.
        self.alert_reason = alert_reason
        # The alert strategy.
        self.alert_strategy = alert_strategy
        # The creation time.
        self.create_time = create_time
        # The creator.
        self.creator = creator
        # The monitoring rule ID.
        self.id = id
        # The last modification time.
        self.modified_time = modified_time
        # The last modifier.
        self.modifier = modifier
        # The ID of the associated monitoring item.
        self.monitored_item_id = monitored_item_id
        # The project ID.
        self.project_id = project_id
        # The enablement status of the rule.
        self.switch_status = switch_status
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        if self.alert_reason:
            self.alert_reason.validate()
        if self.alert_strategy:
            self.alert_strategy.validate()
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_reason is not None:
            result['AlertReason'] = self.alert_reason.to_map()

        if self.alert_strategy is not None:
            result['AlertStrategy'] = self.alert_strategy.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()

        if self.monitored_item_id is not None:
            result['MonitoredItemId'] = self.monitored_item_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.switch_status is not None:
            result['SwitchStatus'] = self.switch_status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertReason') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReason()
            self.alert_reason = temp_model.from_map(m.get('AlertReason'))

        if m.get('AlertStrategy') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategy()
            self.alert_strategy = temp_model.from_map(m.get('AlertStrategy'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Modifier') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListModifier()
            self.modifier = temp_model.from_map(m.get('Modifier'))

        if m.get('MonitoredItemId') is not None:
            self.monitored_item_id = m.get('MonitoredItemId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SwitchStatus') is not None:
            self.switch_status = m.get('SwitchStatus')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListModifier(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The user ID.
        self.id = id
        # The username.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListCreator(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The user ID.
        self.id = id
        # The username.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategy(DaraModel):
    def __init__(
        self,
        alert_frequency: int = None,
        monitored_time_range: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategyMonitoredTimeRange = None,
        receiver_config_list: List[main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategyReceiverConfigList] = None,
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
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategyMonitoredTimeRange()
            self.monitored_time_range = temp_model.from_map(m.get('MonitoredTimeRange'))

        self.receiver_config_list = []
        if m.get('ReceiverConfigList') is not None:
            for k1 in m.get('ReceiverConfigList'):
                temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategyReceiverConfigList()
                self.receiver_config_list.append(temp_model.from_map(k1))

        if m.get('SendTimes') is not None:
            self.send_times = m.get('SendTimes')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategyReceiverConfigList(DaraModel):
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
        # The list of notification methods. Valid values: PHONE, MESSAGE, EMAIL, DING_TALK, FEISHU, WECHAT, and CUSTOM.
        # 
        # This parameter is required.
        self.received_way_list = received_way_list
        # The recipient type. Valid values: OWNER (owner), USER_CUSTOM (custom user), and ON_DUTY_TABLE (on-duty table).
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

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertStrategyMonitoredTimeRange(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The end time in HH:mm format. A value of 0 indicates no limit.
        self.end_time = end_time
        # The start time in HH:mm format. A value of 0 indicates no limit.
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

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReason(DaraModel):
    def __init__(
        self,
        alert_reason_type: str = None,
        fixed_elapsed_time: int = None,
        fixed_unfinished_time: str = None,
        unfinished_rule_detail_config: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfig = None,
    ):
        # The type of the alert reason. Valid values: FAILED, TIME_OUT, UNFINISHED, SUCCESS, and DATA_DELAY.
        self.alert_reason_type = alert_reason_type
        # The timeout period in minutes. This parameter is returned only when the alert reason type is TIME_OUT.
        self.fixed_elapsed_time = fixed_elapsed_time
        # The daily check time for unfinished tasks in HH:mm format. This parameter is returned only when the alert reason type is UNFINISHED.
        self.fixed_unfinished_time = fixed_unfinished_time
        # The detailed configuration of the unfinished rule. This parameter is returned only when the alert reason type is UNFINISHED.
        self.unfinished_rule_detail_config = unfinished_rule_detail_config

    def validate(self):
        if self.unfinished_rule_detail_config:
            self.unfinished_rule_detail_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_reason_type is not None:
            result['AlertReasonType'] = self.alert_reason_type

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

        if m.get('FixedElapsedTime') is not None:
            self.fixed_elapsed_time = m.get('FixedElapsedTime')

        if m.get('FixedUnfinishedTime') is not None:
            self.fixed_unfinished_time = m.get('FixedUnfinishedTime')

        if m.get('UnfinishedRuleDetailConfig') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfig()
            self.unfinished_rule_detail_config = temp_model.from_map(m.get('UnfinishedRuleDetailConfig'))

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfig(DaraModel):
    def __init__(
        self,
        daily_unfinished_config: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigDailyUnfinishedConfig = None,
        multi_period_unfinished_config: main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfig = None,
    ):
        # The daily configuration for unfinished tasks.
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
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigDailyUnfinishedConfig()
            self.daily_unfinished_config = temp_model.from_map(m.get('DailyUnfinishedConfig'))

        if m.get('MultiPeriodUnfinishedConfig') is not None:
            temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfig()
            self.multi_period_unfinished_config = temp_model.from_map(m.get('MultiPeriodUnfinishedConfig'))

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfig(DaraModel):
    def __init__(
        self,
        custom_period_list: List[main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfigCustomPeriodList] = None,
        interval_after_due_time: int = None,
        interval_unit: str = None,
        monitor_period_type: str = None,
        trigger_rule_type: str = None,
    ):
        # The list of custom monitoring periods.
        self.custom_period_list = custom_period_list
        # The interval value.
        self.interval_after_due_time = interval_after_due_time
        # The interval unit. Valid values: SECONDS, MINUTES, and HOURS.
        self.interval_unit = interval_unit
        # The monitoring period type. Valid values: ALL, FIRST, LAST, and CUSTOM.
        self.monitor_period_type = monitor_period_type
        # The trigger rule type.
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
                temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfigCustomPeriodList()
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

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigMultiPeriodUnfinishedConfigCustomPeriodList(DaraModel):
    def __init__(
        self,
        fixed_unfinished_time: str = None,
        period_num: int = None,
    ):
        # The time for the unfinished check, in HH:mm format.
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

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitoredRuleListAlertReasonUnfinishedRuleDetailConfigDailyUnfinishedConfig(DaraModel):
    def __init__(
        self,
        fixed_unfinished_time: str = None,
    ):
        # The time of day for the unfinished check, in HH:mm format.
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

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitorNodeRange(DaraModel):
    def __init__(
        self,
        filter_rule_list: List[main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitorNodeRangeFilterRuleList] = None,
    ):
        # The list of filter rules.
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
                temp_model = main_models.ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitorNodeRangeFilterRuleList()
                self.filter_rule_list.append(temp_model.from_map(k1))

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListMonitorNodeRangeFilterRuleList(DaraModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_value_list: List[str] = None,
        is_exclude: bool = None,
    ):
        # The filter key.
        self.filter_key = filter_key
        # The list of filter values.
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

class ListScheduleMonitorResponseBodyPageResultMonitorItemListLogicTable(DaraModel):
    def __init__(
        self,
        biz_unit_id: int = None,
        id: str = None,
        name: str = None,
        node_sub_type: str = None,
        owner_id_list: List[str] = None,
        project_name: str = None,
        schedule_period_type: str = None,
        support_data_delay: bool = None,
    ):
        # The ID of the business segment.
        self.biz_unit_id = biz_unit_id
        # The ID of the monitoring task.
        self.id = id
        # The name of the monitoring task.
        self.name = name
        # The subtype of the node.
        self.node_sub_type = node_sub_type
        # The list of O&M owner IDs.
        self.owner_id_list = owner_id_list
        # The name of the project to which the task belongs.
        self.project_name = project_name
        # The type of the scheduling period.
        self.schedule_period_type = schedule_period_type
        # Specifies whether data delay is supported.
        self.support_data_delay = support_data_delay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_unit_id is not None:
            result['BizUnitId'] = self.biz_unit_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.node_sub_type is not None:
            result['NodeSubType'] = self.node_sub_type

        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.schedule_period_type is not None:
            result['SchedulePeriodType'] = self.schedule_period_type

        if self.support_data_delay is not None:
            result['SupportDataDelay'] = self.support_data_delay

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizUnitId') is not None:
            self.biz_unit_id = m.get('BizUnitId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeSubType') is not None:
            self.node_sub_type = m.get('NodeSubType')

        if m.get('OwnerIdList') is not None:
            self.owner_id_list = m.get('OwnerIdList')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('SchedulePeriodType') is not None:
            self.schedule_period_type = m.get('SchedulePeriodType')

        if m.get('SupportDataDelay') is not None:
            self.support_data_delay = m.get('SupportDataDelay')

        return self

class ListScheduleMonitorResponseBodyPageResultMonitorItemListBizUnit(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        id: int = None,
        name: str = None,
    ):
        # The display name of the business segment.
        self.display_name = display_name
        # The ID of the business segment.
        self.id = id
        # The name of the business segment.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

