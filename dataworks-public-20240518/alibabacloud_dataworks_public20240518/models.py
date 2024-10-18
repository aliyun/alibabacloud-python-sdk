# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AbolishDeploymentRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the process.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class AbolishDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AbolishDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AbolishDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AbolishDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateProjectToResourceGroupRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class AssociateProjectToResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssociateProjectToResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateProjectToResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateProjectToResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloneDataSourceRequest(TeaModel):
    def __init__(
        self,
        clone_data_source_name: str = None,
        id: int = None,
    ):
        self.clone_data_source_name = clone_data_source_name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clone_data_source_name is not None:
            result['CloneDataSourceName'] = self.clone_data_source_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloneDataSourceName') is not None:
            self.clone_data_source_name = m.get('CloneDataSourceName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class CloneDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloneDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloneDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CloneDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDIAlarmRuleRequestNotificationSettingsNotificationChannels(TeaModel):
    def __init__(
        self,
        channels: List[str] = None,
        severity: str = None,
    ):
        self.channels = channels
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class CreateDIAlarmRuleRequestNotificationSettingsNotificationReceivers(TeaModel):
    def __init__(
        self,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        self.receiver_type = receiver_type
        self.receiver_values = receiver_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type
        if self.receiver_values is not None:
            result['ReceiverValues'] = self.receiver_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')
        if m.get('ReceiverValues') is not None:
            self.receiver_values = m.get('ReceiverValues')
        return self


class CreateDIAlarmRuleRequestNotificationSettings(TeaModel):
    def __init__(
        self,
        inhibition_interval: int = None,
        notification_channels: List[CreateDIAlarmRuleRequestNotificationSettingsNotificationChannels] = None,
        notification_receivers: List[CreateDIAlarmRuleRequestNotificationSettingsNotificationReceivers] = None,
    ):
        self.inhibition_interval = inhibition_interval
        self.notification_channels = notification_channels
        self.notification_receivers = notification_receivers

    def validate(self):
        if self.notification_channels:
            for k in self.notification_channels:
                if k:
                    k.validate()
        if self.notification_receivers:
            for k in self.notification_receivers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inhibition_interval is not None:
            result['InhibitionInterval'] = self.inhibition_interval
        result['NotificationChannels'] = []
        if self.notification_channels is not None:
            for k in self.notification_channels:
                result['NotificationChannels'].append(k.to_map() if k else None)
        result['NotificationReceivers'] = []
        if self.notification_receivers is not None:
            for k in self.notification_receivers:
                result['NotificationReceivers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InhibitionInterval') is not None:
            self.inhibition_interval = m.get('InhibitionInterval')
        self.notification_channels = []
        if m.get('NotificationChannels') is not None:
            for k in m.get('NotificationChannels'):
                temp_model = CreateDIAlarmRuleRequestNotificationSettingsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k))
        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k in m.get('NotificationReceivers'):
                temp_model = CreateDIAlarmRuleRequestNotificationSettingsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k))
        return self


class CreateDIAlarmRuleRequestTriggerConditions(TeaModel):
    def __init__(
        self,
        ddl_report_tags: List[str] = None,
        duration: int = None,
        severity: str = None,
        threshold: int = None,
    ):
        self.ddl_report_tags = ddl_report_tags
        self.duration = duration
        self.severity = severity
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl_report_tags is not None:
            result['DdlReportTags'] = self.ddl_report_tags
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdlReportTags') is not None:
            self.ddl_report_tags = m.get('DdlReportTags')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class CreateDIAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        name: str = None,
        notification_settings: CreateDIAlarmRuleRequestNotificationSettings = None,
        trigger_conditions: List[CreateDIAlarmRuleRequestTriggerConditions] = None,
    ):
        self.client_token = client_token
        # 任务ID，是告警规则关联的任务ID。
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # 描述。
        self.description = description
        # 告警规则是否启用，默认不开启。
        self.enabled = enabled
        # 告警指标类型，可选的枚举值：
        # - Heartbeat（任务状态报警）
        # - FailoverCount（failover次数报警）
        # - Delay（任务延迟报警）
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.notification_settings = notification_settings
        # This parameter is required.
        self.trigger_conditions = trigger_conditions

    def validate(self):
        if self.notification_settings:
            self.notification_settings.validate()
        if self.trigger_conditions:
            for k in self.trigger_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.notification_settings is not None:
            result['NotificationSettings'] = self.notification_settings.to_map()
        result['TriggerConditions'] = []
        if self.trigger_conditions is not None:
            for k in self.trigger_conditions:
                result['TriggerConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotificationSettings') is not None:
            temp_model = CreateDIAlarmRuleRequestNotificationSettings()
            self.notification_settings = temp_model.from_map(m['NotificationSettings'])
        self.trigger_conditions = []
        if m.get('TriggerConditions') is not None:
            for k in m.get('TriggerConditions'):
                temp_model = CreateDIAlarmRuleRequestTriggerConditions()
                self.trigger_conditions.append(temp_model.from_map(k))
        return self


class CreateDIAlarmRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        name: str = None,
        notification_settings_shrink: str = None,
        trigger_conditions_shrink: str = None,
    ):
        self.client_token = client_token
        # 任务ID，是告警规则关联的任务ID。
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # 描述。
        self.description = description
        # 告警规则是否启用，默认不开启。
        self.enabled = enabled
        # 告警指标类型，可选的枚举值：
        # - Heartbeat（任务状态报警）
        # - FailoverCount（failover次数报警）
        # - Delay（任务延迟报警）
        # 
        # This parameter is required.
        self.metric_type = metric_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.notification_settings_shrink = notification_settings_shrink
        # This parameter is required.
        self.trigger_conditions_shrink = trigger_conditions_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.notification_settings_shrink is not None:
            result['NotificationSettings'] = self.notification_settings_shrink
        if self.trigger_conditions_shrink is not None:
            result['TriggerConditions'] = self.trigger_conditions_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotificationSettings') is not None:
            self.notification_settings_shrink = m.get('NotificationSettings')
        if m.get('TriggerConditions') is not None:
            self.trigger_conditions_shrink = m.get('TriggerConditions')
        return self


class CreateDIAlarmRuleResponseBody(TeaModel):
    def __init__(
        self,
        dialarm_rule_id: str = None,
        request_id: str = None,
    ):
        # 代表资源一级ID的资源属性字段
        self.dialarm_rule_id = dialarm_rule_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDIAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDIAlarmRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDIAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDIJobRequestDestinationDataSourceSettings(TeaModel):
    def __init__(
        self,
        data_source_name: str = None,
    ):
        self.data_source_name = data_source_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        return self


class CreateDIJobRequestJobSettingsColumnDataTypeSettings(TeaModel):
    def __init__(
        self,
        destination_data_type: str = None,
        source_data_type: str = None,
    ):
        self.destination_data_type = destination_data_type
        self.source_data_type = source_data_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_data_type is not None:
            result['DestinationDataType'] = self.destination_data_type
        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDataType') is not None:
            self.destination_data_type = m.get('DestinationDataType')
        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')
        return self


class CreateDIJobRequestJobSettingsCycleScheduleSettings(TeaModel):
    def __init__(
        self,
        cycle_migration_type: str = None,
        schedule_parameters: str = None,
    ):
        self.cycle_migration_type = cycle_migration_type
        self.schedule_parameters = schedule_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycle_migration_type is not None:
            result['CycleMigrationType'] = self.cycle_migration_type
        if self.schedule_parameters is not None:
            result['ScheduleParameters'] = self.schedule_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleMigrationType') is not None:
            self.cycle_migration_type = m.get('CycleMigrationType')
        if m.get('ScheduleParameters') is not None:
            self.schedule_parameters = m.get('ScheduleParameters')
        return self


class CreateDIJobRequestJobSettingsDdlHandlingSettings(TeaModel):
    def __init__(
        self,
        action: str = None,
        type: str = None,
    ):
        self.action = action
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDIJobRequestJobSettingsRuntimeSettings(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateDIJobRequestJobSettings(TeaModel):
    def __init__(
        self,
        channel_settings: str = None,
        column_data_type_settings: List[CreateDIJobRequestJobSettingsColumnDataTypeSettings] = None,
        cycle_schedule_settings: CreateDIJobRequestJobSettingsCycleScheduleSettings = None,
        ddl_handling_settings: List[CreateDIJobRequestJobSettingsDdlHandlingSettings] = None,
        runtime_settings: List[CreateDIJobRequestJobSettingsRuntimeSettings] = None,
    ):
        self.channel_settings = channel_settings
        self.column_data_type_settings = column_data_type_settings
        self.cycle_schedule_settings = cycle_schedule_settings
        self.ddl_handling_settings = ddl_handling_settings
        self.runtime_settings = runtime_settings

    def validate(self):
        if self.column_data_type_settings:
            for k in self.column_data_type_settings:
                if k:
                    k.validate()
        if self.cycle_schedule_settings:
            self.cycle_schedule_settings.validate()
        if self.ddl_handling_settings:
            for k in self.ddl_handling_settings:
                if k:
                    k.validate()
        if self.runtime_settings:
            for k in self.runtime_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_settings is not None:
            result['ChannelSettings'] = self.channel_settings
        result['ColumnDataTypeSettings'] = []
        if self.column_data_type_settings is not None:
            for k in self.column_data_type_settings:
                result['ColumnDataTypeSettings'].append(k.to_map() if k else None)
        if self.cycle_schedule_settings is not None:
            result['CycleScheduleSettings'] = self.cycle_schedule_settings.to_map()
        result['DdlHandlingSettings'] = []
        if self.ddl_handling_settings is not None:
            for k in self.ddl_handling_settings:
                result['DdlHandlingSettings'].append(k.to_map() if k else None)
        result['RuntimeSettings'] = []
        if self.runtime_settings is not None:
            for k in self.runtime_settings:
                result['RuntimeSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelSettings') is not None:
            self.channel_settings = m.get('ChannelSettings')
        self.column_data_type_settings = []
        if m.get('ColumnDataTypeSettings') is not None:
            for k in m.get('ColumnDataTypeSettings'):
                temp_model = CreateDIJobRequestJobSettingsColumnDataTypeSettings()
                self.column_data_type_settings.append(temp_model.from_map(k))
        if m.get('CycleScheduleSettings') is not None:
            temp_model = CreateDIJobRequestJobSettingsCycleScheduleSettings()
            self.cycle_schedule_settings = temp_model.from_map(m['CycleScheduleSettings'])
        self.ddl_handling_settings = []
        if m.get('DdlHandlingSettings') is not None:
            for k in m.get('DdlHandlingSettings'):
                temp_model = CreateDIJobRequestJobSettingsDdlHandlingSettings()
                self.ddl_handling_settings.append(temp_model.from_map(k))
        self.runtime_settings = []
        if m.get('RuntimeSettings') is not None:
            for k in m.get('RuntimeSettings'):
                temp_model = CreateDIJobRequestJobSettingsRuntimeSettings()
                self.runtime_settings.append(temp_model.from_map(k))
        return self


class CreateDIJobRequestResourceSettingsOfflineResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class CreateDIJobRequestResourceSettingsRealtimeResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class CreateDIJobRequestResourceSettingsScheduleResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class CreateDIJobRequestResourceSettings(TeaModel):
    def __init__(
        self,
        offline_resource_settings: CreateDIJobRequestResourceSettingsOfflineResourceSettings = None,
        realtime_resource_settings: CreateDIJobRequestResourceSettingsRealtimeResourceSettings = None,
        schedule_resource_settings: CreateDIJobRequestResourceSettingsScheduleResourceSettings = None,
    ):
        self.offline_resource_settings = offline_resource_settings
        self.realtime_resource_settings = realtime_resource_settings
        self.schedule_resource_settings = schedule_resource_settings

    def validate(self):
        if self.offline_resource_settings:
            self.offline_resource_settings.validate()
        if self.realtime_resource_settings:
            self.realtime_resource_settings.validate()
        if self.schedule_resource_settings:
            self.schedule_resource_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offline_resource_settings is not None:
            result['OfflineResourceSettings'] = self.offline_resource_settings.to_map()
        if self.realtime_resource_settings is not None:
            result['RealtimeResourceSettings'] = self.realtime_resource_settings.to_map()
        if self.schedule_resource_settings is not None:
            result['ScheduleResourceSettings'] = self.schedule_resource_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfflineResourceSettings') is not None:
            temp_model = CreateDIJobRequestResourceSettingsOfflineResourceSettings()
            self.offline_resource_settings = temp_model.from_map(m['OfflineResourceSettings'])
        if m.get('RealtimeResourceSettings') is not None:
            temp_model = CreateDIJobRequestResourceSettingsRealtimeResourceSettings()
            self.realtime_resource_settings = temp_model.from_map(m['RealtimeResourceSettings'])
        if m.get('ScheduleResourceSettings') is not None:
            temp_model = CreateDIJobRequestResourceSettingsScheduleResourceSettings()
            self.schedule_resource_settings = temp_model.from_map(m['ScheduleResourceSettings'])
        return self


class CreateDIJobRequestSourceDataSourceSettingsDataSourceProperties(TeaModel):
    def __init__(
        self,
        encoding: str = None,
        timezone: str = None,
    ):
        self.encoding = encoding
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        return self


class CreateDIJobRequestSourceDataSourceSettings(TeaModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_properties: CreateDIJobRequestSourceDataSourceSettingsDataSourceProperties = None,
    ):
        self.data_source_name = data_source_name
        self.data_source_properties = data_source_properties

    def validate(self):
        if self.data_source_properties:
            self.data_source_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_properties is not None:
            result['DataSourceProperties'] = self.data_source_properties.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceProperties') is not None:
            temp_model = CreateDIJobRequestSourceDataSourceSettingsDataSourceProperties()
            self.data_source_properties = temp_model.from_map(m['DataSourceProperties'])
        return self


class CreateDIJobRequestTableMappingsSourceObjectSelectionRules(TeaModel):
    def __init__(
        self,
        action: str = None,
        expression: str = None,
        expression_type: str = None,
        object_type: str = None,
    ):
        self.action = action
        self.expression = expression
        self.expression_type = expression_type
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        return self


class CreateDIJobRequestTableMappingsTransformationRules(TeaModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        self.rule_action_type = rule_action_type
        self.rule_name = rule_name
        self.rule_target_type = rule_target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_target_type is not None:
            result['RuleTargetType'] = self.rule_target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleTargetType') is not None:
            self.rule_target_type = m.get('RuleTargetType')
        return self


class CreateDIJobRequestTableMappings(TeaModel):
    def __init__(
        self,
        source_object_selection_rules: List[CreateDIJobRequestTableMappingsSourceObjectSelectionRules] = None,
        transformation_rules: List[CreateDIJobRequestTableMappingsTransformationRules] = None,
    ):
        self.source_object_selection_rules = source_object_selection_rules
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.source_object_selection_rules:
            for k in self.source_object_selection_rules:
                if k:
                    k.validate()
        if self.transformation_rules:
            for k in self.transformation_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceObjectSelectionRules'] = []
        if self.source_object_selection_rules is not None:
            for k in self.source_object_selection_rules:
                result['SourceObjectSelectionRules'].append(k.to_map() if k else None)
        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k in self.transformation_rules:
                result['TransformationRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_object_selection_rules = []
        if m.get('SourceObjectSelectionRules') is not None:
            for k in m.get('SourceObjectSelectionRules'):
                temp_model = CreateDIJobRequestTableMappingsSourceObjectSelectionRules()
                self.source_object_selection_rules.append(temp_model.from_map(k))
        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k in m.get('TransformationRules'):
                temp_model = CreateDIJobRequestTableMappingsTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k))
        return self


class CreateDIJobRequestTransformationRules(TeaModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_expression: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        self.rule_action_type = rule_action_type
        self.rule_expression = rule_expression
        self.rule_name = rule_name
        self.rule_target_type = rule_target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_target_type is not None:
            result['RuleTargetType'] = self.rule_target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleTargetType') is not None:
            self.rule_target_type = m.get('RuleTargetType')
        return self


class CreateDIJobRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        destination_data_source_settings: List[CreateDIJobRequestDestinationDataSourceSettings] = None,
        destination_data_source_type: str = None,
        job_name: str = None,
        job_settings: CreateDIJobRequestJobSettings = None,
        migration_type: str = None,
        project_id: int = None,
        resource_settings: CreateDIJobRequestResourceSettings = None,
        source_data_source_settings: List[CreateDIJobRequestSourceDataSourceSettings] = None,
        source_data_source_type: str = None,
        table_mappings: List[CreateDIJobRequestTableMappings] = None,
        transformation_rules: List[CreateDIJobRequestTransformationRules] = None,
    ):
        self.description = description
        # This parameter is required.
        self.destination_data_source_settings = destination_data_source_settings
        # This parameter is required.
        self.destination_data_source_type = destination_data_source_type
        # This parameter is required.
        self.job_name = job_name
        self.job_settings = job_settings
        # This parameter is required.
        self.migration_type = migration_type
        self.project_id = project_id
        # This parameter is required.
        self.resource_settings = resource_settings
        # This parameter is required.
        self.source_data_source_settings = source_data_source_settings
        # This parameter is required.
        self.source_data_source_type = source_data_source_type
        # This parameter is required.
        self.table_mappings = table_mappings
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.destination_data_source_settings:
            for k in self.destination_data_source_settings:
                if k:
                    k.validate()
        if self.job_settings:
            self.job_settings.validate()
        if self.resource_settings:
            self.resource_settings.validate()
        if self.source_data_source_settings:
            for k in self.source_data_source_settings:
                if k:
                    k.validate()
        if self.table_mappings:
            for k in self.table_mappings:
                if k:
                    k.validate()
        if self.transformation_rules:
            for k in self.transformation_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        result['DestinationDataSourceSettings'] = []
        if self.destination_data_source_settings is not None:
            for k in self.destination_data_source_settings:
                result['DestinationDataSourceSettings'].append(k.to_map() if k else None)
        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_settings is not None:
            result['JobSettings'] = self.job_settings.to_map()
        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_settings is not None:
            result['ResourceSettings'] = self.resource_settings.to_map()
        result['SourceDataSourceSettings'] = []
        if self.source_data_source_settings is not None:
            for k in self.source_data_source_settings:
                result['SourceDataSourceSettings'].append(k.to_map() if k else None)
        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type
        result['TableMappings'] = []
        if self.table_mappings is not None:
            for k in self.table_mappings:
                result['TableMappings'].append(k.to_map() if k else None)
        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k in self.transformation_rules:
                result['TransformationRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.destination_data_source_settings = []
        if m.get('DestinationDataSourceSettings') is not None:
            for k in m.get('DestinationDataSourceSettings'):
                temp_model = CreateDIJobRequestDestinationDataSourceSettings()
                self.destination_data_source_settings.append(temp_model.from_map(k))
        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobSettings') is not None:
            temp_model = CreateDIJobRequestJobSettings()
            self.job_settings = temp_model.from_map(m['JobSettings'])
        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceSettings') is not None:
            temp_model = CreateDIJobRequestResourceSettings()
            self.resource_settings = temp_model.from_map(m['ResourceSettings'])
        self.source_data_source_settings = []
        if m.get('SourceDataSourceSettings') is not None:
            for k in m.get('SourceDataSourceSettings'):
                temp_model = CreateDIJobRequestSourceDataSourceSettings()
                self.source_data_source_settings.append(temp_model.from_map(k))
        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')
        self.table_mappings = []
        if m.get('TableMappings') is not None:
            for k in m.get('TableMappings'):
                temp_model = CreateDIJobRequestTableMappings()
                self.table_mappings.append(temp_model.from_map(k))
        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k in m.get('TransformationRules'):
                temp_model = CreateDIJobRequestTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k))
        return self


class CreateDIJobShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        destination_data_source_settings_shrink: str = None,
        destination_data_source_type: str = None,
        job_name: str = None,
        job_settings_shrink: str = None,
        migration_type: str = None,
        project_id: int = None,
        resource_settings_shrink: str = None,
        source_data_source_settings_shrink: str = None,
        source_data_source_type: str = None,
        table_mappings_shrink: str = None,
        transformation_rules_shrink: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.destination_data_source_settings_shrink = destination_data_source_settings_shrink
        # This parameter is required.
        self.destination_data_source_type = destination_data_source_type
        # This parameter is required.
        self.job_name = job_name
        self.job_settings_shrink = job_settings_shrink
        # This parameter is required.
        self.migration_type = migration_type
        self.project_id = project_id
        # This parameter is required.
        self.resource_settings_shrink = resource_settings_shrink
        # This parameter is required.
        self.source_data_source_settings_shrink = source_data_source_settings_shrink
        # This parameter is required.
        self.source_data_source_type = source_data_source_type
        # This parameter is required.
        self.table_mappings_shrink = table_mappings_shrink
        self.transformation_rules_shrink = transformation_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_data_source_settings_shrink is not None:
            result['DestinationDataSourceSettings'] = self.destination_data_source_settings_shrink
        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_settings_shrink is not None:
            result['JobSettings'] = self.job_settings_shrink
        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_settings_shrink is not None:
            result['ResourceSettings'] = self.resource_settings_shrink
        if self.source_data_source_settings_shrink is not None:
            result['SourceDataSourceSettings'] = self.source_data_source_settings_shrink
        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type
        if self.table_mappings_shrink is not None:
            result['TableMappings'] = self.table_mappings_shrink
        if self.transformation_rules_shrink is not None:
            result['TransformationRules'] = self.transformation_rules_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationDataSourceSettings') is not None:
            self.destination_data_source_settings_shrink = m.get('DestinationDataSourceSettings')
        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobSettings') is not None:
            self.job_settings_shrink = m.get('JobSettings')
        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceSettings') is not None:
            self.resource_settings_shrink = m.get('ResourceSettings')
        if m.get('SourceDataSourceSettings') is not None:
            self.source_data_source_settings_shrink = m.get('SourceDataSourceSettings')
        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')
        if m.get('TableMappings') is not None:
            self.table_mappings_shrink = m.get('TableMappings')
        if m.get('TransformationRules') is not None:
            self.transformation_rules_shrink = m.get('TransformationRules')
        return self


class CreateDIJobResponseBody(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        request_id: str = None,
    ):
        self.dijob_id = dijob_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDIJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDIJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceRequest(TeaModel):
    def __init__(
        self,
        connection_properties: str = None,
        connection_properties_mode: str = None,
        description: str = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.connection_properties = connection_properties
        # This parameter is required.
        self.connection_properties_mode = connection_properties_mode
        self.description = description
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties
        if self.connection_properties_mode is not None:
            result['ConnectionPropertiesMode'] = self.connection_properties_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')
        if m.get('ConnectionPropertiesMode') is not None:
            self.connection_properties_mode = m.get('ConnectionPropertiesMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDataSourceSharedRuleRequest(TeaModel):
    def __init__(
        self,
        data_source_id: int = None,
        env_type: str = None,
        shared_user: str = None,
        target_project_id: int = None,
    ):
        # This parameter is required.
        self.data_source_id = data_source_id
        # This parameter is required.
        self.env_type = env_type
        self.shared_user = shared_user
        # This parameter is required.
        self.target_project_id = target_project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.shared_user is not None:
            result['SharedUser'] = self.shared_user
        if self.target_project_id is not None:
            result['TargetProjectId'] = self.target_project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('SharedUser') is not None:
            self.shared_user = m.get('SharedUser')
        if m.get('TargetProjectId') is not None:
            self.target_project_id = m.get('TargetProjectId')
        return self


class CreateDataSourceSharedRuleResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataSourceSharedRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDataSourceSharedRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDataSourceSharedRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeploymentRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        object_ids: List[str] = None,
        project_id: str = None,
        type: str = None,
    ):
        # The description of the process.
        self.description = description
        # The IDs of entities to which you want to apply the process.
        # 
        # >  A process can be applied to only a single entity and its child entities. If you specify multiple entities in the array, the process is applied only to the first entity in the array and its child entities. Make sure that the array in your request contains only one element. Extra elements will be ignored.
        # 
        # This parameter is required.
        self.object_ids = object_ids
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specifies whether to deploy or undeploy the entity. Valid values:
        # 
        # *   Online: deploys the entity.
        # *   Offline: undeploys the entity.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.object_ids is not None:
            result['ObjectIds'] = self.object_ids
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectIds') is not None:
            self.object_ids = m.get('ObjectIds')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDeploymentShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        object_ids_shrink: str = None,
        project_id: str = None,
        type: str = None,
    ):
        # The description of the process.
        self.description = description
        # The IDs of entities to which you want to apply the process.
        # 
        # >  A process can be applied to only a single entity and its child entities. If you specify multiple entities in the array, the process is applied only to the first entity in the array and its child entities. Make sure that the array in your request contains only one element. Extra elements will be ignored.
        # 
        # This parameter is required.
        self.object_ids_shrink = object_ids_shrink
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specifies whether to deploy or undeploy the entity. Valid values:
        # 
        # *   Online: deploys the entity.
        # *   Offline: undeploys the entity.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.object_ids_shrink is not None:
            result['ObjectIds'] = self.object_ids_shrink
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ObjectIds') is not None:
            self.object_ids_shrink = m.get('ObjectIds')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # The ID of the process.
        self.id = id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        spec: str = None,
    ):
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec field information about the UDF. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class CreateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # The ID of the UDF.
        self.id = id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetworkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        resource_group_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class CreateNetworkResponseBody(TeaModel):
    def __init__(
        self,
        network_id: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.network_id = network_id
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateNetworkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNetworkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNodeRequest(TeaModel):
    def __init__(
        self,
        container_id: str = None,
        project_id: str = None,
        scene: str = None,
        spec: str = None,
    ):
        # The container ID. If you want to create a node in a container, you must configure this parameter to specify the container. The container can be a workflow or a node in a container.
        # 
        # >  If you configure this parameter, the path field defined in FlowSpec becomes invalid.
        self.container_id = container_id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The scene of the node. This parameter determines the location (the DataStudio pane or the Manual pane) of the node. You can set this parameter to DATAWORKS_MANUAL_WORKFLOW only if the ContainerId parameter is configured and the container specified by ContainerId is a manually triggered workflow.
        # 
        # Valid values:
        # 
        # *   DATAWORKS_PROJECT
        # *   DATAWORKS_MANUAL_WORKFLOW
        # *   DATAWORKS_MANUAL_TASK
        # 
        # This parameter is required.
        self.scene = scene
        # The FlowSpec field information about the node. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class CreateNodeResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # The ID of the node.
        self.id = id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequestAliyunResourceTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[CreateProjectRequestAliyunResourceTags] = None,
        description: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        display_name: str = None,
        name: str = None,
        pai_task_enabled: bool = None,
    ):
        self.aliyun_resource_group_id = aliyun_resource_group_id
        self.aliyun_resource_tags = aliyun_resource_tags
        self.description = description
        self.dev_environment_enabled = dev_environment_enabled
        self.dev_role_disabled = dev_role_disabled
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        self.pai_task_enabled = pai_task_enabled

    def validate(self):
        if self.aliyun_resource_tags:
            for k in self.aliyun_resource_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id
        result['AliyunResourceTags'] = []
        if self.aliyun_resource_tags is not None:
            for k in self.aliyun_resource_tags:
                result['AliyunResourceTags'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled
        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')
        self.aliyun_resource_tags = []
        if m.get('AliyunResourceTags') is not None:
            for k in m.get('AliyunResourceTags'):
                temp_model = CreateProjectRequestAliyunResourceTags()
                self.aliyun_resource_tags.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')
        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')
        return self


class CreateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags_shrink: str = None,
        description: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        display_name: str = None,
        name: str = None,
        pai_task_enabled: bool = None,
    ):
        self.aliyun_resource_group_id = aliyun_resource_group_id
        self.aliyun_resource_tags_shrink = aliyun_resource_tags_shrink
        self.description = description
        self.dev_environment_enabled = dev_environment_enabled
        self.dev_role_disabled = dev_role_disabled
        # This parameter is required.
        self.display_name = display_name
        # This parameter is required.
        self.name = name
        self.pai_task_enabled = pai_task_enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id
        if self.aliyun_resource_tags_shrink is not None:
            result['AliyunResourceTags'] = self.aliyun_resource_tags_shrink
        if self.description is not None:
            result['Description'] = self.description
        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled
        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.name is not None:
            result['Name'] = self.name
        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')
        if m.get('AliyunResourceTags') is not None:
            self.aliyun_resource_tags_shrink = m.get('AliyunResourceTags')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')
        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        request_id: str = None,
    ):
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        spec: str = None,
    ):
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec field information about the file resource. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class CreateResourceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # The ID of the file resource.
        self.id = id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        client_token: str = None,
        name: str = None,
        payment_duration: int = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        remark: str = None,
        spec: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.auto_renew = auto_renew
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.name = name
        self.payment_duration = payment_duration
        self.payment_duration_unit = payment_duration_unit
        # This parameter is required.
        self.payment_type = payment_type
        self.remark = remark
        self.spec = spec
        # This parameter is required.
        self.vpc_id = vpc_id
        # This parameter is required.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_duration is not None:
            result['PaymentDuration'] = self.payment_duration
        if self.payment_duration_unit is not None:
            result['PaymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.spec is not None:
            result['Spec'] = self.spec
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentDuration') is not None:
            self.payment_duration = m.get('PaymentDuration')
        if m.get('PaymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('PaymentDurationUnit')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class CreateResourceGroupResponseBodyResourceGroupOrder(TeaModel):
    def __init__(
        self,
        id: str = None,
        order_id: int = None,
        order_instance_id: str = None,
    ):
        self.id = id
        self.order_id = order_id
        self.order_instance_id = order_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')
        return self


class CreateResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group_order: CreateResourceGroupResponseBodyResourceGroupOrder = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.resource_group_order = resource_group_order
        self.success = success

    def validate(self):
        if self.resource_group_order:
            self.resource_group_order.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_order is not None:
            result['ResourceGroupOrder'] = self.resource_group_order.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupOrder') is not None:
            temp_model = CreateResourceGroupResponseBodyResourceGroupOrder()
            self.resource_group_order = temp_model.from_map(m['ResourceGroupOrder'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRouteRequest(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        network_id: int = None,
    ):
        # This parameter is required.
        self.destination_cidr = destination_cidr
        # This parameter is required.
        self.network_id = network_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        return self


class CreateRouteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        route_id: int = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.route_id = route_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route_id is not None:
            result['RouteId'] = self.route_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        spec: str = None,
    ):
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec field information about the workflow. For more information, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow/).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class CreateWorkflowDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        # The ID of the workflow.
        self.id = id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWorkflowDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWorkflowDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWorkflowDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDIAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        dialarm_rule_id: int = None,
        dijob_id: int = None,
    ):
        # The ID of the alert rule.
        self.dialarm_rule_id = dialarm_rule_id
        # The ID of the synchronization task.
        self.dijob_id = dijob_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        return self


class DeleteDIAlarmRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDIAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDIAlarmRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDIAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDIJobRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.dijob_id = dijob_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteDIJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDIJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDIJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataSourceSharedRuleRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteDataSourceSharedRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDataSourceSharedRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDataSourceSharedRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDataSourceSharedRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the UDF.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID. You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetworkRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteNetworkResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNetworkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNetworkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNodeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the node.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # true\\
        # false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the file resource.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID. You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceGroupRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRouteRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteRouteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the workflow.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteWorkflowDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteWorkflowDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkflowDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWorkflowDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateProjectFromResourceGroupRequest(TeaModel):
    def __init__(
        self,
        project_id: int = None,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class DissociateProjectFromResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DissociateProjectFromResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DissociateProjectFromResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateProjectFromResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecDeploymentStageRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        project_id: str = None,
    ):
        # The code of the stage in the process. You can call the GetDeployment operation to query the code.
        # 
        # This parameter is required.
        self.code = code
        # The ID of the process.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ExecDeploymentStageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # 
        # *   false
        # 
        #     **\
        # 
        #     **Note:** The value of this parameter indicates only whether the stage is triggered but does not indicate whether the execution of the stage is successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecDeploymentStageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecDeploymentStageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecDeploymentStageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDIJobRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        project_id: int = None,
        with_details: bool = None,
    ):
        self.dijob_id = dijob_id
        self.project_id = project_id
        self.with_details = with_details

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.with_details is not None:
            result['WithDetails'] = self.with_details
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('WithDetails') is not None:
            self.with_details = m.get('WithDetails')
        return self


class GetDIJobResponseBodyPagingInfoDestinationDataSourceSettings(TeaModel):
    def __init__(
        self,
        data_source_name: str = None,
    ):
        self.data_source_name = data_source_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        return self


class GetDIJobResponseBodyPagingInfoJobSettingsColumnDataTypeSettings(TeaModel):
    def __init__(
        self,
        destination_data_type: str = None,
        source_data_type: str = None,
    ):
        self.destination_data_type = destination_data_type
        self.source_data_type = source_data_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_data_type is not None:
            result['DestinationDataType'] = self.destination_data_type
        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDataType') is not None:
            self.destination_data_type = m.get('DestinationDataType')
        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')
        return self


class GetDIJobResponseBodyPagingInfoJobSettingsCycleScheduleSettings(TeaModel):
    def __init__(
        self,
        cycle_migration_type: str = None,
        schedule_parameters: str = None,
    ):
        self.cycle_migration_type = cycle_migration_type
        self.schedule_parameters = schedule_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cycle_migration_type is not None:
            result['CycleMigrationType'] = self.cycle_migration_type
        if self.schedule_parameters is not None:
            result['ScheduleParameters'] = self.schedule_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleMigrationType') is not None:
            self.cycle_migration_type = m.get('CycleMigrationType')
        if m.get('ScheduleParameters') is not None:
            self.schedule_parameters = m.get('ScheduleParameters')
        return self


class GetDIJobResponseBodyPagingInfoJobSettingsDdlHandlingSettings(TeaModel):
    def __init__(
        self,
        action: str = None,
        type: str = None,
    ):
        self.action = action
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDIJobResponseBodyPagingInfoJobSettingsRuntimeSettings(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetDIJobResponseBodyPagingInfoJobSettings(TeaModel):
    def __init__(
        self,
        channel_settings: str = None,
        column_data_type_settings: List[GetDIJobResponseBodyPagingInfoJobSettingsColumnDataTypeSettings] = None,
        cycle_schedule_settings: GetDIJobResponseBodyPagingInfoJobSettingsCycleScheduleSettings = None,
        ddl_handling_settings: List[GetDIJobResponseBodyPagingInfoJobSettingsDdlHandlingSettings] = None,
        runtime_settings: List[GetDIJobResponseBodyPagingInfoJobSettingsRuntimeSettings] = None,
    ):
        self.channel_settings = channel_settings
        self.column_data_type_settings = column_data_type_settings
        self.cycle_schedule_settings = cycle_schedule_settings
        self.ddl_handling_settings = ddl_handling_settings
        self.runtime_settings = runtime_settings

    def validate(self):
        if self.column_data_type_settings:
            for k in self.column_data_type_settings:
                if k:
                    k.validate()
        if self.cycle_schedule_settings:
            self.cycle_schedule_settings.validate()
        if self.ddl_handling_settings:
            for k in self.ddl_handling_settings:
                if k:
                    k.validate()
        if self.runtime_settings:
            for k in self.runtime_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_settings is not None:
            result['ChannelSettings'] = self.channel_settings
        result['ColumnDataTypeSettings'] = []
        if self.column_data_type_settings is not None:
            for k in self.column_data_type_settings:
                result['ColumnDataTypeSettings'].append(k.to_map() if k else None)
        if self.cycle_schedule_settings is not None:
            result['CycleScheduleSettings'] = self.cycle_schedule_settings.to_map()
        result['DdlHandlingSettings'] = []
        if self.ddl_handling_settings is not None:
            for k in self.ddl_handling_settings:
                result['DdlHandlingSettings'].append(k.to_map() if k else None)
        result['RuntimeSettings'] = []
        if self.runtime_settings is not None:
            for k in self.runtime_settings:
                result['RuntimeSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelSettings') is not None:
            self.channel_settings = m.get('ChannelSettings')
        self.column_data_type_settings = []
        if m.get('ColumnDataTypeSettings') is not None:
            for k in m.get('ColumnDataTypeSettings'):
                temp_model = GetDIJobResponseBodyPagingInfoJobSettingsColumnDataTypeSettings()
                self.column_data_type_settings.append(temp_model.from_map(k))
        if m.get('CycleScheduleSettings') is not None:
            temp_model = GetDIJobResponseBodyPagingInfoJobSettingsCycleScheduleSettings()
            self.cycle_schedule_settings = temp_model.from_map(m['CycleScheduleSettings'])
        self.ddl_handling_settings = []
        if m.get('DdlHandlingSettings') is not None:
            for k in m.get('DdlHandlingSettings'):
                temp_model = GetDIJobResponseBodyPagingInfoJobSettingsDdlHandlingSettings()
                self.ddl_handling_settings.append(temp_model.from_map(k))
        self.runtime_settings = []
        if m.get('RuntimeSettings') is not None:
            for k in m.get('RuntimeSettings'):
                temp_model = GetDIJobResponseBodyPagingInfoJobSettingsRuntimeSettings()
                self.runtime_settings.append(temp_model.from_map(k))
        return self


class GetDIJobResponseBodyPagingInfoResourceSettingsOfflineResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class GetDIJobResponseBodyPagingInfoResourceSettingsRealtimeResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class GetDIJobResponseBodyPagingInfoResourceSettingsScheduleResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: float = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class GetDIJobResponseBodyPagingInfoResourceSettings(TeaModel):
    def __init__(
        self,
        offline_resource_settings: GetDIJobResponseBodyPagingInfoResourceSettingsOfflineResourceSettings = None,
        realtime_resource_settings: GetDIJobResponseBodyPagingInfoResourceSettingsRealtimeResourceSettings = None,
        schedule_resource_settings: GetDIJobResponseBodyPagingInfoResourceSettingsScheduleResourceSettings = None,
    ):
        self.offline_resource_settings = offline_resource_settings
        self.realtime_resource_settings = realtime_resource_settings
        self.schedule_resource_settings = schedule_resource_settings

    def validate(self):
        if self.offline_resource_settings:
            self.offline_resource_settings.validate()
        if self.realtime_resource_settings:
            self.realtime_resource_settings.validate()
        if self.schedule_resource_settings:
            self.schedule_resource_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offline_resource_settings is not None:
            result['OfflineResourceSettings'] = self.offline_resource_settings.to_map()
        if self.realtime_resource_settings is not None:
            result['RealtimeResourceSettings'] = self.realtime_resource_settings.to_map()
        if self.schedule_resource_settings is not None:
            result['ScheduleResourceSettings'] = self.schedule_resource_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfflineResourceSettings') is not None:
            temp_model = GetDIJobResponseBodyPagingInfoResourceSettingsOfflineResourceSettings()
            self.offline_resource_settings = temp_model.from_map(m['OfflineResourceSettings'])
        if m.get('RealtimeResourceSettings') is not None:
            temp_model = GetDIJobResponseBodyPagingInfoResourceSettingsRealtimeResourceSettings()
            self.realtime_resource_settings = temp_model.from_map(m['RealtimeResourceSettings'])
        if m.get('ScheduleResourceSettings') is not None:
            temp_model = GetDIJobResponseBodyPagingInfoResourceSettingsScheduleResourceSettings()
            self.schedule_resource_settings = temp_model.from_map(m['ScheduleResourceSettings'])
        return self


class GetDIJobResponseBodyPagingInfoSourceDataSourceSettingsDataSourceProperties(TeaModel):
    def __init__(
        self,
        encoding: str = None,
        timezone: str = None,
    ):
        self.encoding = encoding
        self.timezone = timezone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encoding is not None:
            result['Encoding'] = self.encoding
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        return self


class GetDIJobResponseBodyPagingInfoSourceDataSourceSettings(TeaModel):
    def __init__(
        self,
        data_source_name: str = None,
        data_source_properties: GetDIJobResponseBodyPagingInfoSourceDataSourceSettingsDataSourceProperties = None,
    ):
        self.data_source_name = data_source_name
        self.data_source_properties = data_source_properties

    def validate(self):
        if self.data_source_properties:
            self.data_source_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name
        if self.data_source_properties is not None:
            result['DataSourceProperties'] = self.data_source_properties.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')
        if m.get('DataSourceProperties') is not None:
            temp_model = GetDIJobResponseBodyPagingInfoSourceDataSourceSettingsDataSourceProperties()
            self.data_source_properties = temp_model.from_map(m['DataSourceProperties'])
        return self


class GetDIJobResponseBodyPagingInfoTableMappingsSourceObjectSelectionRules(TeaModel):
    def __init__(
        self,
        action: str = None,
        expression: str = None,
        expression_type: str = None,
        object_type: str = None,
    ):
        self.action = action
        self.expression = expression
        self.expression_type = expression_type
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        return self


class GetDIJobResponseBodyPagingInfoTableMappingsTransformationRules(TeaModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        self.rule_action_type = rule_action_type
        self.rule_name = rule_name
        self.rule_target_type = rule_target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_target_type is not None:
            result['RuleTargetType'] = self.rule_target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleTargetType') is not None:
            self.rule_target_type = m.get('RuleTargetType')
        return self


class GetDIJobResponseBodyPagingInfoTableMappings(TeaModel):
    def __init__(
        self,
        source_object_selection_rules: List[GetDIJobResponseBodyPagingInfoTableMappingsSourceObjectSelectionRules] = None,
        transformation_rules: List[GetDIJobResponseBodyPagingInfoTableMappingsTransformationRules] = None,
    ):
        self.source_object_selection_rules = source_object_selection_rules
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.source_object_selection_rules:
            for k in self.source_object_selection_rules:
                if k:
                    k.validate()
        if self.transformation_rules:
            for k in self.transformation_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceObjectSelectionRules'] = []
        if self.source_object_selection_rules is not None:
            for k in self.source_object_selection_rules:
                result['SourceObjectSelectionRules'].append(k.to_map() if k else None)
        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k in self.transformation_rules:
                result['TransformationRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_object_selection_rules = []
        if m.get('SourceObjectSelectionRules') is not None:
            for k in m.get('SourceObjectSelectionRules'):
                temp_model = GetDIJobResponseBodyPagingInfoTableMappingsSourceObjectSelectionRules()
                self.source_object_selection_rules.append(temp_model.from_map(k))
        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k in m.get('TransformationRules'):
                temp_model = GetDIJobResponseBodyPagingInfoTableMappingsTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k))
        return self


class GetDIJobResponseBodyPagingInfoTransformationRules(TeaModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_expression: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        self.rule_action_type = rule_action_type
        self.rule_expression = rule_expression
        self.rule_name = rule_name
        self.rule_target_type = rule_target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_target_type is not None:
            result['RuleTargetType'] = self.rule_target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleTargetType') is not None:
            self.rule_target_type = m.get('RuleTargetType')
        return self


class GetDIJobResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        dijob_id: str = None,
        description: str = None,
        destination_data_source_settings: List[GetDIJobResponseBodyPagingInfoDestinationDataSourceSettings] = None,
        destination_data_source_type: str = None,
        job_name: str = None,
        job_settings: GetDIJobResponseBodyPagingInfoJobSettings = None,
        job_status: str = None,
        migration_type: str = None,
        project_id: int = None,
        resource_settings: GetDIJobResponseBodyPagingInfoResourceSettings = None,
        source_data_source_settings: List[GetDIJobResponseBodyPagingInfoSourceDataSourceSettings] = None,
        source_data_source_type: str = None,
        table_mappings: List[GetDIJobResponseBodyPagingInfoTableMappings] = None,
        transformation_rules: List[GetDIJobResponseBodyPagingInfoTransformationRules] = None,
    ):
        self.dijob_id = dijob_id
        self.description = description
        self.destination_data_source_settings = destination_data_source_settings
        self.destination_data_source_type = destination_data_source_type
        self.job_name = job_name
        self.job_settings = job_settings
        self.job_status = job_status
        self.migration_type = migration_type
        self.project_id = project_id
        self.resource_settings = resource_settings
        self.source_data_source_settings = source_data_source_settings
        self.source_data_source_type = source_data_source_type
        self.table_mappings = table_mappings
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.destination_data_source_settings:
            for k in self.destination_data_source_settings:
                if k:
                    k.validate()
        if self.job_settings:
            self.job_settings.validate()
        if self.resource_settings:
            self.resource_settings.validate()
        if self.source_data_source_settings:
            for k in self.source_data_source_settings:
                if k:
                    k.validate()
        if self.table_mappings:
            for k in self.table_mappings:
                if k:
                    k.validate()
        if self.transformation_rules:
            for k in self.transformation_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.description is not None:
            result['Description'] = self.description
        result['DestinationDataSourceSettings'] = []
        if self.destination_data_source_settings is not None:
            for k in self.destination_data_source_settings:
                result['DestinationDataSourceSettings'].append(k.to_map() if k else None)
        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_settings is not None:
            result['JobSettings'] = self.job_settings.to_map()
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_settings is not None:
            result['ResourceSettings'] = self.resource_settings.to_map()
        result['SourceDataSourceSettings'] = []
        if self.source_data_source_settings is not None:
            for k in self.source_data_source_settings:
                result['SourceDataSourceSettings'].append(k.to_map() if k else None)
        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type
        result['TableMappings'] = []
        if self.table_mappings is not None:
            for k in self.table_mappings:
                result['TableMappings'].append(k.to_map() if k else None)
        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k in self.transformation_rules:
                result['TransformationRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.destination_data_source_settings = []
        if m.get('DestinationDataSourceSettings') is not None:
            for k in m.get('DestinationDataSourceSettings'):
                temp_model = GetDIJobResponseBodyPagingInfoDestinationDataSourceSettings()
                self.destination_data_source_settings.append(temp_model.from_map(k))
        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobSettings') is not None:
            temp_model = GetDIJobResponseBodyPagingInfoJobSettings()
            self.job_settings = temp_model.from_map(m['JobSettings'])
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceSettings') is not None:
            temp_model = GetDIJobResponseBodyPagingInfoResourceSettings()
            self.resource_settings = temp_model.from_map(m['ResourceSettings'])
        self.source_data_source_settings = []
        if m.get('SourceDataSourceSettings') is not None:
            for k in m.get('SourceDataSourceSettings'):
                temp_model = GetDIJobResponseBodyPagingInfoSourceDataSourceSettings()
                self.source_data_source_settings.append(temp_model.from_map(k))
        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')
        self.table_mappings = []
        if m.get('TableMappings') is not None:
            for k in m.get('TableMappings'):
                temp_model = GetDIJobResponseBodyPagingInfoTableMappings()
                self.table_mappings.append(temp_model.from_map(k))
        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k in m.get('TransformationRules'):
                temp_model = GetDIJobResponseBodyPagingInfoTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k))
        return self


class GetDIJobResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: GetDIJobResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        # 代表创建时间的资源属性字段
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = GetDIJobResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDIJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDIJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDIJobLogRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        failover_id: int = None,
        instance_id: int = None,
    ):
        # The ID of the synchronization task.
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # The failover ID.
        self.failover_id = failover_id
        # The instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.failover_id is not None:
            result['FailoverId'] = self.failover_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('FailoverId') is not None:
            self.failover_id = m.get('FailoverId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDIJobLogResponseBody(TeaModel):
    def __init__(
        self,
        log: str = None,
        request_id: str = None,
    ):
        # The log.
        self.log = log
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log is not None:
            result['Log'] = self.log
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Log') is not None:
            self.log = m.get('Log')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDIJobLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDIJobLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDIJobLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetDataSourceResponseBodyDataSource(TeaModel):
    def __init__(
        self,
        connection_properties: Any = None,
        connection_properties_mode: str = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        name: str = None,
        project_id: int = None,
        qualified_name: str = None,
        type: str = None,
    ):
        self.connection_properties = connection_properties
        self.connection_properties_mode = connection_properties_mode
        self.create_time = create_time
        self.create_user = create_user
        self.description = description
        self.id = id
        self.modify_time = modify_time
        self.modify_user = modify_user
        self.name = name
        self.project_id = project_id
        self.qualified_name = qualified_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties
        if self.connection_properties_mode is not None:
            result['ConnectionPropertiesMode'] = self.connection_properties_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')
        if m.get('ConnectionPropertiesMode') is not None:
            self.connection_properties_mode = m.get('ConnectionPropertiesMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        data_source: GetDataSourceResponseBodyDataSource = None,
        request_id: str = None,
    ):
        self.data_source = data_source
        self.request_id = request_id

    def validate(self):
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSource') is not None:
            temp_model = GetDataSourceResponseBodyDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeploymentRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the process.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetDeploymentResponseBodyPipelineStages(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        detail: Dict[str, Any] = None,
        message: str = None,
        name: str = None,
        status: str = None,
        step: int = None,
        type: str = None,
    ):
        # The code of the stage.
        self.code = code
        # The description of the stage.
        self.description = description
        # The details of the stage.
        self.detail = detail
        # The error message returned for the stage.
        self.message = message
        # The name of the stage.
        self.name = name
        # The status of the stage.
        # 
        # Valid values:
        # 
        # *   INIT
        # *   RUNNING
        # *   SUCCESS
        # *   FAIL
        # *   TERMINATION
        # *   CANCEL
        self.status = status
        # The step number of the stage.
        self.step = step
        # The type of the stage.
        # 
        # Valid values:
        # 
        # *   DELETE
        # *   BUILD
        # *   CHECK
        # *   DEPLOY
        # *   OFFLINE
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.step is not None:
            result['Step'] = self.step
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDeploymentResponseBodyPipeline(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        creator: str = None,
        id: str = None,
        message: str = None,
        modify_time: int = None,
        project_id: str = None,
        stages: List[GetDeploymentResponseBodyPipelineStages] = None,
        status: str = None,
    ):
        # The time when the process was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The creator of the process.
        self.creator = creator
        # The ID of the process.
        self.id = id
        # The error message returned when the process fails.
        self.message = message
        # The time when the process was modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The information about stages in the process.
        self.stages = stages
        # The status of the process.
        # 
        # Valid values:
        # 
        # *   INIT
        # *   RUNNING
        # *   SUCCESS
        # *   FAIL
        # *   TERMINATION
        # *   CANCEL
        self.status = status

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = GetDeploymentResponseBodyPipelineStages()
                self.stages.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        pipeline: GetDeploymentResponseBodyPipeline = None,
        request_id: str = None,
    ):
        # The information about the process.
        self.pipeline = pipeline
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.pipeline:
            self.pipeline.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline is not None:
            result['Pipeline'] = self.pipeline.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pipeline') is not None:
            temp_model = GetDeploymentResponseBodyPipeline()
            self.pipeline = temp_model.from_map(m['Pipeline'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFunctionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the UDF.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetFunctionResponseBodyFunction(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # The time when the UDF was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the UDF.
        self.id = id
        # The time when the UDF was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the UDF.
        self.name = name
        # The owner of the UDF.
        self.owner = owner
        # The ID of the DataWorks workspace to which the UDF belongs.
        self.project_id = project_id
        # The FlowSpec field information about the UDF. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class GetFunctionResponseBody(TeaModel):
    def __init__(
        self,
        function: GetFunctionResponseBodyFunction = None,
        request_id: str = None,
    ):
        # The information about the UDF.
        self.function = function
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.function:
            self.function.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function is not None:
            result['Function'] = self.function.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            temp_model = GetFunctionResponseBodyFunction()
            self.function = temp_model.from_map(m['Function'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobStatusRequest(TeaModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetJobStatusResponseBodyJobStatus(TeaModel):
    def __init__(
        self,
        completed: str = None,
        create_time: str = None,
        error: str = None,
        job_id: str = None,
        job_type: str = None,
        status: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.job_id = job_id
        self.job_type = job_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetJobStatusResponseBody(TeaModel):
    def __init__(
        self,
        job_status: GetJobStatusResponseBodyJobStatus = None,
        request_id: str = None,
    ):
        self.job_status = job_status
        self.request_id = request_id

    def validate(self):
        if self.job_status:
            self.job_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_status is not None:
            result['JobStatus'] = self.job_status.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobStatus') is not None:
            temp_model = GetJobStatusResponseBodyJobStatus()
            self.job_status = temp_model.from_map(m['JobStatus'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetJobStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetworkRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetNetworkResponseBodyNetwork(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        id: int = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        status: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.status = status
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class GetNetworkResponseBody(TeaModel):
    def __init__(
        self,
        network: GetNetworkResponseBodyNetwork = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.network = network
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Network') is not None:
            temp_model = GetNetworkResponseBodyNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNetworkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNetworkResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNetworkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNodeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the node.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the workspace ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetNodeResponseBodyNode(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # The time when the node was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the node.
        self.id = id
        # The time when the node was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the node.
        self.name = name
        # The owner of the node.
        self.owner = owner
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The FlowSpec field information about this node. For more information, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class GetNodeResponseBody(TeaModel):
    def __init__(
        self,
        node: GetNodeResponseBodyNode = None,
        request_id: str = None,
    ):
        # The information about the node.
        self.node = node
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node is not None:
            result['Node'] = self.node.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Node') is not None:
            temp_model = GetNodeResponseBodyNode()
            self.node = temp_model.from_map(m['Node'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetProjectResponseBodyProjectAliyunResourceTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetProjectResponseBodyProject(TeaModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[GetProjectResponseBodyProjectAliyunResourceTags] = None,
        description: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        display_name: str = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        pai_task_enabled: bool = None,
        status: str = None,
    ):
        self.aliyun_resource_group_id = aliyun_resource_group_id
        self.aliyun_resource_tags = aliyun_resource_tags
        self.description = description
        self.dev_environment_enabled = dev_environment_enabled
        self.dev_role_disabled = dev_role_disabled
        self.display_name = display_name
        self.id = id
        self.name = name
        self.owner = owner
        self.pai_task_enabled = pai_task_enabled
        self.status = status

    def validate(self):
        if self.aliyun_resource_tags:
            for k in self.aliyun_resource_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id
        result['AliyunResourceTags'] = []
        if self.aliyun_resource_tags is not None:
            for k in self.aliyun_resource_tags:
                result['AliyunResourceTags'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled
        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')
        self.aliyun_resource_tags = []
        if m.get('AliyunResourceTags') is not None:
            for k in m.get('AliyunResourceTags'):
                temp_model = GetProjectResponseBodyProjectAliyunResourceTags()
                self.aliyun_resource_tags.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')
        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: GetProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        self.project = project
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['Project'] = self.project.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = GetProjectResponseBodyProject()
            self.project = temp_model.from_map(m['Project'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRoleRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetProjectRoleResponseBodyProjectRole(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        self.code = code
        self.name = name
        self.project_id = project_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetProjectRoleResponseBody(TeaModel):
    def __init__(
        self,
        project_role: GetProjectRoleResponseBodyProjectRole = None,
        request_id: str = None,
    ):
        self.project_role = project_role
        self.request_id = request_id

    def validate(self):
        if self.project_role:
            self.project_role.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_role is not None:
            result['ProjectRole'] = self.project_role.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectRole') is not None:
            temp_model = GetProjectRoleResponseBodyProjectRole()
            self.project_role = temp_model.from_map(m['ProjectRole'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProjectRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the file resource.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetResourceResponseBodyResource(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # The time when the file resource was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the file resource.
        self.id = id
        # The time when the file resource was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the file resource.
        self.name = name
        # The owner of the file resource.
        self.owner = owner
        # The ID of the workspace to which the file resource belongs.
        self.project_id = project_id
        # The FlowSpec field information about the file resource. For more information, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class GetResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource: GetResourceResponseBodyResource = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the file resource.
        self.resource = resource

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Resource') is not None:
            temp_model = GetResourceResponseBodyResource()
            self.resource = temp_model.from_map(m['Resource'])
        return self


class GetResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceGroupRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetResourceGroupResponseBodyResourceGroupSpec(TeaModel):
    def __init__(
        self,
        amount: int = None,
        standard: str = None,
    ):
        self.amount = amount
        self.standard = standard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.standard is not None:
            result['Standard'] = self.standard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Standard') is not None:
            self.standard = m.get('Standard')
        return self


class GetResourceGroupResponseBodyResourceGroup(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        default_vpc_id: str = None,
        default_vswitch_id: str = None,
        id: str = None,
        name: str = None,
        order_instance_id: str = None,
        payment_type: str = None,
        remark: str = None,
        resource_group_type: str = None,
        spec: GetResourceGroupResponseBodyResourceGroupSpec = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.default_vpc_id = default_vpc_id
        self.default_vswitch_id = default_vswitch_id
        self.id = id
        self.name = name
        self.order_instance_id = order_instance_id
        self.payment_type = payment_type
        self.remark = remark
        self.resource_group_type = resource_group_type
        self.spec = spec
        self.status = status

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.default_vpc_id is not None:
            result['DefaultVpcId'] = self.default_vpc_id
        if self.default_vswitch_id is not None:
            result['DefaultVswitchId'] = self.default_vswitch_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_type is not None:
            result['ResourceGroupType'] = self.resource_group_type
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DefaultVpcId') is not None:
            self.default_vpc_id = m.get('DefaultVpcId')
        if m.get('DefaultVswitchId') is not None:
            self.default_vswitch_id = m.get('DefaultVswitchId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupType') is not None:
            self.resource_group_type = m.get('ResourceGroupType')
        if m.get('Spec') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroupSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group: GetResourceGroupResponseBodyResourceGroup = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.resource_group = resource_group
        self.success = success

    def validate(self):
        if self.resource_group:
            self.resource_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroup') is not None:
            temp_model = GetResourceGroupResponseBodyResourceGroup()
            self.resource_group = temp_model.from_map(m['ResourceGroup'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRouteRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetRouteResponseBodyRoute(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        destination_cidr: str = None,
        id: int = None,
        network_id: int = None,
        resource_group_id: str = None,
        resource_id: str = None,
    ):
        self.create_time = create_time
        self.destination_cidr = destination_cidr
        self.id = id
        self.network_id = network_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.id is not None:
            result['Id'] = self.id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class GetRouteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        route: GetRouteResponseBodyRoute = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.route = route
        self.success = success

    def validate(self):
        if self.route:
            self.route.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.route is not None:
            result['Route'] = self.route.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Route') is not None:
            temp_model = GetRouteResponseBodyRoute()
            self.route = temp_model.from_map(m['Route'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # The ID of the workflow.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetWorkflowDefinitionResponseBodyWorkflowDefinition(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # The time when the workflow was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the workflow.
        self.id = id
        # The time when the workflow was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the workflow.
        self.name = name
        # The owner of the workflow.
        self.owner = owner
        # The ID of the workspace to which the workflow belongs.
        self.project_id = project_id
        # The FlowSpec field information about the workflow. For more information, see [FlowSpec](https://github.com/aliyun/alibabacloud-dataworks-tool-dflow/).
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class GetWorkflowDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        workflow_definition: GetWorkflowDefinitionResponseBodyWorkflowDefinition = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the workflow.
        self.workflow_definition = workflow_definition

    def validate(self):
        if self.workflow_definition:
            self.workflow_definition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.workflow_definition is not None:
            result['WorkflowDefinition'] = self.workflow_definition.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WorkflowDefinition') is not None:
            temp_model = GetWorkflowDefinitionResponseBodyWorkflowDefinition()
            self.workflow_definition = temp_model.from_map(m['WorkflowDefinition'])
        return self


class GetWorkflowDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWorkflowDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetWorkflowDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        spec: str = None,
    ):
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class ImportWorkflowDefinitionResponseBodyAsyncJob(TeaModel):
    def __init__(
        self,
        completed: bool = None,
        create_time: int = None,
        error: str = None,
        id: str = None,
        progress: int = None,
        response: str = None,
        status: str = None,
        type: str = None,
    ):
        self.completed = completed
        self.create_time = create_time
        self.error = error
        self.id = id
        self.progress = progress
        self.response = response
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.completed is not None:
            result['Completed'] = self.completed
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.error is not None:
            result['Error'] = self.error
        if self.id is not None:
            result['Id'] = self.id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.response is not None:
            result['Response'] = self.response
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Completed') is not None:
            self.completed = m.get('Completed')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Error') is not None:
            self.error = m.get('Error')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Response') is not None:
            self.response = m.get('Response')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ImportWorkflowDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        async_job: ImportWorkflowDefinitionResponseBodyAsyncJob = None,
        request_id: str = None,
    ):
        self.async_job = async_job
        self.request_id = request_id

    def validate(self):
        if self.async_job:
            self.async_job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_job is not None:
            result['AsyncJob'] = self.async_job.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncJob') is not None:
            temp_model = ImportWorkflowDefinitionResponseBodyAsyncJob()
            self.async_job = temp_model.from_map(m['AsyncJob'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportWorkflowDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportWorkflowDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ImportWorkflowDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDIAlarmRulesRequest(TeaModel):
    def __init__(
        self,
        dialarm_rule_id: int = None,
        job_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.dialarm_rule_id = dialarm_rule_id
        self.job_id = job_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettingsNotificationChannels(TeaModel):
    def __init__(
        self,
        channels: List[str] = None,
        severity: str = None,
    ):
        self.channels = channels
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettingsNotificationReceivers(TeaModel):
    def __init__(
        self,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        self.receiver_type = receiver_type
        self.receiver_values = receiver_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type
        if self.receiver_values is not None:
            result['ReceiverValues'] = self.receiver_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')
        if m.get('ReceiverValues') is not None:
            self.receiver_values = m.get('ReceiverValues')
        return self


class ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettings(TeaModel):
    def __init__(
        self,
        inhibition_interval: int = None,
        notification_channels: List[ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettingsNotificationChannels] = None,
        notification_receivers: List[ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettingsNotificationReceivers] = None,
    ):
        self.inhibition_interval = inhibition_interval
        self.notification_channels = notification_channels
        self.notification_receivers = notification_receivers

    def validate(self):
        if self.notification_channels:
            for k in self.notification_channels:
                if k:
                    k.validate()
        if self.notification_receivers:
            for k in self.notification_receivers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inhibition_interval is not None:
            result['InhibitionInterval'] = self.inhibition_interval
        result['NotificationChannels'] = []
        if self.notification_channels is not None:
            for k in self.notification_channels:
                result['NotificationChannels'].append(k.to_map() if k else None)
        result['NotificationReceivers'] = []
        if self.notification_receivers is not None:
            for k in self.notification_receivers:
                result['NotificationReceivers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InhibitionInterval') is not None:
            self.inhibition_interval = m.get('InhibitionInterval')
        self.notification_channels = []
        if m.get('NotificationChannels') is not None:
            for k in m.get('NotificationChannels'):
                temp_model = ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettingsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k))
        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k in m.get('NotificationReceivers'):
                temp_model = ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettingsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k))
        return self


class ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesTriggerConditions(TeaModel):
    def __init__(
        self,
        ddl_report_tags: List[str] = None,
        duration: int = None,
        severity: str = None,
        threshold: int = None,
    ):
        self.ddl_report_tags = ddl_report_tags
        self.duration = duration
        self.severity = severity
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl_report_tags is not None:
            result['DdlReportTags'] = self.ddl_report_tags
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdlReportTags') is not None:
            self.ddl_report_tags = m.get('DdlReportTags')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRules(TeaModel):
    def __init__(
        self,
        dialarm_rule_id: int = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        name: str = None,
        notification_settings: ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettings = None,
        trigger_conditions: List[ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesTriggerConditions] = None,
    ):
        self.dialarm_rule_id = dialarm_rule_id
        self.dijob_id = dijob_id
        self.description = description
        self.enabled = enabled
        self.metric_type = metric_type
        self.name = name
        self.notification_settings = notification_settings
        self.trigger_conditions = trigger_conditions

    def validate(self):
        if self.notification_settings:
            self.notification_settings.validate()
        if self.trigger_conditions:
            for k in self.trigger_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.notification_settings is not None:
            result['NotificationSettings'] = self.notification_settings.to_map()
        result['TriggerConditions'] = []
        if self.trigger_conditions is not None:
            for k in self.trigger_conditions:
                result['TriggerConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotificationSettings') is not None:
            temp_model = ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesNotificationSettings()
            self.notification_settings = temp_model.from_map(m['NotificationSettings'])
        self.trigger_conditions = []
        if m.get('TriggerConditions') is not None:
            for k in m.get('TriggerConditions'):
                temp_model = ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRulesTriggerConditions()
                self.trigger_conditions.append(temp_model.from_map(k))
        return self


class ListDIAlarmRulesResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        dijob_alarm_rules: List[ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRules] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.dijob_alarm_rules = dijob_alarm_rules
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.dijob_alarm_rules:
            for k in self.dijob_alarm_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DIJobAlarmRules'] = []
        if self.dijob_alarm_rules is not None:
            for k in self.dijob_alarm_rules:
                result['DIJobAlarmRules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dijob_alarm_rules = []
        if m.get('DIJobAlarmRules') is not None:
            for k in m.get('DIJobAlarmRules'):
                temp_model = ListDIAlarmRulesResponseBodyPagingInfoDIJobAlarmRules()
                self.dijob_alarm_rules.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDIAlarmRulesResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListDIAlarmRulesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListDIAlarmRulesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDIAlarmRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDIAlarmRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDIAlarmRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDIJobEventsRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        end_time: int = None,
        event_type: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        self.dijob_id = dijob_id
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.event_type = event_type
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDIJobEventsResponseBodyPagingInfoDIJobEvent(TeaModel):
    def __init__(
        self,
        action: str = None,
        channels: str = None,
        create_time: str = None,
        detail: str = None,
        dst_sql: str = None,
        dst_table: str = None,
        failover_message: str = None,
        id: str = None,
        severity: str = None,
        src_sql: str = None,
        src_table: str = None,
        status: str = None,
        type: str = None,
    ):
        self.action = action
        self.channels = channels
        self.create_time = create_time
        self.detail = detail
        self.dst_sql = dst_sql
        self.dst_table = dst_table
        self.failover_message = failover_message
        self.id = id
        self.severity = severity
        self.src_sql = src_sql
        self.src_table = src_table
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.dst_sql is not None:
            result['DstSql'] = self.dst_sql
        if self.dst_table is not None:
            result['DstTable'] = self.dst_table
        if self.failover_message is not None:
            result['FailoverMessage'] = self.failover_message
        if self.id is not None:
            result['Id'] = self.id
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.src_sql is not None:
            result['SrcSql'] = self.src_sql
        if self.src_table is not None:
            result['SrcTable'] = self.src_table
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('DstSql') is not None:
            self.dst_sql = m.get('DstSql')
        if m.get('DstTable') is not None:
            self.dst_table = m.get('DstTable')
        if m.get('FailoverMessage') is not None:
            self.failover_message = m.get('FailoverMessage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('SrcSql') is not None:
            self.src_sql = m.get('SrcSql')
        if m.get('SrcTable') is not None:
            self.src_table = m.get('SrcTable')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDIJobEventsResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        dijob_event: List[ListDIJobEventsResponseBodyPagingInfoDIJobEvent] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.dijob_event = dijob_event
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.dijob_event:
            for k in self.dijob_event:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DIJobEvent'] = []
        if self.dijob_event is not None:
            for k in self.dijob_event:
                result['DIJobEvent'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dijob_event = []
        if m.get('DIJobEvent') is not None:
            for k in m.get('DIJobEvent'):
                temp_model = ListDIJobEventsResponseBodyPagingInfoDIJobEvent()
                self.dijob_event.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDIJobEventsResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListDIJobEventsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListDIJobEventsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDIJobEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDIJobEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDIJobEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDIJobMetricsRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        end_time: int = None,
        metric_name: List[str] = None,
        start_time: int = None,
    ):
        self.dijob_id = dijob_id
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.metric_name = metric_name
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDIJobMetricsShrinkRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        end_time: int = None,
        metric_name_shrink: str = None,
        start_time: int = None,
    ):
        self.dijob_id = dijob_id
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.metric_name_shrink = metric_name_shrink
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_name_shrink is not None:
            result['MetricName'] = self.metric_name_shrink
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricName') is not None:
            self.metric_name_shrink = m.get('MetricName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDIJobMetricsResponseBodyPagingInfoJobMetricsSeriesList(TeaModel):
    def __init__(
        self,
        time: int = None,
        value: float = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListDIJobMetricsResponseBodyPagingInfoJobMetrics(TeaModel):
    def __init__(
        self,
        name: str = None,
        series_list: List[ListDIJobMetricsResponseBodyPagingInfoJobMetricsSeriesList] = None,
    ):
        self.name = name
        self.series_list = series_list

    def validate(self):
        if self.series_list:
            for k in self.series_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        result['SeriesList'] = []
        if self.series_list is not None:
            for k in self.series_list:
                result['SeriesList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.series_list = []
        if m.get('SeriesList') is not None:
            for k in m.get('SeriesList'):
                temp_model = ListDIJobMetricsResponseBodyPagingInfoJobMetricsSeriesList()
                self.series_list.append(temp_model.from_map(k))
        return self


class ListDIJobMetricsResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        job_metrics: List[ListDIJobMetricsResponseBodyPagingInfoJobMetrics] = None,
    ):
        self.job_metrics = job_metrics

    def validate(self):
        if self.job_metrics:
            for k in self.job_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobMetrics'] = []
        if self.job_metrics is not None:
            for k in self.job_metrics:
                result['JobMetrics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_metrics = []
        if m.get('JobMetrics') is not None:
            for k in m.get('JobMetrics'):
                temp_model = ListDIJobMetricsResponseBodyPagingInfoJobMetrics()
                self.job_metrics.append(temp_model.from_map(k))
        return self


class ListDIJobMetricsResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListDIJobMetricsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListDIJobMetricsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDIJobMetricsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDIJobMetricsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDIJobMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDIJobRunDetailsRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        instance_id: int = None,
        page_number: int = None,
        page_size: int = None,
        source_data_source_name: str = None,
        source_database_name: str = None,
        source_schema_name: str = None,
        source_table_name: str = None,
    ):
        # This parameter is required.
        self.dijob_id = dijob_id
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.source_data_source_name = source_data_source_name
        self.source_database_name = source_database_name
        self.source_schema_name = source_schema_name
        self.source_table_name = source_table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_data_source_name is not None:
            result['SourceDataSourceName'] = self.source_data_source_name
        if self.source_database_name is not None:
            result['SourceDatabaseName'] = self.source_database_name
        if self.source_schema_name is not None:
            result['SourceSchemaName'] = self.source_schema_name
        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceDataSourceName') is not None:
            self.source_data_source_name = m.get('SourceDataSourceName')
        if m.get('SourceDatabaseName') is not None:
            self.source_database_name = m.get('SourceDatabaseName')
        if m.get('SourceSchemaName') is not None:
            self.source_schema_name = m.get('SourceSchemaName')
        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')
        return self


class ListDIJobRunDetailsResponseBodyPagingInfoJobRunInfos(TeaModel):
    def __init__(
        self,
        destination_database_name: str = None,
        destination_datasource_name: str = None,
        destination_schema_name: str = None,
        destination_table_name: str = None,
        full_migration_error_message: str = None,
        full_migration_status: str = None,
        offline_error_records: int = None,
        offline_total_bytes: int = None,
        offline_total_records: int = None,
        realtime_migration_error_message: str = None,
        realtime_migration_status: str = None,
        source_database_name: str = None,
        source_datasource_name: str = None,
        source_schema_name: str = None,
        source_table_name: str = None,
        structure_migration_error_message: str = None,
        structure_migration_status: str = None,
    ):
        self.destination_database_name = destination_database_name
        self.destination_datasource_name = destination_datasource_name
        self.destination_schema_name = destination_schema_name
        self.destination_table_name = destination_table_name
        self.full_migration_error_message = full_migration_error_message
        self.full_migration_status = full_migration_status
        self.offline_error_records = offline_error_records
        self.offline_total_bytes = offline_total_bytes
        self.offline_total_records = offline_total_records
        self.realtime_migration_error_message = realtime_migration_error_message
        self.realtime_migration_status = realtime_migration_status
        self.source_database_name = source_database_name
        self.source_datasource_name = source_datasource_name
        self.source_schema_name = source_schema_name
        self.source_table_name = source_table_name
        self.structure_migration_error_message = structure_migration_error_message
        self.structure_migration_status = structure_migration_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_database_name is not None:
            result['DestinationDatabaseName'] = self.destination_database_name
        if self.destination_datasource_name is not None:
            result['DestinationDatasourceName'] = self.destination_datasource_name
        if self.destination_schema_name is not None:
            result['DestinationSchemaName'] = self.destination_schema_name
        if self.destination_table_name is not None:
            result['DestinationTableName'] = self.destination_table_name
        if self.full_migration_error_message is not None:
            result['FullMigrationErrorMessage'] = self.full_migration_error_message
        if self.full_migration_status is not None:
            result['FullMigrationStatus'] = self.full_migration_status
        if self.offline_error_records is not None:
            result['OfflineErrorRecords'] = self.offline_error_records
        if self.offline_total_bytes is not None:
            result['OfflineTotalBytes'] = self.offline_total_bytes
        if self.offline_total_records is not None:
            result['OfflineTotalRecords'] = self.offline_total_records
        if self.realtime_migration_error_message is not None:
            result['RealtimeMigrationErrorMessage'] = self.realtime_migration_error_message
        if self.realtime_migration_status is not None:
            result['RealtimeMigrationStatus'] = self.realtime_migration_status
        if self.source_database_name is not None:
            result['SourceDatabaseName'] = self.source_database_name
        if self.source_datasource_name is not None:
            result['SourceDatasourceName'] = self.source_datasource_name
        if self.source_schema_name is not None:
            result['SourceSchemaName'] = self.source_schema_name
        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name
        if self.structure_migration_error_message is not None:
            result['StructureMigrationErrorMessage'] = self.structure_migration_error_message
        if self.structure_migration_status is not None:
            result['StructureMigrationStatus'] = self.structure_migration_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDatabaseName') is not None:
            self.destination_database_name = m.get('DestinationDatabaseName')
        if m.get('DestinationDatasourceName') is not None:
            self.destination_datasource_name = m.get('DestinationDatasourceName')
        if m.get('DestinationSchemaName') is not None:
            self.destination_schema_name = m.get('DestinationSchemaName')
        if m.get('DestinationTableName') is not None:
            self.destination_table_name = m.get('DestinationTableName')
        if m.get('FullMigrationErrorMessage') is not None:
            self.full_migration_error_message = m.get('FullMigrationErrorMessage')
        if m.get('FullMigrationStatus') is not None:
            self.full_migration_status = m.get('FullMigrationStatus')
        if m.get('OfflineErrorRecords') is not None:
            self.offline_error_records = m.get('OfflineErrorRecords')
        if m.get('OfflineTotalBytes') is not None:
            self.offline_total_bytes = m.get('OfflineTotalBytes')
        if m.get('OfflineTotalRecords') is not None:
            self.offline_total_records = m.get('OfflineTotalRecords')
        if m.get('RealtimeMigrationErrorMessage') is not None:
            self.realtime_migration_error_message = m.get('RealtimeMigrationErrorMessage')
        if m.get('RealtimeMigrationStatus') is not None:
            self.realtime_migration_status = m.get('RealtimeMigrationStatus')
        if m.get('SourceDatabaseName') is not None:
            self.source_database_name = m.get('SourceDatabaseName')
        if m.get('SourceDatasourceName') is not None:
            self.source_datasource_name = m.get('SourceDatasourceName')
        if m.get('SourceSchemaName') is not None:
            self.source_schema_name = m.get('SourceSchemaName')
        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')
        if m.get('StructureMigrationErrorMessage') is not None:
            self.structure_migration_error_message = m.get('StructureMigrationErrorMessage')
        if m.get('StructureMigrationStatus') is not None:
            self.structure_migration_status = m.get('StructureMigrationStatus')
        return self


class ListDIJobRunDetailsResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        job_run_infos: List[ListDIJobRunDetailsResponseBodyPagingInfoJobRunInfos] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        self.job_run_infos = job_run_infos
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.job_run_infos:
            for k in self.job_run_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobRunInfos'] = []
        if self.job_run_infos is not None:
            for k in self.job_run_infos:
                result['JobRunInfos'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_run_infos = []
        if m.get('JobRunInfos') is not None:
            for k in m.get('JobRunInfos'):
                temp_model = ListDIJobRunDetailsResponseBodyPagingInfoJobRunInfos()
                self.job_run_infos.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDIJobRunDetailsResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListDIJobRunDetailsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListDIJobRunDetailsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDIJobRunDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDIJobRunDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDIJobRunDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDIJobsRequest(TeaModel):
    def __init__(
        self,
        destination_data_source_type: str = None,
        migration_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        source_data_source_type: str = None,
    ):
        # The destination type. If you do not configure this parameter, no limits are imposed on the tasks.
        self.destination_data_source_type = destination_data_source_type
        # The synchronization type. Valid values:
        # 
        # *   FullAndRealtimeIncremental: one-time full synchronization and real-time incremental synchronization
        # *   RealtimeIncremental: real-time incremental synchronization
        # *   Full: full synchronization
        # *   OfflineIncremental: batch incremental synchronization
        # *   FullAndOfflineIncremental: one-time full synchronization and batch incremental synchronization
        self.migration_type = migration_type
        # The name of the export task.
        # 
        # The name of each export task must be unique. You must make sure that the names of the export tasks in the current workspace are unique.
        self.name = name
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The source type. If you do not configure this parameter, no limits are imposed on the tasks.
        self.source_data_source_type = source_data_source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type
        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type
        if self.name is not None:
            result['Name'] = self.name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')
        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')
        return self


class ListDIJobsResponseBodyPagingInfoDIJobs(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        destination_data_source_type: str = None,
        job_name: str = None,
        job_status: str = None,
        migration_type: str = None,
        project_id: int = None,
        source_data_source_type: str = None,
    ):
        # The ID of the synchronization task.
        self.dijob_id = dijob_id
        # The destination type. Valid values: Hologres and Hive.
        self.destination_data_source_type = destination_data_source_type
        # The name of the synchronization task.
        self.job_name = job_name
        # The status of the synchronization task. Valid values:
        # 
        # *   Finished
        # *   Initialized
        # *   Stopped
        # *   Failed
        # *   Running
        # *   Stopping
        self.job_status = job_status
        # The synchronization type. Valid values:
        # 
        # *   FullAndRealtimeIncremental: one-time full synchronization and real-time incremental synchronization
        # *   RealtimeIncremental: real-time incremental synchronization
        # *   Full: full synchronization
        # *   OfflineIncremental: batch incremental synchronization
        # *   FullAndOfflineIncremental: one-time full synchronization and batch incremental synchronization
        self.migration_type = migration_type
        # The ID of the DataWorks workspace to which the synchronization task belongs.
        self.project_id = project_id
        # The source type. The value MySQL is returned.
        self.source_data_source_type = source_data_source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.destination_data_source_type is not None:
            result['DestinationDataSourceType'] = self.destination_data_source_type
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.migration_type is not None:
            result['MigrationType'] = self.migration_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.source_data_source_type is not None:
            result['SourceDataSourceType'] = self.source_data_source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('DestinationDataSourceType') is not None:
            self.destination_data_source_type = m.get('DestinationDataSourceType')
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('MigrationType') is not None:
            self.migration_type = m.get('MigrationType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SourceDataSourceType') is not None:
            self.source_data_source_type = m.get('SourceDataSourceType')
        return self


class ListDIJobsResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        dijobs: List[ListDIJobsResponseBodyPagingInfoDIJobs] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The synchronization tasks that are returned.
        self.dijobs = dijobs
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.dijobs:
            for k in self.dijobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DIJobs'] = []
        if self.dijobs is not None:
            for k in self.dijobs:
                result['DIJobs'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dijobs = []
        if m.get('DIJobs') is not None:
            for k in m.get('DIJobs'):
                temp_model = ListDIJobsResponseBodyPagingInfoDIJobs()
                self.dijobs.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDIJobsResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListDIJobsResponseBodyPagingInfo = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListDIJobsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDIJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDIJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDIJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourceSharedRulesRequest(TeaModel):
    def __init__(
        self,
        data_source_id: int = None,
        target_project_id: int = None,
    ):
        # This parameter is required.
        self.data_source_id = data_source_id
        self.target_project_id = target_project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.target_project_id is not None:
            result['TargetProjectId'] = self.target_project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('TargetProjectId') is not None:
            self.target_project_id = m.get('TargetProjectId')
        return self


class ListDataSourceSharedRulesResponseBodyDataSourceSharedRules(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        data_source_id: int = None,
        env_type: str = None,
        id: int = None,
        shared_data_source_name: str = None,
        shared_user: str = None,
        source_project_id: int = None,
        target_project_id: int = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.data_source_id = data_source_id
        self.env_type = env_type
        self.id = id
        self.shared_data_source_name = shared_data_source_name
        self.shared_user = shared_user
        self.source_project_id = source_project_id
        self.target_project_id = target_project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.id is not None:
            result['Id'] = self.id
        if self.shared_data_source_name is not None:
            result['SharedDataSourceName'] = self.shared_data_source_name
        if self.shared_user is not None:
            result['SharedUser'] = self.shared_user
        if self.source_project_id is not None:
            result['SourceProjectId'] = self.source_project_id
        if self.target_project_id is not None:
            result['TargetProjectId'] = self.target_project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SharedDataSourceName') is not None:
            self.shared_data_source_name = m.get('SharedDataSourceName')
        if m.get('SharedUser') is not None:
            self.shared_user = m.get('SharedUser')
        if m.get('SourceProjectId') is not None:
            self.source_project_id = m.get('SourceProjectId')
        if m.get('TargetProjectId') is not None:
            self.target_project_id = m.get('TargetProjectId')
        return self


class ListDataSourceSharedRulesResponseBody(TeaModel):
    def __init__(
        self,
        data_source_shared_rules: List[ListDataSourceSharedRulesResponseBodyDataSourceSharedRules] = None,
        request_id: str = None,
    ):
        self.data_source_shared_rules = data_source_shared_rules
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data_source_shared_rules:
            for k in self.data_source_shared_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSourceSharedRules'] = []
        if self.data_source_shared_rules is not None:
            for k in self.data_source_shared_rules:
                result['DataSourceSharedRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source_shared_rules = []
        if m.get('DataSourceSharedRules') is not None:
            for k in m.get('DataSourceSharedRules'):
                temp_model = ListDataSourceSharedRulesResponseBodyDataSourceSharedRules()
                self.data_source_shared_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataSourceSharedRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourceSharedRulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourceSharedRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDataSourcesRequest(TeaModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        tags: str = None,
        types: List[str] = None,
    ):
        self.env_type = env_type
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
        self.sort_by = sort_by
        self.tags = tags
        self.types = types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class ListDataSourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        env_type: str = None,
        name: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        sort_by: str = None,
        tags: str = None,
        types_shrink: str = None,
    ):
        self.env_type = env_type
        self.name = name
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
        self.sort_by = sort_by
        self.tags = tags
        self.types_shrink = types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env_type is not None:
            result['EnvType'] = self.env_type
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.types_shrink is not None:
            result['Types'] = self.types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Types') is not None:
            self.types_shrink = m.get('Types')
        return self


class ListDataSourcesResponseBodyPagingInfoDataSourcesDataSource(TeaModel):
    def __init__(
        self,
        connection_properties: Any = None,
        connection_properties_mode: str = None,
        create_time: int = None,
        create_user: str = None,
        description: str = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        qualified_name: str = None,
    ):
        self.connection_properties = connection_properties
        self.connection_properties_mode = connection_properties_mode
        self.create_time = create_time
        self.create_user = create_user
        self.description = description
        self.id = id
        self.modify_time = modify_time
        self.modify_user = modify_user
        self.qualified_name = qualified_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties
        if self.connection_properties_mode is not None:
            result['ConnectionPropertiesMode'] = self.connection_properties_mode
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user
        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')
        if m.get('ConnectionPropertiesMode') is not None:
            self.connection_properties_mode = m.get('ConnectionPropertiesMode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')
        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')
        return self


class ListDataSourcesResponseBodyPagingInfoDataSources(TeaModel):
    def __init__(
        self,
        data_source: List[ListDataSourcesResponseBodyPagingInfoDataSourcesDataSource] = None,
        name: str = None,
        type: str = None,
    ):
        self.data_source = data_source
        self.name = name
        self.type = type

    def validate(self):
        if self.data_source:
            for k in self.data_source:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSource'] = []
        if self.data_source is not None:
            for k in self.data_source:
                result['DataSource'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_source = []
        if m.get('DataSource') is not None:
            for k in m.get('DataSource'):
                temp_model = ListDataSourcesResponseBodyPagingInfoDataSourcesDataSource()
                self.data_source.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDataSourcesResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        data_sources: List[ListDataSourcesResponseBodyPagingInfoDataSources] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.data_sources = data_sources
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.data_sources:
            for k in self.data_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataSources'] = []
        if self.data_sources is not None:
            for k in self.data_sources:
                result['DataSources'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sources = []
        if m.get('DataSources') is not None:
            for k in m.get('DataSources'):
                temp_model = ListDataSourcesResponseBodyPagingInfoDataSources()
                self.data_sources.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDataSourcesResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListDataSourcesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListDataSourcesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDataSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDataSourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDataSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentsRequest(TeaModel):
    def __init__(
        self,
        creator: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        status: str = None,
    ):
        # The ID of the user who creates the processes. This parameter specifies a filter condition.
        self.creator = creator
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The status of the processes. This parameter specifies a filter condition.
        # 
        # Valid values:
        # 
        # *   INIT
        # *   RUNNING
        # *   SUCCESS
        # *   FAIL
        # *   TERMINATION
        # *   CANCEL
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDeploymentsResponseBodyPagingInfoDeploymentsStages(TeaModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        detail: Dict[str, Any] = None,
        message: str = None,
        name: str = None,
        status: str = None,
        step: int = None,
        type: str = None,
    ):
        # The code of the stage.
        self.code = code
        # The description of the stage.
        self.description = description
        # The additional information about the stage.
        self.detail = detail
        # The error message returned during the stage.
        self.message = message
        # The name of the stage.
        self.name = name
        # The status of the stage.
        # 
        # Valid values:
        # 
        # *   INIT
        # *   RUNNING
        # *   SUCCESS
        # *   FAIL
        # *   TERMINATION
        # *   CANCEL
        self.status = status
        # The step number of the stage.
        self.step = step
        # The type of the stage. This parameter indicates the operation type in the stage.
        # 
        # Valid values:
        # 
        # *   DEPLOY
        # *   CHECK
        # *   OFFLINE.
        # *   BUILD
        # *   DELETE
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.step is not None:
            result['Step'] = self.step
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListDeploymentsResponseBodyPagingInfoDeployments(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        creator: str = None,
        id: str = None,
        message: str = None,
        modify_time: int = None,
        project_id: str = None,
        stages: List[ListDeploymentsResponseBodyPagingInfoDeploymentsStages] = None,
        status: str = None,
    ):
        # The time when the process was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The ID of the user who creates the process.
        self.creator = creator
        # The process ID.
        self.id = id
        # The error message returned if the process fails.
        self.message = message
        # The time when the process was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The stages of the process.
        self.stages = stages
        # The status of the process.
        # 
        # Valid values:
        # 
        # *   INIT
        # *   RUNNING
        # *   FAIL
        # *   SUCCESS
        # *   TERMINATION
        # *   CANCEL
        self.status = status

    def validate(self):
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['Stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['Stages'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.stages = []
        if m.get('Stages') is not None:
            for k in m.get('Stages'):
                temp_model = ListDeploymentsResponseBodyPagingInfoDeploymentsStages()
                self.stages.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDeploymentsResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        deployments: List[ListDeploymentsResponseBodyPagingInfoDeployments] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The processes.
        self.deployments = deployments
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.deployments:
            for k in self.deployments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Deployments'] = []
        if self.deployments is not None:
            for k in self.deployments:
                result['Deployments'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployments = []
        if m.get('Deployments') is not None:
            for k in m.get('Deployments'):
                temp_model = ListDeploymentsResponseBodyPagingInfoDeployments()
                self.deployments.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListDeploymentsResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListDeploymentsResponseBodyPagingInfo = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListDeploymentsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeploymentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeploymentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeploymentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionsRequest(TeaModel):
    def __init__(
        self,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        type: str = None,
    ):
        # The ID of the owner of the UDF. This parameter specifies a filter condition.
        self.owner = owner
        # The page number. Default value: 1. Minimum value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The UDF type. This parameter specifies a filter condition.
        # 
        # Valid values:
        # 
        # *   MATH: mathematical operation function
        # *   AGGREGATE: aggregate function
        # *   STRING: string processing function
        # *   DATE: date function
        # *   ANALYTIC: window function
        # *   OTHER: others
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFunctionsResponseBodyPagingInfoFunctionsDataSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the data source.
        self.name = name
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFunctionsResponseBodyPagingInfoFunctionsRuntimeResource(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The ID of the resource group used when you run the UDF.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFunctionsResponseBodyPagingInfoFunctionsScriptRuntime(TeaModel):
    def __init__(
        self,
        command: str = None,
    ):
        # The command.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class ListFunctionsResponseBodyPagingInfoFunctionsScript(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: ListFunctionsResponseBodyPagingInfoFunctionsScriptRuntime = None,
    ):
        # The script ID.
        self.id = id
        # The script path.
        self.path = path
        # The runtime.
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Runtime') is not None:
            temp_model = ListFunctionsResponseBodyPagingInfoFunctionsScriptRuntime()
            self.runtime = temp_model.from_map(m['Runtime'])
        return self


class ListFunctionsResponseBodyPagingInfoFunctions(TeaModel):
    def __init__(
        self,
        arm_resource: str = None,
        class_name: str = None,
        command_description: str = None,
        create_time: int = None,
        data_source: ListFunctionsResponseBodyPagingInfoFunctionsDataSource = None,
        database_name: str = None,
        description: str = None,
        embedded_code: str = None,
        embedded_code_type: str = None,
        embedded_resource_type: str = None,
        example_description: str = None,
        file_resource: str = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        parameter_description: str = None,
        project_id: str = None,
        return_value_description: str = None,
        runtime_resource: ListFunctionsResponseBodyPagingInfoFunctionsRuntimeResource = None,
        script: ListFunctionsResponseBodyPagingInfoFunctionsScript = None,
        type: str = None,
    ):
        # The file resources in an Advanced RISC Machines (ARM) cluster.
        self.arm_resource = arm_resource
        # The fully qualified class name of the UDF.
        self.class_name = class_name
        # The description of the command.
        self.command_description = command_description
        # The time when the UDF was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The data source information about the UDF.
        self.data_source = data_source
        # The name of the database. This parameter is returned for E-MapReduce (EMR) functions.
        self.database_name = database_name
        # The overall description of the UDF.
        self.description = description
        # The code of the embedded UDF.
        self.embedded_code = embedded_code
        # The type of the nested code.
        # 
        # Valid values:
        # 
        # *   Python2
        # *   Python3
        # *   Java8
        # *   Java11
        # *   Java17
        self.embedded_code_type = embedded_code_type
        # The type of the nested resource.
        # 
        # Valid values:
        # 
        # *   File: general resources
        # *   Embedded: embedded resources
        self.embedded_resource_type = embedded_resource_type
        # The description of the example.
        self.example_description = example_description
        # The files resources.
        self.file_resource = file_resource
        # The ID of the UDF.
        self.id = id
        # The time when the UDF was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the UDF.
        self.name = name
        # The owner of the UDF.
        self.owner = owner
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The ID of the workspace to which the UDF belongs.
        self.project_id = project_id
        # The description of the return value.
        self.return_value_description = return_value_description
        # The information about the resource group used when you run the UDF.
        self.runtime_resource = runtime_resource
        # The script information about the UDF.
        self.script = script
        # The UDF type.
        # 
        # Valid values:
        # 
        # *   MATH: mathematical operation function
        # *   AGGREGATE: aggregate function
        # *   STRING: string processing function
        # *   DATE: date function
        # *   ANALYTIC: window function
        # *   OTHER: others
        self.type = type

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.script:
            self.script.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arm_resource is not None:
            result['ArmResource'] = self.arm_resource
        if self.class_name is not None:
            result['ClassName'] = self.class_name
        if self.command_description is not None:
            result['CommandDescription'] = self.command_description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name
        if self.description is not None:
            result['Description'] = self.description
        if self.embedded_code is not None:
            result['EmbeddedCode'] = self.embedded_code
        if self.embedded_code_type is not None:
            result['EmbeddedCodeType'] = self.embedded_code_type
        if self.embedded_resource_type is not None:
            result['EmbeddedResourceType'] = self.embedded_resource_type
        if self.example_description is not None:
            result['ExampleDescription'] = self.example_description
        if self.file_resource is not None:
            result['FileResource'] = self.file_resource
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.return_value_description is not None:
            result['ReturnValueDescription'] = self.return_value_description
        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArmResource') is not None:
            self.arm_resource = m.get('ArmResource')
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')
        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSource') is not None:
            temp_model = ListFunctionsResponseBodyPagingInfoFunctionsDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EmbeddedCode') is not None:
            self.embedded_code = m.get('EmbeddedCode')
        if m.get('EmbeddedCodeType') is not None:
            self.embedded_code_type = m.get('EmbeddedCodeType')
        if m.get('EmbeddedResourceType') is not None:
            self.embedded_resource_type = m.get('EmbeddedResourceType')
        if m.get('ExampleDescription') is not None:
            self.example_description = m.get('ExampleDescription')
        if m.get('FileResource') is not None:
            self.file_resource = m.get('FileResource')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ReturnValueDescription') is not None:
            self.return_value_description = m.get('ReturnValueDescription')
        if m.get('RuntimeResource') is not None:
            temp_model = ListFunctionsResponseBodyPagingInfoFunctionsRuntimeResource()
            self.runtime_resource = temp_model.from_map(m['RuntimeResource'])
        if m.get('Script') is not None:
            temp_model = ListFunctionsResponseBodyPagingInfoFunctionsScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListFunctionsResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        functions: List[ListFunctionsResponseBodyPagingInfoFunctions] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The UDFs.
        self.functions = functions
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.functions:
            for k in self.functions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Functions'] = []
        if self.functions is not None:
            for k in self.functions:
                result['Functions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('Functions') is not None:
            for k in m.get('Functions'):
                temp_model = ListFunctionsResponseBodyPagingInfoFunctions()
                self.functions.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFunctionsResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListFunctionsResponseBodyPagingInfo = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListFunctionsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFunctionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFunctionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFunctionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetworksRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # This parameter is required.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListNetworksResponseBodyNetworkList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        id: int = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        status: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.status = status
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class ListNetworksResponseBody(TeaModel):
    def __init__(
        self,
        network_list: List[ListNetworksResponseBodyNetworkList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.network_list = network_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.network_list:
            for k in self.network_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NetworkList'] = []
        if self.network_list is not None:
            for k in self.network_list:
                result['NetworkList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_list = []
        if m.get('NetworkList') is not None:
            for k in m.get('NetworkList'):
                temp_model = ListNetworksResponseBodyNetworkList()
                self.network_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListNetworksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNetworksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNetworksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeDependenciesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
    ):
        # The ID of the node.
        # 
        # This parameter is required.
        self.id = id
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesDataSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the data source.
        self.name = name
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesInputsNodeOutputs(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        # The node output.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesInputsTables(TeaModel):
    def __init__(
        self,
        guid: str = None,
    ):
        # The table ID.
        self.guid = guid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guid is not None:
            result['Guid'] = self.guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariablesNode(TeaModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The output of the node.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariables(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        id: str = None,
        name: str = None,
        node: ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariablesNode = None,
        scope: str = None,
        type: str = None,
        value: str = None,
    ):
        # The artifact type.
        self.artifact_type = artifact_type
        # The variable ID.
        self.id = id
        # The name of the variable.
        self.name = name
        # The node to which the variable belongs.
        self.node = node
        # The scope of the variable.
        # 
        # Valid values:
        # 
        # *   NodeParameter
        # *   NodeContext
        # *   Workflow
        # *   Workspace
        self.scope = scope
        # The type of the variable.
        # 
        # Valid values:
        # 
        # *   NoKvVariableExpression
        # *   Constant
        # *   PassThrough
        # *   System
        # *   NodeOutput
        self.type = type
        # The value of the variable.
        self.value = value

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.node is not None:
            result['Node'] = self.node.to_map()
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Node') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariablesNode()
            self.node = temp_model.from_map(m['Node'])
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesInputs(TeaModel):
    def __init__(
        self,
        node_outputs: List[ListNodeDependenciesResponseBodyPagingInfoNodesInputsNodeOutputs] = None,
        tables: List[ListNodeDependenciesResponseBodyPagingInfoNodesInputsTables] = None,
        variables: List[ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariables] = None,
    ):
        # The node outputs.
        self.node_outputs = node_outputs
        # The tables.
        self.tables = tables
        # The variables.
        self.variables = variables

    def validate(self):
        if self.node_outputs:
            for k in self.node_outputs:
                if k:
                    k.validate()
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeOutputs'] = []
        if self.node_outputs is not None:
            for k in self.node_outputs:
                result['NodeOutputs'].append(k.to_map() if k else None)
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_outputs = []
        if m.get('NodeOutputs') is not None:
            for k in m.get('NodeOutputs'):
                temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesInputsNodeOutputs()
                self.node_outputs.append(temp_model.from_map(k))
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesInputsTables()
                self.tables.append(temp_model.from_map(k))
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesInputsVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesOutputsNodeOutputs(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        # The node output.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesOutputsTables(TeaModel):
    def __init__(
        self,
        guid: str = None,
    ):
        # The table ID.
        self.guid = guid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guid is not None:
            result['Guid'] = self.guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariablesNode(TeaModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The output of the node to which the variable belongs.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariables(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        id: str = None,
        name: str = None,
        node: ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariablesNode = None,
        scope: str = None,
        type: str = None,
        value: str = None,
    ):
        # The artifact type.
        self.artifact_type = artifact_type
        # The variable ID.
        self.id = id
        # The name of the variable.
        self.name = name
        # The node to which the variable belongs.
        self.node = node
        # The scope of the variable.
        # 
        # Valid values:
        # 
        # *   NodeParameter
        # *   NodeContext
        # *   Workflow
        # *   Workspace
        self.scope = scope
        # The type of the variable.
        # 
        # Valid values:
        # 
        # *   NoKvVariableExpression
        # *   Constant
        # *   PassThrough
        # *   System
        # *   NodeOutput
        self.type = type
        # The value of the variable.
        self.value = value

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.node is not None:
            result['Node'] = self.node.to_map()
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Node') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariablesNode()
            self.node = temp_model.from_map(m['Node'])
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesOutputs(TeaModel):
    def __init__(
        self,
        node_outputs: List[ListNodeDependenciesResponseBodyPagingInfoNodesOutputsNodeOutputs] = None,
        tables: List[ListNodeDependenciesResponseBodyPagingInfoNodesOutputsTables] = None,
        variables: List[ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariables] = None,
    ):
        # The node outputs.
        self.node_outputs = node_outputs
        # The tables.
        self.tables = tables
        # The variables.
        self.variables = variables

    def validate(self):
        if self.node_outputs:
            for k in self.node_outputs:
                if k:
                    k.validate()
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeOutputs'] = []
        if self.node_outputs is not None:
            for k in self.node_outputs:
                result['NodeOutputs'].append(k.to_map() if k else None)
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_outputs = []
        if m.get('NodeOutputs') is not None:
            for k in m.get('NodeOutputs'):
                temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesOutputsNodeOutputs()
                self.node_outputs.append(temp_model.from_map(k))
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesOutputsTables()
                self.tables.append(temp_model.from_map(k))
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesOutputsVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesRuntimeResource(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesScriptRuntime(TeaModel):
    def __init__(
        self,
        command: str = None,
    ):
        # The command used to distinguish node types.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesScript(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: ListNodeDependenciesResponseBodyPagingInfoNodesScriptRuntime = None,
    ):
        # The script ID.
        self.id = id
        # The script path.
        self.path = path
        # The runtime.
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Runtime') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesScriptRuntime()
            self.runtime = temp_model.from_map(m['Runtime'])
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesStrategy(TeaModel):
    def __init__(
        self,
        instance_mode: str = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        timeout: int = None,
    ):
        # The instance generation mode.
        self.instance_mode = instance_mode
        # The rerun interval after a failure. Unit: milliseconds.
        self.rerun_interval = rerun_interval
        # The rerun mode.
        self.rerun_mode = rerun_mode
        # The number of reruns after a failure.
        self.rerun_times = rerun_times
        # The timeout period. Unit: milliseconds.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode
        if self.rerun_interval is not None:
            result['RerunInterval'] = self.rerun_interval
        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode
        if self.rerun_times is not None:
            result['RerunTimes'] = self.rerun_times
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')
        if m.get('RerunInterval') is not None:
            self.rerun_interval = m.get('RerunInterval')
        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')
        if m.get('RerunTimes') is not None:
            self.rerun_times = m.get('RerunTimes')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodesTrigger(TeaModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        id: str = None,
        start_time: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The CRON expression for scheduling.
        self.cron = cron
        # The end time of the validity period of the scheduling. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.end_time = end_time
        # The trigger ID.
        self.id = id
        # The start time of the validity period of the scheduling. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.start_time = start_time
        # The time zone.
        self.timezone = timezone
        # The type of the trigger.
        # 
        # Valid values:
        # 
        # *   Scheduler
        # *   Manual
        # *   Streaming
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron is not None:
            result['Cron'] = self.cron
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNodeDependenciesResponseBodyPagingInfoNodes(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data_source: ListNodeDependenciesResponseBodyPagingInfoNodesDataSource = None,
        description: str = None,
        id: str = None,
        inputs: ListNodeDependenciesResponseBodyPagingInfoNodesInputs = None,
        modify_time: int = None,
        name: str = None,
        outputs: ListNodeDependenciesResponseBodyPagingInfoNodesOutputs = None,
        owner: str = None,
        project_id: str = None,
        recurrence: str = None,
        runtime_resource: ListNodeDependenciesResponseBodyPagingInfoNodesRuntimeResource = None,
        script: ListNodeDependenciesResponseBodyPagingInfoNodesScript = None,
        strategy: ListNodeDependenciesResponseBodyPagingInfoNodesStrategy = None,
        tags: List[ListNodeDependenciesResponseBodyPagingInfoNodesTags] = None,
        task_id: str = None,
        trigger: ListNodeDependenciesResponseBodyPagingInfoNodesTrigger = None,
    ):
        # The time when the node was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The information about the data source.
        self.data_source = data_source
        # The description of the node.
        self.description = description
        # The ID of the node.
        self.id = id
        # The input of the node.
        self.inputs = inputs
        # The time when the node was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the node.
        self.name = name
        # The output of the node.
        self.outputs = outputs
        # The owner of the node.
        self.owner = owner
        # The ID of the workspace to which the node belongs.
        self.project_id = project_id
        # The scheduling type.
        # 
        # Valid values:
        # 
        # *   Normal: The node is scheduled as expected.
        # *   Pause: The node is paused, and the running of its descendant nodes is blocked.
        # *   Skip: The node is dry run. The system does not actually run the node but directly prompts that the node is successfully run. The running duration of the node is 0 seconds. In addition, the node does not occupy resources or block the running of its descendant nodes.
        self.recurrence = recurrence
        # The information about the resource group.
        self.runtime_resource = runtime_resource
        # The script information.
        self.script = script
        # The scheduling policy.
        self.strategy = strategy
        # The tags. This parameter is not in use.
        self.tags = tags
        # The scheduling task ID.
        self.task_id = task_id
        # The trigger.
        self.trigger = trigger

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.inputs:
            self.inputs.validate()
        if self.outputs:
            self.outputs.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.script:
            self.script.validate()
        if self.strategy:
            self.strategy.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence
        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSource') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Inputs') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesInputs()
            self.inputs = temp_model.from_map(m['Inputs'])
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Outputs') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesOutputs()
            self.outputs = temp_model.from_map(m['Outputs'])
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')
        if m.get('RuntimeResource') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesRuntimeResource()
            self.runtime_resource = temp_model.from_map(m['RuntimeResource'])
        if m.get('Script') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('Strategy') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesStrategy()
            self.strategy = temp_model.from_map(m['Strategy'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Trigger') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfoNodesTrigger()
            self.trigger = temp_model.from_map(m['Trigger'])
        return self


class ListNodeDependenciesResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        nodes: List[ListNodeDependenciesResponseBodyPagingInfoNodes] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The descendant nodes.
        self.nodes = nodes
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListNodeDependenciesResponseBodyPagingInfoNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeDependenciesResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListNodeDependenciesResponseBodyPagingInfo = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListNodeDependenciesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNodeDependenciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeDependenciesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodeDependenciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodesRequest(TeaModel):
    def __init__(
        self,
        container_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        recurrence: str = None,
        rerun_mode: str = None,
        scene: str = None,
    ):
        # The container ID. This parameter specifies a filter condition.
        self.container_id = container_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        self.recurrence = recurrence
        # The rerun mode. Valid values:
        # 
        # *   Allowed: The nodes can be rerun regardless of whether they are successfully run or fail to run.
        # *   FailureAllowed: The nodes can be rerun only after they fail to run.
        # *   Denied: The nodes cannot be rerun regardless of whether they are successfully run or fail to run.
        self.rerun_mode = rerun_mode
        # The scene of nodes. This parameter specifies a filter condition.
        # 
        # Valid values:
        # 
        # *   DATAWORKS_PROJECT
        # *   MANUAL_WORKFLOW
        # *   MANUAL_NODE
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_id is not None:
            result['ContainerId'] = self.container_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence
        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerId') is not None:
            self.container_id = m.get('ContainerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')
        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ListNodesResponseBodyPagingInfoNodesDataSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the data source.
        self.name = name
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNodesResponseBodyPagingInfoNodesInputsNodeOutputs(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        # The node output.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListNodesResponseBodyPagingInfoNodesInputsTables(TeaModel):
    def __init__(
        self,
        guid: str = None,
    ):
        # The table ID.
        self.guid = guid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guid is not None:
            result['Guid'] = self.guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')
        return self


class ListNodesResponseBodyPagingInfoNodesInputsVariablesNode(TeaModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The output of the node.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class ListNodesResponseBodyPagingInfoNodesInputsVariables(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        id: str = None,
        name: str = None,
        node: ListNodesResponseBodyPagingInfoNodesInputsVariablesNode = None,
        scope: str = None,
        type: str = None,
        value: str = None,
    ):
        # The artifact type.
        self.artifact_type = artifact_type
        # The variable ID.
        self.id = id
        # The name of the variable.
        self.name = name
        # The node to which the variable belongs.
        self.node = node
        # The scope of the variable.
        # 
        # Valid values:
        # 
        # *   WorkSpace
        # *   NodeParameter
        # *   NodeContext
        # *   Workflow
        self.scope = scope
        # The type of the variable.
        # 
        # Valid values:
        # 
        # *   NoKvVariableExpression
        # *   Constant
        # *   PassThrough
        # *   System
        # *   NodeOutput
        self.type = type
        # The value of the variable.
        self.value = value

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.node is not None:
            result['Node'] = self.node.to_map()
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Node') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesInputsVariablesNode()
            self.node = temp_model.from_map(m['Node'])
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNodesResponseBodyPagingInfoNodesInputs(TeaModel):
    def __init__(
        self,
        node_outputs: List[ListNodesResponseBodyPagingInfoNodesInputsNodeOutputs] = None,
        tables: List[ListNodesResponseBodyPagingInfoNodesInputsTables] = None,
        variables: List[ListNodesResponseBodyPagingInfoNodesInputsVariables] = None,
    ):
        # The node outputs.
        self.node_outputs = node_outputs
        # The tables.
        self.tables = tables
        # The variables.
        self.variables = variables

    def validate(self):
        if self.node_outputs:
            for k in self.node_outputs:
                if k:
                    k.validate()
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeOutputs'] = []
        if self.node_outputs is not None:
            for k in self.node_outputs:
                result['NodeOutputs'].append(k.to_map() if k else None)
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_outputs = []
        if m.get('NodeOutputs') is not None:
            for k in m.get('NodeOutputs'):
                temp_model = ListNodesResponseBodyPagingInfoNodesInputsNodeOutputs()
                self.node_outputs.append(temp_model.from_map(k))
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = ListNodesResponseBodyPagingInfoNodesInputsTables()
                self.tables.append(temp_model.from_map(k))
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = ListNodesResponseBodyPagingInfoNodesInputsVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListNodesResponseBodyPagingInfoNodesOutputsNodeOutputs(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        # The node output.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListNodesResponseBodyPagingInfoNodesOutputsTables(TeaModel):
    def __init__(
        self,
        guid: str = None,
    ):
        # The table ID.
        self.guid = guid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.guid is not None:
            result['Guid'] = self.guid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Guid') is not None:
            self.guid = m.get('Guid')
        return self


class ListNodesResponseBodyPagingInfoNodesOutputsVariablesNode(TeaModel):
    def __init__(
        self,
        output: str = None,
    ):
        # The output of the node.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')
        return self


class ListNodesResponseBodyPagingInfoNodesOutputsVariables(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        id: str = None,
        name: str = None,
        node: ListNodesResponseBodyPagingInfoNodesOutputsVariablesNode = None,
        scope: str = None,
        type: str = None,
        value: str = None,
    ):
        # The artifact type.
        self.artifact_type = artifact_type
        # The variable ID.
        self.id = id
        # The name of the variable.
        self.name = name
        # The node to which the variable belongs.
        self.node = node
        # The scope of the variable.
        # 
        # Valid values:
        # 
        # *   NodeParameter
        # *   NodeContext
        # *   Workflow
        # *   Workspace
        self.scope = scope
        # The type of the variable.
        # 
        # Valid values:
        # 
        # *   NoKvVariableExpression
        # *   Constant
        # *   PassThrough
        # *   System
        # *   NodeOutput
        self.type = type
        # The value of the variable.
        self.value = value

    def validate(self):
        if self.node:
            self.node.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.node is not None:
            result['Node'] = self.node.to_map()
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Node') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesOutputsVariablesNode()
            self.node = temp_model.from_map(m['Node'])
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNodesResponseBodyPagingInfoNodesOutputs(TeaModel):
    def __init__(
        self,
        node_outputs: List[ListNodesResponseBodyPagingInfoNodesOutputsNodeOutputs] = None,
        tables: List[ListNodesResponseBodyPagingInfoNodesOutputsTables] = None,
        variables: List[ListNodesResponseBodyPagingInfoNodesOutputsVariables] = None,
    ):
        # The node outputs.
        self.node_outputs = node_outputs
        # The tables.
        self.tables = tables
        # The variables.
        self.variables = variables

    def validate(self):
        if self.node_outputs:
            for k in self.node_outputs:
                if k:
                    k.validate()
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeOutputs'] = []
        if self.node_outputs is not None:
            for k in self.node_outputs:
                result['NodeOutputs'].append(k.to_map() if k else None)
        result['Tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['Tables'].append(k.to_map() if k else None)
        result['Variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['Variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node_outputs = []
        if m.get('NodeOutputs') is not None:
            for k in m.get('NodeOutputs'):
                temp_model = ListNodesResponseBodyPagingInfoNodesOutputsNodeOutputs()
                self.node_outputs.append(temp_model.from_map(k))
        self.tables = []
        if m.get('Tables') is not None:
            for k in m.get('Tables'):
                temp_model = ListNodesResponseBodyPagingInfoNodesOutputsTables()
                self.tables.append(temp_model.from_map(k))
        self.variables = []
        if m.get('Variables') is not None:
            for k in m.get('Variables'):
                temp_model = ListNodesResponseBodyPagingInfoNodesOutputsVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListNodesResponseBodyPagingInfoNodesRuntimeResource(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
    ):
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListNodesResponseBodyPagingInfoNodesScriptRuntime(TeaModel):
    def __init__(
        self,
        command: str = None,
    ):
        # The command used to distinguish node types.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class ListNodesResponseBodyPagingInfoNodesScript(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: ListNodesResponseBodyPagingInfoNodesScriptRuntime = None,
    ):
        # The script ID.
        self.id = id
        # The script path.
        self.path = path
        # The runtime.
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Runtime') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesScriptRuntime()
            self.runtime = temp_model.from_map(m['Runtime'])
        return self


class ListNodesResponseBodyPagingInfoNodesStrategy(TeaModel):
    def __init__(
        self,
        instance_mode: str = None,
        rerun_interval: int = None,
        rerun_mode: str = None,
        rerun_times: int = None,
        timeout: int = None,
    ):
        # The instance generation mode.
        self.instance_mode = instance_mode
        # The rerun interval. Unit: milliseconds.
        self.rerun_interval = rerun_interval
        # The rerun mode.
        self.rerun_mode = rerun_mode
        # The number of reruns.
        self.rerun_times = rerun_times
        # The timeout period.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_mode is not None:
            result['InstanceMode'] = self.instance_mode
        if self.rerun_interval is not None:
            result['RerunInterval'] = self.rerun_interval
        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode
        if self.rerun_times is not None:
            result['RerunTimes'] = self.rerun_times
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceMode') is not None:
            self.instance_mode = m.get('InstanceMode')
        if m.get('RerunInterval') is not None:
            self.rerun_interval = m.get('RerunInterval')
        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')
        if m.get('RerunTimes') is not None:
            self.rerun_times = m.get('RerunTimes')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class ListNodesResponseBodyPagingInfoNodesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListNodesResponseBodyPagingInfoNodesTrigger(TeaModel):
    def __init__(
        self,
        cron: str = None,
        end_time: str = None,
        id: str = None,
        start_time: str = None,
        timezone: str = None,
        type: str = None,
    ):
        # The CRON expression for scheduling.
        self.cron = cron
        # The end time of the validity period of the trigger.
        self.end_time = end_time
        # The trigger ID.
        self.id = id
        # The start time of the validity period of the trigger.
        self.start_time = start_time
        # The time zone.
        self.timezone = timezone
        # The type of the trigger.
        # 
        # Valid values:
        # 
        # *   Scheduler
        # *   Manual
        # *   Steaming
        # 
        # <!---->
        # 
        # *\
        # *\
        # *\
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron is not None:
            result['Cron'] = self.cron
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNodesResponseBodyPagingInfoNodes(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data_source: ListNodesResponseBodyPagingInfoNodesDataSource = None,
        description: str = None,
        id: str = None,
        inputs: ListNodesResponseBodyPagingInfoNodesInputs = None,
        modify_time: int = None,
        name: str = None,
        outputs: ListNodesResponseBodyPagingInfoNodesOutputs = None,
        owner: str = None,
        project_id: str = None,
        recurrence: str = None,
        runtime_resource: ListNodesResponseBodyPagingInfoNodesRuntimeResource = None,
        script: ListNodesResponseBodyPagingInfoNodesScript = None,
        strategy: ListNodesResponseBodyPagingInfoNodesStrategy = None,
        tags: List[ListNodesResponseBodyPagingInfoNodesTags] = None,
        task_id: str = None,
        trigger: ListNodesResponseBodyPagingInfoNodesTrigger = None,
    ):
        # The time when the node was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The information about the data source.
        self.data_source = data_source
        # The description of the node.
        self.description = description
        # The ID of the node.
        self.id = id
        # The input of the node.
        self.inputs = inputs
        # The time when the node was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the node.
        self.name = name
        # The output of the node.
        self.outputs = outputs
        # The owner of the node.
        self.owner = owner
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        self.project_id = project_id
        # The scheduling type.
        # 
        # Valid values:
        # 
        # *   Normal: The node is scheduled as expected.
        # *   Pause: The node is paused, and the running of its descendant nodes is blocked.
        # *   Skip: The node is dry run. The system does not actually run the node but directly prompts that the node is successfully run. The running duration of the node is 0 seconds. In addition, the node does not occupy resources or block the running of its descendant nodes.
        self.recurrence = recurrence
        # The information about the resource group.
        self.runtime_resource = runtime_resource
        # The script information.
        self.script = script
        # The scheduling policy.
        self.strategy = strategy
        # The tags. This parameter is not in use.
        self.tags = tags
        # The scheduling task ID.
        self.task_id = task_id
        # The trigger.
        self.trigger = trigger

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.inputs:
            self.inputs.validate()
        if self.outputs:
            self.outputs.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()
        if self.script:
            self.script.validate()
        if self.strategy:
            self.strategy.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.inputs is not None:
            result['Inputs'] = self.inputs.to_map()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.outputs is not None:
            result['Outputs'] = self.outputs.to_map()
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.recurrence is not None:
            result['Recurrence'] = self.recurrence
        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSource') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Inputs') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesInputs()
            self.inputs = temp_model.from_map(m['Inputs'])
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Outputs') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesOutputs()
            self.outputs = temp_model.from_map(m['Outputs'])
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Recurrence') is not None:
            self.recurrence = m.get('Recurrence')
        if m.get('RuntimeResource') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesRuntimeResource()
            self.runtime_resource = temp_model.from_map(m['RuntimeResource'])
        if m.get('Script') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('Strategy') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesStrategy()
            self.strategy = temp_model.from_map(m['Strategy'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListNodesResponseBodyPagingInfoNodesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Trigger') is not None:
            temp_model = ListNodesResponseBodyPagingInfoNodesTrigger()
            self.trigger = temp_model.from_map(m['Trigger'])
        return self


class ListNodesResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        nodes: List[ListNodesResponseBodyPagingInfoNodes] = None,
        page_number: str = None,
        page_size: str = None,
        total_count: str = None,
    ):
        # The nodes.
        self.nodes = nodes
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListNodesResponseBodyPagingInfoNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodesResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListNodesResponseBodyPagingInfo = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListNodesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRolesRequest(TeaModel):
    def __init__(
        self,
        codes: List[str] = None,
        names: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        type: str = None,
    ):
        self.codes = codes
        self.names = names
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes is not None:
            result['Codes'] = self.codes
        if self.names is not None:
            result['Names'] = self.names
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes = m.get('Codes')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectRolesShrinkRequest(TeaModel):
    def __init__(
        self,
        codes_shrink: str = None,
        names_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        type: str = None,
    ):
        self.codes_shrink = codes_shrink
        self.names_shrink = names_shrink
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.codes_shrink is not None:
            result['Codes'] = self.codes_shrink
        if self.names_shrink is not None:
            result['Names'] = self.names_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes_shrink = m.get('Codes')
        if m.get('Names') is not None:
            self.names_shrink = m.get('Names')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectRolesResponseBodyPagingInfoProjectRoles(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        project_id: int = None,
        type: str = None,
    ):
        self.code = code
        self.name = name
        self.project_id = project_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListProjectRolesResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        project_roles: List[ListProjectRolesResponseBodyPagingInfoProjectRoles] = None,
        total_count: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.project_roles = project_roles
        self.total_count = total_count

    def validate(self):
        if self.project_roles:
            for k in self.project_roles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ProjectRoles'] = []
        if self.project_roles is not None:
            for k in self.project_roles:
                result['ProjectRoles'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.project_roles = []
        if m.get('ProjectRoles') is not None:
            for k in m.get('ProjectRoles'):
                temp_model = ListProjectRolesResponseBodyPagingInfoProjectRoles()
                self.project_roles.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectRolesResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListProjectRolesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListProjectRolesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectRolesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectRolesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectRolesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequestAliyunResourceTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[ListProjectsRequestAliyunResourceTags] = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        ids: List[int] = None,
        names: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        pai_task_enabled: bool = None,
        status: str = None,
    ):
        self.aliyun_resource_group_id = aliyun_resource_group_id
        self.aliyun_resource_tags = aliyun_resource_tags
        self.dev_environment_enabled = dev_environment_enabled
        self.dev_role_disabled = dev_role_disabled
        self.ids = ids
        self.names = names
        self.page_number = page_number
        self.page_size = page_size
        self.pai_task_enabled = pai_task_enabled
        self.status = status

    def validate(self):
        if self.aliyun_resource_tags:
            for k in self.aliyun_resource_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id
        result['AliyunResourceTags'] = []
        if self.aliyun_resource_tags is not None:
            for k in self.aliyun_resource_tags:
                result['AliyunResourceTags'].append(k.to_map() if k else None)
        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled
        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.names is not None:
            result['Names'] = self.names
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')
        self.aliyun_resource_tags = []
        if m.get('AliyunResourceTags') is not None:
            for k in m.get('AliyunResourceTags'):
                temp_model = ListProjectsRequestAliyunResourceTags()
                self.aliyun_resource_tags.append(temp_model.from_map(k))
        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')
        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Names') is not None:
            self.names = m.get('Names')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListProjectsShrinkRequest(TeaModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags_shrink: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        ids_shrink: str = None,
        names_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        pai_task_enabled: bool = None,
        status: str = None,
    ):
        self.aliyun_resource_group_id = aliyun_resource_group_id
        self.aliyun_resource_tags_shrink = aliyun_resource_tags_shrink
        self.dev_environment_enabled = dev_environment_enabled
        self.dev_role_disabled = dev_role_disabled
        self.ids_shrink = ids_shrink
        self.names_shrink = names_shrink
        self.page_number = page_number
        self.page_size = page_size
        self.pai_task_enabled = pai_task_enabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id
        if self.aliyun_resource_tags_shrink is not None:
            result['AliyunResourceTags'] = self.aliyun_resource_tags_shrink
        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled
        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled
        if self.ids_shrink is not None:
            result['Ids'] = self.ids_shrink
        if self.names_shrink is not None:
            result['Names'] = self.names_shrink
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')
        if m.get('AliyunResourceTags') is not None:
            self.aliyun_resource_tags_shrink = m.get('AliyunResourceTags')
        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')
        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')
        if m.get('Ids') is not None:
            self.ids_shrink = m.get('Ids')
        if m.get('Names') is not None:
            self.names_shrink = m.get('Names')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListProjectsResponseBodyPagingInfoProjectsAliyunResourceTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProjectsResponseBodyPagingInfoProjects(TeaModel):
    def __init__(
        self,
        aliyun_resource_group_id: str = None,
        aliyun_resource_tags: List[ListProjectsResponseBodyPagingInfoProjectsAliyunResourceTags] = None,
        description: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        display_name: str = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        pai_task_enabled: bool = None,
        status: str = None,
    ):
        self.aliyun_resource_group_id = aliyun_resource_group_id
        self.aliyun_resource_tags = aliyun_resource_tags
        self.description = description
        self.dev_environment_enabled = dev_environment_enabled
        self.dev_role_disabled = dev_role_disabled
        self.display_name = display_name
        self.id = id
        self.name = name
        self.owner = owner
        self.pai_task_enabled = pai_task_enabled
        self.status = status

    def validate(self):
        if self.aliyun_resource_tags:
            for k in self.aliyun_resource_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_resource_group_id is not None:
            result['AliyunResourceGroupId'] = self.aliyun_resource_group_id
        result['AliyunResourceTags'] = []
        if self.aliyun_resource_tags is not None:
            for k in self.aliyun_resource_tags:
                result['AliyunResourceTags'].append(k.to_map() if k else None)
        if self.description is not None:
            result['Description'] = self.description
        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled
        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunResourceGroupId') is not None:
            self.aliyun_resource_group_id = m.get('AliyunResourceGroupId')
        self.aliyun_resource_tags = []
        if m.get('AliyunResourceTags') is not None:
            for k in m.get('AliyunResourceTags'):
                temp_model = ListProjectsResponseBodyPagingInfoProjectsAliyunResourceTags()
                self.aliyun_resource_tags.append(temp_model.from_map(k))
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')
        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListProjectsResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        projects: List[ListProjectsResponseBodyPagingInfoProjects] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.projects = projects
        self.total_count = total_count

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['Projects'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.projects = []
        if m.get('Projects') is not None:
            for k in m.get('Projects'):
                temp_model = ListProjectsResponseBodyPagingInfoProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListProjectsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        self.paging_info = paging_info
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListProjectsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        payment_type: str = None,
        project_id: int = None,
        resource_group_types: List[str] = None,
        statuses: List[str] = None,
    ):
        self.name = name
        self.payment_type = payment_type
        self.project_id = project_id
        self.resource_group_types = resource_group_types
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_group_types is not None:
            result['ResourceGroupTypes'] = self.resource_group_types
        if self.statuses is not None:
            result['Statuses'] = self.statuses
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceGroupTypes') is not None:
            self.resource_group_types = m.get('ResourceGroupTypes')
        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')
        return self


class ListResourceGroupsShrinkRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        payment_type: str = None,
        project_id: int = None,
        resource_group_types_shrink: str = None,
        statuses_shrink: str = None,
    ):
        self.name = name
        self.payment_type = payment_type
        self.project_id = project_id
        self.resource_group_types_shrink = resource_group_types_shrink
        self.statuses_shrink = statuses_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_group_types_shrink is not None:
            result['ResourceGroupTypes'] = self.resource_group_types_shrink
        if self.statuses_shrink is not None:
            result['Statuses'] = self.statuses_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceGroupTypes') is not None:
            self.resource_group_types_shrink = m.get('ResourceGroupTypes')
        if m.get('Statuses') is not None:
            self.statuses_shrink = m.get('Statuses')
        return self


class ListResourceGroupsResponseBodyResourceGroupListSpec(TeaModel):
    def __init__(
        self,
        amount: int = None,
        standard: str = None,
    ):
        self.amount = amount
        self.standard = standard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.standard is not None:
            result['Standard'] = self.standard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Standard') is not None:
            self.standard = m.get('Standard')
        return self


class ListResourceGroupsResponseBodyResourceGroupList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        create_user: str = None,
        default_vpc_id: str = None,
        default_vswicth_id: str = None,
        id: str = None,
        name: str = None,
        order_instance_id: str = None,
        payment_type: str = None,
        remark: str = None,
        resource_group_type: str = None,
        spec: ListResourceGroupsResponseBodyResourceGroupListSpec = None,
        status: str = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.default_vpc_id = default_vpc_id
        self.default_vswicth_id = default_vswicth_id
        self.id = id
        self.name = name
        self.order_instance_id = order_instance_id
        self.payment_type = payment_type
        self.remark = remark
        self.resource_group_type = resource_group_type
        self.spec = spec
        self.status = status

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.default_vpc_id is not None:
            result['DefaultVpcId'] = self.default_vpc_id
        if self.default_vswicth_id is not None:
            result['DefaultVswicthId'] = self.default_vswicth_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.order_instance_id is not None:
            result['OrderInstanceId'] = self.order_instance_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_group_type is not None:
            result['ResourceGroupType'] = self.resource_group_type
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DefaultVpcId') is not None:
            self.default_vpc_id = m.get('DefaultVpcId')
        if m.get('DefaultVswicthId') is not None:
            self.default_vswicth_id = m.get('DefaultVswicthId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderInstanceId') is not None:
            self.order_instance_id = m.get('OrderInstanceId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceGroupType') is not None:
            self.resource_group_type = m.get('ResourceGroupType')
        if m.get('Spec') is not None:
            temp_model = ListResourceGroupsResponseBodyResourceGroupListSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group_list: List[ListResourceGroupsResponseBodyResourceGroupList] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.resource_group_list = resource_group_list
        self.success = success

    def validate(self):
        if self.resource_group_list:
            for k in self.resource_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceGroupList'] = []
        if self.resource_group_list is not None:
            for k in self.resource_group_list:
                result['ResourceGroupList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_group_list = []
        if m.get('ResourceGroupList') is not None:
            for k in m.get('ResourceGroupList'):
                temp_model = ListResourceGroupsResponseBodyResourceGroupList()
                self.resource_group_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        type: str = None,
    ):
        # The ID of the Alibaba Cloud account used by the workspace administrator. You can log on to the Alibaba Cloud Management Console and view the ID on the Security Settings page.
        self.owner = owner
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The resource type. This parameter specifies a filter condition.
        # 
        # Valid values:
        # 
        # *   python
        # *   jar
        # *   archive
        # *   file
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcesResponseBodyPagingInfoResourcesDataSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the data source.
        self.name = name
        # The type of the data source.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcesResponseBodyPagingInfoResourcesScriptRuntime(TeaModel):
    def __init__(
        self,
        command: str = None,
    ):
        # The command used to distinguish file resource types.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class ListResourcesResponseBodyPagingInfoResourcesScript(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: ListResourcesResponseBodyPagingInfoResourcesScriptRuntime = None,
    ):
        # The script ID.
        self.id = id
        # The script path.
        self.path = path
        # The runtime.
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Runtime') is not None:
            temp_model = ListResourcesResponseBodyPagingInfoResourcesScriptRuntime()
            self.runtime = temp_model.from_map(m['Runtime'])
        return self


class ListResourcesResponseBodyPagingInfoResources(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        data_source: ListResourcesResponseBodyPagingInfoResourcesDataSource = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        script: ListResourcesResponseBodyPagingInfoResourcesScript = None,
        source_path: str = None,
        source_type: str = None,
        target_path: str = None,
        target_type: str = None,
        type: str = None,
    ):
        # The time when the file resource was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The information about the data source.
        self.data_source = data_source
        # The ID of the file resource.
        self.id = id
        # The times when the file resource was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the file resource.
        self.name = name
        # The owner of the file resource.
        self.owner = owner
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        self.project_id = project_id
        # The script information.
        self.script = script
        # The storage path of the source of the file resource. If the value of the SourecType parameter is local, this parameter is empty.
        self.source_path = source_path
        # The storage type of the source of the file resource.
        self.source_type = source_type
        # The storage path of the destination of the file resource.
        self.target_path = target_path
        # The storage type of the destination of the file resource.
        self.target_type = target_type
        # The type of the file resource.
        # 
        # Valid values:
        # 
        # *   jar
        # *   python
        # *   file
        # *   archive
        self.type = type

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.script:
            self.script.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.source_path is not None:
            result['SourcePath'] = self.source_path
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        if self.target_path is not None:
            result['TargetPath'] = self.target_path
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataSource') is not None:
            temp_model = ListResourcesResponseBodyPagingInfoResourcesDataSource()
            self.data_source = temp_model.from_map(m['DataSource'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Script') is not None:
            temp_model = ListResourcesResponseBodyPagingInfoResourcesScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('SourcePath') is not None:
            self.source_path = m.get('SourcePath')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        if m.get('TargetPath') is not None:
            self.target_path = m.get('TargetPath')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListResourcesResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resources: List[ListResourcesResponseBodyPagingInfoResources] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The file resources.
        self.resources = resources
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListResourcesResponseBodyPagingInfoResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListResourcesResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListResourcesResponseBodyPagingInfo = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListResourcesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoutesRequest(TeaModel):
    def __init__(
        self,
        network_id: int = None,
    ):
        # This parameter is required.
        self.network_id = network_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        return self


class ListRoutesResponseBodyRouteList(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        destination_cidr: str = None,
        id: int = None,
        network_id: int = None,
        resource_group_id: str = None,
        resource_id: str = None,
    ):
        self.create_time = create_time
        self.destination_cidr = destination_cidr
        self.id = id
        self.network_id = network_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.id is not None:
            result['Id'] = self.id
        if self.network_id is not None:
            result['NetworkId'] = self.network_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class ListRoutesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        route_list: List[ListRoutesResponseBodyRouteList] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.route_list = route_list
        self.success = success

    def validate(self):
        if self.route_list:
            for k in self.route_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RouteList'] = []
        if self.route_list is not None:
            for k in self.route_list:
                result['RouteList'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.route_list = []
        if m.get('RouteList') is not None:
            for k in m.get('RouteList'):
                temp_model = ListRoutesResponseBodyRouteList()
                self.route_list.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRoutesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRoutesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRoutesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkflowDefinitionsRequest(TeaModel):
    def __init__(
        self,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        type: str = None,
    ):
        # The ID of the Alibaba Cloud account used by the workspace administrator. You can log on to the Alibaba Cloud Management Console and view the ID on the Security Settings page.
        self.owner = owner
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The workflow type. This parameter specifies a filter condition.
        # 
        # Valid values:
        # 
        # *   CycleWorkflow
        # *   ManualWorkflow
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScriptRuntime(TeaModel):
    def __init__(
        self,
        command: str = None,
    ):
        # The command.
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        return self


class ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScript(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        runtime: ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScriptRuntime = None,
    ):
        # The script ID.
        self.id = id
        # The script path.
        self.path = path
        # The runtime.
        self.runtime = runtime

    def validate(self):
        if self.runtime:
            self.runtime.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('Runtime') is not None:
            temp_model = ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScriptRuntime()
            self.runtime = temp_model.from_map(m['Runtime'])
        return self


class ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitions(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        owner: str = None,
        project_id: str = None,
        script: ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScript = None,
        type: str = None,
    ):
        # The time when the workflow was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The description of the workflow.
        self.description = description
        # The ID of the workflow.
        self.id = id
        # The times when the workflow was last modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The name of the workflow.
        self.name = name
        # The owner.
        self.owner = owner
        # The ID of the DataWorks workspace to which the workflow belongs.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The script information.
        self.script = script
        # The type of the workflow.
        # 
        # Valid values:
        # 
        # *   CycleWorkflow
        # *   ManualWorkflow
        self.type = type

    def validate(self):
        if self.script:
            self.script.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Script') is not None:
            temp_model = ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitionsScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListWorkflowDefinitionsResponseBodyPagingInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        workflow_definitions: List[ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitions] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count
        # The workflows.
        self.workflow_definitions = workflow_definitions

    def validate(self):
        if self.workflow_definitions:
            for k in self.workflow_definitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WorkflowDefinitions'] = []
        if self.workflow_definitions is not None:
            for k in self.workflow_definitions:
                result['WorkflowDefinitions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.workflow_definitions = []
        if m.get('WorkflowDefinitions') is not None:
            for k in m.get('WorkflowDefinitions'):
                temp_model = ListWorkflowDefinitionsResponseBodyPagingInfoWorkflowDefinitions()
                self.workflow_definitions.append(temp_model.from_map(k))
        return self


class ListWorkflowDefinitionsResponseBody(TeaModel):
    def __init__(
        self,
        paging_info: ListWorkflowDefinitionsResponseBodyPagingInfo = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = ListWorkflowDefinitionsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m['PagingInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListWorkflowDefinitionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkflowDefinitionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWorkflowDefinitionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveFunctionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        project_id: str = None,
    ):
        # The ID of the UDF.
        # 
        # This parameter is required.
        self.id = id
        # The path to which you want to move the UDF. You do not need to specify a UDF name in the path.
        # 
        # For example, if you want to move the test UDF to root/demo/test, you must set this parameter to root/demo.
        # 
        # This parameter is required.
        self.path = path
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class MoveFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MoveFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveNodeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        project_id: str = None,
    ):
        # The ID of the node.
        # 
        # This parameter is required.
        self.id = id
        # The path to which you want to move the node. You do not need to specify a node name in the path.
        # 
        # For example, if you want to move the test node to root/demo/test, you must set this parameter to root/demo.
        # 
        # This parameter is required.
        self.path = path
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class MoveNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MoveNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        project_id: str = None,
    ):
        # The ID of the file resource.
        # 
        # This parameter is required.
        self.id = id
        # The path to which you want to move the file resource. You do not need to specify a file resource name in the path.
        # 
        # For example, if you want to move the test file resource to root/demo/test, you must set this parameter to root/demo.
        # 
        # This parameter is required.
        self.path = path
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class MoveResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MoveResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        path: str = None,
        project_id: str = None,
    ):
        # The ID of the workflow.
        # 
        # This parameter is required.
        self.id = id
        # The path to which you want to move the workflow. You do not need to specify a workflow name in the path.
        # 
        # For example, if you want to move the test workflow to root/demo/test, you must set this parameter to root/demo.
        # 
        # This parameter is required.
        self.path = path
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID. You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.path is not None:
            result['Path'] = self.path
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class MoveWorkflowDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MoveWorkflowDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveWorkflowDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveWorkflowDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameFunctionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        project_id: str = None,
    ):
        # The ID of the UDF.
        # 
        # This parameter is required.
        self.id = id
        # The new name.
        # 
        # This parameter is required.
        self.name = name
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class RenameFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenameFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenameFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameNodeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        project_id: str = None,
    ):
        # The ID of the node.
        # 
        # This parameter is required.
        self.id = id
        # The new name.
        # 
        # This parameter is required.
        self.name = name
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class RenameNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenameNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenameNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameResourceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        project_id: str = None,
    ):
        # The ID of the file resource.
        # 
        # This parameter is required.
        self.id = id
        # The new name.
        # 
        # This parameter is required.
        self.name = name
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class RenameResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenameResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenameResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        project_id: str = None,
    ):
        # The unique identifier of the workflow.
        # 
        # This parameter is required.
        self.id = id
        # The new name.
        # 
        # This parameter is required.
        self.name = name
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to obtain the ID. You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class RenameWorkflowDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID. You can troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenameWorkflowDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameWorkflowDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RenameWorkflowDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDIJobRequestRealtimeStartSettingsFailoverSettings(TeaModel):
    def __init__(
        self,
        interval: int = None,
        upper_limit: int = None,
    ):
        self.interval = interval
        self.upper_limit = upper_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.interval is not None:
            result['Interval'] = self.interval
        if self.upper_limit is not None:
            result['UpperLimit'] = self.upper_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')
        if m.get('UpperLimit') is not None:
            self.upper_limit = m.get('UpperLimit')
        return self


class StartDIJobRequestRealtimeStartSettings(TeaModel):
    def __init__(
        self,
        failover_settings: StartDIJobRequestRealtimeStartSettingsFailoverSettings = None,
        start_time: int = None,
    ):
        self.failover_settings = failover_settings
        self.start_time = start_time

    def validate(self):
        if self.failover_settings:
            self.failover_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failover_settings is not None:
            result['FailoverSettings'] = self.failover_settings.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailoverSettings') is not None:
            temp_model = StartDIJobRequestRealtimeStartSettingsFailoverSettings()
            self.failover_settings = temp_model.from_map(m['FailoverSettings'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class StartDIJobRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        force_to_rerun: bool = None,
        realtime_start_settings: StartDIJobRequestRealtimeStartSettings = None,
    ):
        # The instance ID.
        self.dijob_id = dijob_id
        self.force_to_rerun = force_to_rerun
        self.realtime_start_settings = realtime_start_settings

    def validate(self):
        if self.realtime_start_settings:
            self.realtime_start_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.force_to_rerun is not None:
            result['ForceToRerun'] = self.force_to_rerun
        if self.realtime_start_settings is not None:
            result['RealtimeStartSettings'] = self.realtime_start_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('ForceToRerun') is not None:
            self.force_to_rerun = m.get('ForceToRerun')
        if m.get('RealtimeStartSettings') is not None:
            temp_model = StartDIJobRequestRealtimeStartSettings()
            self.realtime_start_settings = temp_model.from_map(m['RealtimeStartSettings'])
        return self


class StartDIJobShrinkRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        force_to_rerun: bool = None,
        realtime_start_settings_shrink: str = None,
    ):
        # The instance ID.
        self.dijob_id = dijob_id
        self.force_to_rerun = force_to_rerun
        self.realtime_start_settings_shrink = realtime_start_settings_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.force_to_rerun is not None:
            result['ForceToRerun'] = self.force_to_rerun
        if self.realtime_start_settings_shrink is not None:
            result['RealtimeStartSettings'] = self.realtime_start_settings_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('ForceToRerun') is not None:
            self.force_to_rerun = m.get('ForceToRerun')
        if m.get('RealtimeStartSettings') is not None:
            self.realtime_start_settings_shrink = m.get('RealtimeStartSettings')
        return self


class StartDIJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartDIJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartDIJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartDIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDIJobRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        instance_id: int = None,
    ):
        # The ID of the synchronization task.
        self.dijob_id = dijob_id
        # The instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopDIJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopDIJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopDIJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopDIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDIAlarmRuleRequestNotificationSettingsNotificationChannels(TeaModel):
    def __init__(
        self,
        channels: List[str] = None,
        severity: str = None,
    ):
        self.channels = channels
        self.severity = severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channels is not None:
            result['Channels'] = self.channels
        if self.severity is not None:
            result['Severity'] = self.severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channels') is not None:
            self.channels = m.get('Channels')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        return self


class UpdateDIAlarmRuleRequestNotificationSettingsNotificationReceivers(TeaModel):
    def __init__(
        self,
        receiver_type: str = None,
        receiver_values: List[str] = None,
    ):
        self.receiver_type = receiver_type
        self.receiver_values = receiver_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receiver_type is not None:
            result['ReceiverType'] = self.receiver_type
        if self.receiver_values is not None:
            result['ReceiverValues'] = self.receiver_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverType') is not None:
            self.receiver_type = m.get('ReceiverType')
        if m.get('ReceiverValues') is not None:
            self.receiver_values = m.get('ReceiverValues')
        return self


class UpdateDIAlarmRuleRequestNotificationSettings(TeaModel):
    def __init__(
        self,
        inhibition_interval: int = None,
        notification_channels: List[UpdateDIAlarmRuleRequestNotificationSettingsNotificationChannels] = None,
        notification_receivers: List[UpdateDIAlarmRuleRequestNotificationSettingsNotificationReceivers] = None,
    ):
        self.inhibition_interval = inhibition_interval
        self.notification_channels = notification_channels
        self.notification_receivers = notification_receivers

    def validate(self):
        if self.notification_channels:
            for k in self.notification_channels:
                if k:
                    k.validate()
        if self.notification_receivers:
            for k in self.notification_receivers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.inhibition_interval is not None:
            result['InhibitionInterval'] = self.inhibition_interval
        result['NotificationChannels'] = []
        if self.notification_channels is not None:
            for k in self.notification_channels:
                result['NotificationChannels'].append(k.to_map() if k else None)
        result['NotificationReceivers'] = []
        if self.notification_receivers is not None:
            for k in self.notification_receivers:
                result['NotificationReceivers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InhibitionInterval') is not None:
            self.inhibition_interval = m.get('InhibitionInterval')
        self.notification_channels = []
        if m.get('NotificationChannels') is not None:
            for k in m.get('NotificationChannels'):
                temp_model = UpdateDIAlarmRuleRequestNotificationSettingsNotificationChannels()
                self.notification_channels.append(temp_model.from_map(k))
        self.notification_receivers = []
        if m.get('NotificationReceivers') is not None:
            for k in m.get('NotificationReceivers'):
                temp_model = UpdateDIAlarmRuleRequestNotificationSettingsNotificationReceivers()
                self.notification_receivers.append(temp_model.from_map(k))
        return self


class UpdateDIAlarmRuleRequestTriggerConditions(TeaModel):
    def __init__(
        self,
        ddl_report_tags: List[str] = None,
        duration: int = None,
        severity: str = None,
        threshold: int = None,
    ):
        self.ddl_report_tags = ddl_report_tags
        self.duration = duration
        self.severity = severity
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ddl_report_tags is not None:
            result['DdlReportTags'] = self.ddl_report_tags
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DdlReportTags') is not None:
            self.ddl_report_tags = m.get('DdlReportTags')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class UpdateDIAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        dialarm_rule_id: int = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        name: str = None,
        notification_settings: UpdateDIAlarmRuleRequestNotificationSettings = None,
        trigger_conditions: List[UpdateDIAlarmRuleRequestTriggerConditions] = None,
    ):
        # This parameter is required.
        self.dialarm_rule_id = dialarm_rule_id
        self.dijob_id = dijob_id
        self.description = description
        self.enabled = enabled
        self.metric_type = metric_type
        self.name = name
        self.notification_settings = notification_settings
        self.trigger_conditions = trigger_conditions

    def validate(self):
        if self.notification_settings:
            self.notification_settings.validate()
        if self.trigger_conditions:
            for k in self.trigger_conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.notification_settings is not None:
            result['NotificationSettings'] = self.notification_settings.to_map()
        result['TriggerConditions'] = []
        if self.trigger_conditions is not None:
            for k in self.trigger_conditions:
                result['TriggerConditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotificationSettings') is not None:
            temp_model = UpdateDIAlarmRuleRequestNotificationSettings()
            self.notification_settings = temp_model.from_map(m['NotificationSettings'])
        self.trigger_conditions = []
        if m.get('TriggerConditions') is not None:
            for k in m.get('TriggerConditions'):
                temp_model = UpdateDIAlarmRuleRequestTriggerConditions()
                self.trigger_conditions.append(temp_model.from_map(k))
        return self


class UpdateDIAlarmRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        dialarm_rule_id: int = None,
        dijob_id: int = None,
        description: str = None,
        enabled: bool = None,
        metric_type: str = None,
        name: str = None,
        notification_settings_shrink: str = None,
        trigger_conditions_shrink: str = None,
    ):
        # This parameter is required.
        self.dialarm_rule_id = dialarm_rule_id
        self.dijob_id = dijob_id
        self.description = description
        self.enabled = enabled
        self.metric_type = metric_type
        self.name = name
        self.notification_settings_shrink = notification_settings_shrink
        self.trigger_conditions_shrink = trigger_conditions_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialarm_rule_id is not None:
            result['DIAlarmRuleId'] = self.dialarm_rule_id
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.description is not None:
            result['Description'] = self.description
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.name is not None:
            result['Name'] = self.name
        if self.notification_settings_shrink is not None:
            result['NotificationSettings'] = self.notification_settings_shrink
        if self.trigger_conditions_shrink is not None:
            result['TriggerConditions'] = self.trigger_conditions_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIAlarmRuleId') is not None:
            self.dialarm_rule_id = m.get('DIAlarmRuleId')
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NotificationSettings') is not None:
            self.notification_settings_shrink = m.get('NotificationSettings')
        if m.get('TriggerConditions') is not None:
            self.trigger_conditions_shrink = m.get('TriggerConditions')
        return self


class UpdateDIAlarmRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDIAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDIAlarmRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDIAlarmRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDIJobRequestJobSettingsColumnDataTypeSettings(TeaModel):
    def __init__(
        self,
        destination_data_type: str = None,
        source_data_type: str = None,
    ):
        self.destination_data_type = destination_data_type
        self.source_data_type = source_data_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_data_type is not None:
            result['DestinationDataType'] = self.destination_data_type
        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDataType') is not None:
            self.destination_data_type = m.get('DestinationDataType')
        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')
        return self


class UpdateDIJobRequestJobSettingsCycleScheduleSettings(TeaModel):
    def __init__(
        self,
        schedule_parameters: str = None,
    ):
        self.schedule_parameters = schedule_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schedule_parameters is not None:
            result['ScheduleParameters'] = self.schedule_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleParameters') is not None:
            self.schedule_parameters = m.get('ScheduleParameters')
        return self


class UpdateDIJobRequestJobSettingsDdlHandlingSettings(TeaModel):
    def __init__(
        self,
        action: str = None,
        type: str = None,
    ):
        self.action = action
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateDIJobRequestJobSettingsRuntimeSettings(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateDIJobRequestJobSettings(TeaModel):
    def __init__(
        self,
        channel_settings: str = None,
        column_data_type_settings: List[UpdateDIJobRequestJobSettingsColumnDataTypeSettings] = None,
        cycle_schedule_settings: UpdateDIJobRequestJobSettingsCycleScheduleSettings = None,
        ddl_handling_settings: List[UpdateDIJobRequestJobSettingsDdlHandlingSettings] = None,
        runtime_settings: List[UpdateDIJobRequestJobSettingsRuntimeSettings] = None,
    ):
        self.channel_settings = channel_settings
        self.column_data_type_settings = column_data_type_settings
        self.cycle_schedule_settings = cycle_schedule_settings
        self.ddl_handling_settings = ddl_handling_settings
        self.runtime_settings = runtime_settings

    def validate(self):
        if self.column_data_type_settings:
            for k in self.column_data_type_settings:
                if k:
                    k.validate()
        if self.cycle_schedule_settings:
            self.cycle_schedule_settings.validate()
        if self.ddl_handling_settings:
            for k in self.ddl_handling_settings:
                if k:
                    k.validate()
        if self.runtime_settings:
            for k in self.runtime_settings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_settings is not None:
            result['ChannelSettings'] = self.channel_settings
        result['ColumnDataTypeSettings'] = []
        if self.column_data_type_settings is not None:
            for k in self.column_data_type_settings:
                result['ColumnDataTypeSettings'].append(k.to_map() if k else None)
        if self.cycle_schedule_settings is not None:
            result['CycleScheduleSettings'] = self.cycle_schedule_settings.to_map()
        result['DdlHandlingSettings'] = []
        if self.ddl_handling_settings is not None:
            for k in self.ddl_handling_settings:
                result['DdlHandlingSettings'].append(k.to_map() if k else None)
        result['RuntimeSettings'] = []
        if self.runtime_settings is not None:
            for k in self.runtime_settings:
                result['RuntimeSettings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelSettings') is not None:
            self.channel_settings = m.get('ChannelSettings')
        self.column_data_type_settings = []
        if m.get('ColumnDataTypeSettings') is not None:
            for k in m.get('ColumnDataTypeSettings'):
                temp_model = UpdateDIJobRequestJobSettingsColumnDataTypeSettings()
                self.column_data_type_settings.append(temp_model.from_map(k))
        if m.get('CycleScheduleSettings') is not None:
            temp_model = UpdateDIJobRequestJobSettingsCycleScheduleSettings()
            self.cycle_schedule_settings = temp_model.from_map(m['CycleScheduleSettings'])
        self.ddl_handling_settings = []
        if m.get('DdlHandlingSettings') is not None:
            for k in m.get('DdlHandlingSettings'):
                temp_model = UpdateDIJobRequestJobSettingsDdlHandlingSettings()
                self.ddl_handling_settings.append(temp_model.from_map(k))
        self.runtime_settings = []
        if m.get('RuntimeSettings') is not None:
            for k in m.get('RuntimeSettings'):
                temp_model = UpdateDIJobRequestJobSettingsRuntimeSettings()
                self.runtime_settings.append(temp_model.from_map(k))
        return self


class UpdateDIJobRequestResourceSettingsOfflineResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: int = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class UpdateDIJobRequestResourceSettingsRealtimeResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: int = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class UpdateDIJobRequestResourceSettingsScheduleResourceSettings(TeaModel):
    def __init__(
        self,
        requested_cu: int = None,
        resource_group_identifier: str = None,
    ):
        self.requested_cu = requested_cu
        self.resource_group_identifier = resource_group_identifier

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.requested_cu is not None:
            result['RequestedCu'] = self.requested_cu
        if self.resource_group_identifier is not None:
            result['ResourceGroupIdentifier'] = self.resource_group_identifier
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestedCu') is not None:
            self.requested_cu = m.get('RequestedCu')
        if m.get('ResourceGroupIdentifier') is not None:
            self.resource_group_identifier = m.get('ResourceGroupIdentifier')
        return self


class UpdateDIJobRequestResourceSettings(TeaModel):
    def __init__(
        self,
        offline_resource_settings: UpdateDIJobRequestResourceSettingsOfflineResourceSettings = None,
        realtime_resource_settings: UpdateDIJobRequestResourceSettingsRealtimeResourceSettings = None,
        schedule_resource_settings: UpdateDIJobRequestResourceSettingsScheduleResourceSettings = None,
    ):
        self.offline_resource_settings = offline_resource_settings
        self.realtime_resource_settings = realtime_resource_settings
        self.schedule_resource_settings = schedule_resource_settings

    def validate(self):
        if self.offline_resource_settings:
            self.offline_resource_settings.validate()
        if self.realtime_resource_settings:
            self.realtime_resource_settings.validate()
        if self.schedule_resource_settings:
            self.schedule_resource_settings.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offline_resource_settings is not None:
            result['OfflineResourceSettings'] = self.offline_resource_settings.to_map()
        if self.realtime_resource_settings is not None:
            result['RealtimeResourceSettings'] = self.realtime_resource_settings.to_map()
        if self.schedule_resource_settings is not None:
            result['ScheduleResourceSettings'] = self.schedule_resource_settings.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfflineResourceSettings') is not None:
            temp_model = UpdateDIJobRequestResourceSettingsOfflineResourceSettings()
            self.offline_resource_settings = temp_model.from_map(m['OfflineResourceSettings'])
        if m.get('RealtimeResourceSettings') is not None:
            temp_model = UpdateDIJobRequestResourceSettingsRealtimeResourceSettings()
            self.realtime_resource_settings = temp_model.from_map(m['RealtimeResourceSettings'])
        if m.get('ScheduleResourceSettings') is not None:
            temp_model = UpdateDIJobRequestResourceSettingsScheduleResourceSettings()
            self.schedule_resource_settings = temp_model.from_map(m['ScheduleResourceSettings'])
        return self


class UpdateDIJobRequestTableMappingsSourceObjectSelectionRules(TeaModel):
    def __init__(
        self,
        action: str = None,
        expression: str = None,
        expression_type: str = None,
        object_type: str = None,
    ):
        self.action = action
        self.expression = expression
        self.expression_type = expression_type
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.expression_type is not None:
            result['ExpressionType'] = self.expression_type
        if self.object_type is not None:
            result['ObjectType'] = self.object_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('ExpressionType') is not None:
            self.expression_type = m.get('ExpressionType')
        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')
        return self


class UpdateDIJobRequestTableMappingsTransformationRules(TeaModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        self.rule_action_type = rule_action_type
        self.rule_name = rule_name
        self.rule_target_type = rule_target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_target_type is not None:
            result['RuleTargetType'] = self.rule_target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleTargetType') is not None:
            self.rule_target_type = m.get('RuleTargetType')
        return self


class UpdateDIJobRequestTableMappings(TeaModel):
    def __init__(
        self,
        source_object_selection_rules: List[UpdateDIJobRequestTableMappingsSourceObjectSelectionRules] = None,
        transformation_rules: List[UpdateDIJobRequestTableMappingsTransformationRules] = None,
    ):
        self.source_object_selection_rules = source_object_selection_rules
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.source_object_selection_rules:
            for k in self.source_object_selection_rules:
                if k:
                    k.validate()
        if self.transformation_rules:
            for k in self.transformation_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SourceObjectSelectionRules'] = []
        if self.source_object_selection_rules is not None:
            for k in self.source_object_selection_rules:
                result['SourceObjectSelectionRules'].append(k.to_map() if k else None)
        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k in self.transformation_rules:
                result['TransformationRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.source_object_selection_rules = []
        if m.get('SourceObjectSelectionRules') is not None:
            for k in m.get('SourceObjectSelectionRules'):
                temp_model = UpdateDIJobRequestTableMappingsSourceObjectSelectionRules()
                self.source_object_selection_rules.append(temp_model.from_map(k))
        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k in m.get('TransformationRules'):
                temp_model = UpdateDIJobRequestTableMappingsTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k))
        return self


class UpdateDIJobRequestTransformationRules(TeaModel):
    def __init__(
        self,
        rule_action_type: str = None,
        rule_expression: str = None,
        rule_name: str = None,
        rule_target_type: str = None,
    ):
        self.rule_action_type = rule_action_type
        self.rule_expression = rule_expression
        self.rule_name = rule_name
        self.rule_target_type = rule_target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type
        if self.rule_expression is not None:
            result['RuleExpression'] = self.rule_expression
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.rule_target_type is not None:
            result['RuleTargetType'] = self.rule_target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')
        if m.get('RuleExpression') is not None:
            self.rule_expression = m.get('RuleExpression')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('RuleTargetType') is not None:
            self.rule_target_type = m.get('RuleTargetType')
        return self


class UpdateDIJobRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        description: str = None,
        job_settings: UpdateDIJobRequestJobSettings = None,
        project_id: int = None,
        resource_settings: UpdateDIJobRequestResourceSettings = None,
        table_mappings: List[UpdateDIJobRequestTableMappings] = None,
        transformation_rules: List[UpdateDIJobRequestTransformationRules] = None,
    ):
        # This parameter is required.
        self.dijob_id = dijob_id
        self.description = description
        self.job_settings = job_settings
        self.project_id = project_id
        self.resource_settings = resource_settings
        self.table_mappings = table_mappings
        self.transformation_rules = transformation_rules

    def validate(self):
        if self.job_settings:
            self.job_settings.validate()
        if self.resource_settings:
            self.resource_settings.validate()
        if self.table_mappings:
            for k in self.table_mappings:
                if k:
                    k.validate()
        if self.transformation_rules:
            for k in self.transformation_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.description is not None:
            result['Description'] = self.description
        if self.job_settings is not None:
            result['JobSettings'] = self.job_settings.to_map()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_settings is not None:
            result['ResourceSettings'] = self.resource_settings.to_map()
        result['TableMappings'] = []
        if self.table_mappings is not None:
            for k in self.table_mappings:
                result['TableMappings'].append(k.to_map() if k else None)
        result['TransformationRules'] = []
        if self.transformation_rules is not None:
            for k in self.transformation_rules:
                result['TransformationRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobSettings') is not None:
            temp_model = UpdateDIJobRequestJobSettings()
            self.job_settings = temp_model.from_map(m['JobSettings'])
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceSettings') is not None:
            temp_model = UpdateDIJobRequestResourceSettings()
            self.resource_settings = temp_model.from_map(m['ResourceSettings'])
        self.table_mappings = []
        if m.get('TableMappings') is not None:
            for k in m.get('TableMappings'):
                temp_model = UpdateDIJobRequestTableMappings()
                self.table_mappings.append(temp_model.from_map(k))
        self.transformation_rules = []
        if m.get('TransformationRules') is not None:
            for k in m.get('TransformationRules'):
                temp_model = UpdateDIJobRequestTransformationRules()
                self.transformation_rules.append(temp_model.from_map(k))
        return self


class UpdateDIJobShrinkRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
        description: str = None,
        job_settings_shrink: str = None,
        project_id: int = None,
        resource_settings_shrink: str = None,
        table_mappings_shrink: str = None,
        transformation_rules_shrink: str = None,
    ):
        # This parameter is required.
        self.dijob_id = dijob_id
        self.description = description
        self.job_settings_shrink = job_settings_shrink
        self.project_id = project_id
        self.resource_settings_shrink = resource_settings_shrink
        self.table_mappings_shrink = table_mappings_shrink
        self.transformation_rules_shrink = transformation_rules_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        if self.description is not None:
            result['Description'] = self.description
        if self.job_settings_shrink is not None:
            result['JobSettings'] = self.job_settings_shrink
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_settings_shrink is not None:
            result['ResourceSettings'] = self.resource_settings_shrink
        if self.table_mappings_shrink is not None:
            result['TableMappings'] = self.table_mappings_shrink
        if self.transformation_rules_shrink is not None:
            result['TransformationRules'] = self.transformation_rules_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JobSettings') is not None:
            self.job_settings_shrink = m.get('JobSettings')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceSettings') is not None:
            self.resource_settings_shrink = m.get('ResourceSettings')
        if m.get('TableMappings') is not None:
            self.table_mappings_shrink = m.get('TableMappings')
        if m.get('TransformationRules') is not None:
            self.transformation_rules_shrink = m.get('TransformationRules')
        return self


class UpdateDIJobResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDIJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDIJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDIJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDataSourceRequest(TeaModel):
    def __init__(
        self,
        connection_properties: str = None,
        connection_properties_mode: str = None,
        description: str = None,
        id: int = None,
        project_id: int = None,
    ):
        # This parameter is required.
        self.connection_properties = connection_properties
        self.connection_properties_mode = connection_properties_mode
        self.description = description
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_properties is not None:
            result['ConnectionProperties'] = self.connection_properties
        if self.connection_properties_mode is not None:
            result['ConnectionPropertiesMode'] = self.connection_properties_mode
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionProperties') is not None:
            self.connection_properties = m.get('ConnectionProperties')
        if m.get('ConnectionPropertiesMode') is not None:
            self.connection_properties_mode = m.get('ConnectionPropertiesMode')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class UpdateDataSourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateDataSourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDataSourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDataSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # The ID of the UDF.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec field information about the UDF. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class UpdateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # true
        # 
        # false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFunctionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNodeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # The ID of the node.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec field information about the node. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class UpdateNodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        dev_environment_enabled: bool = None,
        dev_role_disabled: bool = None,
        display_name: str = None,
        id: int = None,
        pai_task_enabled: bool = None,
        status: str = None,
    ):
        self.description = description
        self.dev_environment_enabled = dev_environment_enabled
        self.dev_role_disabled = dev_role_disabled
        self.display_name = display_name
        # This parameter is required.
        self.id = id
        self.pai_task_enabled = pai_task_enabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dev_environment_enabled is not None:
            result['DevEnvironmentEnabled'] = self.dev_environment_enabled
        if self.dev_role_disabled is not None:
            result['DevRoleDisabled'] = self.dev_role_disabled
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.pai_task_enabled is not None:
            result['PaiTaskEnabled'] = self.pai_task_enabled
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DevEnvironmentEnabled') is not None:
            self.dev_environment_enabled = m.get('DevEnvironmentEnabled')
        if m.get('DevRoleDisabled') is not None:
            self.dev_role_disabled = m.get('DevRoleDisabled')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PaiTaskEnabled') is not None:
            self.pai_task_enabled = m.get('PaiTaskEnabled')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # The ID of the file resource.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec field information about the file resource. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class UpdateResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceGroupRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        remark: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.name = name
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRouteRequest(TeaModel):
    def __init__(
        self,
        destination_cidr: str = None,
        id: int = None,
    ):
        # This parameter is required.
        self.destination_cidr = destination_cidr
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class UpdateRouteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRouteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRouteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # The ID of the workflow.
        # 
        # This parameter is required.
        self.id = id
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The FlowSpec field information about the workflow. For more information, see [FlowSpec](https://github.com/aliyun/dataworks-spec/blob/master/README_zh_CN.md).
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.spec is not None:
            result['Spec'] = self.spec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Spec') is not None:
            self.spec = m.get('Spec')
        return self


class UpdateWorkflowDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateWorkflowDefinitionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkflowDefinitionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWorkflowDefinitionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


