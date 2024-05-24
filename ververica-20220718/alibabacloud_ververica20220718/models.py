# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


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
        local_variables: List[LocalVariable] = None,
        logging: Logging = None,
        modified_at: str = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        namespace: str = None,
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
        self.local_variables = local_variables
        self.logging = logging
        self.modified_at = modified_at
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.name = name
        self.namespace = namespace
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
        if m.get('streamingResourceSetting') is not None:
            temp_model = StreamingResourceSetting()
            self.streaming_resource_setting = temp_model.from_map(m['streamingResourceSetting'])
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


class DeploymentTarget(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
    ):
        self.name = name
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
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
        running: JobStatusRunning = None,
    ):
        self.current_job_status = current_job_status
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
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status
        if self.failure is not None:
            result['failure'] = self.failure.to_map()
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


class JobStartParameters(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        local_variables: List[LocalVariable] = None,
        resource_queue_name: str = None,
        restore_strategy: DeploymentRestoreStrategy = None,
    ):
        self.deployment_id = deployment_id
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
        catalog: str = None,
        database: str = None,
        flink_configuration: Dict[str, Any] = None,
        statement: str = None,
        version_name: str = None,
    ):
        self.additional_dependencies = additional_dependencies
        # This parameter is required.
        self.batch_mode = batch_mode
        self.catalog = catalog
        self.database = database
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
        if self.catalog is not None:
            result['catalog'] = self.catalog
        if self.database is not None:
            result['database'] = self.database
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
        if m.get('catalog') is not None:
            self.catalog = m.get('catalog')
        if m.get('database') is not None:
            self.database = m.get('database')
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


class CreateDeploymentHeaders(TeaModel):
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


class CreateDeploymentRequest(TeaModel):
    def __init__(
        self,
        body: Deployment = None,
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


class CreateMemberHeaders(TeaModel):
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


class CreateMemberRequest(TeaModel):
    def __init__(
        self,
        body: Member = None,
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
        # This parameter is required.
        self.deployment_id = deployment_id
        self.description = description
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


class CreateVariableHeaders(TeaModel):
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


class CreateVariableRequest(TeaModel):
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


class DeleteDeploymentHeaders(TeaModel):
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


class DeleteDeploymentResponseBody(TeaModel):
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


class DeleteJobHeaders(TeaModel):
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


class DeleteJobResponseBody(TeaModel):
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


class DeleteVariableHeaders(TeaModel):
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


class DeleteVariableResponseBody(TeaModel):
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


class FlinkApiProxyHeaders(TeaModel):
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


class FlinkApiProxyRequest(TeaModel):
    def __init__(
        self,
        flink_api_path: str = None,
        namespace: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.flink_api_path = flink_api_path
        # This parameter is required.
        self.namespace = namespace
        # This parameter is required.
        self.resource_id = resource_id
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
        self.data = data
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


class GetDeploymentHeaders(TeaModel):
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


class GetGenerateResourcePlanResultHeaders(TeaModel):
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


class GetJobHeaders(TeaModel):
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


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        data: Job = None,
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


class GetMemberHeaders(TeaModel):
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


class GetSavepointHeaders(TeaModel):
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


class ListDeploymentTargetsHeaders(TeaModel):
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


class ListDeploymentTargetsRequest(TeaModel):
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
        status: str = None,
    ):
        self.creator = creator
        self.execution_mode = execution_mode
        self.label_key = label_key
        self.label_value_array = label_value_array
        self.modifier = modifier
        self.name = name
        self.page_index = page_index
        self.page_size = page_size
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
        # This parameter is required.
        self.deployment_id = deployment_id
        self.page_index = page_index
        self.page_size = page_size
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
        self.deployment_id = deployment_id
        self.job_id = job_id
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


class ListVariablesHeaders(TeaModel):
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


class ListVariablesRequest(TeaModel):
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


class StartJobHeaders(TeaModel):
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


class StartJobRequest(TeaModel):
    def __init__(
        self,
        body: StartJobRequestBody = None,
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
            temp_model = StartJobRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobResponseBody(TeaModel):
    def __init__(
        self,
        data: Job = None,
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
        data: Job = None,
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


class StopJobHeaders(TeaModel):
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


class StopJobRequest(TeaModel):
    def __init__(
        self,
        body: StopJobRequestBody = None,
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
            temp_model = StopJobRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopJobResponseBody(TeaModel):
    def __init__(
        self,
        data: Job = None,
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


class UpdateDeploymentHeaders(TeaModel):
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


class UpdateDeploymentRequest(TeaModel):
    def __init__(
        self,
        body: Deployment = None,
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


class UpdateMemberHeaders(TeaModel):
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


class UpdateMemberRequest(TeaModel):
    def __init__(
        self,
        body: Member = None,
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


