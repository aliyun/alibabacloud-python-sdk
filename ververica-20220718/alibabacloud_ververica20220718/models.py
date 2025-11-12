# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class MetadataInfo(TeaModel):
    def __init__(
        self,
        key: str = None,
        virtual: bool = None,
    ):
        self.key = key
        self.virtual = virtual

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.virtual is not None:
            result['virtual'] = self.virtual
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('virtual') is not None:
            self.virtual = m.get('virtual')
        return self


class TableColumn(TeaModel):
    def __init__(
        self,
        expression: str = None,
        logical_type: str = None,
        metadata_info: MetadataInfo = None,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        self.expression = expression
        self.logical_type = logical_type
        self.metadata_info = metadata_info
        # This parameter is required.
        self.name = name
        self.nullable = nullable
        self.type = type

    def validate(self):
        if self.metadata_info:
            self.metadata_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['expression'] = self.expression
        if self.logical_type is not None:
            result['logicalType'] = self.logical_type
        if self.metadata_info is not None:
            result['metadataInfo'] = self.metadata_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expression') is not None:
            self.expression = m.get('expression')
        if m.get('logicalType') is not None:
            self.logical_type = m.get('logicalType')
        if m.get('metadataInfo') is not None:
            temp_model = MetadataInfo()
            self.metadata_info = temp_model.from_map(m['metadataInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class PrimaryKey(TeaModel):
    def __init__(
        self,
        columns: List[str] = None,
        constraint_name: str = None,
        constraint_type: str = None,
        enforced: bool = None,
    ):
        # This parameter is required.
        self.columns = columns
        # This parameter is required.
        self.constraint_name = constraint_name
        # This parameter is required.
        self.constraint_type = constraint_type
        # This parameter is required.
        self.enforced = enforced

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.constraint_name is not None:
            result['constraintName'] = self.constraint_name
        if self.constraint_type is not None:
            result['constraintType'] = self.constraint_type
        if self.enforced is not None:
            result['enforced'] = self.enforced
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('constraintName') is not None:
            self.constraint_name = m.get('constraintName')
        if m.get('constraintType') is not None:
            self.constraint_type = m.get('constraintType')
        if m.get('enforced') is not None:
            self.enforced = m.get('enforced')
        return self


class WatermarkSpec(TeaModel):
    def __init__(
        self,
        column: str = None,
        watermark_expression: str = None,
        watermark_type: str = None,
    ):
        self.column = column
        self.watermark_expression = watermark_expression
        self.watermark_type = watermark_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column is not None:
            result['column'] = self.column
        if self.watermark_expression is not None:
            result['watermarkExpression'] = self.watermark_expression
        if self.watermark_type is not None:
            result['watermarkType'] = self.watermark_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('column') is not None:
            self.column = m.get('column')
        if m.get('watermarkExpression') is not None:
            self.watermark_expression = m.get('watermarkExpression')
        if m.get('watermarkType') is not None:
            self.watermark_type = m.get('watermarkType')
        return self


class Schema(TeaModel):
    def __init__(
        self,
        columns: List[TableColumn] = None,
        primary_key: PrimaryKey = None,
        watermark_specs: List[WatermarkSpec] = None,
    ):
        self.columns = columns
        self.primary_key = primary_key
        self.watermark_specs = watermark_specs

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()
        if self.primary_key:
            self.primary_key.validate()
        if self.watermark_specs:
            for k in self.watermark_specs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['columns'].append(k.to_map() if k else None)
        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key.to_map()
        result['watermarkSpecs'] = []
        if self.watermark_specs is not None:
            for k in self.watermark_specs:
                result['watermarkSpecs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k in m.get('columns'):
                temp_model = TableColumn()
                self.columns.append(temp_model.from_map(k))
        if m.get('primaryKey') is not None:
            temp_model = PrimaryKey()
            self.primary_key = temp_model.from_map(m['primaryKey'])
        self.watermark_specs = []
        if m.get('watermarkSpecs') is not None:
            for k in m.get('watermarkSpecs'):
                temp_model = WatermarkSpec()
                self.watermark_specs.append(temp_model.from_map(k))
        return self


class AiModel(TeaModel):
    def __init__(
        self,
        comment: str = None,
        input_schema: Schema = None,
        name: str = None,
        options: Dict[str, str] = None,
        output_schema: Schema = None,
    ):
        self.comment = comment
        self.input_schema = input_schema
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.options = options
        self.output_schema = output_schema

    def validate(self):
        if self.input_schema:
            self.input_schema.validate()
        if self.output_schema:
            self.output_schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.input_schema is not None:
            result['inputSchema'] = self.input_schema.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.options is not None:
            result['options'] = self.options
        if self.output_schema is not None:
            result['outputSchema'] = self.output_schema.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('inputSchema') is not None:
            temp_model = Schema()
            self.input_schema = temp_model.from_map(m['inputSchema'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('outputSchema') is not None:
            temp_model = Schema()
            self.output_schema = temp_model.from_map(m['outputSchema'])
        return self


class JarArtifact(TeaModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        entry_class: str = None,
        jar_uri: str = None,
        main_args: str = None,
    ):
        self.additional_dependencies = additional_dependencies
        self.entry_class = entry_class
        self.jar_uri = jar_uri
        self.main_args = main_args

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies
        if self.entry_class is not None:
            result['entryClass'] = self.entry_class
        if self.jar_uri is not None:
            result['jarUri'] = self.jar_uri
        if self.main_args is not None:
            result['mainArgs'] = self.main_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')
        if m.get('entryClass') is not None:
            self.entry_class = m.get('entryClass')
        if m.get('jarUri') is not None:
            self.jar_uri = m.get('jarUri')
        if m.get('mainArgs') is not None:
            self.main_args = m.get('mainArgs')
        return self


class PythonArtifact(TeaModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        additional_python_archives: List[str] = None,
        additional_python_libraries: List[str] = None,
        entry_module: str = None,
        main_args: str = None,
        python_artifact_uri: str = None,
    ):
        self.additional_dependencies = additional_dependencies
        self.additional_python_archives = additional_python_archives
        self.additional_python_libraries = additional_python_libraries
        self.entry_module = entry_module
        self.main_args = main_args
        self.python_artifact_uri = python_artifact_uri

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies
        if self.additional_python_archives is not None:
            result['additionalPythonArchives'] = self.additional_python_archives
        if self.additional_python_libraries is not None:
            result['additionalPythonLibraries'] = self.additional_python_libraries
        if self.entry_module is not None:
            result['entryModule'] = self.entry_module
        if self.main_args is not None:
            result['mainArgs'] = self.main_args
        if self.python_artifact_uri is not None:
            result['pythonArtifactUri'] = self.python_artifact_uri
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')
        if m.get('additionalPythonArchives') is not None:
            self.additional_python_archives = m.get('additionalPythonArchives')
        if m.get('additionalPythonLibraries') is not None:
            self.additional_python_libraries = m.get('additionalPythonLibraries')
        if m.get('entryModule') is not None:
            self.entry_module = m.get('entryModule')
        if m.get('mainArgs') is not None:
            self.main_args = m.get('mainArgs')
        if m.get('pythonArtifactUri') is not None:
            self.python_artifact_uri = m.get('pythonArtifactUri')
        return self


class SqlArtifact(TeaModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        sql_script: str = None,
    ):
        self.additional_dependencies = additional_dependencies
        self.sql_script = sql_script

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies
        if self.sql_script is not None:
            result['sqlScript'] = self.sql_script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')
        if m.get('sqlScript') is not None:
            self.sql_script = m.get('sqlScript')
        return self


class Artifact(TeaModel):
    def __init__(
        self,
        jar_artifact: JarArtifact = None,
        kind: str = None,
        python_artifact: PythonArtifact = None,
        sql_artifact: SqlArtifact = None,
    ):
        self.jar_artifact = jar_artifact
        self.kind = kind
        self.python_artifact = python_artifact
        self.sql_artifact = sql_artifact

    def validate(self):
        if self.jar_artifact:
            self.jar_artifact.validate()
        if self.python_artifact:
            self.python_artifact.validate()
        if self.sql_artifact:
            self.sql_artifact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jar_artifact is not None:
            result['jarArtifact'] = self.jar_artifact.to_map()
        if self.kind is not None:
            result['kind'] = self.kind
        if self.python_artifact is not None:
            result['pythonArtifact'] = self.python_artifact.to_map()
        if self.sql_artifact is not None:
            result['sqlArtifact'] = self.sql_artifact.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jarArtifact') is not None:
            temp_model = JarArtifact()
            self.jar_artifact = temp_model.from_map(m['jarArtifact'])
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('pythonArtifact') is not None:
            temp_model = PythonArtifact()
            self.python_artifact = temp_model.from_map(m['pythonArtifact'])
        if m.get('sqlArtifact') is not None:
            temp_model = SqlArtifact()
            self.sql_artifact = temp_model.from_map(m['sqlArtifact'])
        return self


class ValidationErrorDetails(TeaModel):
    def __init__(
        self,
        column_number: str = None,
        end_column_number: str = None,
        end_line_number: str = None,
        line_number: str = None,
        message: str = None,
    ):
        self.column_number = column_number
        self.end_column_number = end_column_number
        self.end_line_number = end_line_number
        self.line_number = line_number
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_number is not None:
            result['columnNumber'] = self.column_number
        if self.end_column_number is not None:
            result['endColumnNumber'] = self.end_column_number
        if self.end_line_number is not None:
            result['endLineNumber'] = self.end_line_number
        if self.line_number is not None:
            result['lineNumber'] = self.line_number
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnNumber') is not None:
            self.column_number = m.get('columnNumber')
        if m.get('endColumnNumber') is not None:
            self.end_column_number = m.get('endColumnNumber')
        if m.get('endLineNumber') is not None:
            self.end_line_number = m.get('endLineNumber')
        if m.get('lineNumber') is not None:
            self.line_number = m.get('lineNumber')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ValidateStatementResult(TeaModel):
    def __init__(
        self,
        error_details: ValidationErrorDetails = None,
        validation_result: str = None,
    ):
        self.error_details = error_details
        self.validation_result = validation_result

    def validate(self):
        if self.error_details:
            self.error_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_details is not None:
            result['errorDetails'] = self.error_details.to_map()
        if self.validation_result is not None:
            result['validationResult'] = self.validation_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorDetails') is not None:
            temp_model = ValidationErrorDetails()
            self.error_details = temp_model.from_map(m['errorDetails'])
        if m.get('validationResult') is not None:
            self.validation_result = m.get('validationResult')
        return self


class AsyncDraftDeployResult(TeaModel):
    def __init__(
        self,
        artifact_validation_detail: ValidateStatementResult = None,
        deployment_id: str = None,
        message: str = None,
        success: bool = None,
        ticket_status: str = None,
    ):
        self.artifact_validation_detail = artifact_validation_detail
        self.deployment_id = deployment_id
        self.message = message
        self.success = success
        self.ticket_status = ticket_status

    def validate(self):
        if self.artifact_validation_detail:
            self.artifact_validation_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_validation_detail is not None:
            result['artifactValidationDetail'] = self.artifact_validation_detail.to_map()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.ticket_status is not None:
            result['ticketStatus'] = self.ticket_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactValidationDetail') is not None:
            temp_model = ValidateStatementResult()
            self.artifact_validation_detail = temp_model.from_map(m['artifactValidationDetail'])
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('ticketStatus') is not None:
            self.ticket_status = m.get('ticketStatus')
        return self


class AsyncResourcePlanOperationResult(TeaModel):
    def __init__(
        self,
        message: str = None,
        plan: str = None,
        ticket_status: str = None,
    ):
        self.message = message
        self.plan = plan
        self.ticket_status = ticket_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.plan is not None:
            result['plan'] = self.plan
        if self.ticket_status is not None:
            result['ticketStatus'] = self.ticket_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('plan') is not None:
            self.plan = m.get('plan')
        if m.get('ticketStatus') is not None:
            self.ticket_status = m.get('ticketStatus')
        return self


class BasicResourceSettingSpec(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.memory is not None:
            result['memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        return self


class BasicResourceSetting(TeaModel):
    def __init__(
        self,
        jobmanager_resource_setting_spec: BasicResourceSettingSpec = None,
        parallelism: int = None,
        taskmanager_resource_setting_spec: BasicResourceSettingSpec = None,
    ):
        self.jobmanager_resource_setting_spec = jobmanager_resource_setting_spec
        self.parallelism = parallelism
        self.taskmanager_resource_setting_spec = taskmanager_resource_setting_spec

    def validate(self):
        if self.jobmanager_resource_setting_spec:
            self.jobmanager_resource_setting_spec.validate()
        if self.taskmanager_resource_setting_spec:
            self.taskmanager_resource_setting_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jobmanager_resource_setting_spec is not None:
            result['jobmanagerResourceSettingSpec'] = self.jobmanager_resource_setting_spec.to_map()
        if self.parallelism is not None:
            result['parallelism'] = self.parallelism
        if self.taskmanager_resource_setting_spec is not None:
            result['taskmanagerResourceSettingSpec'] = self.taskmanager_resource_setting_spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobmanagerResourceSettingSpec') is not None:
            temp_model = BasicResourceSettingSpec()
            self.jobmanager_resource_setting_spec = temp_model.from_map(m['jobmanagerResourceSettingSpec'])
        if m.get('parallelism') is not None:
            self.parallelism = m.get('parallelism')
        if m.get('taskmanagerResourceSettingSpec') is not None:
            temp_model = BasicResourceSettingSpec()
            self.taskmanager_resource_setting_spec = temp_model.from_map(m['taskmanagerResourceSettingSpec'])
        return self


class BatchResourceSetting(TeaModel):
    def __init__(
        self,
        basic_resource_setting: BasicResourceSetting = None,
        max_slot: int = None,
    ):
        self.basic_resource_setting = basic_resource_setting
        self.max_slot = max_slot

    def validate(self):
        if self.basic_resource_setting:
            self.basic_resource_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_resource_setting is not None:
            result['basicResourceSetting'] = self.basic_resource_setting.to_map()
        if self.max_slot is not None:
            result['maxSlot'] = self.max_slot
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basicResourceSetting') is not None:
            temp_model = BasicResourceSetting()
            self.basic_resource_setting = temp_model.from_map(m['basicResourceSetting'])
        if m.get('maxSlot') is not None:
            self.max_slot = m.get('maxSlot')
        return self


class BriefDeploymentTarget(TeaModel):
    def __init__(
        self,
        mode: str = None,
        name: str = None,
    ):
        self.mode = mode
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['mode'] = self.mode
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ExpertResourceSetting(TeaModel):
    def __init__(
        self,
        jobmanager_resource_setting_spec: BasicResourceSettingSpec = None,
        resource_plan: str = None,
    ):
        self.jobmanager_resource_setting_spec = jobmanager_resource_setting_spec
        self.resource_plan = resource_plan

    def validate(self):
        if self.jobmanager_resource_setting_spec:
            self.jobmanager_resource_setting_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jobmanager_resource_setting_spec is not None:
            result['jobmanagerResourceSettingSpec'] = self.jobmanager_resource_setting_spec.to_map()
        if self.resource_plan is not None:
            result['resourcePlan'] = self.resource_plan
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobmanagerResourceSettingSpec') is not None:
            temp_model = BasicResourceSettingSpec()
            self.jobmanager_resource_setting_spec = temp_model.from_map(m['jobmanagerResourceSettingSpec'])
        if m.get('resourcePlan') is not None:
            self.resource_plan = m.get('resourcePlan')
        return self


class StreamingResourceSetting(TeaModel):
    def __init__(
        self,
        basic_resource_setting: BasicResourceSetting = None,
        expert_resource_setting: ExpertResourceSetting = None,
        resource_setting_mode: str = None,
    ):
        self.basic_resource_setting = basic_resource_setting
        self.expert_resource_setting = expert_resource_setting
        self.resource_setting_mode = resource_setting_mode

    def validate(self):
        if self.basic_resource_setting:
            self.basic_resource_setting.validate()
        if self.expert_resource_setting:
            self.expert_resource_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_resource_setting is not None:
            result['basicResourceSetting'] = self.basic_resource_setting.to_map()
        if self.expert_resource_setting is not None:
            result['expertResourceSetting'] = self.expert_resource_setting.to_map()
        if self.resource_setting_mode is not None:
            result['resourceSettingMode'] = self.resource_setting_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basicResourceSetting') is not None:
            temp_model = BasicResourceSetting()
            self.basic_resource_setting = temp_model.from_map(m['basicResourceSetting'])
        if m.get('expertResourceSetting') is not None:
            temp_model = ExpertResourceSetting()
            self.expert_resource_setting = temp_model.from_map(m['expertResourceSetting'])
        if m.get('resourceSettingMode') is not None:
            self.resource_setting_mode = m.get('resourceSettingMode')
        return self


class BriefResourceSetting(TeaModel):
    def __init__(
        self,
        batch_resource_setting: BatchResourceSetting = None,
        flink_conf: Dict[str, Any] = None,
        streaming_resource_setting: StreamingResourceSetting = None,
    ):
        self.batch_resource_setting = batch_resource_setting
        self.flink_conf = flink_conf
        self.streaming_resource_setting = streaming_resource_setting

    def validate(self):
        if self.batch_resource_setting:
            self.batch_resource_setting.validate()
        if self.streaming_resource_setting:
            self.streaming_resource_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_resource_setting is not None:
            result['batchResourceSetting'] = self.batch_resource_setting.to_map()
        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf
        if self.streaming_resource_setting is not None:
            result['streamingResourceSetting'] = self.streaming_resource_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchResourceSetting') is not None:
            temp_model = BatchResourceSetting()
            self.batch_resource_setting = temp_model.from_map(m['batchResourceSetting'])
        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')
        if m.get('streamingResourceSetting') is not None:
            temp_model = StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m['streamingResourceSetting'])
        return self


class Catalog(TeaModel):
    def __init__(
        self,
        extension_conf: Dict[str, str] = None,
        name: str = None,
        properties: Dict[str, Any] = None,
    ):
        self.extension_conf = extension_conf
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension_conf is not None:
            result['extensionConf'] = self.extension_conf
        if self.name is not None:
            result['name'] = self.name
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extensionConf') is not None:
            self.extension_conf = m.get('extensionConf')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self


class Cell(TeaModel):
    def __init__(
        self,
        value: str = None,
    ):
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class Property(TeaModel):
    def __init__(
        self,
        default_value: str = None,
        defines_format: bool = None,
        description: str = None,
        key: str = None,
        required: bool = None,
        sensitive: bool = None,
    ):
        self.default_value = default_value
        self.defines_format = defines_format
        self.description = description
        self.key = key
        self.required = required
        self.sensitive = sensitive

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.defines_format is not None:
            result['definesFormat'] = self.defines_format
        if self.description is not None:
            result['description'] = self.description
        if self.key is not None:
            result['key'] = self.key
        if self.required is not None:
            result['required'] = self.required
        if self.sensitive is not None:
            result['sensitive'] = self.sensitive
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('definesFormat') is not None:
            self.defines_format = m.get('definesFormat')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('sensitive') is not None:
            self.sensitive = m.get('sensitive')
        return self


class Connector(TeaModel):
    def __init__(
        self,
        creator: str = None,
        creator_name: str = None,
        dependencies: List[str] = None,
        lookup: bool = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        properties: List[Property] = None,
        sink: bool = None,
        source: bool = None,
        supported_formats: List[str] = None,
        type: str = None,
    ):
        self.creator = creator
        self.creator_name = creator_name
        self.dependencies = dependencies
        self.lookup = lookup
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.properties = properties
        self.sink = sink
        self.source = source
        self.supported_formats = supported_formats
        self.type = type

    def validate(self):
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.dependencies is not None:
            result['dependencies'] = self.dependencies
        if self.lookup is not None:
            result['lookup'] = self.lookup
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.name is not None:
            result['name'] = self.name
        result['properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['properties'].append(k.to_map() if k else None)
        if self.sink is not None:
            result['sink'] = self.sink
        if self.source is not None:
            result['source'] = self.source
        if self.supported_formats is not None:
            result['supportedFormats'] = self.supported_formats
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('dependencies') is not None:
            self.dependencies = m.get('dependencies')
        if m.get('lookup') is not None:
            self.lookup = m.get('lookup')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.properties = []
        if m.get('properties') is not None:
            for k in m.get('properties'):
                temp_model = Property()
                self.properties.append(temp_model.from_map(k))
        if m.get('sink') is not None:
            self.sink = m.get('sink')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('supportedFormats') is not None:
            self.supported_formats = m.get('supportedFormats')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UdfClass(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        class_type: str = None,
        function_names: List[str] = None,
        udf_artifact_name: str = None,
    ):
        self.class_name = class_name
        self.class_type = class_type
        self.function_names = function_names
        self.udf_artifact_name = udf_artifact_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.class_type is not None:
            result['classType'] = self.class_type
        if self.function_names is not None:
            result['functionNames'] = self.function_names
        if self.udf_artifact_name is not None:
            result['udfArtifactName'] = self.udf_artifact_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('classType') is not None:
            self.class_type = m.get('classType')
        if m.get('functionNames') is not None:
            self.function_names = m.get('functionNames')
        if m.get('udfArtifactName') is not None:
            self.udf_artifact_name = m.get('udfArtifactName')
        return self


class UdfArtifact(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        created_at: int = None,
        creator: str = None,
        dependency_jar_uris: List[str] = None,
        jar_url: str = None,
        modified_at: int = None,
        name: str = None,
        namespace: str = None,
        udf_classes: List[UdfClass] = None,
    ):
        self.artifact_type = artifact_type
        self.created_at = created_at
        self.creator = creator
        self.dependency_jar_uris = dependency_jar_uris
        self.jar_url = jar_url
        self.modified_at = modified_at
        self.name = name
        self.namespace = namespace
        self.udf_classes = udf_classes

    def validate(self):
        if self.udf_classes:
            for k in self.udf_classes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['artifactType'] = self.artifact_type
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.dependency_jar_uris is not None:
            result['dependencyJarUris'] = self.dependency_jar_uris
        if self.jar_url is not None:
            result['jarUrl'] = self.jar_url
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        result['udfClasses'] = []
        if self.udf_classes is not None:
            for k in self.udf_classes:
                result['udfClasses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactType') is not None:
            self.artifact_type = m.get('artifactType')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('dependencyJarUris') is not None:
            self.dependency_jar_uris = m.get('dependencyJarUris')
        if m.get('jarUrl') is not None:
            self.jar_url = m.get('jarUrl')
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        self.udf_classes = []
        if m.get('udfClasses') is not None:
            for k in m.get('udfClasses'):
                temp_model = UdfClass()
                self.udf_classes.append(temp_model.from_map(k))
        return self


class CreateUdfArtifactResult(TeaModel):
    def __init__(
        self,
        colliding_classes: List[UdfClass] = None,
        create_success: bool = None,
        message: str = None,
        udf_artifact: UdfArtifact = None,
    ):
        self.colliding_classes = colliding_classes
        self.create_success = create_success
        self.message = message
        self.udf_artifact = udf_artifact

    def validate(self):
        if self.colliding_classes:
            for k in self.colliding_classes:
                if k:
                    k.validate()
        if self.udf_artifact:
            self.udf_artifact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['collidingClasses'] = []
        if self.colliding_classes is not None:
            for k in self.colliding_classes:
                result['collidingClasses'].append(k.to_map() if k else None)
        if self.create_success is not None:
            result['createSuccess'] = self.create_success
        if self.message is not None:
            result['message'] = self.message
        if self.udf_artifact is not None:
            result['udfArtifact'] = self.udf_artifact.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.colliding_classes = []
        if m.get('collidingClasses') is not None:
            for k in m.get('collidingClasses'):
                temp_model = UdfClass()
                self.colliding_classes.append(temp_model.from_map(k))
        if m.get('createSuccess') is not None:
            self.create_success = m.get('createSuccess')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('udfArtifact') is not None:
            temp_model = UdfArtifact()
            self.udf_artifact = temp_model.from_map(m['udfArtifact'])
        return self


class Database(TeaModel):
    def __init__(
        self,
        comment: str = None,
        name: str = None,
        properties: Dict[str, Any] = None,
    ):
        self.comment = comment
        self.name = name
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.name is not None:
            result['name'] = self.name
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self


class DeleteUdfArtifactResult(TeaModel):
    def __init__(
        self,
        delete_success: bool = None,
        message: str = None,
        referenced_classes: List[UdfClass] = None,
    ):
        self.delete_success = delete_success
        self.message = message
        self.referenced_classes = referenced_classes

    def validate(self):
        if self.referenced_classes:
            for k in self.referenced_classes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_success is not None:
            result['deleteSuccess'] = self.delete_success
        if self.message is not None:
            result['message'] = self.message
        result['referencedClasses'] = []
        if self.referenced_classes is not None:
            for k in self.referenced_classes:
                result['referencedClasses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deleteSuccess') is not None:
            self.delete_success = m.get('deleteSuccess')
        if m.get('message') is not None:
            self.message = m.get('message')
        self.referenced_classes = []
        if m.get('referencedClasses') is not None:
            for k in m.get('referencedClasses'):
                temp_model = UdfClass()
                self.referenced_classes.append(temp_model.from_map(k))
        return self


class JobSummary(TeaModel):
    def __init__(
        self,
        cancelled: int = None,
        cancelling: int = None,
        failed: int = None,
        finished: int = None,
        running: int = None,
        starting: int = None,
    ):
        self.cancelled = cancelled
        self.cancelling = cancelling
        self.failed = failed
        self.finished = finished
        self.running = running
        self.starting = starting

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cancelled is not None:
            result['cancelled'] = self.cancelled
        if self.cancelling is not None:
            result['cancelling'] = self.cancelling
        if self.failed is not None:
            result['failed'] = self.failed
        if self.finished is not None:
            result['finished'] = self.finished
        if self.running is not None:
            result['running'] = self.running
        if self.starting is not None:
            result['starting'] = self.starting
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancelled') is not None:
            self.cancelled = m.get('cancelled')
        if m.get('cancelling') is not None:
            self.cancelling = m.get('cancelling')
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        if m.get('finished') is not None:
            self.finished = m.get('finished')
        if m.get('running') is not None:
            self.running = m.get('running')
        if m.get('starting') is not None:
            self.starting = m.get('starting')
        return self


class LocalVariable(TeaModel):
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
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class Log4jLogger(TeaModel):
    def __init__(
        self,
        logger_level: str = None,
        logger_name: str = None,
    ):
        self.logger_level = logger_level
        self.logger_name = logger_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logger_level is not None:
            result['loggerLevel'] = self.logger_level
        if self.logger_name is not None:
            result['loggerName'] = self.logger_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('loggerLevel') is not None:
            self.logger_level = m.get('loggerLevel')
        if m.get('loggerName') is not None:
            self.logger_name = m.get('loggerName')
        return self


class LogReservePolicy(TeaModel):
    def __init__(
        self,
        expiration_days: int = None,
        open_history: bool = None,
    ):
        self.expiration_days = expiration_days
        self.open_history = open_history

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expiration_days is not None:
            result['expirationDays'] = self.expiration_days
        if self.open_history is not None:
            result['openHistory'] = self.open_history
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expirationDays') is not None:
            self.expiration_days = m.get('expirationDays')
        if m.get('openHistory') is not None:
            self.open_history = m.get('openHistory')
        return self


class Logging(TeaModel):
    def __init__(
        self,
        log_4j_2configuration_template: str = None,
        log_4j_loggers: List[Log4jLogger] = None,
        log_reserve_policy: LogReservePolicy = None,
        logging_profile: str = None,
    ):
        self.log_4j_2configuration_template = log_4j_2configuration_template
        self.log_4j_loggers = log_4j_loggers
        self.log_reserve_policy = log_reserve_policy
        self.logging_profile = logging_profile

    def validate(self):
        if self.log_4j_loggers:
            for k in self.log_4j_loggers:
                if k:
                    k.validate()
        if self.log_reserve_policy:
            self.log_reserve_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_4j_2configuration_template is not None:
            result['log4j2ConfigurationTemplate'] = self.log_4j_2configuration_template
        result['log4jLoggers'] = []
        if self.log_4j_loggers is not None:
            for k in self.log_4j_loggers:
                result['log4jLoggers'].append(k.to_map() if k else None)
        if self.log_reserve_policy is not None:
            result['logReservePolicy'] = self.log_reserve_policy.to_map()
        if self.logging_profile is not None:
            result['loggingProfile'] = self.logging_profile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('log4j2ConfigurationTemplate') is not None:
            self.log_4j_2configuration_template = m.get('log4j2ConfigurationTemplate')
        self.log_4j_loggers = []
        if m.get('log4jLoggers') is not None:
            for k in m.get('log4jLoggers'):
                temp_model = Log4jLogger()
                self.log_4j_loggers.append(temp_model.from_map(k))
        if m.get('logReservePolicy') is not None:
            temp_model = LogReservePolicy()
            self.log_reserve_policy = temp_model.from_map(m['logReservePolicy'])
        if m.get('loggingProfile') is not None:
            self.logging_profile = m.get('loggingProfile')
        return self


class Deployment(TeaModel):
    def __init__(
        self,
        artifact: Artifact = None,
        batch_resource_setting: BatchResourceSetting = None,
        created_at: str = None,
        creator: str = None,
        creator_name: str = None,
        deployment_has_changed: bool = None,
        deployment_id: str = None,
        deployment_target: BriefDeploymentTarget = None,
        description: str = None,
        engine_version: str = None,
        execution_mode: str = None,
        flink_conf: Dict[str, Any] = None,
        job_summary: JobSummary = None,
        labels: Dict[str, Any] = None,
        local_variables: List[LocalVariable] = None,
        logging: Logging = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        referenced_deployment_draft_id: str = None,
        streaming_resource_setting: StreamingResourceSetting = None,
        workspace: str = None,
    ):
        self.artifact = artifact
        self.batch_resource_setting = batch_resource_setting
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_has_changed = deployment_has_changed
        self.deployment_id = deployment_id
        self.deployment_target = deployment_target
        self.description = description
        self.engine_version = engine_version
        self.execution_mode = execution_mode
        self.flink_conf = flink_conf
        self.job_summary = job_summary
        self.labels = labels
        self.local_variables = local_variables
        self.logging = logging
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
        self.referenced_deployment_draft_id = referenced_deployment_draft_id
        self.streaming_resource_setting = streaming_resource_setting
        self.workspace = workspace

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.batch_resource_setting:
            self.batch_resource_setting.validate()
        if self.deployment_target:
            self.deployment_target.validate()
        if self.job_summary:
            self.job_summary.validate()
        if self.local_variables:
            for k in self.local_variables:
                if k:
                    k.validate()
        if self.logging:
            self.logging.validate()
        if self.streaming_resource_setting:
            self.streaming_resource_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()
        if self.batch_resource_setting is not None:
            result['batchResourceSetting'] = self.batch_resource_setting.to_map()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.deployment_has_changed is not None:
            result['deploymentHasChanged'] = self.deployment_has_changed
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.deployment_target is not None:
            result['deploymentTarget'] = self.deployment_target.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode
        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf
        if self.job_summary is not None:
            result['jobSummary'] = self.job_summary.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        result['localVariables'] = []
        if self.local_variables is not None:
            for k in self.local_variables:
                result['localVariables'].append(k.to_map() if k else None)
        if self.logging is not None:
            result['logging'] = self.logging.to_map()
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.referenced_deployment_draft_id is not None:
            result['referencedDeploymentDraftId'] = self.referenced_deployment_draft_id
        if self.streaming_resource_setting is not None:
            result['streamingResourceSetting'] = self.streaming_resource_setting.to_map()
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = Artifact()
            self.artifact = temp_model.from_map(m['artifact'])
        if m.get('batchResourceSetting') is not None:
            temp_model = BatchResourceSetting()
            self.batch_resource_setting = temp_model.from_map(m['batchResourceSetting'])
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('deploymentHasChanged') is not None:
            self.deployment_has_changed = m.get('deploymentHasChanged')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('deploymentTarget') is not None:
            temp_model = BriefDeploymentTarget()
            self.deployment_target = temp_model.from_map(m['deploymentTarget'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')
        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')
        if m.get('jobSummary') is not None:
            temp_model = JobSummary()
            self.job_summary = temp_model.from_map(m['jobSummary'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        self.local_variables = []
        if m.get('localVariables') is not None:
            for k in m.get('localVariables'):
                temp_model = LocalVariable()
                self.local_variables.append(temp_model.from_map(k))
        if m.get('logging') is not None:
            temp_model = Logging()
            self.logging = temp_model.from_map(m['logging'])
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('referencedDeploymentDraftId') is not None:
            self.referenced_deployment_draft_id = m.get('referencedDeploymentDraftId')
        if m.get('streamingResourceSetting') is not None:
            temp_model = StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m['streamingResourceSetting'])
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class Lock(TeaModel):
    def __init__(
        self,
        holder_id: str = None,
        holder_name: str = None,
        id: str = None,
        namespace: str = None,
        workspace: str = None,
    ):
        self.holder_id = holder_id
        self.holder_name = holder_name
        self.id = id
        self.namespace = namespace
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.holder_id is not None:
            result['holderId'] = self.holder_id
        if self.holder_name is not None:
            result['holderName'] = self.holder_name
        if self.id is not None:
            result['id'] = self.id
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('holderId') is not None:
            self.holder_id = m.get('holderId')
        if m.get('holderName') is not None:
            self.holder_name = m.get('holderName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeploymentDraft(TeaModel):
    def __init__(
        self,
        artifact: Artifact = None,
        created_at: int = None,
        creator: str = None,
        creator_name: str = None,
        deployment_draft_id: str = None,
        engine_version: str = None,
        execution_mode: str = None,
        labels: Dict[str, Any] = None,
        local_variables: List[LocalVariable] = None,
        lock: Lock = None,
        modified_at: int = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        parent_id: str = None,
        referenced_deployment_id: str = None,
        workspace: str = None,
    ):
        self.artifact = artifact
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_draft_id = deployment_draft_id
        self.engine_version = engine_version
        self.execution_mode = execution_mode
        self.labels = labels
        self.local_variables = local_variables
        self.lock = lock
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
        self.parent_id = parent_id
        self.referenced_deployment_id = referenced_deployment_id
        self.workspace = workspace

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.local_variables:
            for k in self.local_variables:
                if k:
                    k.validate()
        if self.lock:
            self.lock.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.deployment_draft_id is not None:
            result['deploymentDraftId'] = self.deployment_draft_id
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode
        if self.labels is not None:
            result['labels'] = self.labels
        result['localVariables'] = []
        if self.local_variables is not None:
            for k in self.local_variables:
                result['localVariables'].append(k.to_map() if k else None)
        if self.lock is not None:
            result['lock'] = self.lock.to_map()
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        if self.referenced_deployment_id is not None:
            result['referencedDeploymentId'] = self.referenced_deployment_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = Artifact()
            self.artifact = temp_model.from_map(m['artifact'])
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('deploymentDraftId') is not None:
            self.deployment_draft_id = m.get('deploymentDraftId')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        self.local_variables = []
        if m.get('localVariables') is not None:
            for k in m.get('localVariables'):
                temp_model = LocalVariable()
                self.local_variables.append(temp_model.from_map(k))
        if m.get('lock') is not None:
            temp_model = Lock()
            self.lock = temp_model.from_map(m['lock'])
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        if m.get('referencedDeploymentId') is not None:
            self.referenced_deployment_id = m.get('referencedDeploymentId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeploymentRestoreStrategy(TeaModel):
    def __init__(
        self,
        allow_non_restored_state: bool = None,
        job_start_time_in_ms: int = None,
        kind: str = None,
        savepoint_id: str = None,
    ):
        self.allow_non_restored_state = allow_non_restored_state
        self.job_start_time_in_ms = job_start_time_in_ms
        self.kind = kind
        self.savepoint_id = savepoint_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_non_restored_state is not None:
            result['allowNonRestoredState'] = self.allow_non_restored_state
        if self.job_start_time_in_ms is not None:
            result['jobStartTimeInMs'] = self.job_start_time_in_ms
        if self.kind is not None:
            result['kind'] = self.kind
        if self.savepoint_id is not None:
            result['savepointId'] = self.savepoint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowNonRestoredState') is not None:
            self.allow_non_restored_state = m.get('allowNonRestoredState')
        if m.get('jobStartTimeInMs') is not None:
            self.job_start_time_in_ms = m.get('jobStartTimeInMs')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('savepointId') is not None:
            self.savepoint_id = m.get('savepointId')
        return self


class ResourceSpec(TeaModel):
    def __init__(
        self,
        cpu: float = None,
        memory: str = None,
    ):
        self.cpu = cpu
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.memory is not None:
            result['memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        return self


class ResourceQuota(TeaModel):
    def __init__(
        self,
        limit: ResourceSpec = None,
        request: ResourceSpec = None,
        used: ResourceSpec = None,
    ):
        self.limit = limit
        self.request = request
        self.used = used

    def validate(self):
        if self.limit:
            self.limit.validate()
        if self.request:
            self.request.validate()
        if self.used:
            self.used.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit.to_map()
        if self.request is not None:
            result['request'] = self.request.to_map()
        if self.used is not None:
            result['used'] = self.used.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            temp_model = ResourceSpec()
            self.limit = temp_model.from_map(m['limit'])
        if m.get('request') is not None:
            temp_model = ResourceSpec()
            self.request = temp_model.from_map(m['request'])
        if m.get('used') is not None:
            temp_model = ResourceSpec()
            self.used = temp_model.from_map(m['used'])
        return self


class DeploymentTarget(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        quota: ResourceQuota = None,
    ):
        self.name = name
        self.namespace = namespace
        self.quota = quota

    def validate(self):
        if self.quota:
            self.quota.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.quota is not None:
            result['quota'] = self.quota.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('quota') is not None:
            temp_model = ResourceQuota()
            self.quota = temp_model.from_map(m['quota'])
        return self


class DraftDeployParams(TeaModel):
    def __init__(
        self,
        deployment_draft_id: str = None,
        deployment_target: BriefDeploymentTarget = None,
        skip_validate: bool = None,
    ):
        self.deployment_draft_id = deployment_draft_id
        self.deployment_target = deployment_target
        self.skip_validate = skip_validate

    def validate(self):
        if self.deployment_target:
            self.deployment_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_draft_id is not None:
            result['deploymentDraftId'] = self.deployment_draft_id
        if self.deployment_target is not None:
            result['deploymentTarget'] = self.deployment_target.to_map()
        if self.skip_validate is not None:
            result['skipValidate'] = self.skip_validate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentDraftId') is not None:
            self.deployment_draft_id = m.get('deploymentDraftId')
        if m.get('deploymentTarget') is not None:
            temp_model = BriefDeploymentTarget()
            self.deployment_target = temp_model.from_map(m['deploymentTarget'])
        if m.get('skipValidate') is not None:
            self.skip_validate = m.get('skipValidate')
        return self


class DraftDeployResult(TeaModel):
    def __init__(
        self,
        artifact_validation_detail: ValidateStatementResult = None,
        deployment_id: str = None,
        message: str = None,
        success: bool = None,
    ):
        self.artifact_validation_detail = artifact_validation_detail
        self.deployment_id = deployment_id
        self.message = message
        self.success = success

    def validate(self):
        if self.artifact_validation_detail:
            self.artifact_validation_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_validation_detail is not None:
            result['artifactValidationDetail'] = self.artifact_validation_detail.to_map()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactValidationDetail') is not None:
            temp_model = ValidateStatementResult()
            self.artifact_validation_detail = temp_model.from_map(m['artifactValidationDetail'])
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class Relation(TeaModel):
    def __init__(
        self,
        destination: str = None,
        job_id: str = None,
        source: str = None,
    ):
        self.destination = destination
        self.job_id = job_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['destination'] = self.destination
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('destination') is not None:
            self.destination = m.get('destination')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class Edge(TeaModel):
    def __init__(
        self,
        column_lineage: List[Relation] = None,
        table_lineage: List[Relation] = None,
    ):
        self.column_lineage = column_lineage
        self.table_lineage = table_lineage

    def validate(self):
        if self.column_lineage:
            for k in self.column_lineage:
                if k:
                    k.validate()
        if self.table_lineage:
            for k in self.table_lineage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['columnLineage'] = []
        if self.column_lineage is not None:
            for k in self.column_lineage:
                result['columnLineage'].append(k.to_map() if k else None)
        result['tableLineage'] = []
        if self.table_lineage is not None:
            for k in self.table_lineage:
                result['tableLineage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_lineage = []
        if m.get('columnLineage') is not None:
            for k in m.get('columnLineage'):
                temp_model = Relation()
                self.column_lineage.append(temp_model.from_map(k))
        self.table_lineage = []
        if m.get('tableLineage') is not None:
            for k in m.get('tableLineage'):
                temp_model = Relation()
                self.table_lineage.append(temp_model.from_map(k))
        return self


class EditableNamespace(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        role: str = None,
        workspace_id: str = None,
    ):
        self.namespace = namespace
        self.role = role
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.role is not None:
            result['Role'] = self.role
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class EngineVersionSupportedFeatures(TeaModel):
    def __init__(
        self,
        support_native_savepoint: bool = None,
        use_for_sql_deployments: bool = None,
    ):
        self.support_native_savepoint = support_native_savepoint
        self.use_for_sql_deployments = use_for_sql_deployments

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.support_native_savepoint is not None:
            result['supportNativeSavepoint'] = self.support_native_savepoint
        if self.use_for_sql_deployments is not None:
            result['useForSqlDeployments'] = self.use_for_sql_deployments
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('supportNativeSavepoint') is not None:
            self.support_native_savepoint = m.get('supportNativeSavepoint')
        if m.get('useForSqlDeployments') is not None:
            self.use_for_sql_deployments = m.get('useForSqlDeployments')
        return self


class EngineVersionMetadata(TeaModel):
    def __init__(
        self,
        engine_version: str = None,
        features: EngineVersionSupportedFeatures = None,
        status: str = None,
    ):
        # This parameter is required.
        self.engine_version = engine_version
        self.features = features
        # This parameter is required.
        self.status = status

    def validate(self):
        if self.features:
            self.features.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.features is not None:
            result['features'] = self.features.to_map()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('features') is not None:
            temp_model = EngineVersionSupportedFeatures()
            self.features = temp_model.from_map(m['features'])
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class EngineVersionMetadataIndex(TeaModel):
    def __init__(
        self,
        default_engine_version: str = None,
        engine_version_metadata: List[EngineVersionMetadata] = None,
    ):
        self.default_engine_version = default_engine_version
        self.engine_version_metadata = engine_version_metadata

    def validate(self):
        if self.engine_version_metadata:
            for k in self.engine_version_metadata:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_engine_version is not None:
            result['defaultEngineVersion'] = self.default_engine_version
        result['engineVersionMetadata'] = []
        if self.engine_version_metadata is not None:
            for k in self.engine_version_metadata:
                result['engineVersionMetadata'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultEngineVersion') is not None:
            self.default_engine_version = m.get('defaultEngineVersion')
        self.engine_version_metadata = []
        if m.get('engineVersionMetadata') is not None:
            for k in m.get('engineVersionMetadata'):
                temp_model = EngineVersionMetadata()
                self.engine_version_metadata.append(temp_model.from_map(k))
        return self


class ErrorDetails(TeaModel):
    def __init__(
        self,
        column_number: str = None,
        end_column_number: str = None,
        end_line_number: str = None,
        invalidflink_conf: List[str] = None,
        line_number: str = None,
        message: str = None,
    ):
        self.column_number = column_number
        self.end_column_number = end_column_number
        self.end_line_number = end_line_number
        self.invalidflink_conf = invalidflink_conf
        self.line_number = line_number
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_number is not None:
            result['columnNumber'] = self.column_number
        if self.end_column_number is not None:
            result['endColumnNumber'] = self.end_column_number
        if self.end_line_number is not None:
            result['endLineNumber'] = self.end_line_number
        if self.invalidflink_conf is not None:
            result['invalidflinkConf'] = self.invalidflink_conf
        if self.line_number is not None:
            result['lineNumber'] = self.line_number
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnNumber') is not None:
            self.column_number = m.get('columnNumber')
        if m.get('endColumnNumber') is not None:
            self.end_column_number = m.get('endColumnNumber')
        if m.get('endLineNumber') is not None:
            self.end_line_number = m.get('endLineNumber')
        if m.get('invalidflinkConf') is not None:
            self.invalidflink_conf = m.get('invalidflinkConf')
        if m.get('lineNumber') is not None:
            self.line_number = m.get('lineNumber')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class Event(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        deployment_id: str = None,
        event_id: str = None,
        event_name: str = None,
        job_id: str = None,
        message: str = None,
        namespace: str = None,
        workspace: str = None,
    ):
        self.created_at = created_at
        self.deployment_id = deployment_id
        self.event_id = event_id
        self.event_name = event_name
        self.job_id = job_id
        self.message = message
        self.namespace = namespace
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.event_name is not None:
            result['eventName'] = self.event_name
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.message is not None:
            result['message'] = self.message
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('eventName') is not None:
            self.event_name = m.get('eventName')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class Row(TeaModel):
    def __init__(
        self,
        cells: List[Cell] = None,
    ):
        self.cells = cells

    def validate(self):
        if self.cells:
            for k in self.cells:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['cells'] = []
        if self.cells is not None:
            for k in self.cells:
                result['cells'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cells = []
        if m.get('cells') is not None:
            for k in m.get('cells'):
                temp_model = Cell()
                self.cells.append(temp_model.from_map(k))
        return self


class RowUpdate(TeaModel):
    def __init__(
        self,
        row: Row = None,
        row_kind: str = None,
    ):
        self.row = row
        self.row_kind = row_kind

    def validate(self):
        if self.row:
            self.row.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.row is not None:
            result['row'] = self.row.to_map()
        if self.row_kind is not None:
            result['rowKind'] = self.row_kind
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('row') is not None:
            temp_model = Row()
            self.row = temp_model.from_map(m['row'])
        if m.get('rowKind') is not None:
            self.row_kind = m.get('rowKind')
        return self


class TableResult(TeaModel):
    def __init__(
        self,
        row_updates: List[RowUpdate] = None,
        table_name: str = None,
    ):
        self.row_updates = row_updates
        self.table_name = table_name

    def validate(self):
        if self.row_updates:
            for k in self.row_updates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['rowUpdates'] = []
        if self.row_updates is not None:
            for k in self.row_updates:
                result['rowUpdates'].append(k.to_map() if k else None)
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.row_updates = []
        if m.get('rowUpdates') is not None:
            for k in m.get('rowUpdates'):
                temp_model = RowUpdate()
                self.row_updates.append(temp_model.from_map(k))
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class FetchResult(TeaModel):
    def __init__(
        self,
        result_message: str = None,
        result_type: str = None,
        table_results: List[TableResult] = None,
    ):
        self.result_message = result_message
        self.result_type = result_type
        self.table_results = table_results

    def validate(self):
        if self.table_results:
            for k in self.table_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_message is not None:
            result['resultMessage'] = self.result_message
        if self.result_type is not None:
            result['resultType'] = self.result_type
        result['tableResults'] = []
        if self.table_results is not None:
            for k in self.table_results:
                result['tableResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resultMessage') is not None:
            self.result_message = m.get('resultMessage')
        if m.get('resultType') is not None:
            self.result_type = m.get('resultType')
        self.table_results = []
        if m.get('tableResults') is not None:
            for k in m.get('tableResults'):
                temp_model = TableResult()
                self.table_results.append(temp_model.from_map(k))
        return self


class SubFolder(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        self.folder_id = folder_id
        self.name = name
        self.parent_id = parent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        return self


class Folder(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        folder_id: str = None,
        modified_at: int = None,
        name: str = None,
        namespace: str = None,
        parent_id: str = None,
        sub_folder: List[SubFolder] = None,
        workspace: str = None,
    ):
        self.created_at = created_at
        self.folder_id = folder_id
        self.modified_at = modified_at
        self.name = name
        self.namespace = namespace
        self.parent_id = parent_id
        self.sub_folder = sub_folder
        self.workspace = workspace

    def validate(self):
        if self.sub_folder:
            for k in self.sub_folder:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.parent_id is not None:
            result['parentId'] = self.parent_id
        result['subFolder'] = []
        if self.sub_folder is not None:
            for k in self.sub_folder:
                result['subFolder'].append(k.to_map() if k else None)
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('parentId') is not None:
            self.parent_id = m.get('parentId')
        self.sub_folder = []
        if m.get('subFolder') is not None:
            for k in m.get('subFolder'):
                temp_model = SubFolder()
                self.sub_folder.append(temp_model.from_map(k))
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class Function(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        description: str = None,
        function_language: str = None,
        function_type: str = None,
        gmt_modified: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.class_name = class_name
        self.description = description
        # This parameter is required.
        self.function_language = function_language
        # This parameter is required.
        self.function_type = function_type
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.description is not None:
            result['description'] = self.description
        if self.function_language is not None:
            result['functionLanguage'] = self.function_language
        if self.function_type is not None:
            result['functionType'] = self.function_type
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('functionLanguage') is not None:
            self.function_language = m.get('functionLanguage')
        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetLineageInfoParams(TeaModel):
    def __init__(
        self,
        depth: int = None,
        direction: str = None,
        id: str = None,
        id_type: str = None,
        is_column_level: bool = None,
        is_temporary: bool = None,
        namespace: str = None,
        workspace: str = None,
    ):
        self.depth = depth
        self.direction = direction
        self.id = id
        self.id_type = id_type
        self.is_column_level = is_column_level
        self.is_temporary = is_temporary
        self.namespace = namespace
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.depth is not None:
            result['depth'] = self.depth
        if self.direction is not None:
            result['direction'] = self.direction
        if self.id is not None:
            result['id'] = self.id
        if self.id_type is not None:
            result['idType'] = self.id_type
        if self.is_column_level is not None:
            result['isColumnLevel'] = self.is_column_level
        if self.is_temporary is not None:
            result['isTemporary'] = self.is_temporary
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depth') is not None:
            self.depth = m.get('depth')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('idType') is not None:
            self.id_type = m.get('idType')
        if m.get('isColumnLevel') is not None:
            self.is_column_level = m.get('isColumnLevel')
        if m.get('isTemporary') is not None:
            self.is_temporary = m.get('isTemporary')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetPreSignedUrlForObjectResult(TeaModel):
    def __init__(
        self,
        jar_url: str = None,
        pre_signed_url: str = None,
    ):
        self.jar_url = jar_url
        self.pre_signed_url = pre_signed_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jar_url is not None:
            result['jarUrl'] = self.jar_url
        if self.pre_signed_url is not None:
            result['preSignedUrl'] = self.pre_signed_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jarUrl') is not None:
            self.jar_url = m.get('jarUrl')
        if m.get('preSignedUrl') is not None:
            self.pre_signed_url = m.get('preSignedUrl')
        return self


class HotUpdateJobFailureInfo(TeaModel):
    def __init__(
        self,
        failure_severity: str = None,
        message: str = None,
        reason: str = None,
    ):
        self.failure_severity = failure_severity
        self.message = message
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure_severity is not None:
            result['failureSeverity'] = self.failure_severity
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failureSeverity') is not None:
            self.failure_severity = m.get('failureSeverity')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class RescaleJobParam(TeaModel):
    def __init__(
        self,
        job_parallelism: int = None,
    ):
        self.job_parallelism = job_parallelism

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_parallelism is not None:
            result['jobParallelism'] = self.job_parallelism
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobParallelism') is not None:
            self.job_parallelism = m.get('jobParallelism')
        return self


class UpdateJobConfigParam(TeaModel):
    def __init__(
        self,
        new_flink_conf: Dict[str, Any] = None,
    ):
        self.new_flink_conf = new_flink_conf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_flink_conf is not None:
            result['newFlinkConf'] = self.new_flink_conf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('newFlinkConf') is not None:
            self.new_flink_conf = m.get('newFlinkConf')
        return self


class HotUpdateJobParams(TeaModel):
    def __init__(
        self,
        rescale_job_param: RescaleJobParam = None,
        update_job_config_param: UpdateJobConfigParam = None,
    ):
        self.rescale_job_param = rescale_job_param
        self.update_job_config_param = update_job_config_param

    def validate(self):
        if self.rescale_job_param:
            self.rescale_job_param.validate()
        if self.update_job_config_param:
            self.update_job_config_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rescale_job_param is not None:
            result['rescaleJobParam'] = self.rescale_job_param.to_map()
        if self.update_job_config_param is not None:
            result['updateJobConfigParam'] = self.update_job_config_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rescaleJobParam') is not None:
            temp_model = RescaleJobParam()
            self.rescale_job_param = temp_model.from_map(m['rescaleJobParam'])
        if m.get('updateJobConfigParam') is not None:
            temp_model = UpdateJobConfigParam()
            self.update_job_config_param = temp_model.from_map(m['updateJobConfigParam'])
        return self


class HotUpdateJobStatus(TeaModel):
    def __init__(
        self,
        failure: HotUpdateJobFailureInfo = None,
        request_id: str = None,
        status: str = None,
    ):
        self.failure = failure
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.failure:
            self.failure.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure is not None:
            result['failure'] = self.failure.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failure') is not None:
            temp_model = HotUpdateJobFailureInfo()
            self.failure = temp_model.from_map(m['failure'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class HotUpdateJobResult(TeaModel):
    def __init__(
        self,
        hot_update_params: HotUpdateJobParams = None,
        job_hot_update_id: str = None,
        job_id: str = None,
        status: HotUpdateJobStatus = None,
        target_resource_setting: BriefResourceSetting = None,
    ):
        self.hot_update_params = hot_update_params
        self.job_hot_update_id = job_hot_update_id
        self.job_id = job_id
        self.status = status
        self.target_resource_setting = target_resource_setting

    def validate(self):
        if self.hot_update_params:
            self.hot_update_params.validate()
        if self.status:
            self.status.validate()
        if self.target_resource_setting:
            self.target_resource_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hot_update_params is not None:
            result['hotUpdateParams'] = self.hot_update_params.to_map()
        if self.job_hot_update_id is not None:
            result['jobHotUpdateId'] = self.job_hot_update_id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.target_resource_setting is not None:
            result['targetResourceSetting'] = self.target_resource_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotUpdateParams') is not None:
            temp_model = HotUpdateJobParams()
            self.hot_update_params = temp_model.from_map(m['hotUpdateParams'])
        if m.get('jobHotUpdateId') is not None:
            self.job_hot_update_id = m.get('jobHotUpdateId')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('status') is not None:
            temp_model = HotUpdateJobStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('targetResourceSetting') is not None:
            temp_model = BriefResourceSetting()
            self.target_resource_setting = temp_model.from_map(m['targetResourceSetting'])
        return self


class JobMetric(TeaModel):
    def __init__(
        self,
        total_cpu: float = None,
        total_memory_byte: int = None,
    ):
        self.total_cpu = total_cpu
        self.total_memory_byte = total_memory_byte

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_cpu is not None:
            result['totalCpu'] = self.total_cpu
        if self.total_memory_byte is not None:
            result['totalMemoryByte'] = self.total_memory_byte
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('totalCpu') is not None:
            self.total_cpu = m.get('totalCpu')
        if m.get('totalMemoryByte') is not None:
            self.total_memory_byte = m.get('totalMemoryByte')
        return self


class JobFailure(TeaModel):
    def __init__(
        self,
        failed_at: int = None,
        message: str = None,
        reason: str = None,
    ):
        self.failed_at = failed_at
        self.message = message
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_at is not None:
            result['failedAt'] = self.failed_at
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedAt') is not None:
            self.failed_at = m.get('failedAt')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class JobStatusRunning(TeaModel):
    def __init__(
        self,
        observed_flink_job_restarts: int = None,
        observed_flink_job_status: str = None,
    ):
        self.observed_flink_job_restarts = observed_flink_job_restarts
        self.observed_flink_job_status = observed_flink_job_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.observed_flink_job_restarts is not None:
            result['observedFlinkJobRestarts'] = self.observed_flink_job_restarts
        if self.observed_flink_job_status is not None:
            result['observedFlinkJobStatus'] = self.observed_flink_job_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('observedFlinkJobRestarts') is not None:
            self.observed_flink_job_restarts = m.get('observedFlinkJobRestarts')
        if m.get('observedFlinkJobStatus') is not None:
            self.observed_flink_job_status = m.get('observedFlinkJobStatus')
        return self


class JobStatus(TeaModel):
    def __init__(
        self,
        current_job_status: str = None,
        failure: JobFailure = None,
        health_score: int = None,
        risk_level: str = None,
        running: JobStatusRunning = None,
    ):
        self.current_job_status = current_job_status
        self.failure = failure
        self.health_score = health_score
        self.risk_level = risk_level
        self.running = running

    def validate(self):
        if self.failure:
            self.failure.validate()
        if self.running:
            self.running.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status
        if self.failure is not None:
            result['failure'] = self.failure.to_map()
        if self.health_score is not None:
            result['healthScore'] = self.health_score
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.running is not None:
            result['running'] = self.running.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')
        if m.get('failure') is not None:
            temp_model = JobFailure()
            self.failure = temp_model.from_map(m['failure'])
        if m.get('healthScore') is not None:
            self.health_score = m.get('healthScore')
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('running') is not None:
            temp_model = JobStatusRunning()
            self.running = temp_model.from_map(m['running'])
        return self


class Job(TeaModel):
    def __init__(
        self,
        artifact: Artifact = None,
        batch_resource_setting: BatchResourceSetting = None,
        created_at: str = None,
        creator: str = None,
        creator_name: str = None,
        deployment_id: str = None,
        deployment_name: str = None,
        end_time: int = None,
        engine_version: str = None,
        execution_mode: str = None,
        flink_conf: Dict[str, Any] = None,
        job_id: str = None,
        local_variables: List[LocalVariable] = None,
        logging: Logging = None,
        metric: JobMetric = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        namespace: str = None,
        restore_strategy: DeploymentRestoreStrategy = None,
        session_cluster_name: str = None,
        start_time: int = None,
        status: JobStatus = None,
        streaming_resource_setting: StreamingResourceSetting = None,
        user_flink_conf: Dict[str, Any] = None,
        workspace: str = None,
    ):
        self.artifact = artifact
        self.batch_resource_setting = batch_resource_setting
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_id = deployment_id
        self.deployment_name = deployment_name
        self.end_time = end_time
        self.engine_version = engine_version
        self.execution_mode = execution_mode
        self.flink_conf = flink_conf
        self.job_id = job_id
        self.local_variables = local_variables
        self.logging = logging
        self.metric = metric
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.namespace = namespace
        self.restore_strategy = restore_strategy
        self.session_cluster_name = session_cluster_name
        self.start_time = start_time
        self.status = status
        self.streaming_resource_setting = streaming_resource_setting
        self.user_flink_conf = user_flink_conf
        self.workspace = workspace

    def validate(self):
        if self.artifact:
            self.artifact.validate()
        if self.batch_resource_setting:
            self.batch_resource_setting.validate()
        if self.local_variables:
            for k in self.local_variables:
                if k:
                    k.validate()
        if self.logging:
            self.logging.validate()
        if self.metric:
            self.metric.validate()
        if self.restore_strategy:
            self.restore_strategy.validate()
        if self.status:
            self.status.validate()
        if self.streaming_resource_setting:
            self.streaming_resource_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact is not None:
            result['artifact'] = self.artifact.to_map()
        if self.batch_resource_setting is not None:
            result['batchResourceSetting'] = self.batch_resource_setting.to_map()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode
        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf
        if self.job_id is not None:
            result['jobId'] = self.job_id
        result['localVariables'] = []
        if self.local_variables is not None:
            for k in self.local_variables:
                result['localVariables'].append(k.to_map() if k else None)
        if self.logging is not None:
            result['logging'] = self.logging.to_map()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.restore_strategy is not None:
            result['restoreStrategy'] = self.restore_strategy.to_map()
        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.streaming_resource_setting is not None:
            result['streamingResourceSetting'] = self.streaming_resource_setting.to_map()
        if self.user_flink_conf is not None:
            result['userFlinkConf'] = self.user_flink_conf
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifact') is not None:
            temp_model = Artifact()
            self.artifact = temp_model.from_map(m['artifact'])
        if m.get('batchResourceSetting') is not None:
            temp_model = BatchResourceSetting()
            self.batch_resource_setting = temp_model.from_map(m['batchResourceSetting'])
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')
        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        self.local_variables = []
        if m.get('localVariables') is not None:
            for k in m.get('localVariables'):
                temp_model = LocalVariable()
                self.local_variables.append(temp_model.from_map(k))
        if m.get('logging') is not None:
            temp_model = Logging()
            self.logging = temp_model.from_map(m['logging'])
        if m.get('metric') is not None:
            temp_model = JobMetric()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('restoreStrategy') is not None:
            temp_model = DeploymentRestoreStrategy()
            self.restore_strategy = temp_model.from_map(m['restoreStrategy'])
        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            temp_model = JobStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('streamingResourceSetting') is not None:
            temp_model = StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m['streamingResourceSetting'])
        if m.get('userFlinkConf') is not None:
            self.user_flink_conf = m.get('userFlinkConf')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class JobDiagnosisSymptom(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        recommendation: str = None,
    ):
        self.description = description
        self.name = name
        self.recommendation = recommendation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.recommendation is not None:
            result['recommendation'] = self.recommendation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('recommendation') is not None:
            self.recommendation = m.get('recommendation')
        return self


class JobDiagnosisSymptoms(TeaModel):
    def __init__(
        self,
        autopilot: JobDiagnosisSymptom = None,
        others: List[JobDiagnosisSymptom] = None,
        runtime: List[JobDiagnosisSymptom] = None,
        startup: List[JobDiagnosisSymptom] = None,
        state: List[JobDiagnosisSymptom] = None,
        troubleshooting: List[JobDiagnosisSymptom] = None,
    ):
        self.autopilot = autopilot
        self.others = others
        self.runtime = runtime
        self.startup = startup
        self.state = state
        self.troubleshooting = troubleshooting

    def validate(self):
        if self.autopilot:
            self.autopilot.validate()
        if self.others:
            for k in self.others:
                if k:
                    k.validate()
        if self.runtime:
            for k in self.runtime:
                if k:
                    k.validate()
        if self.startup:
            for k in self.startup:
                if k:
                    k.validate()
        if self.state:
            for k in self.state:
                if k:
                    k.validate()
        if self.troubleshooting:
            for k in self.troubleshooting:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.autopilot is not None:
            result['autopilot'] = self.autopilot.to_map()
        result['others'] = []
        if self.others is not None:
            for k in self.others:
                result['others'].append(k.to_map() if k else None)
        result['runtime'] = []
        if self.runtime is not None:
            for k in self.runtime:
                result['runtime'].append(k.to_map() if k else None)
        result['startup'] = []
        if self.startup is not None:
            for k in self.startup:
                result['startup'].append(k.to_map() if k else None)
        result['state'] = []
        if self.state is not None:
            for k in self.state:
                result['state'].append(k.to_map() if k else None)
        result['troubleshooting'] = []
        if self.troubleshooting is not None:
            for k in self.troubleshooting:
                result['troubleshooting'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autopilot') is not None:
            temp_model = JobDiagnosisSymptom()
            self.autopilot = temp_model.from_map(m['autopilot'])
        self.others = []
        if m.get('others') is not None:
            for k in m.get('others'):
                temp_model = JobDiagnosisSymptom()
                self.others.append(temp_model.from_map(k))
        self.runtime = []
        if m.get('runtime') is not None:
            for k in m.get('runtime'):
                temp_model = JobDiagnosisSymptom()
                self.runtime.append(temp_model.from_map(k))
        self.startup = []
        if m.get('startup') is not None:
            for k in m.get('startup'):
                temp_model = JobDiagnosisSymptom()
                self.startup.append(temp_model.from_map(k))
        self.state = []
        if m.get('state') is not None:
            for k in m.get('state'):
                temp_model = JobDiagnosisSymptom()
                self.state.append(temp_model.from_map(k))
        self.troubleshooting = []
        if m.get('troubleshooting') is not None:
            for k in m.get('troubleshooting'):
                temp_model = JobDiagnosisSymptom()
                self.troubleshooting.append(temp_model.from_map(k))
        return self


class JobDiagnosis(TeaModel):
    def __init__(
        self,
        diagnose_id: str = None,
        diagnose_time: int = None,
        namespace: str = None,
        risk_level: str = None,
        symptoms: JobDiagnosisSymptoms = None,
        workspace: str = None,
    ):
        self.diagnose_id = diagnose_id
        self.diagnose_time = diagnose_time
        self.namespace = namespace
        self.risk_level = risk_level
        self.symptoms = symptoms
        self.workspace = workspace

    def validate(self):
        if self.symptoms:
            self.symptoms.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnose_id is not None:
            result['diagnoseId'] = self.diagnose_id
        if self.diagnose_time is not None:
            result['diagnoseTime'] = self.diagnose_time
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.symptoms is not None:
            result['symptoms'] = self.symptoms.to_map()
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diagnoseId') is not None:
            self.diagnose_id = m.get('diagnoseId')
        if m.get('diagnoseTime') is not None:
            self.diagnose_time = m.get('diagnoseTime')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('symptoms') is not None:
            temp_model = JobDiagnosisSymptoms()
            self.symptoms = temp_model.from_map(m['symptoms'])
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class JobInfo(TeaModel):
    def __init__(
        self,
        id: str = None,
        properties: Dict[str, Any] = None,
    ):
        self.id = id
        self.properties = properties

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.properties is not None:
            result['properties'] = self.properties
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        return self


class JobStartParameters(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        job_id: str = None,
        local_variables: List[LocalVariable] = None,
        resource_queue_name: str = None,
        restore_strategy: DeploymentRestoreStrategy = None,
    ):
        self.deployment_id = deployment_id
        self.job_id = job_id
        self.local_variables = local_variables
        self.resource_queue_name = resource_queue_name
        self.restore_strategy = restore_strategy

    def validate(self):
        if self.local_variables:
            for k in self.local_variables:
                if k:
                    k.validate()
        if self.restore_strategy:
            self.restore_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        result['localVariables'] = []
        if self.local_variables is not None:
            for k in self.local_variables:
                result['localVariables'].append(k.to_map() if k else None)
        if self.resource_queue_name is not None:
            result['resourceQueueName'] = self.resource_queue_name
        if self.restore_strategy is not None:
            result['restoreStrategy'] = self.restore_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        self.local_variables = []
        if m.get('localVariables') is not None:
            for k in m.get('localVariables'):
                temp_model = LocalVariable()
                self.local_variables.append(temp_model.from_map(k))
        if m.get('resourceQueueName') is not None:
            self.resource_queue_name = m.get('resourceQueueName')
        if m.get('restoreStrategy') is not None:
            temp_model = DeploymentRestoreStrategy()
            self.restore_strategy = temp_model.from_map(m['restoreStrategy'])
        return self


class LineageColumn(TeaModel):
    def __init__(
        self,
        column_name: str = None,
        column_native_type: str = None,
        column_type: str = None,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        id: str = None,
        modified_at: int = None,
        modifier: str = None,
        nullable: bool = None,
    ):
        self.column_name = column_name
        self.column_native_type = column_native_type
        self.column_type = column_type
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.id = id
        self.modified_at = modified_at
        self.modifier = modifier
        self.nullable = nullable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.column_name is not None:
            result['columnName'] = self.column_name
        if self.column_native_type is not None:
            result['columnNativeType'] = self.column_native_type
        if self.column_type is not None:
            result['columnType'] = self.column_type
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.nullable is not None:
            result['nullable'] = self.nullable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnName') is not None:
            self.column_name = m.get('columnName')
        if m.get('columnNativeType') is not None:
            self.column_native_type = m.get('columnNativeType')
        if m.get('columnType') is not None:
            self.column_type = m.get('columnType')
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        return self


class LineageTable(TeaModel):
    def __init__(
        self,
        columns: List[LineageColumn] = None,
        id: str = None,
        properties: Dict[str, Any] = None,
        table_name: str = None,
        with_: Dict[str, Any] = None,
    ):
        self.columns = columns
        self.id = id
        self.properties = properties
        self.table_name = table_name
        self.with_ = with_

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['columns'].append(k.to_map() if k else None)
        if self.id is not None:
            result['id'] = self.id
        if self.properties is not None:
            result['properties'] = self.properties
        if self.table_name is not None:
            result['tableName'] = self.table_name
        if self.with_ is not None:
            result['with'] = self.with_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k in m.get('columns'):
                temp_model = LineageColumn()
                self.columns.append(temp_model.from_map(k))
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        if m.get('with') is not None:
            self.with_ = m.get('with')
        return self


class Node(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        connector: str = None,
        database_name: str = None,
        id: str = None,
        is_temporary: bool = None,
        tables: List[LineageTable] = None,
    ):
        self.catalog_name = catalog_name
        self.connector = connector
        self.database_name = database_name
        self.id = id
        self.is_temporary = is_temporary
        self.tables = tables

    def validate(self):
        if self.tables:
            for k in self.tables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name
        if self.connector is not None:
            result['connector'] = self.connector
        if self.database_name is not None:
            result['databaseName'] = self.database_name
        if self.id is not None:
            result['id'] = self.id
        if self.is_temporary is not None:
            result['isTemporary'] = self.is_temporary
        result['tables'] = []
        if self.tables is not None:
            for k in self.tables:
                result['tables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')
        if m.get('connector') is not None:
            self.connector = m.get('connector')
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('isTemporary') is not None:
            self.is_temporary = m.get('isTemporary')
        self.tables = []
        if m.get('tables') is not None:
            for k in m.get('tables'):
                temp_model = LineageTable()
                self.tables.append(temp_model.from_map(k))
        return self


class LineageInfo(TeaModel):
    def __init__(
        self,
        edges: Edge = None,
        job_infos: List[JobInfo] = None,
        nodes: List[Node] = None,
    ):
        self.edges = edges
        self.job_infos = job_infos
        self.nodes = nodes

    def validate(self):
        if self.edges:
            self.edges.validate()
        if self.job_infos:
            for k in self.job_infos:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edges is not None:
            result['edges'] = self.edges.to_map()
        result['jobInfos'] = []
        if self.job_infos is not None:
            for k in self.job_infos:
                result['jobInfos'].append(k.to_map() if k else None)
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edges') is not None:
            temp_model = Edge()
            self.edges = temp_model.from_map(m['edges'])
        self.job_infos = []
        if m.get('jobInfos') is not None:
            for k in m.get('jobInfos'):
                temp_model = JobInfo()
                self.job_infos.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = Node()
                self.nodes.append(temp_model.from_map(k))
        return self


class Member(TeaModel):
    def __init__(
        self,
        member: str = None,
        role: str = None,
    ):
        # This parameter is required.
        self.member = member
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member is not None:
            result['member'] = self.member
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('member') is not None:
            self.member = m.get('member')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class NodeExecutionContextDTO(TeaModel):
    def __init__(
        self,
        context: Dict[str, str] = None,
    ):
        self.context = context

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            self.context = m.get('context')
        return self


class NodeExecutionStatusDTO(TeaModel):
    def __init__(
        self,
        execution_id: str = None,
        namespace: str = None,
        resource_id: str = None,
        status: str = None,
        type: str = None,
        workspace: str = None,
    ):
        self.execution_id = execution_id
        self.namespace = namespace
        self.resource_id = resource_id
        self.status = status
        self.type = type
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_id is not None:
            result['executionId'] = self.execution_id
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class PeriodicSchedulingPolicy(TeaModel):
    def __init__(
        self,
        is_finished: bool = None,
        only_once_trigger_time: int = None,
        only_once_trigger_time_is_expired: bool = None,
        periodic_scheduling_level: str = None,
        periodic_scheduling_values: List[int] = None,
        periodic_trigger_time: int = None,
        resource_setting: BriefResourceSetting = None,
    ):
        self.is_finished = is_finished
        self.only_once_trigger_time = only_once_trigger_time
        self.only_once_trigger_time_is_expired = only_once_trigger_time_is_expired
        self.periodic_scheduling_level = periodic_scheduling_level
        self.periodic_scheduling_values = periodic_scheduling_values
        self.periodic_trigger_time = periodic_trigger_time
        self.resource_setting = resource_setting

    def validate(self):
        if self.resource_setting:
            self.resource_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_finished is not None:
            result['isFinished'] = self.is_finished
        if self.only_once_trigger_time is not None:
            result['onlyOnceTriggerTime'] = self.only_once_trigger_time
        if self.only_once_trigger_time_is_expired is not None:
            result['onlyOnceTriggerTimeIsExpired'] = self.only_once_trigger_time_is_expired
        if self.periodic_scheduling_level is not None:
            result['periodicSchedulingLevel'] = self.periodic_scheduling_level
        if self.periodic_scheduling_values is not None:
            result['periodicSchedulingValues'] = self.periodic_scheduling_values
        if self.periodic_trigger_time is not None:
            result['periodicTriggerTime'] = self.periodic_trigger_time
        if self.resource_setting is not None:
            result['resourceSetting'] = self.resource_setting.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isFinished') is not None:
            self.is_finished = m.get('isFinished')
        if m.get('onlyOnceTriggerTime') is not None:
            self.only_once_trigger_time = m.get('onlyOnceTriggerTime')
        if m.get('onlyOnceTriggerTimeIsExpired') is not None:
            self.only_once_trigger_time_is_expired = m.get('onlyOnceTriggerTimeIsExpired')
        if m.get('periodicSchedulingLevel') is not None:
            self.periodic_scheduling_level = m.get('periodicSchedulingLevel')
        if m.get('periodicSchedulingValues') is not None:
            self.periodic_scheduling_values = m.get('periodicSchedulingValues')
        if m.get('periodicTriggerTime') is not None:
            self.periodic_trigger_time = m.get('periodicTriggerTime')
        if m.get('resourceSetting') is not None:
            temp_model = BriefResourceSetting()
            self.resource_setting = temp_model.from_map(m['resourceSetting'])
        return self


class Resource(TeaModel):
    def __init__(
        self,
        elastic_resource: ResourceSpec = None,
        fixed_resource: ResourceSpec = None,
    ):
        self.elastic_resource = elastic_resource
        # This parameter is required.
        self.fixed_resource = fixed_resource

    def validate(self):
        if self.elastic_resource:
            self.elastic_resource.validate()
        if self.fixed_resource:
            self.fixed_resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elastic_resource is not None:
            result['elasticResource'] = self.elastic_resource.to_map()
        if self.fixed_resource is not None:
            result['fixedResource'] = self.fixed_resource.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elasticResource') is not None:
            temp_model = ResourceSpec()
            self.elastic_resource = temp_model.from_map(m['elasticResource'])
        if m.get('fixedResource') is not None:
            temp_model = ResourceSpec()
            self.fixed_resource = temp_model.from_map(m['fixedResource'])
        return self


class SavepointFailure(TeaModel):
    def __init__(
        self,
        failed_at: int = None,
        message: str = None,
        reason: str = None,
    ):
        self.failed_at = failed_at
        self.message = message
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_at is not None:
            result['failedAt'] = self.failed_at
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedAt') is not None:
            self.failed_at = m.get('failedAt')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class SavepointStatus(TeaModel):
    def __init__(
        self,
        failure: SavepointFailure = None,
        state: str = None,
    ):
        self.failure = failure
        self.state = state

    def validate(self):
        if self.failure:
            self.failure.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failure is not None:
            result['failure'] = self.failure.to_map()
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failure') is not None:
            temp_model = SavepointFailure()
            self.failure = temp_model.from_map(m['failure'])
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class Savepoint(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        deployment_id: str = None,
        description: str = None,
        job_id: str = None,
        modified_at: int = None,
        namespace: str = None,
        native_format: bool = None,
        savepoint_id: str = None,
        savepoint_location: str = None,
        savepoint_origin: str = None,
        status: SavepointStatus = None,
        stop_with_drain_enabled: bool = None,
    ):
        self.created_at = created_at
        self.deployment_id = deployment_id
        self.description = description
        self.job_id = job_id
        self.modified_at = modified_at
        self.namespace = namespace
        self.native_format = native_format
        self.savepoint_id = savepoint_id
        self.savepoint_location = savepoint_location
        self.savepoint_origin = savepoint_origin
        self.status = status
        self.stop_with_drain_enabled = stop_with_drain_enabled

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.description is not None:
            result['description'] = self.description
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.native_format is not None:
            result['nativeFormat'] = self.native_format
        if self.savepoint_id is not None:
            result['savepointId'] = self.savepoint_id
        if self.savepoint_location is not None:
            result['savepointLocation'] = self.savepoint_location
        if self.savepoint_origin is not None:
            result['savepointOrigin'] = self.savepoint_origin
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.stop_with_drain_enabled is not None:
            result['stopWithDrainEnabled'] = self.stop_with_drain_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('nativeFormat') is not None:
            self.native_format = m.get('nativeFormat')
        if m.get('savepointId') is not None:
            self.savepoint_id = m.get('savepointId')
        if m.get('savepointLocation') is not None:
            self.savepoint_location = m.get('savepointLocation')
        if m.get('savepointOrigin') is not None:
            self.savepoint_origin = m.get('savepointOrigin')
        if m.get('status') is not None:
            temp_model = SavepointStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('stopWithDrainEnabled') is not None:
            self.stop_with_drain_enabled = m.get('stopWithDrainEnabled')
        return self


class ScheduledPlan(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        creator_name: str = None,
        deployment_id: str = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        origin: str = None,
        periodic_scheduling_policies: List[PeriodicSchedulingPolicy] = None,
        scheduled_plan_id: str = None,
        status: str = None,
        updated_by_user: bool = None,
        workspace: str = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_id = deployment_id
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
        self.origin = origin
        self.periodic_scheduling_policies = periodic_scheduling_policies
        self.scheduled_plan_id = scheduled_plan_id
        self.status = status
        self.updated_by_user = updated_by_user
        self.workspace = workspace

    def validate(self):
        if self.periodic_scheduling_policies:
            for k in self.periodic_scheduling_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.origin is not None:
            result['origin'] = self.origin
        result['periodicSchedulingPolicies'] = []
        if self.periodic_scheduling_policies is not None:
            for k in self.periodic_scheduling_policies:
                result['periodicSchedulingPolicies'].append(k.to_map() if k else None)
        if self.scheduled_plan_id is not None:
            result['scheduledPlanId'] = self.scheduled_plan_id
        if self.status is not None:
            result['status'] = self.status
        if self.updated_by_user is not None:
            result['updatedByUser'] = self.updated_by_user
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('origin') is not None:
            self.origin = m.get('origin')
        self.periodic_scheduling_policies = []
        if m.get('periodicSchedulingPolicies') is not None:
            for k in m.get('periodicSchedulingPolicies'):
                temp_model = PeriodicSchedulingPolicy()
                self.periodic_scheduling_policies.append(temp_model.from_map(k))
        if m.get('scheduledPlanId') is not None:
            self.scheduled_plan_id = m.get('scheduledPlanId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updatedByUser') is not None:
            self.updated_by_user = m.get('updatedByUser')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ScheduledPlanAppliedInfo(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        expected_state: str = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        namespace: str = None,
        scheduled_plan_id: str = None,
        scheduled_plan_name: str = None,
        status_state: str = None,
        workspace: str = None,
    ):
        self.deployment_id = deployment_id
        self.expected_state = expected_state
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.namespace = namespace
        self.scheduled_plan_id = scheduled_plan_id
        self.scheduled_plan_name = scheduled_plan_name
        self.status_state = status_state
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.expected_state is not None:
            result['expectedState'] = self.expected_state
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.scheduled_plan_id is not None:
            result['scheduledPlanId'] = self.scheduled_plan_id
        if self.scheduled_plan_name is not None:
            result['scheduledPlanName'] = self.scheduled_plan_name
        if self.status_state is not None:
            result['statusState'] = self.status_state
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('expectedState') is not None:
            self.expected_state = m.get('expectedState')
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('scheduledPlanId') is not None:
            self.scheduled_plan_id = m.get('scheduledPlanId')
        if m.get('scheduledPlanName') is not None:
            self.scheduled_plan_name = m.get('scheduledPlanName')
        if m.get('statusState') is not None:
            self.status_state = m.get('statusState')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ScheduledPlanExecutedStatus(TeaModel):
    def __init__(
        self,
        restart_type: str = None,
        status_state: str = None,
    ):
        self.restart_type = restart_type
        self.status_state = status_state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restart_type is not None:
            result['restartType'] = self.restart_type
        if self.status_state is not None:
            result['statusState'] = self.status_state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('restartType') is not None:
            self.restart_type = m.get('restartType')
        if m.get('statusState') is not None:
            self.status_state = m.get('statusState')
        return self


class ScheduledPlanExecutedInfo(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        creator_name: str = None,
        deployment_id: str = None,
        job_resource_upgrading_id: str = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        origin: str = None,
        origin_job_id: str = None,
        status: ScheduledPlanExecutedStatus = None,
        workspace: str = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_id = deployment_id
        self.job_resource_upgrading_id = job_resource_upgrading_id
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
        self.origin = origin
        self.origin_job_id = origin_job_id
        self.status = status
        self.workspace = workspace

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.job_resource_upgrading_id is not None:
            result['jobResourceUpgradingId'] = self.job_resource_upgrading_id
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.origin is not None:
            result['origin'] = self.origin
        if self.origin_job_id is not None:
            result['originJobId'] = self.origin_job_id
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('jobResourceUpgradingId') is not None:
            self.job_resource_upgrading_id = m.get('jobResourceUpgradingId')
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('origin') is not None:
            self.origin = m.get('origin')
        if m.get('originJobId') is not None:
            self.origin_job_id = m.get('originJobId')
        if m.get('status') is not None:
            temp_model = ScheduledPlanExecutedStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class SessionClusterFailureInfo(TeaModel):
    def __init__(
        self,
        failed_at: int = None,
        message: str = None,
        reason: str = None,
    ):
        self.failed_at = failed_at
        self.message = message
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.failed_at is not None:
            result['failedAt'] = self.failed_at
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failedAt') is not None:
            self.failed_at = m.get('failedAt')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class SessionClusterRunningInfo(TeaModel):
    def __init__(
        self,
        last_update_time: int = None,
        reference_deployment_ids: List[str] = None,
        started_at: int = None,
    ):
        self.last_update_time = last_update_time
        self.reference_deployment_ids = reference_deployment_ids
        self.started_at = started_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.reference_deployment_ids is not None:
            result['referenceDeploymentIds'] = self.reference_deployment_ids
        if self.started_at is not None:
            result['startedAt'] = self.started_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('referenceDeploymentIds') is not None:
            self.reference_deployment_ids = m.get('referenceDeploymentIds')
        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')
        return self


class SessionClusterStatus(TeaModel):
    def __init__(
        self,
        current_session_cluster_status: str = None,
        failure: SessionClusterFailureInfo = None,
        running: SessionClusterRunningInfo = None,
    ):
        self.current_session_cluster_status = current_session_cluster_status
        self.failure = failure
        self.running = running

    def validate(self):
        if self.failure:
            self.failure.validate()
        if self.running:
            self.running.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_session_cluster_status is not None:
            result['currentSessionClusterStatus'] = self.current_session_cluster_status
        if self.failure is not None:
            result['failure'] = self.failure.to_map()
        if self.running is not None:
            result['running'] = self.running.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentSessionClusterStatus') is not None:
            self.current_session_cluster_status = m.get('currentSessionClusterStatus')
        if m.get('failure') is not None:
            temp_model = SessionClusterFailureInfo()
            self.failure = temp_model.from_map(m['failure'])
        if m.get('running') is not None:
            temp_model = SessionClusterRunningInfo()
            self.running = temp_model.from_map(m['running'])
        return self


class SessionCluster(TeaModel):
    def __init__(
        self,
        basic_resource_setting: BasicResourceSetting = None,
        created_at: int = None,
        creator: str = None,
        creator_name: str = None,
        deployment_target_name: str = None,
        engine_version: str = None,
        flink_conf: Dict[str, Any] = None,
        labels: Dict[str, Any] = None,
        logging: Logging = None,
        modified_at: int = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
        session_cluster_id: str = None,
        status: SessionClusterStatus = None,
        workspace: str = None,
    ):
        self.basic_resource_setting = basic_resource_setting
        self.created_at = created_at
        self.creator = creator
        self.creator_name = creator_name
        self.deployment_target_name = deployment_target_name
        self.engine_version = engine_version
        self.flink_conf = flink_conf
        self.labels = labels
        self.logging = logging
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
        self.session_cluster_id = session_cluster_id
        self.status = status
        self.workspace = workspace

    def validate(self):
        if self.basic_resource_setting:
            self.basic_resource_setting.validate()
        if self.logging:
            self.logging.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic_resource_setting is not None:
            result['basicResourceSetting'] = self.basic_resource_setting.to_map()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name
        if self.deployment_target_name is not None:
            result['deploymentTargetName'] = self.deployment_target_name
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.flink_conf is not None:
            result['flinkConf'] = self.flink_conf
        if self.labels is not None:
            result['labels'] = self.labels
        if self.logging is not None:
            result['logging'] = self.logging.to_map()
        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('basicResourceSetting') is not None:
            temp_model = BasicResourceSetting()
            self.basic_resource_setting = temp_model.from_map(m['basicResourceSetting'])
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')
        if m.get('deploymentTargetName') is not None:
            self.deployment_target_name = m.get('deploymentTargetName')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('flinkConf') is not None:
            self.flink_conf = m.get('flinkConf')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('logging') is not None:
            temp_model = Logging()
            self.logging = temp_model.from_map(m['logging'])
        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
        if m.get('status') is not None:
            temp_model = SessionClusterStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class SqlStatementExecuteResult(TeaModel):
    def __init__(
        self,
        error_details: ErrorDetails = None,
        execute_success: bool = None,
        statement: str = None,
    ):
        self.error_details = error_details
        self.execute_success = execute_success
        self.statement = statement

    def validate(self):
        if self.error_details:
            self.error_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_details is not None:
            result['errorDetails'] = self.error_details.to_map()
        if self.execute_success is not None:
            result['executeSuccess'] = self.execute_success
        if self.statement is not None:
            result['statement'] = self.statement
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorDetails') is not None:
            temp_model = ErrorDetails()
            self.error_details = temp_model.from_map(m['errorDetails'])
        if m.get('executeSuccess') is not None:
            self.execute_success = m.get('executeSuccess')
        if m.get('statement') is not None:
            self.statement = m.get('statement')
        return self


class SqlStatementValidationResult(TeaModel):
    def __init__(
        self,
        error_details: ErrorDetails = None,
        message: str = None,
        success: bool = None,
        validation_result: str = None,
    ):
        self.error_details = error_details
        self.message = message
        self.success = success
        self.validation_result = validation_result

    def validate(self):
        if self.error_details:
            self.error_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_details is not None:
            result['errorDetails'] = self.error_details.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.validation_result is not None:
            result['validationResult'] = self.validation_result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorDetails') is not None:
            temp_model = ErrorDetails()
            self.error_details = temp_model.from_map(m['errorDetails'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('validationResult') is not None:
            self.validation_result = m.get('validationResult')
        return self


class SqlStatementWithContext(TeaModel):
    def __init__(
        self,
        additional_dependencies: List[str] = None,
        batch_mode: bool = None,
        flink_configuration: Dict[str, Any] = None,
        statement: str = None,
        version_name: str = None,
    ):
        self.additional_dependencies = additional_dependencies
        # This parameter is required.
        self.batch_mode = batch_mode
        self.flink_configuration = flink_configuration
        # This parameter is required.
        self.statement = statement
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_dependencies is not None:
            result['additionalDependencies'] = self.additional_dependencies
        if self.batch_mode is not None:
            result['batchMode'] = self.batch_mode
        if self.flink_configuration is not None:
            result['flinkConfiguration'] = self.flink_configuration
        if self.statement is not None:
            result['statement'] = self.statement
        if self.version_name is not None:
            result['versionName'] = self.version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalDependencies') is not None:
            self.additional_dependencies = m.get('additionalDependencies')
        if m.get('batchMode') is not None:
            self.batch_mode = m.get('batchMode')
        if m.get('flinkConfiguration') is not None:
            self.flink_configuration = m.get('flinkConfiguration')
        if m.get('statement') is not None:
            self.statement = m.get('statement')
        if m.get('versionName') is not None:
            self.version_name = m.get('versionName')
        return self


class StartJobRequestBody(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        resource_setting_spec: BriefResourceSetting = None,
        restore_strategy: DeploymentRestoreStrategy = None,
    ):
        self.deployment_id = deployment_id
        self.resource_setting_spec = resource_setting_spec
        self.restore_strategy = restore_strategy

    def validate(self):
        if self.resource_setting_spec:
            self.resource_setting_spec.validate()
        if self.restore_strategy:
            self.restore_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.resource_setting_spec is not None:
            result['resourceSettingSpec'] = self.resource_setting_spec.to_map()
        if self.restore_strategy is not None:
            result['restoreStrategy'] = self.restore_strategy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('resourceSettingSpec') is not None:
            temp_model = BriefResourceSetting()
            self.resource_setting_spec = temp_model.from_map(m['resourceSettingSpec'])
        if m.get('restoreStrategy') is not None:
            temp_model = DeploymentRestoreStrategy()
            self.restore_strategy = temp_model.from_map(m['restoreStrategy'])
        return self


class StopJobRequestBody(TeaModel):
    def __init__(
        self,
        stop_strategy: str = None,
    ):
        # This parameter is required.
        self.stop_strategy = stop_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stop_strategy is not None:
            result['stopStrategy'] = self.stop_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stopStrategy') is not None:
            self.stop_strategy = m.get('stopStrategy')
        return self


class TableSchema(TeaModel):
    def __init__(
        self,
        schema: Schema = None,
        table_name: str = None,
    ):
        self.schema = schema
        self.table_name = table_name

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('schema') is not None:
            temp_model = Schema()
            self.schema = temp_model.from_map(m['schema'])
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class SubmitPreview(TeaModel):
    def __init__(
        self,
        query_name: str = None,
        session_id: str = None,
        table_schemas: List[TableSchema] = None,
    ):
        self.query_name = query_name
        self.session_id = session_id
        self.table_schemas = table_schemas

    def validate(self):
        if self.table_schemas:
            for k in self.table_schemas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_name is not None:
            result['queryName'] = self.query_name
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        result['tableSchemas'] = []
        if self.table_schemas is not None:
            for k in self.table_schemas:
                result['tableSchemas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryName') is not None:
            self.query_name = m.get('queryName')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        self.table_schemas = []
        if m.get('tableSchemas') is not None:
            for k in m.get('tableSchemas'):
                temp_model = TableSchema()
                self.table_schemas.append(temp_model.from_map(k))
        return self


class SubmitPreviewResult(TeaModel):
    def __init__(
        self,
        query_id: str = None,
        session_id: str = None,
        table_schemas: List[TableSchema] = None,
    ):
        self.query_id = query_id
        self.session_id = session_id
        self.table_schemas = table_schemas

    def validate(self):
        if self.table_schemas:
            for k in self.table_schemas:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['queryId'] = self.query_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        result['tableSchemas'] = []
        if self.table_schemas is not None:
            for k in self.table_schemas:
                result['tableSchemas'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryId') is not None:
            self.query_id = m.get('queryId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        self.table_schemas = []
        if m.get('tableSchemas') is not None:
            for k in m.get('tableSchemas'):
                temp_model = TableSchema()
                self.table_schemas.append(temp_model.from_map(k))
        return self


class Table(TeaModel):
    def __init__(
        self,
        comment: str = None,
        metadata: Dict[str, str] = None,
        name: str = None,
        partition_keys: List[str] = None,
        properties: Dict[str, Any] = None,
        schema: Schema = None,
        table_type: str = None,
    ):
        self.comment = comment
        self.metadata = metadata
        # This parameter is required.
        self.name = name
        self.partition_keys = partition_keys
        self.properties = properties
        self.schema = schema
        # This parameter is required.
        self.table_type = table_type

    def validate(self):
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.metadata is not None:
            result['metadata'] = self.metadata
        if self.name is not None:
            result['name'] = self.name
        if self.partition_keys is not None:
            result['partitionKeys'] = self.partition_keys
        if self.properties is not None:
            result['properties'] = self.properties
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        if self.table_type is not None:
            result['tableType'] = self.table_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('partitionKeys') is not None:
            self.partition_keys = m.get('partitionKeys')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('schema') is not None:
            temp_model = Schema()
            self.schema = temp_model.from_map(m['schema'])
        if m.get('tableType') is not None:
            self.table_type = m.get('tableType')
        return self


class TableMeta(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
        database_name: str = None,
        table_name: str = None,
    ):
        self.catalog_name = catalog_name
        self.database_name = database_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name
        if self.database_name is not None:
            result['databaseName'] = self.database_name
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class UdfFunction(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        function_name: str = None,
        udf_artifact_name: str = None,
    ):
        self.class_name = class_name
        self.function_name = function_name
        self.udf_artifact_name = udf_artifact_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.udf_artifact_name is not None:
            result['udfArtifactName'] = self.udf_artifact_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('udfArtifactName') is not None:
            self.udf_artifact_name = m.get('udfArtifactName')
        return self


class UpdateUdfArtifactResult(TeaModel):
    def __init__(
        self,
        colliding_classes: List[UdfClass] = None,
        message: str = None,
        missing_classes: List[UdfClass] = None,
        udf_artifact: UdfArtifact = None,
        update_success: bool = None,
    ):
        self.colliding_classes = colliding_classes
        self.message = message
        self.missing_classes = missing_classes
        self.udf_artifact = udf_artifact
        self.update_success = update_success

    def validate(self):
        if self.colliding_classes:
            for k in self.colliding_classes:
                if k:
                    k.validate()
        if self.missing_classes:
            for k in self.missing_classes:
                if k:
                    k.validate()
        if self.udf_artifact:
            self.udf_artifact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['collidingClasses'] = []
        if self.colliding_classes is not None:
            for k in self.colliding_classes:
                result['collidingClasses'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        result['missingClasses'] = []
        if self.missing_classes is not None:
            for k in self.missing_classes:
                result['missingClasses'].append(k.to_map() if k else None)
        if self.udf_artifact is not None:
            result['udfArtifact'] = self.udf_artifact.to_map()
        if self.update_success is not None:
            result['updateSuccess'] = self.update_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.colliding_classes = []
        if m.get('collidingClasses') is not None:
            for k in m.get('collidingClasses'):
                temp_model = UdfClass()
                self.colliding_classes.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        self.missing_classes = []
        if m.get('missingClasses') is not None:
            for k in m.get('missingClasses'):
                temp_model = UdfClass()
                self.missing_classes.append(temp_model.from_map(k))
        if m.get('udfArtifact') is not None:
            temp_model = UdfArtifact()
            self.udf_artifact = temp_model.from_map(m['udfArtifact'])
        if m.get('updateSuccess') is not None:
            self.update_success = m.get('updateSuccess')
        return self


class Variable(TeaModel):
    def __init__(
        self,
        description: str = None,
        kind: str = None,
        name: str = None,
        value: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.kind = kind
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ApplyScheduledPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ApplyScheduledPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: ScheduledPlanAppliedInfo = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ScheduledPlanAppliedInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ApplyScheduledPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApplyScheduledPlanResponseBody = None,
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
            temp_model = ApplyScheduledPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelSqlPreviewHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CancelSqlPreviewRequest(TeaModel):
    def __init__(
        self,
        query_id: str = None,
        session_cluster_name: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.query_id = query_id
        # This parameter is required.
        self.session_cluster_name = session_cluster_name
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['queryId'] = self.query_id
        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryId') is not None:
            self.query_id = m.get('queryId')
        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CancelSqlPreviewResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CancelSqlPreviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelSqlPreviewResponseBody = None,
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
            temp_model = CancelSqlPreviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeploymentHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateDeploymentRequest(TeaModel):
    def __init__(
        self,
        body: Deployment = None,
    ):
        # The content of the deployment.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Deployment()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        data: Deployment = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the deployment that you created was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Deployment()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
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


class CreateDeploymentDraftHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateDeploymentDraftRequest(TeaModel):
    def __init__(
        self,
        body: DeploymentDraft = None,
    ):
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DeploymentDraft()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeploymentDraftResponseBody(TeaModel):
    def __init__(
        self,
        data: DeploymentDraft = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploymentDraft()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateDeploymentDraftResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeploymentDraftResponseBody = None,
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
            temp_model = CreateDeploymentDraftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeploymentTargetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateDeploymentTargetRequest(TeaModel):
    def __init__(
        self,
        body: ResourceSpec = None,
        deployment_target_name: str = None,
    ):
        self.body = body
        # This parameter is required.
        self.deployment_target_name = deployment_target_name

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.deployment_target_name is not None:
            result['deploymentTargetName'] = self.deployment_target_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ResourceSpec()
            self.body = temp_model.from_map(m['body'])
        if m.get('deploymentTargetName') is not None:
            self.deployment_target_name = m.get('deploymentTargetName')
        return self


class CreateDeploymentTargetResponseBody(TeaModel):
    def __init__(
        self,
        data: DeploymentTarget = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploymentTarget()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateDeploymentTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeploymentTargetResponseBody = None,
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
            temp_model = CreateDeploymentTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeploymentTargetV2Headers(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateDeploymentTargetV2Request(TeaModel):
    def __init__(
        self,
        body: Resource = None,
        deployment_target_name: str = None,
    ):
        self.body = body
        # This parameter is required.
        self.deployment_target_name = deployment_target_name

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.deployment_target_name is not None:
            result['deploymentTargetName'] = self.deployment_target_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Resource()
            self.body = temp_model.from_map(m['body'])
        if m.get('deploymentTargetName') is not None:
            self.deployment_target_name = m.get('deploymentTargetName')
        return self


class CreateDeploymentTargetV2ResponseBody(TeaModel):
    def __init__(
        self,
        data: DeploymentTarget = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploymentTarget()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateDeploymentTargetV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeploymentTargetV2ResponseBody = None,
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
            temp_model = CreateDeploymentTargetV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFolderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateFolderRequest(TeaModel):
    def __init__(
        self,
        body: Folder = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Folder()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFolderResponseBody(TeaModel):
    def __init__(
        self,
        data: Folder = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Folder()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFolderResponseBody = None,
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
            temp_model = CreateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMemberHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateMemberRequest(TeaModel):
    def __init__(
        self,
        body: Member = None,
    ):
        # The mappings between the ID and permissions of the member.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Member()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMemberResponseBody(TeaModel):
    def __init__(
        self,
        data: Member = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was false, a null value was returned.
        # *   If the value of success was true, the authorization information was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Member()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMemberResponseBody = None,
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
            temp_model = CreateMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSavepointHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateSavepointRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        description: str = None,
        native_format: bool = None,
    ):
        # The deployment ID.
        # 
        # This parameter is required.
        self.deployment_id = deployment_id
        # The description of the savepoint.
        self.description = description
        # Specifies whether to use the native format mode. Valid values:
        # 
        # *   true: The native format mode is used.
        # *   false: The native format mode is not used.
        self.native_format = native_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.description is not None:
            result['description'] = self.description
        if self.native_format is not None:
            result['nativeFormat'] = self.native_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('nativeFormat') is not None:
            self.native_format = m.get('nativeFormat')
        return self


class CreateSavepointResponseBody(TeaModel):
    def __init__(
        self,
        data: Savepoint = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the savepoint that was created was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Savepoint()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSavepointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSavepointResponseBody = None,
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
            temp_model = CreateSavepointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateScheduledPlanRequest(TeaModel):
    def __init__(
        self,
        body: ScheduledPlan = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ScheduledPlan()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduledPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: ScheduledPlan = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ScheduledPlan()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateScheduledPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduledPlanResponseBody = None,
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
            temp_model = CreateScheduledPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSessionClusterHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateSessionClusterRequest(TeaModel):
    def __init__(
        self,
        body: SessionCluster = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SessionCluster()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: SessionCluster = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SessionCluster()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateSessionClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSessionClusterResponseBody = None,
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
            temp_model = CreateSessionClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUdfArtifactHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateUdfArtifactRequest(TeaModel):
    def __init__(
        self,
        body: UdfArtifact = None,
    ):
        # The resource file of the UDF.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UdfArtifact()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUdfArtifactResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateUdfArtifactResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result of creating an artifact configuration for the UDF.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateUdfArtifactResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateUdfArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUdfArtifactResponseBody = None,
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
            temp_model = CreateUdfArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVariableHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateVariableRequest(TeaModel):
    def __init__(
        self,
        body: Variable = None,
    ):
        # The parameter that is used to create the variable.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Variable()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVariableResponseBody(TeaModel):
    def __init__(
        self,
        data: Variable = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the variable that you created was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Variable()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateVariableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVariableResponseBody = None,
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
            temp_model = CreateVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomConnectorHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteCustomConnectorResponseBody(TeaModel):
    def __init__(
        self,
        data: List[TableMeta] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the value of success was true, a list of deployments in which custom connectors were deleted was returned. If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = TableMeta()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteCustomConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomConnectorResponseBody = None,
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
            temp_model = DeleteCustomConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeploymentHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDeploymentResponseBody = None,
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
            temp_model = DeleteDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeploymentDraftHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteDeploymentDraftResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteDeploymentDraftResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDeploymentDraftResponseBody = None,
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
            temp_model = DeleteDeploymentDraftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeploymentTargetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteDeploymentTargetResponseBody(TeaModel):
    def __init__(
        self,
        data: DeploymentTarget = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploymentTarget()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteDeploymentTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDeploymentTargetResponseBody = None,
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
            temp_model = DeleteDeploymentTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFolderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteFolderResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFolderResponseBody = None,
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
            temp_model = DeleteFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteJobResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteJobResponseBody = None,
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
            temp_model = DeleteJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMemberHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteMemberResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMemberResponseBody = None,
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
            temp_model = DeleteMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSavepointHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteSavepointResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteSavepointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSavepointResponseBody = None,
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
            temp_model = DeleteSavepointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduledPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteScheduledPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: ScheduledPlan = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ScheduledPlan()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteScheduledPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScheduledPlanResponseBody = None,
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
            temp_model = DeleteScheduledPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSessionClusterHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: SessionCluster = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SessionCluster()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteSessionClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSessionClusterResponseBody = None,
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
            temp_model = DeleteSessionClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUdfArtifactHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteUdfArtifactResponseBody(TeaModel):
    def __init__(
        self,
        data: DeleteUdfArtifactResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeleteUdfArtifactResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteUdfArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUdfArtifactResponseBody = None,
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
            temp_model = DeleteUdfArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUdfFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteUdfFunctionRequest(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        udf_artifact_name: str = None,
    ):
        # The name of the class that corresponds to the UDF.
        # 
        # This parameter is required.
        self.class_name = class_name
        # The name of the resource that corresponds to the UDF that you want to delete.
        # 
        # This parameter is required.
        self.udf_artifact_name = udf_artifact_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.udf_artifact_name is not None:
            result['udfArtifactName'] = self.udf_artifact_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('udfArtifactName') is not None:
            self.udf_artifact_name = m.get('udfArtifactName')
        return self


class DeleteUdfFunctionResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteUdfFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUdfFunctionResponseBody = None,
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
            temp_model = DeleteUdfFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVariableHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeleteVariableResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteVariableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVariableResponseBody = None,
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
            temp_model = DeleteVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployDeploymentDraftAsyncHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DeployDeploymentDraftAsyncRequest(TeaModel):
    def __init__(
        self,
        body: DraftDeployParams = None,
    ):
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DraftDeployParams()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployDeploymentDraftAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        ticket_id: str = None,
    ):
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['ticketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ticketId') is not None:
            self.ticket_id = m.get('ticketId')
        return self


class DeployDeploymentDraftAsyncResponseBody(TeaModel):
    def __init__(
        self,
        data: DeployDeploymentDraftAsyncResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeployDeploymentDraftAsyncResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeployDeploymentDraftAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployDeploymentDraftAsyncResponseBody = None,
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
            temp_model = DeployDeploymentDraftAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteSqlStatementHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ExecuteSqlStatementRequest(TeaModel):
    def __init__(
        self,
        body: SqlStatementWithContext = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SqlStatementWithContext()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteSqlStatementResponseBody(TeaModel):
    def __init__(
        self,
        data: SqlStatementExecuteResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SqlStatementExecuteResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExecuteSqlStatementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteSqlStatementResponseBody = None,
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
            temp_model = ExecuteSqlStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchSqlPreviewResultsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class FetchSqlPreviewResultsRequest(TeaModel):
    def __init__(
        self,
        query_id: str = None,
        session_cluster_name: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.query_id = query_id
        # This parameter is required.
        self.session_cluster_name = session_cluster_name
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['queryId'] = self.query_id
        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queryId') is not None:
            self.query_id = m.get('queryId')
        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class FetchSqlPreviewResultsResponseBody(TeaModel):
    def __init__(
        self,
        data: FetchResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = FetchResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class FetchSqlPreviewResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchSqlPreviewResultsResponseBody = None,
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
            temp_model = FetchSqlPreviewResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FlinkApiProxyHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class FlinkApiProxyRequest(TeaModel):
    def __init__(
        self,
        flink_api_path: str = None,
        namespace: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The path of the Flink UI.
        # 
        # This parameter is required.
        self.flink_api_path = flink_api_path
        # The name of the namespace.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Valid values:
        # 
        # *   jobs
        # *   sessionclusters
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flink_api_path is not None:
            result['flinkApiPath'] = self.flink_api_path
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flinkApiPath') is not None:
            self.flink_api_path = m.get('flinkApiPath')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class FlinkApiProxyResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the result of the proxy request was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class FlinkApiProxyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FlinkApiProxyResponseBody = None,
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
            temp_model = FlinkApiProxyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateResourcePlanWithFlinkConfAsyncHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GenerateResourcePlanWithFlinkConfAsyncRequest(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
    ):
        # The Flink configuration that is used to generate a resource plan.
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class GenerateResourcePlanWithFlinkConfAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        ticket_id: str = None,
    ):
        # The ID of the ticket for you to query the asynchronous generation result.
        self.ticket_id = ticket_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket_id is not None:
            result['ticketId'] = self.ticket_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ticketId') is not None:
            self.ticket_id = m.get('ticketId')
        return self


class GenerateResourcePlanWithFlinkConfAsyncResponseBody(TeaModel):
    def __init__(
        self,
        data: GenerateResourcePlanWithFlinkConfAsyncResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the asynchronous generation result was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GenerateResourcePlanWithFlinkConfAsyncResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GenerateResourcePlanWithFlinkConfAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateResourcePlanWithFlinkConfAsyncResponseBody = None,
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
            temp_model = GenerateResourcePlanWithFlinkConfAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppliedScheduledPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetAppliedScheduledPlanRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
    ):
        # This parameter is required.
        self.deployment_id = deployment_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        return self


class GetAppliedScheduledPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: ScheduledPlanAppliedInfo = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ScheduledPlanAppliedInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetAppliedScheduledPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAppliedScheduledPlanResponseBody = None,
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
            temp_model = GetAppliedScheduledPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCatalogsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetCatalogsRequest(TeaModel):
    def __init__(
        self,
        catalog_name: str = None,
    ):
        self.catalog_name = catalog_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.catalog_name is not None:
            result['catalogName'] = self.catalog_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('catalogName') is not None:
            self.catalog_name = m.get('catalogName')
        return self


class GetCatalogsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Catalog] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Catalog()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetCatalogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCatalogsResponseBody = None,
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
            temp_model = GetCatalogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDatabasesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetDatabasesRequest(TeaModel):
    def __init__(
        self,
        database_name: str = None,
    ):
        self.database_name = database_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.database_name is not None:
            result['databaseName'] = self.database_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')
        return self


class GetDatabasesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Database] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Database()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDatabasesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDatabasesResponseBody = None,
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
            temp_model = GetDatabasesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeployDeploymentDraftResultHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetDeployDeploymentDraftResultResponseBody(TeaModel):
    def __init__(
        self,
        data: AsyncDraftDeployResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AsyncDraftDeployResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeployDeploymentDraftResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeployDeploymentDraftResultResponseBody = None,
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
            temp_model = GetDeployDeploymentDraftResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeploymentHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        data: Deployment = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the details of the deployment were returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Deployment()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
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


class GetDeploymentDraftHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetDeploymentDraftResponseBody(TeaModel):
    def __init__(
        self,
        data: DeploymentDraft = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploymentDraft()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeploymentDraftResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeploymentDraftResponseBody = None,
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
            temp_model = GetDeploymentDraftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeploymentDraftLockHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetDeploymentDraftLockRequest(TeaModel):
    def __init__(
        self,
        deployment_draft_id: str = None,
    ):
        # This parameter is required.
        self.deployment_draft_id = deployment_draft_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_draft_id is not None:
            result['deploymentDraftId'] = self.deployment_draft_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentDraftId') is not None:
            self.deployment_draft_id = m.get('deploymentDraftId')
        return self


class GetDeploymentDraftLockResponseBody(TeaModel):
    def __init__(
        self,
        data: Lock = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Lock()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeploymentDraftLockResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeploymentDraftLockResponseBody = None,
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
            temp_model = GetDeploymentDraftLockResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEventsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetEventsRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.deployment_id = deployment_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetEventsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Event] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Event()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class GetEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEventsResponseBody = None,
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
            temp_model = GetEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFolderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetFolderRequest(TeaModel):
    def __init__(
        self,
        folder_id: str = None,
    ):
        self.folder_id = folder_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.folder_id is not None:
            result['folderId'] = self.folder_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')
        return self


class GetFolderResponseBody(TeaModel):
    def __init__(
        self,
        data: Folder = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The data structure of the folder.
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Folder()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFolderResponseBody = None,
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
            temp_model = GetFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGenerateResourcePlanResultHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetGenerateResourcePlanResultResponseBody(TeaModel):
    def __init__(
        self,
        data: AsyncResourcePlanOperationResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the asynchronous generation result was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = AsyncResourcePlanOperationResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetGenerateResourcePlanResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGenerateResourcePlanResultResponseBody = None,
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
            temp_model = GetGenerateResourcePlanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotUpdateJobResultHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetHotUpdateJobResultResponseBody(TeaModel):
    def __init__(
        self,
        data: HotUpdateJobResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = HotUpdateJobResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetHotUpdateJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotUpdateJobResultResponseBody = None,
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
            temp_model = GetHotUpdateJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: Job = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # *   If the value of success was true, the details of the job was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('data') is not None:
            temp_model = Job()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
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
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobDiagnosisHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetJobDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: JobDiagnosis = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('data') is not None:
            temp_model = JobDiagnosis()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetJobDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobDiagnosisResponseBody = None,
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
            temp_model = GetJobDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLatestJobStartLogHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetLatestJobStartLogResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the value of success was false, the latest logs of the deployment were returned. If the value of success was true, a null value was returned.
        self.data = data
        # If the value of success was false, an error code was returned. If the value of success was true, a null value was returned.
        self.error_code = error_code
        # If the value of success was false, an error message was returned. If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetLatestJobStartLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLatestJobStartLogResponseBody = None,
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
            temp_model = GetLatestJobStartLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLineageInfoHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetLineageInfoRequest(TeaModel):
    def __init__(
        self,
        body: GetLineageInfoParams = None,
    ):
        # The parameters about the lineage information.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = GetLineageInfoParams()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLineageInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: LineageInfo = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The lineage information.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = LineageInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetLineageInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLineageInfoResponseBody = None,
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
            temp_model = GetLineageInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMemberHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetMemberResponseBody(TeaModel):
    def __init__(
        self,
        data: Member = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was false, a null value was returned.
        # *   If the value of success was true, the authorization information was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Member()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMemberResponseBody = None,
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
            temp_model = GetMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPreSignedUrlForPutObjectHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetPreSignedUrlForPutObjectRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
    ):
        # This parameter is required.
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        return self


class GetPreSignedUrlForPutObjectResponseBody(TeaModel):
    def __init__(
        self,
        data: GetPreSignedUrlForObjectResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetPreSignedUrlForObjectResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetPreSignedUrlForPutObjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPreSignedUrlForPutObjectResponseBody = None,
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
            temp_model = GetPreSignedUrlForPutObjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSavepointHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetSavepointResponseBody(TeaModel):
    def __init__(
        self,
        data: Savepoint = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the savepoint information was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Savepoint()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSavepointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSavepointResponseBody = None,
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
            temp_model = GetSavepointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionClusterHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: SessionCluster = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SessionCluster()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetSessionClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSessionClusterResponseBody = None,
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
            temp_model = GetSessionClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTablesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetTablesRequest(TeaModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.table_name is not None:
            result['tableName'] = self.table_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')
        return self


class GetTablesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Table] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the value of success was true, the list and details of tables that meet the condition were returned. If the value of success was false, a null value was returned.
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Table()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTablesResponseBody = None,
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
            temp_model = GetTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUdfArtifactsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetUdfArtifactsRequest(TeaModel):
    def __init__(
        self,
        udf_artifact_name: str = None,
    ):
        # The name of the JAR or Python file that corresponds to the UDF.
        self.udf_artifact_name = udf_artifact_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.udf_artifact_name is not None:
            result['udfArtifactName'] = self.udf_artifact_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('udfArtifactName') is not None:
            self.udf_artifact_name = m.get('udfArtifactName')
        return self


class GetUdfArtifactsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[UdfArtifact] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the value of success was true, the details of the JAR or Python file that corresponds to the UDF were returned. If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = UdfArtifact()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetUdfArtifactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUdfArtifactsResponseBody = None,
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
            temp_model = GetUdfArtifactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HotUpdateJobHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class HotUpdateJobResponseBody(TeaModel):
    def __init__(
        self,
        data: HotUpdateJobResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The dynamic update result.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = HotUpdateJobResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class HotUpdateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HotUpdateJobResponseBody = None,
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
            temp_model = HotUpdateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomConnectorsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListCustomConnectorsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Connector] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the value of success was true, the list of custom connectors in the namespace was returned. If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Connector()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListCustomConnectorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomConnectorsResponseBody = None,
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
            temp_model = ListCustomConnectorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentDraftsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListDeploymentDraftsRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDeploymentDraftsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DeploymentDraft] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = DeploymentDraft()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListDeploymentDraftsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeploymentDraftsResponseBody = None,
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
            temp_model = ListDeploymentDraftsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentTargetsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListDeploymentTargetsRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        # The page number. Minimum value: 1. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListDeploymentTargetsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[DeploymentTarget] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # *   If the value of success was true, a list of clusters in which the deployment is deployed was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = DeploymentTarget()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListDeploymentTargetsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeploymentTargetsResponseBody = None,
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
            temp_model = ListDeploymentTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeploymentsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListDeploymentsRequest(TeaModel):
    def __init__(
        self,
        creator: str = None,
        execution_mode: str = None,
        label_key: str = None,
        label_value_array: str = None,
        modifier: str = None,
        name: str = None,
        page_index: int = None,
        page_size: int = None,
        sort_name: str = None,
        status: str = None,
    ):
        # The ID of the user who creates the deployment.
        self.creator = creator
        # The execution mode of the deployment.
        # 
        # Valid values:
        # 
        # *   BATCH
        # *   STREAMING
        self.execution_mode = execution_mode
        # The tag key.
        self.label_key = label_key
        # The tag value. Separate multiple values with semicolon (;).
        self.label_value_array = label_value_array
        # The ID of the user who modifies the deployment.
        self.modifier = modifier
        # The name of the deployment.
        self.name = name
        # The page number. Minimum value: 1. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        self.sort_name = sort_name
        # The latest status of the deployment.
        # 
        # Valid values:
        # 
        # *   CANCELLED
        # *   FAILED
        # *   RUNNING
        # *   TRANSITIONING
        # *   FINISHED
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.execution_mode is not None:
            result['executionMode'] = self.execution_mode
        if self.label_key is not None:
            result['labelKey'] = self.label_key
        if self.label_value_array is not None:
            result['labelValueArray'] = self.label_value_array
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort_name is not None:
            result['sortName'] = self.sort_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('executionMode') is not None:
            self.execution_mode = m.get('executionMode')
        if m.get('labelKey') is not None:
            self.label_key = m.get('labelKey')
        if m.get('labelValueArray') is not None:
            self.label_value_array = m.get('labelValueArray')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sortName') is not None:
            self.sort_name = m.get('sortName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListDeploymentsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Deployment] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # *   If the value of success was true, the list of all deployments was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Deployment()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
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


class ListEditableNamespaceRequest(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        page_index: str = None,
        page_size: str = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        self.namespace = namespace
        self.page_index = page_index
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListEditableNamespaceResponseBodyData(TeaModel):
    def __init__(
        self,
        editable_namespaces: List[EditableNamespace] = None,
        page_index: str = None,
        page_size: str = None,
        total: str = None,
    ):
        self.editable_namespaces = editable_namespaces
        self.page_index = page_index
        self.page_size = page_size
        self.total = total

    def validate(self):
        if self.editable_namespaces:
            for k in self.editable_namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['editableNamespaces'] = []
        if self.editable_namespaces is not None:
            for k in self.editable_namespaces:
                result['editableNamespaces'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.editable_namespaces = []
        if m.get('editableNamespaces') is not None:
            for k in m.get('editableNamespaces'):
                temp_model = EditableNamespace()
                self.editable_namespaces.append(temp_model.from_map(k))
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListEditableNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        data: ListEditableNamespaceResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        reason: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.http_code = http_code
        self.message = message
        self.reason = reason
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ListEditableNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEditableNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEditableNamespaceResponseBody = None,
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
            temp_model = ListEditableNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEngineVersionMetadataHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListEngineVersionMetadataResponseBody(TeaModel):
    def __init__(
        self,
        data: EngineVersionMetadataIndex = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the engine versions that are supported by Realtime Compute for Apache Flink were returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = EngineVersionMetadataIndex()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListEngineVersionMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEngineVersionMetadataResponseBody = None,
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
            temp_model = ListEngineVersionMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        page_index: int = None,
        page_size: int = None,
        sort_name: str = None,
    ):
        # The deployment ID.
        # 
        # This parameter is required.
        self.deployment_id = deployment_id
        # The page number. Minimum value: 1. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The collation.
        # 
        # Valid values:
        # 
        # *   gmt_create
        # *   job_id
        # *   status
        self.sort_name = sort_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.sort_name is not None:
            result['sortName'] = self.sort_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('sortName') is not None:
            self.sort_name = m.get('sortName')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[Job] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        # *   If the value of success was true, all jobs that meet the condition were returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Job()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
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
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMembersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListMembersRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        # The page number. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListMembersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Member] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # *   If the value of success was false, a null value was returned.
        # *   If the value of success was true, the authorization information was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Member()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMembersResponseBody = None,
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
            temp_model = ListMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSavepointsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListSavepointsRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        job_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # The deployment ID. This parameter is optional.
        self.deployment_id = deployment_id
        # The job ID. This parameter is optional.
        self.job_id = job_id
        # The page number. Minimum value: 1. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListSavepointsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Savepoint] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # *   If the value of success was true, a list of savepoints was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Savepoint()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListSavepointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSavepointsResponseBody = None,
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
            temp_model = ListSavepointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListScheduledPlanRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.deployment_id = deployment_id
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListScheduledPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ScheduledPlan] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ScheduledPlan()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListScheduledPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScheduledPlanResponseBody = None,
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
            temp_model = ListScheduledPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScheduledPlanExecutedHistoryHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListScheduledPlanExecutedHistoryRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        origin: str = None,
    ):
        # This parameter is required.
        self.deployment_id = deployment_id
        self.origin = origin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.origin is not None:
            result['origin'] = self.origin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('origin') is not None:
            self.origin = m.get('origin')
        return self


class ListScheduledPlanExecutedHistoryResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ScheduledPlanExecutedInfo] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.page_index = page_index
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ScheduledPlanExecutedInfo()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListScheduledPlanExecutedHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScheduledPlanExecutedHistoryResponseBody = None,
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
            temp_model = ListScheduledPlanExecutedHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSessionClustersHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListSessionClustersResponseBody(TeaModel):
    def __init__(
        self,
        data: List[SessionCluster] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = SessionCluster()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListSessionClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSessionClustersResponseBody = None,
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
            temp_model = ListSessionClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVariablesHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListVariablesRequest(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
    ):
        # The page number. Minimum value: 1. Default value: 1.
        self.page_index = page_index
        # The number of entries per page. Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListVariablesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Variable] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        # *   If the value of success was true, a list of variables was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The page number.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Variable()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListVariablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVariablesResponseBody = None,
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
            temp_model = ListVariablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterCustomConnectorHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class RegisterCustomConnectorRequest(TeaModel):
    def __init__(
        self,
        jar_url: str = None,
    ):
        # The URL in which the JAR package of the custom connector is stored. The platform must be able to access this address.
        # 
        # This parameter is required.
        self.jar_url = jar_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jar_url is not None:
            result['jarUrl'] = self.jar_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jarUrl') is not None:
            self.jar_url = m.get('jarUrl')
        return self


class RegisterCustomConnectorResponseBody(TeaModel):
    def __init__(
        self,
        data: List[Connector] = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the value of success was true, a list of deployments in which custom connectors were deleted was returned. If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = Connector()
                self.data.append(temp_model.from_map(k))
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RegisterCustomConnectorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterCustomConnectorResponseBody = None,
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
            temp_model = RegisterCustomConnectorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterUdfFunctionHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class RegisterUdfFunctionRequest(TeaModel):
    def __init__(
        self,
        class_name: str = None,
        function_name: str = None,
        udf_artifact_name: str = None,
    ):
        # The name of the class that corresponds to the UDF.
        # 
        # This parameter is required.
        self.class_name = class_name
        # The name of the UDF. In most cases, the name of the UDF is the same as the class name. You can specify a name for the UDF.
        # 
        # This parameter is required.
        self.function_name = function_name
        # The name of the JAR or Python file that corresponds to the UDF.
        # 
        # This parameter is required.
        self.udf_artifact_name = udf_artifact_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_name is not None:
            result['className'] = self.class_name
        if self.function_name is not None:
            result['functionName'] = self.function_name
        if self.udf_artifact_name is not None:
            result['udfArtifactName'] = self.udf_artifact_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('className') is not None:
            self.class_name = m.get('className')
        if m.get('functionName') is not None:
            self.function_name = m.get('functionName')
        if m.get('udfArtifactName') is not None:
            self.udf_artifact_name = m.get('udfArtifactName')
        return self


class RegisterUdfFunctionResponseBody(TeaModel):
    def __init__(
        self,
        data: UdfFunction = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the UDF.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UdfFunction()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RegisterUdfFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterUdfFunctionResponseBody = None,
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
            temp_model = RegisterUdfFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class StartJobRequest(TeaModel):
    def __init__(
        self,
        body: StartJobRequestBody = None,
    ):
        # The parameter that is used to start the job.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = StartJobRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: Job = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # *   If the value of success was true, the job that you created was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('data') is not None:
            temp_model = Job()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartJobResponseBody = None,
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
            temp_model = StartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobWithParamsHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class StartJobWithParamsRequest(TeaModel):
    def __init__(
        self,
        body: JobStartParameters = None,
    ):
        # The parameter that is used to start the job.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = JobStartParameters()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobWithParamsResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: Job = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The details of the job of the deployment returned.
        self.data = data
        # If the value of success was false, an error code was returned. If the value of success was true, a null value was returned.
        self.error_code = error_code
        # If the value of success was false, an error message was returned. If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('data') is not None:
            temp_model = Job()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartJobWithParamsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartJobWithParamsResponseBody = None,
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
            temp_model = StartJobWithParamsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSessionClusterHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class StartSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartSessionClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartSessionClusterResponseBody = None,
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
            temp_model = StartSessionClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopApplyScheduledPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class StopApplyScheduledPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: ScheduledPlanAppliedInfo = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ScheduledPlanAppliedInfo()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StopApplyScheduledPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopApplyScheduledPlanResponseBody = None,
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
            temp_model = StopApplyScheduledPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class StopJobRequest(TeaModel):
    def __init__(
        self,
        body: StopJobRequestBody = None,
    ):
        # The parameter that is used to stop the job.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = StopJobRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: Job = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        # *   If the value of success was true, the job that you stopped was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('data') is not None:
            temp_model = Job()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StopJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopJobResponseBody = None,
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
            temp_model = StopJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSessionClusterHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class StopSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StopSessionClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopSessionClusterResponseBody = None,
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
            temp_model = StopSessionClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSqlPreviewHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class SubmitSqlPreviewRequest(TeaModel):
    def __init__(
        self,
        body: SqlStatementWithContext = None,
        session_cluster_name: str = None,
    ):
        self.body = body
        # This parameter is required.
        self.session_cluster_name = session_cluster_name

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        if self.session_cluster_name is not None:
            result['sessionClusterName'] = self.session_cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SqlStatementWithContext()
            self.body = temp_model.from_map(m['body'])
        if m.get('sessionClusterName') is not None:
            self.session_cluster_name = m.get('sessionClusterName')
        return self


class SubmitSqlPreviewResponseBody(TeaModel):
    def __init__(
        self,
        data: SubmitPreviewResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SubmitPreviewResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class SubmitSqlPreviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSqlPreviewResponseBody = None,
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
            temp_model = SubmitSqlPreviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateDeploymentRequest(TeaModel):
    def __init__(
        self,
        body: Deployment = None,
    ):
        # The information about the deployment that you want to update.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Deployment()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        data: Deployment = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # *   If the value of success was true, the information about the deployment after the update was returned.
        # *   If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Deployment()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeploymentResponseBody = None,
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
            temp_model = UpdateDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentDraftHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateDeploymentDraftRequest(TeaModel):
    def __init__(
        self,
        body: DeploymentDraft = None,
    ):
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DeploymentDraft()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentDraftResponseBody(TeaModel):
    def __init__(
        self,
        data: DeploymentDraft = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploymentDraft()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateDeploymentDraftResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeploymentDraftResponseBody = None,
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
            temp_model = UpdateDeploymentDraftResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentTargetHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateDeploymentTargetRequest(TeaModel):
    def __init__(
        self,
        body: ResourceSpec = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ResourceSpec()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentTargetResponseBody(TeaModel):
    def __init__(
        self,
        data: DeploymentTarget = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploymentTarget()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateDeploymentTargetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeploymentTargetResponseBody = None,
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
            temp_model = UpdateDeploymentTargetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentTargetV2Headers(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateDeploymentTargetV2Request(TeaModel):
    def __init__(
        self,
        body: Resource = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Resource()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeploymentTargetV2ResponseBody(TeaModel):
    def __init__(
        self,
        data: DeploymentTarget = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = DeploymentTarget()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateDeploymentTargetV2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeploymentTargetV2ResponseBody = None,
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
            temp_model = UpdateDeploymentTargetV2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFolderHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateFolderRequest(TeaModel):
    def __init__(
        self,
        body: Folder = None,
    ):
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Folder()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFolderResponseBody(TeaModel):
    def __init__(
        self,
        data: Folder = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Folder()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateFolderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFolderResponseBody = None,
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
            temp_model = UpdateFolderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMemberHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateMemberRequest(TeaModel):
    def __init__(
        self,
        body: Member = None,
    ):
        # The permission information about the member.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Member()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMemberResponseBody(TeaModel):
    def __init__(
        self,
        data: Member = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # If the value of success was true, the member that was created was returned. If the value of success was false, a null value was returned.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Member()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMemberResponseBody = None,
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
            temp_model = UpdateMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateScheduledPlanHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateScheduledPlanRequest(TeaModel):
    def __init__(
        self,
        body: ScheduledPlan = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ScheduledPlan()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateScheduledPlanResponseBody(TeaModel):
    def __init__(
        self,
        data: ScheduledPlan = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = ScheduledPlan()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateScheduledPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateScheduledPlanResponseBody = None,
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
            temp_model = UpdateScheduledPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSessionClusterHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateSessionClusterRequest(TeaModel):
    def __init__(
        self,
        body: SessionCluster = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SessionCluster()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: SessionCluster = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SessionCluster()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateSessionClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSessionClusterResponseBody = None,
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
            temp_model = UpdateSessionClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUdfArtifactHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateUdfArtifactRequest(TeaModel):
    def __init__(
        self,
        body: UdfArtifact = None,
    ):
        # The details of the JAR file of the UDF.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UdfArtifact()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUdfArtifactResponseBody(TeaModel):
    def __init__(
        self,
        data: UpdateUdfArtifactResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The result of updating the JAR file of the UDF.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200. The status code 200 indicates that the request was successful.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = UpdateUdfArtifactResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateUdfArtifactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUdfArtifactResponseBody = None,
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
            temp_model = UpdateUdfArtifactResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVariableHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateVariableRequest(TeaModel):
    def __init__(
        self,
        body: Variable = None,
    ):
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = Variable()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVariableResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: Variable = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        self.http_code = http_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')
        if m.get('data') is not None:
            temp_model = Variable()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateVariableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateVariableResponseBody = None,
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
            temp_model = UpdateVariableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateSqlStatementHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        workspace: str = None,
    ):
        self.common_headers = common_headers
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ValidateSqlStatementRequest(TeaModel):
    def __init__(
        self,
        body: SqlStatementWithContext = None,
    ):
        # The content of the code that you want to verify.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = SqlStatementWithContext()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateSqlStatementResponseBody(TeaModel):
    def __init__(
        self,
        data: SqlStatementValidationResult = None,
        error_code: str = None,
        error_message: str = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data, which represents the details of SQL validation results.
        self.data = data
        # If the value of success was false, an error code was returned. If the value of success was true, a null value was returned.
        self.error_code = error_code
        # If the value of success was false, an error message was returned. If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The status code returned. The value was fixed to 200.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = SqlStatementValidationResult()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ValidateSqlStatementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateSqlStatementResponseBody = None,
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
            temp_model = ValidateSqlStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


