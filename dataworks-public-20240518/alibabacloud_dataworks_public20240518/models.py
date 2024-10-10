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
        self.description = description
        # This parameter is required.
        self.object_ids = object_ids
        # 项目Id
        # 
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
        self.description = description
        # This parameter is required.
        self.object_ids_shrink = object_ids_shrink
        # 项目Id
        # 
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


class CreateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
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


class CreateNodeRequest(TeaModel):
    def __init__(
        self,
        container_id: str = None,
        project_id: str = None,
        scene: str = None,
        spec: str = None,
    ):
        self.container_id = container_id
        # This parameter is required.
        self.project_id = project_id
        # This parameter is required.
        self.scene = scene
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
        # This parameter is required.
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
        # This parameter is required.
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
        # 资源文件的项目id
        # 
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


class CreateResourceResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
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


class CreateWorkflowDefinitionRequest(TeaModel):
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


class CreateWorkflowDefinitionResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
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


class DeleteDIJobRequest(TeaModel):
    def __init__(
        self,
        dijob_id: int = None,
    ):
        # This parameter is required.
        self.dijob_id = dijob_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
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


class DeleteNodeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
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


class DeleteWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
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


class ExecDeploymentStageRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        id: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.code = code
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
        dijob_id: str = None,
        with_details: bool = None,
    ):
        # This parameter is required.
        self.dijob_id = dijob_id
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
        if self.with_details is not None:
            result['WithDetails'] = self.with_details
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')
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
        # This parameter is required.
        self.dijob_id = dijob_id
        self.failover_id = failover_id
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
        # 代表资源一级ID的资源属性字段
        self.log = log
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
        # 阶段代号
        self.code = code
        # 阶段描述
        self.description = description
        self.detail = detail
        # 阶段信息
        self.message = message
        # 阶段名称
        self.name = name
        # 阶段状态
        self.status = status
        # 步骤
        self.step = step
        # 阶段类型
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
        # 发布包创建时间戳
        self.create_time = create_time
        # 创建人
        self.creator = creator
        # 发布流程Id
        self.id = id
        self.message = message
        # 修改时间
        self.modify_time = modify_time
        self.project_id = project_id
        # 步骤详情
        self.stages = stages
        # 发布流程状态
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
        self.pipeline = pipeline
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
        # This parameter is required.
        self.id = id
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
        self.create_time = create_time
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.project_id = project_id
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
        self.function = function
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


class GetNodeRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.id = id
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
        self.create_time = create_time
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.project_id = project_id
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
        self.node = node
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


class GetResourceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.id = id
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
        self.create_time = create_time
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.project_id = project_id
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
        self.request_id = request_id
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


class GetWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.id = id
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
        self.create_time = create_time
        self.id = id
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.project_id = project_id
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
        self.request_id = request_id
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


class ListDIJobEventsRequest(TeaModel):
    def __init__(
        self,
        dijob_id: str = None,
        end_time: int = None,
        event_type: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # This parameter is required.
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
        dijob_id: str = None,
        end_time: int = None,
        metric_name: List[str] = None,
        start_time: int = None,
    ):
        # This parameter is required.
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
        dijob_id: str = None,
        end_time: int = None,
        metric_name_shrink: str = None,
        start_time: int = None,
    ):
        # This parameter is required.
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
        self.destination_data_source_type = destination_data_source_type
        self.migration_type = migration_type
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
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
        self.dijob_id = dijob_id
        self.destination_data_source_type = destination_data_source_type
        self.job_name = job_name
        self.job_status = job_status
        self.migration_type = migration_type
        self.project_id = project_id
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
        self.dijobs = dijobs
        self.page_number = page_number
        self.page_size = page_size
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
        self.paging_info = paging_info
        # Id of the request
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
        self.creator = creator
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
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
        # 阶段代号
        self.code = code
        # 阶段描述
        self.description = description
        # 阶段详细信息
        self.detail = detail
        # 阶段信息
        self.message = message
        # 阶段名称
        self.name = name
        # 阶段状态
        self.status = status
        # 步骤
        self.step = step
        # 阶段类型
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
        # 发布包创建时间戳
        self.create_time = create_time
        # 创建人
        self.creator = creator
        # 发布流程Id
        self.id = id
        self.message = message
        # 修改时间
        self.modify_time = modify_time
        # 项目Id
        self.project_id = project_id
        # 步骤详情
        self.stages = stages
        # 发布流程状态
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
        self.deployments = deployments
        self.page_number = page_number
        self.page_size = page_size
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
        self.owner = owner
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
        # 数据源名称
        self.name = name
        # 数据源类型
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
        # 运行时资源组Id
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
        # 脚本所属类型
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
        # 脚本的id
        self.id = id
        # 脚本路径
        self.path = path
        # 脚本的运行时信息
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
        # ARM集群资源文件列表
        self.arm_resource = arm_resource
        # 函数实现类名
        self.class_name = class_name
        # 命令描述
        self.command_description = command_description
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 函数注册到的数据源信息
        self.data_source = data_source
        # 数据库名，可选
        self.database_name = database_name
        # 对funciotn的描述
        self.description = description
        # 嵌套函数代码内容
        self.embedded_code = embedded_code
        # 嵌套代码类型
        self.embedded_code_type = embedded_code_type
        # 嵌套资源类型
        self.embedded_resource_type = embedded_resource_type
        # 示例说明
        self.example_description = example_description
        # 函数的实现代码
        self.file_resource = file_resource
        # 代表资源一级ID的资源属性字段
        self.id = id
        # 修改时间
        self.modify_time = modify_time
        # 代表资源名称的资源属性字段
        self.name = name
        # 函数责任人
        self.owner = owner
        # 命令描述
        self.parameter_description = parameter_description
        # 项目Id
        self.project_id = project_id
        # 返回值说明
        self.return_value_description = return_value_description
        # 运行时资源组信息
        self.runtime_resource = runtime_resource
        # 工作流的脚本信息
        self.script = script
        # 函数类型
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
        self.functions = functions
        self.page_number = page_number
        self.page_size = page_size
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


class ListNodeDependenciesRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
    ):
        # This parameter is required.
        self.id = id
        self.page_number = page_number
        self.page_size = page_size
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
        # 数据源名称
        self.name = name
        # 数据源类型
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
        # 节点输出
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
        # 表id
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
        # 节点输出
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
        # 制品类型
        self.artifact_type = artifact_type
        # 变量id
        self.id = id
        # 变量名
        self.name = name
        # 变量所属节点
        self.node = node
        # 范围
        self.scope = scope
        # 类型
        self.type = type
        # 变量值
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
        # 节点输出列表
        self.node_outputs = node_outputs
        # 表列表
        self.tables = tables
        # 变量列表
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
        # 节点输出
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
        # 表id
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
        # 节点输出
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
        # 制品类型
        self.artifact_type = artifact_type
        # 变量id
        self.id = id
        # 变量名
        self.name = name
        # 变量所属节点
        self.node = node
        # 范围
        self.scope = scope
        # 类型
        self.type = type
        # 变量值
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
        # 节点输出列表
        self.node_outputs = node_outputs
        # 表列表
        self.tables = tables
        # 变量列表
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
        # 资源组id
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
        # 脚本所属类型
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
        # 脚本的id
        self.id = id
        # 脚本路径
        self.path = path
        # 脚本的运行时信息
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
        # 生成实例的模式
        self.instance_mode = instance_mode
        # 重试时间间隔
        self.rerun_interval = rerun_interval
        # 允许重跑的模式
        self.rerun_mode = rerun_mode
        # 重试次数
        self.rerun_times = rerun_times
        # 超时时间
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
        # 标签键
        self.key = key
        # 标签值
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
        # 触发器的cron表达式
        self.cron = cron
        # 结束时间，格式为yyyy-MM-dd HH:mm:ss
        self.end_time = end_time
        # 触发器id
        self.id = id
        # 开始时间，格式为yyyy-MM-dd HH:mm:ss
        self.start_time = start_time
        # 时区
        self.timezone = timezone
        # 触发器类型
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
        # 节点的创建时间
        self.create_time = create_time
        # 数据源信息
        self.data_source = data_source
        # 描述
        self.description = description
        self.id = id
        # 节点输入
        self.inputs = inputs
        # 属性修改时间
        self.modify_time = modify_time
        # 节点名
        self.name = name
        # 节点输出
        self.outputs = outputs
        # 节点的责任人
        self.owner = owner
        self.project_id = project_id
        self.recurrence = recurrence
        # 资源组信息
        self.runtime_resource = runtime_resource
        # 工作流的脚本信息
        self.script = script
        # 调度策略
        self.strategy = strategy
        # 标签信息
        self.tags = tags
        # 调度任务Id
        self.task_id = task_id
        # 触发器信息
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
        self.nodes = nodes
        self.page_number = page_number
        self.page_size = page_size
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
        rerun_mode: str = None,
        rerurrence: str = None,
        scene: str = None,
    ):
        self.container_id = container_id
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.project_id = project_id
        self.rerun_mode = rerun_mode
        self.rerurrence = rerurrence
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
        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode
        if self.rerurrence is not None:
            result['Rerurrence'] = self.rerurrence
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
        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')
        if m.get('Rerurrence') is not None:
            self.rerurrence = m.get('Rerurrence')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ListNodesResponseBodyPagingInfoNodesDataSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # 数据源名称
        self.name = name
        # 数据源类型
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
        # 节点输出
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
        # 表id
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
        # 节点输出
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
        # 制品类型
        self.artifact_type = artifact_type
        # 变量id
        self.id = id
        # 变量名
        self.name = name
        # 变量所属节点
        self.node = node
        # 范围
        self.scope = scope
        # 类型
        self.type = type
        # 变量值
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
        # 节点输出列表
        self.node_outputs = node_outputs
        # 表列表
        self.tables = tables
        # 变量列表
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
        # 节点输出
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
        # 表id
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
        # 节点输出
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
        # 制品类型
        self.artifact_type = artifact_type
        # 变量id
        self.id = id
        # 变量名
        self.name = name
        # 变量所属节点
        self.node = node
        # 范围
        self.scope = scope
        # 类型
        self.type = type
        # 变量值
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
        # 节点输出列表
        self.node_outputs = node_outputs
        # 表列表
        self.tables = tables
        # 变量列表
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
        # 资源组id
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
        # 脚本所属类型
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
        # 脚本的id
        self.id = id
        # 脚本路径
        self.path = path
        # 脚本的运行时信息
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
        # 生成实例的模式
        self.instance_mode = instance_mode
        # 重试时间间隔
        self.rerun_interval = rerun_interval
        # 允许重跑的模式
        self.rerun_mode = rerun_mode
        # 重试次数
        self.rerun_times = rerun_times
        # 超时时间
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
        # 标签键
        self.key = key
        # 标签值
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
        # 触发器的cron表达式
        self.cron = cron
        # 结束时间，格式为yyyy-MM-dd HH:mm:ss
        self.end_time = end_time
        # 触发器id
        self.id = id
        # 开始时间，格式为yyyy-MM-dd HH:mm:ss
        self.start_time = start_time
        # 时区
        self.timezone = timezone
        # 触发器类型
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
        # 节点的创建时间
        self.create_time = create_time
        # 数据源信息
        self.data_source = data_source
        # 描述
        self.description = description
        self.id = id
        # 节点输入
        self.inputs = inputs
        # 属性修改时间
        self.modify_time = modify_time
        # 节点名
        self.name = name
        # 节点输出
        self.outputs = outputs
        # 节点的责任人
        self.owner = owner
        self.project_id = project_id
        self.recurrence = recurrence
        # 资源组信息
        self.runtime_resource = runtime_resource
        # 工作流的脚本信息
        self.script = script
        # 调度策略
        self.strategy = strategy
        # 标签信息
        self.tags = tags
        # 调度任务Id
        self.task_id = task_id
        # 触发器信息
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
        self.nodes = nodes
        self.page_number = page_number
        self.page_size = page_size
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


class ListResourcesRequest(TeaModel):
    def __init__(
        self,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        type: str = None,
    ):
        self.owner = owner
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
        # 数据源名称
        self.name = name
        # 数据源类型
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
        # 脚本所属类型
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
        # 工作流脚本的id
        self.id = id
        # 工作流的脚本路径
        self.path = path
        # 脚本的运行时信息
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
        self.create_time = create_time
        # 函数注册到的数据源信息
        self.data_source = data_source
        # 代表资源组的资源属性字段
        self.id = id
        # 资源文件的最近修改时间
        self.modify_time = modify_time
        # 代表资源名称的资源属性字段
        self.name = name
        # 资源文件的责任人
        self.owner = owner
        # 资源文件的项目id
        self.project_id = project_id
        # 工作流的脚本信息
        self.script = script
        # 文件目标存储路径
        self.source_path = source_path
        # 文件资源来源存储类型
        self.source_type = source_type
        # 文件来源路径
        self.target_path = target_path
        # 文件目标存储类型
        self.target_type = target_type
        # 资源类型
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
        self.page_number = page_number
        self.page_size = page_size
        self.resources = resources
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


class ListWorkflowDefinitionsRequest(TeaModel):
    def __init__(
        self,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        type: str = None,
    ):
        self.owner = owner
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
        # 脚本所属类型
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
        # 工作流脚本的id
        self.id = id
        # 工作流的脚本路径
        self.path = path
        # 脚本的运行时信息
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
        # 工作流的创建时间
        self.create_time = create_time
        # 工作流的描述
        self.description = description
        # 工作流定义的唯一ID
        self.id = id
        # 工作流的最近修改时间
        self.modify_time = modify_time
        # 工作流的名称
        self.name = name
        # 工作流的责任人
        self.owner = owner
        # 工作流定义的所属项目空间
        # 
        # This parameter is required.
        self.project_id = project_id
        # 工作流的脚本信息
        self.script = script
        # 工作流类型，可选值：CycleWorkflow、ManualWorkflow，分别表示周期工作流和手动工作流
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
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
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
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.path = path
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
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.path = path
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
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.path = path
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
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.path = path
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
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name
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
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name
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
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name
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
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name
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
        dijob_id: str = None,
        force_to_rerun: bool = None,
        realtime_start_settings: StartDIJobRequestRealtimeStartSettings = None,
    ):
        # This parameter is required.
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
        dijob_id: str = None,
        force_to_rerun: bool = None,
        realtime_start_settings_shrink: str = None,
    ):
        # This parameter is required.
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
        resource_settings: UpdateDIJobRequestResourceSettings = None,
        table_mappings: List[UpdateDIJobRequestTableMappings] = None,
        transformation_rules: List[UpdateDIJobRequestTransformationRules] = None,
    ):
        # This parameter is required.
        self.dijob_id = dijob_id
        self.description = description
        self.job_settings = job_settings
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
        resource_settings_shrink: str = None,
        table_mappings_shrink: str = None,
        transformation_rules_shrink: str = None,
    ):
        # This parameter is required.
        self.dijob_id = dijob_id
        self.description = description
        self.job_settings_shrink = job_settings_shrink
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
        # This parameter is required.
        self.id = id
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
        # This parameter is required.
        self.id = id
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
        # This parameter is required.
        self.id = id
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


class UpdateWorkflowDefinitionRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        project_id: str = None,
        spec: str = None,
    ):
        # This parameter is required.
        self.id = id
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


