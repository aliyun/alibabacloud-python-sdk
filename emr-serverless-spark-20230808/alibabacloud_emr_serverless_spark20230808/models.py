# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class Credential(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        # This parameter is required.
        self.access_id = access_id
        # This parameter is required.
        self.dir = dir
        # This parameter is required.
        self.expire = expire
        # This parameter is required.
        self.host = host
        # This parameter is required.
        self.policy = policy
        # This parameter is required.
        self.security_token = security_token
        # This parameter is required.
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['accessId'] = self.access_id
        if self.dir is not None:
            result['dir'] = self.dir
        if self.expire is not None:
            result['expire'] = self.expire
        if self.host is not None:
            result['host'] = self.host
        if self.policy is not None:
            result['policy'] = self.policy
        if self.security_token is not None:
            result['securityToken'] = self.security_token
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')
        if m.get('dir') is not None:
            self.dir = m.get('dir')
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class Artifact(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        creator: int = None,
        credential: Credential = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        location: str = None,
        modifier: int = None,
        name: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.creator = creator
        self.credential = credential
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.location = location
        # This parameter is required.
        self.modifier = modifier
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.location is not None:
            result['location'] = self.location
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('credential') is not None:
            temp_model = Credential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class Category(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        creator: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        modifier: int = None,
        name: str = None,
        parent_biz_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.creator = creator
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.modifier = modifier
        # This parameter is required.
        self.name = name
        self.parent_biz_id = parent_biz_id
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.parent_biz_id is not None:
            result['parentBizId'] = self.parent_biz_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentBizId') is not None:
            self.parent_biz_id = m.get('parentBizId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class Configuration(TeaModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        self.config_file_name = config_file_name
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')
        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')
        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')
        return self


class ConfigurationOverridesConfigurations(TeaModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        self.config_file_name = config_file_name
        self.config_item_key = config_item_key
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')
        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')
        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')
        return self


class ConfigurationOverrides(TeaModel):
    def __init__(
        self,
        configurations: List[ConfigurationOverridesConfigurations] = None,
    ):
        self.configurations = configurations

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['configurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k in m.get('configurations'):
                temp_model = ConfigurationOverridesConfigurations()
                self.configurations.append(temp_model.from_map(k))
        return self


class JobDriverSparkSubmit(TeaModel):
    def __init__(
        self,
        entry_point: str = None,
        entry_point_arguments: List[str] = None,
        spark_submit_parameters: str = None,
    ):
        self.entry_point = entry_point
        self.entry_point_arguments = entry_point_arguments
        self.spark_submit_parameters = spark_submit_parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_point is not None:
            result['entryPoint'] = self.entry_point
        if self.entry_point_arguments is not None:
            result['entryPointArguments'] = self.entry_point_arguments
        if self.spark_submit_parameters is not None:
            result['sparkSubmitParameters'] = self.spark_submit_parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entryPoint') is not None:
            self.entry_point = m.get('entryPoint')
        if m.get('entryPointArguments') is not None:
            self.entry_point_arguments = m.get('entryPointArguments')
        if m.get('sparkSubmitParameters') is not None:
            self.spark_submit_parameters = m.get('sparkSubmitParameters')
        return self


class JobDriver(TeaModel):
    def __init__(
        self,
        spark_submit: JobDriverSparkSubmit = None,
    ):
        self.spark_submit = spark_submit

    def validate(self):
        if self.spark_submit:
            self.spark_submit.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spark_submit is not None:
            result['sparkSubmit'] = self.spark_submit.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sparkSubmit') is not None:
            temp_model = JobDriverSparkSubmit()
            self.spark_submit = temp_model.from_map(m['sparkSubmit'])
        return self


class PrincipalAction(TeaModel):
    def __init__(
        self,
        action_arn: str = None,
        principal_arn: str = None,
    ):
        self.action_arn = action_arn
        self.principal_arn = principal_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_arn is not None:
            result['actionArn'] = self.action_arn
        if self.principal_arn is not None:
            result['principalArn'] = self.principal_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionArn') is not None:
            self.action_arn = m.get('actionArn')
        if m.get('principalArn') is not None:
            self.principal_arn = m.get('principalArn')
        return self


class ReleaseVersionImage(TeaModel):
    def __init__(
        self,
        cpu_architecture: str = None,
        image_id: str = None,
        runtime_engine_type: str = None,
    ):
        self.cpu_architecture = cpu_architecture
        self.image_id = image_id
        self.runtime_engine_type = runtime_engine_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_architecture is not None:
            result['cpuArchitecture'] = self.cpu_architecture
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.runtime_engine_type is not None:
            result['runtimeEngineType'] = self.runtime_engine_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuArchitecture') is not None:
            self.cpu_architecture = m.get('cpuArchitecture')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('runtimeEngineType') is not None:
            self.runtime_engine_type = m.get('runtimeEngineType')
        return self


class RunLog(TeaModel):
    def __init__(
        self,
        driver_startup: str = None,
        driver_std_error: str = None,
        driver_std_out: str = None,
        driver_syslog: str = None,
    ):
        self.driver_startup = driver_startup
        self.driver_std_error = driver_std_error
        self.driver_std_out = driver_std_out
        self.driver_syslog = driver_syslog

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.driver_startup is not None:
            result['driverStartup'] = self.driver_startup
        if self.driver_std_error is not None:
            result['driverStdError'] = self.driver_std_error
        if self.driver_std_out is not None:
            result['driverStdOut'] = self.driver_std_out
        if self.driver_syslog is not None:
            result['driverSyslog'] = self.driver_syslog
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('driverStartup') is not None:
            self.driver_startup = m.get('driverStartup')
        if m.get('driverStdError') is not None:
            self.driver_std_error = m.get('driverStdError')
        if m.get('driverStdOut') is not None:
            self.driver_std_out = m.get('driverStdOut')
        if m.get('driverSyslog') is not None:
            self.driver_syslog = m.get('driverSyslog')
        return self


class SparkConf(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SqlOutputRows(TeaModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class SqlOutputSchemaFields(TeaModel):
    def __init__(
        self,
        name: str = None,
        nullable: bool = None,
        type: str = None,
    ):
        self.name = name
        self.nullable = nullable
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.nullable is not None:
            result['nullable'] = self.nullable
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SqlOutputSchema(TeaModel):
    def __init__(
        self,
        fields: List[SqlOutputSchemaFields] = None,
    ):
        self.fields = fields

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = SqlOutputSchemaFields()
                self.fields.append(temp_model.from_map(k))
        return self


class SqlOutput(TeaModel):
    def __init__(
        self,
        rows: List[SqlOutputRows] = None,
        schema: SqlOutputSchema = None,
    ):
        self.rows = rows
        self.schema = schema

    def validate(self):
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()
        if self.schema:
            self.schema.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['rows'] = []
        if self.rows is not None:
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        if self.schema is not None:
            result['schema'] = self.schema.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rows = []
        if m.get('rows') is not None:
            for k in m.get('rows'):
                temp_model = SqlOutputRows()
                self.rows.append(temp_model.from_map(k))
        if m.get('schema') is not None:
            temp_model = SqlOutputSchema()
            self.schema = temp_model.from_map(m['schema'])
        return self


class Tag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签key值。
        self.key = key
        # 标签key值。
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class Task(TeaModel):
    def __init__(
        self,
        archives: List[str] = None,
        artifact_url: str = None,
        biz_id: str = None,
        category_biz_id: str = None,
        content: str = None,
        creator: int = None,
        default_catalog_id: str = None,
        default_database: str = None,
        default_resource_queue_id: str = None,
        default_sql_compute_id: str = None,
        deployment_id: str = None,
        extra_artifact_ids: List[str] = None,
        extra_spark_submit_params: str = None,
        files: List[str] = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        has_changed: bool = None,
        has_commited: bool = None,
        is_streaming: bool = None,
        jars: List[str] = None,
        last_run_resource_queue_id: str = None,
        modifier: int = None,
        name: str = None,
        py_files: List[str] = None,
        spark_args: str = None,
        spark_conf: List[SparkConf] = None,
        spark_driver_cores: int = None,
        spark_driver_memory: int = None,
        spark_entrypoint: str = None,
        spark_executor_cores: int = None,
        spark_executor_memory: int = None,
        spark_log_level: str = None,
        spark_log_path: str = None,
        spark_submit_clause: str = None,
        spark_version: str = None,
        tags: Dict[str, str] = None,
        type: str = None,
    ):
        self.archives = archives
        self.artifact_url = artifact_url
        # This parameter is required.
        self.biz_id = biz_id
        self.category_biz_id = category_biz_id
        self.content = content
        # This parameter is required.
        self.creator = creator
        self.default_catalog_id = default_catalog_id
        self.default_database = default_database
        self.default_resource_queue_id = default_resource_queue_id
        self.default_sql_compute_id = default_sql_compute_id
        self.deployment_id = deployment_id
        self.extra_artifact_ids = extra_artifact_ids
        self.extra_spark_submit_params = extra_spark_submit_params
        self.files = files
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        self.has_changed = has_changed
        # This parameter is required.
        self.has_commited = has_commited
        self.is_streaming = is_streaming
        self.jars = jars
        self.last_run_resource_queue_id = last_run_resource_queue_id
        # This parameter is required.
        self.modifier = modifier
        # This parameter is required.
        self.name = name
        self.py_files = py_files
        self.spark_args = spark_args
        self.spark_conf = spark_conf
        # This parameter is required.
        self.spark_driver_cores = spark_driver_cores
        # This parameter is required.
        self.spark_driver_memory = spark_driver_memory
        self.spark_entrypoint = spark_entrypoint
        # This parameter is required.
        self.spark_executor_cores = spark_executor_cores
        # This parameter is required.
        self.spark_executor_memory = spark_executor_memory
        # This parameter is required.
        self.spark_log_level = spark_log_level
        # This parameter is required.
        self.spark_log_path = spark_log_path
        self.spark_submit_clause = spark_submit_clause
        # This parameter is required.
        self.spark_version = spark_version
        self.tags = tags
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.spark_conf:
            for k in self.spark_conf:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archives is not None:
            result['archives'] = self.archives
        if self.artifact_url is not None:
            result['artifactUrl'] = self.artifact_url
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.category_biz_id is not None:
            result['categoryBizId'] = self.category_biz_id
        if self.content is not None:
            result['content'] = self.content
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_catalog_id is not None:
            result['defaultCatalogId'] = self.default_catalog_id
        if self.default_database is not None:
            result['defaultDatabase'] = self.default_database
        if self.default_resource_queue_id is not None:
            result['defaultResourceQueueId'] = self.default_resource_queue_id
        if self.default_sql_compute_id is not None:
            result['defaultSqlComputeId'] = self.default_sql_compute_id
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id
        if self.extra_artifact_ids is not None:
            result['extraArtifactIds'] = self.extra_artifact_ids
        if self.extra_spark_submit_params is not None:
            result['extraSparkSubmitParams'] = self.extra_spark_submit_params
        if self.files is not None:
            result['files'] = self.files
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.has_changed is not None:
            result['hasChanged'] = self.has_changed
        if self.has_commited is not None:
            result['hasCommited'] = self.has_commited
        if self.is_streaming is not None:
            result['isStreaming'] = self.is_streaming
        if self.jars is not None:
            result['jars'] = self.jars
        if self.last_run_resource_queue_id is not None:
            result['lastRunResourceQueueId'] = self.last_run_resource_queue_id
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.py_files is not None:
            result['pyFiles'] = self.py_files
        if self.spark_args is not None:
            result['sparkArgs'] = self.spark_args
        result['sparkConf'] = []
        if self.spark_conf is not None:
            for k in self.spark_conf:
                result['sparkConf'].append(k.to_map() if k else None)
        if self.spark_driver_cores is not None:
            result['sparkDriverCores'] = self.spark_driver_cores
        if self.spark_driver_memory is not None:
            result['sparkDriverMemory'] = self.spark_driver_memory
        if self.spark_entrypoint is not None:
            result['sparkEntrypoint'] = self.spark_entrypoint
        if self.spark_executor_cores is not None:
            result['sparkExecutorCores'] = self.spark_executor_cores
        if self.spark_executor_memory is not None:
            result['sparkExecutorMemory'] = self.spark_executor_memory
        if self.spark_log_level is not None:
            result['sparkLogLevel'] = self.spark_log_level
        if self.spark_log_path is not None:
            result['sparkLogPath'] = self.spark_log_path
        if self.spark_submit_clause is not None:
            result['sparkSubmitClause'] = self.spark_submit_clause
        if self.spark_version is not None:
            result['sparkVersion'] = self.spark_version
        if self.tags is not None:
            result['tags'] = self.tags
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('archives') is not None:
            self.archives = m.get('archives')
        if m.get('artifactUrl') is not None:
            self.artifact_url = m.get('artifactUrl')
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('categoryBizId') is not None:
            self.category_biz_id = m.get('categoryBizId')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('defaultCatalogId') is not None:
            self.default_catalog_id = m.get('defaultCatalogId')
        if m.get('defaultDatabase') is not None:
            self.default_database = m.get('defaultDatabase')
        if m.get('defaultResourceQueueId') is not None:
            self.default_resource_queue_id = m.get('defaultResourceQueueId')
        if m.get('defaultSqlComputeId') is not None:
            self.default_sql_compute_id = m.get('defaultSqlComputeId')
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')
        if m.get('extraArtifactIds') is not None:
            self.extra_artifact_ids = m.get('extraArtifactIds')
        if m.get('extraSparkSubmitParams') is not None:
            self.extra_spark_submit_params = m.get('extraSparkSubmitParams')
        if m.get('files') is not None:
            self.files = m.get('files')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('hasChanged') is not None:
            self.has_changed = m.get('hasChanged')
        if m.get('hasCommited') is not None:
            self.has_commited = m.get('hasCommited')
        if m.get('isStreaming') is not None:
            self.is_streaming = m.get('isStreaming')
        if m.get('jars') is not None:
            self.jars = m.get('jars')
        if m.get('lastRunResourceQueueId') is not None:
            self.last_run_resource_queue_id = m.get('lastRunResourceQueueId')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pyFiles') is not None:
            self.py_files = m.get('pyFiles')
        if m.get('sparkArgs') is not None:
            self.spark_args = m.get('sparkArgs')
        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k in m.get('sparkConf'):
                temp_model = SparkConf()
                self.spark_conf.append(temp_model.from_map(k))
        if m.get('sparkDriverCores') is not None:
            self.spark_driver_cores = m.get('sparkDriverCores')
        if m.get('sparkDriverMemory') is not None:
            self.spark_driver_memory = m.get('sparkDriverMemory')
        if m.get('sparkEntrypoint') is not None:
            self.spark_entrypoint = m.get('sparkEntrypoint')
        if m.get('sparkExecutorCores') is not None:
            self.spark_executor_cores = m.get('sparkExecutorCores')
        if m.get('sparkExecutorMemory') is not None:
            self.spark_executor_memory = m.get('sparkExecutorMemory')
        if m.get('sparkLogLevel') is not None:
            self.spark_log_level = m.get('sparkLogLevel')
        if m.get('sparkLogPath') is not None:
            self.spark_log_path = m.get('sparkLogPath')
        if m.get('sparkSubmitClause') is not None:
            self.spark_submit_clause = m.get('sparkSubmitClause')
        if m.get('sparkVersion') is not None:
            self.spark_version = m.get('sparkVersion')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class TaskInstance(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        creator: int = None,
        fenix_run_id: str = None,
        gmt_created: str = None,
        task_biz_id: str = None,
        task_info: Task = None,
        task_status: str = None,
        workspace_biz_id: str = None,
    ):
        self.biz_id = biz_id
        self.creator = creator
        self.fenix_run_id = fenix_run_id
        self.gmt_created = gmt_created
        self.task_biz_id = task_biz_id
        self.task_info = task_info
        self.task_status = task_status
        self.workspace_biz_id = workspace_biz_id

    def validate(self):
        if self.task_info:
            self.task_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.fenix_run_id is not None:
            result['fenixRunId'] = self.fenix_run_id
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id
        if self.task_info is not None:
            result['taskInfo'] = self.task_info.to_map()
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.workspace_biz_id is not None:
            result['workspaceBizId'] = self.workspace_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('fenixRunId') is not None:
            self.fenix_run_id = m.get('fenixRunId')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')
        if m.get('taskInfo') is not None:
            temp_model = Task()
            self.task_info = temp_model.from_map(m['taskInfo'])
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('workspaceBizId') is not None:
            self.workspace_biz_id = m.get('workspaceBizId')
        return self


class TaskSnapshot(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        commiter: int = None,
        gmt_created: str = None,
        item: Task = None,
        message: str = None,
        task_biz_id: str = None,
        version: str = None,
    ):
        self.biz_id = biz_id
        self.commiter = commiter
        self.gmt_created = gmt_created
        self.item = item
        self.message = message
        self.task_biz_id = task_biz_id
        self.version = version

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.commiter is not None:
            result['commiter'] = self.commiter
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.item is not None:
            result['item'] = self.item.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('commiter') is not None:
            self.commiter = m.get('commiter')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('item') is not None:
            temp_model = Task()
            self.item = temp_model.from_map(m['item'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Template(TeaModel):
    def __init__(
        self,
        creator: int = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        modifier: int = None,
        spark_conf: List[SparkConf] = None,
        spark_driver_cores: int = None,
        spark_driver_memory: int = None,
        spark_executor_cores: int = None,
        spark_executor_memory: int = None,
        spark_log_level: str = None,
        spark_log_path: str = None,
        spark_version: str = None,
        template_type: str = None,
    ):
        # This parameter is required.
        self.creator = creator
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.modifier = modifier
        self.spark_conf = spark_conf
        # This parameter is required.
        self.spark_driver_cores = spark_driver_cores
        # This parameter is required.
        self.spark_driver_memory = spark_driver_memory
        # This parameter is required.
        self.spark_executor_cores = spark_executor_cores
        # This parameter is required.
        self.spark_executor_memory = spark_executor_memory
        # This parameter is required.
        self.spark_log_level = spark_log_level
        # This parameter is required.
        self.spark_log_path = spark_log_path
        # This parameter is required.
        self.spark_version = spark_version
        self.template_type = template_type

    def validate(self):
        if self.spark_conf:
            for k in self.spark_conf:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.modifier is not None:
            result['modifier'] = self.modifier
        result['sparkConf'] = []
        if self.spark_conf is not None:
            for k in self.spark_conf:
                result['sparkConf'].append(k.to_map() if k else None)
        if self.spark_driver_cores is not None:
            result['sparkDriverCores'] = self.spark_driver_cores
        if self.spark_driver_memory is not None:
            result['sparkDriverMemory'] = self.spark_driver_memory
        if self.spark_executor_cores is not None:
            result['sparkExecutorCores'] = self.spark_executor_cores
        if self.spark_executor_memory is not None:
            result['sparkExecutorMemory'] = self.spark_executor_memory
        if self.spark_log_level is not None:
            result['sparkLogLevel'] = self.spark_log_level
        if self.spark_log_path is not None:
            result['sparkLogPath'] = self.spark_log_path
        if self.spark_version is not None:
            result['sparkVersion'] = self.spark_version
        if self.template_type is not None:
            result['templateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k in m.get('sparkConf'):
                temp_model = SparkConf()
                self.spark_conf.append(temp_model.from_map(k))
        if m.get('sparkDriverCores') is not None:
            self.spark_driver_cores = m.get('sparkDriverCores')
        if m.get('sparkDriverMemory') is not None:
            self.spark_driver_memory = m.get('sparkDriverMemory')
        if m.get('sparkExecutorCores') is not None:
            self.spark_executor_cores = m.get('sparkExecutorCores')
        if m.get('sparkExecutorMemory') is not None:
            self.spark_executor_memory = m.get('sparkExecutorMemory')
        if m.get('sparkLogLevel') is not None:
            self.spark_log_level = m.get('sparkLogLevel')
        if m.get('sparkLogPath') is not None:
            self.spark_log_path = m.get('sparkLogPath')
        if m.get('sparkVersion') is not None:
            self.spark_version = m.get('sparkVersion')
        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')
        return self


class TimeRange(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # 时间范围结束时间。
        self.end_time = end_time
        # 时间范围开始时间。
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class AddMembersRequest(TeaModel):
    def __init__(
        self,
        member_arns: List[str] = None,
        workspace_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.member_arns = member_arns
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.member_arns is not None:
            result['memberArns'] = self.member_arns
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memberArns') is not None:
            self.member_arns = m.get('memberArns')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class AddMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AddMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddMembersResponseBody = None,
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
            temp_model = AddMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelJobRunRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CancelJobRunResponseBody(TeaModel):
    def __init__(
        self,
        job_run_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_run_id = job_run_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelJobRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelJobRunResponseBody = None,
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
            temp_model = CancelJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSqlStatementRequest(TeaModel):
    def __init__(
        self,
        code_content: str = None,
        default_catalog: str = None,
        default_database: str = None,
        limit: int = None,
        sql_compute_id: str = None,
        region_id: str = None,
    ):
        # The SQL code. You can specify one or more SQL statements.
        self.code_content = code_content
        # The default Data Lake Formation (DLF) catalog ID.
        self.default_catalog = default_catalog
        # The name of the default database.
        self.default_database = default_database
        # The maximum number of entries to return. Valid values: 1 to 10000.
        self.limit = limit
        # The SQL Compute ID. You can create an SQL Compute in the workspace created in EMR Serverless Spark.
        self.sql_compute_id = sql_compute_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_content is not None:
            result['codeContent'] = self.code_content
        if self.default_catalog is not None:
            result['defaultCatalog'] = self.default_catalog
        if self.default_database is not None:
            result['defaultDatabase'] = self.default_database
        if self.limit is not None:
            result['limit'] = self.limit
        if self.sql_compute_id is not None:
            result['sqlComputeId'] = self.sql_compute_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeContent') is not None:
            self.code_content = m.get('codeContent')
        if m.get('defaultCatalog') is not None:
            self.default_catalog = m.get('defaultCatalog')
        if m.get('defaultDatabase') is not None:
            self.default_database = m.get('defaultDatabase')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sqlComputeId') is not None:
            self.sql_compute_id = m.get('sqlComputeId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateSqlStatementResponseBodyData(TeaModel):
    def __init__(
        self,
        statement_id: str = None,
    ):
        # The ID of the SQL query.
        self.statement_id = statement_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.statement_id is not None:
            result['statementId'] = self.statement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statementId') is not None:
            self.statement_id = m.get('statementId')
        return self


class CreateSqlStatementResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateSqlStatementResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateSqlStatementResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateSqlStatementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSqlStatementResponseBody = None,
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
            temp_model = CreateSqlStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRunRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetJobRunResponseBodyJobRunConfigurationOverrides(TeaModel):
    def __init__(
        self,
        configurations: List[Configuration] = None,
    ):
        # The configurations.
        self.configurations = configurations

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['configurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k in m.get('configurations'):
                temp_model = Configuration()
                self.configurations.append(temp_model.from_map(k))
        return self


class GetJobRunResponseBodyJobRunStateChangeReason(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetJobRunResponseBodyJobRun(TeaModel):
    def __init__(
        self,
        code_type: str = None,
        configuration_overrides: GetJobRunResponseBodyJobRunConfigurationOverrides = None,
        end_time: int = None,
        execution_timeout_seconds: int = None,
        job_driver: JobDriver = None,
        job_run_id: str = None,
        log: RunLog = None,
        name: str = None,
        release_version: str = None,
        resource_owner_id: str = None,
        resource_queue_id: str = None,
        state: str = None,
        state_change_reason: GetJobRunResponseBodyJobRunStateChangeReason = None,
        submit_time: int = None,
        tags: List[Tag] = None,
        web_ui: str = None,
        workspace_id: str = None,
    ):
        # The code type of the job. Valid values:
        # 
        # *   SQL
        # *   JAR
        # *   PYTHON
        self.code_type = code_type
        # The task configurations of Spark.
        self.configuration_overrides = configuration_overrides
        # The end time of the job.
        self.end_time = end_time
        # The timeout period of the job.
        self.execution_timeout_seconds = execution_timeout_seconds
        # The information about Spark Driver.
        self.job_driver = job_driver
        # The job ID.
        self.job_run_id = job_run_id
        # The path where the operational logs are stored.
        self.log = log
        # The job name.
        self.name = name
        # The version of the Spark engine on which the job runs.
        self.release_version = release_version
        # The ID of the user who created the job.
        self.resource_owner_id = resource_owner_id
        # The name of the queue on which the job runs.
        self.resource_queue_id = resource_queue_id
        # The job state.
        self.state = state
        # The reason of the job status change.
        self.state_change_reason = state_change_reason
        # The time when the job was submitted.
        self.submit_time = submit_time
        # The tags of the job.
        self.tags = tags
        # The web UI of the job.
        self.web_ui = web_ui
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.configuration_overrides:
            self.configuration_overrides.validate()
        if self.job_driver:
            self.job_driver.validate()
        if self.log:
            self.log.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_type is not None:
            result['codeType'] = self.code_type
        if self.configuration_overrides is not None:
            result['configurationOverrides'] = self.configuration_overrides.to_map()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.log is not None:
            result['log'] = self.log.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.resource_owner_id is not None:
            result['resourceOwnerId'] = self.resource_owner_id
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.state is not None:
            result['state'] = self.state
        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()
        if self.submit_time is not None:
            result['submitTime'] = self.submit_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.web_ui is not None:
            result['webUI'] = self.web_ui
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')
        if m.get('configurationOverrides') is not None:
            temp_model = GetJobRunResponseBodyJobRunConfigurationOverrides()
            self.configuration_overrides = temp_model.from_map(m['configurationOverrides'])
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('jobDriver') is not None:
            temp_model = JobDriver()
            self.job_driver = temp_model.from_map(m['jobDriver'])
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('log') is not None:
            temp_model = RunLog()
            self.log = temp_model.from_map(m['log'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('resourceOwnerId') is not None:
            self.resource_owner_id = m.get('resourceOwnerId')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('stateChangeReason') is not None:
            temp_model = GetJobRunResponseBodyJobRunStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['stateChangeReason'])
        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class GetJobRunResponseBody(TeaModel):
    def __init__(
        self,
        job_run: GetJobRunResponseBodyJobRun = None,
        request_id: str = None,
    ):
        # The details of the job.
        self.job_run = job_run
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job_run:
            self.job_run.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_run is not None:
            result['jobRun'] = self.job_run.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobRun') is not None:
            temp_model = GetJobRunResponseBodyJobRun()
            self.job_run = temp_model.from_map(m['jobRun'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetJobRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobRunResponseBody = None,
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
            temp_model = GetJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSqlStatementRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetSqlStatementResponseBodyDataSqlOutputs(TeaModel):
    def __init__(
        self,
        rows: str = None,
        schema: str = None,
    ):
        # The queried data, which is a string in the JSON format.
        self.rows = rows
        # The information about the schema, which is a string in the JSON format.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['rows'] = self.rows
        if self.schema is not None:
            result['schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rows') is not None:
            self.rows = m.get('rows')
        if m.get('schema') is not None:
            self.schema = m.get('schema')
        return self


class GetSqlStatementResponseBodyData(TeaModel):
    def __init__(
        self,
        execution_time: List[int] = None,
        sql_error_code: str = None,
        sql_error_message: str = None,
        sql_outputs: List[GetSqlStatementResponseBodyDataSqlOutputs] = None,
        state: str = None,
        statement_id: str = None,
    ):
        # The list of time that is consumed by SQL queries.
        self.execution_time = execution_time
        # The error code.
        self.sql_error_code = sql_error_code
        # The error message.
        self.sql_error_message = sql_error_message
        # The query results.
        self.sql_outputs = sql_outputs
        # The query status.
        # 
        # Valid values:
        # 
        # *   running
        # *   available
        # *   cancelled
        # *   error
        # *   cancelling
        self.state = state
        # The query ID.
        self.statement_id = statement_id

    def validate(self):
        if self.sql_outputs:
            for k in self.sql_outputs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.execution_time is not None:
            result['executionTime'] = self.execution_time
        if self.sql_error_code is not None:
            result['sqlErrorCode'] = self.sql_error_code
        if self.sql_error_message is not None:
            result['sqlErrorMessage'] = self.sql_error_message
        result['sqlOutputs'] = []
        if self.sql_outputs is not None:
            for k in self.sql_outputs:
                result['sqlOutputs'].append(k.to_map() if k else None)
        if self.state is not None:
            result['state'] = self.state
        if self.statement_id is not None:
            result['statementId'] = self.statement_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executionTime') is not None:
            self.execution_time = m.get('executionTime')
        if m.get('sqlErrorCode') is not None:
            self.sql_error_code = m.get('sqlErrorCode')
        if m.get('sqlErrorMessage') is not None:
            self.sql_error_message = m.get('sqlErrorMessage')
        self.sql_outputs = []
        if m.get('sqlOutputs') is not None:
            for k in m.get('sqlOutputs'):
                temp_model = GetSqlStatementResponseBodyDataSqlOutputs()
                self.sql_outputs.append(temp_model.from_map(k))
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('statementId') is not None:
            self.statement_id = m.get('statementId')
        return self


class GetSqlStatementResponseBody(TeaModel):
    def __init__(
        self,
        data: GetSqlStatementResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetSqlStatementResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetSqlStatementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSqlStatementResponseBody = None,
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
            temp_model = GetSqlStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantRoleToUsersRequest(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        user_arns: List[str] = None,
        region_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the role.
        self.role_arn = role_arn
        self.user_arns = user_arns
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_arn is not None:
            result['roleArn'] = self.role_arn
        if self.user_arns is not None:
            result['userArns'] = self.user_arns
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')
        if m.get('userArns') is not None:
            self.user_arns = m.get('userArns')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GrantRoleToUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GrantRoleToUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GrantRoleToUsersResponseBody = None,
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
            temp_model = GrantRoleToUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobRunsRequestEndTime(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end of the end time range.
        self.end_time = end_time
        # The beginning of the end time range.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListJobRunsRequestStartTime(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end of the start time range.
        self.end_time = end_time
        # The beginning of the start time range.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class ListJobRunsRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListJobRunsRequest(TeaModel):
    def __init__(
        self,
        creator: str = None,
        end_time: ListJobRunsRequestEndTime = None,
        job_run_deployment_id: str = None,
        job_run_id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_queue_id: str = None,
        start_time: ListJobRunsRequestStartTime = None,
        states: List[str] = None,
        tags: List[ListJobRunsRequestTags] = None,
    ):
        # The ID of the user who creates a Spark job.
        self.creator = creator
        # The range of end time.
        self.end_time = end_time
        self.job_run_deployment_id = job_run_deployment_id
        # The job ID.
        self.job_run_id = job_run_id
        # The maximum number of entries to return.
        self.max_results = max_results
        # The job name.
        self.name = name
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The name of the resource queue on which the Spark jobs run.
        self.resource_queue_id = resource_queue_id
        # The range of start time.
        self.start_time = start_time
        # The job states.
        self.states = states
        # The tags of the job.
        self.tags = tags

    def validate(self):
        if self.end_time:
            self.end_time.validate()
        if self.start_time:
            self.start_time.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.end_time is not None:
            result['endTime'] = self.end_time.to_map()
        if self.job_run_deployment_id is not None:
            result['jobRunDeploymentId'] = self.job_run_deployment_id
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.name is not None:
            result['name'] = self.name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.start_time is not None:
            result['startTime'] = self.start_time.to_map()
        if self.states is not None:
            result['states'] = self.states
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('endTime') is not None:
            temp_model = ListJobRunsRequestEndTime()
            self.end_time = temp_model.from_map(m['endTime'])
        if m.get('jobRunDeploymentId') is not None:
            self.job_run_deployment_id = m.get('jobRunDeploymentId')
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('startTime') is not None:
            temp_model = ListJobRunsRequestStartTime()
            self.start_time = temp_model.from_map(m['startTime'])
        if m.get('states') is not None:
            self.states = m.get('states')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListJobRunsRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListJobRunsShrinkRequest(TeaModel):
    def __init__(
        self,
        creator: str = None,
        end_time_shrink: str = None,
        job_run_deployment_id: str = None,
        job_run_id: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_queue_id: str = None,
        start_time_shrink: str = None,
        states_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The ID of the user who creates a Spark job.
        self.creator = creator
        # The range of end time.
        self.end_time_shrink = end_time_shrink
        self.job_run_deployment_id = job_run_deployment_id
        # The job ID.
        self.job_run_id = job_run_id
        # The maximum number of entries to return.
        self.max_results = max_results
        # The job name.
        self.name = name
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The name of the resource queue on which the Spark jobs run.
        self.resource_queue_id = resource_queue_id
        # The range of start time.
        self.start_time_shrink = start_time_shrink
        # The job states.
        self.states_shrink = states_shrink
        # The tags of the job.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.end_time_shrink is not None:
            result['endTime'] = self.end_time_shrink
        if self.job_run_deployment_id is not None:
            result['jobRunDeploymentId'] = self.job_run_deployment_id
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.name is not None:
            result['name'] = self.name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.start_time_shrink is not None:
            result['startTime'] = self.start_time_shrink
        if self.states_shrink is not None:
            result['states'] = self.states_shrink
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('endTime') is not None:
            self.end_time_shrink = m.get('endTime')
        if m.get('jobRunDeploymentId') is not None:
            self.job_run_deployment_id = m.get('jobRunDeploymentId')
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('startTime') is not None:
            self.start_time_shrink = m.get('startTime')
        if m.get('states') is not None:
            self.states_shrink = m.get('states')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        return self


class ListJobRunsResponseBodyJobRunsConfigurationOverrides(TeaModel):
    def __init__(
        self,
        configurations: List[Configuration] = None,
    ):
        # The SparkConf objects.
        self.configurations = configurations

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['configurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k in m.get('configurations'):
                temp_model = Configuration()
                self.configurations.append(temp_model.from_map(k))
        return self


class ListJobRunsResponseBodyJobRunsStateChangeReason(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListJobRunsResponseBodyJobRuns(TeaModel):
    def __init__(
        self,
        code_type: str = None,
        configuration_overrides: ListJobRunsResponseBodyJobRunsConfigurationOverrides = None,
        creator: str = None,
        end_time: int = None,
        execution_timeout_seconds: int = None,
        job_driver: JobDriver = None,
        job_run_id: str = None,
        log: RunLog = None,
        name: str = None,
        release_version: str = None,
        state: str = None,
        state_change_reason: ListJobRunsResponseBodyJobRunsStateChangeReason = None,
        submit_time: int = None,
        tags: List[Tag] = None,
        web_ui: str = None,
        workspace_id: str = None,
    ):
        # The code type of the job. Valid values:
        # 
        # SQL
        # 
        # JAR
        # 
        # PYTHON
        self.code_type = code_type
        # The advanced configurations of Spark.
        self.configuration_overrides = configuration_overrides
        # The ID of the user who created the job.
        self.creator = creator
        # The end time of the job.
        self.end_time = end_time
        # The timeout period of the job.
        self.execution_timeout_seconds = execution_timeout_seconds
        # The information about Spark Driver.
        self.job_driver = job_driver
        # The job ID.
        self.job_run_id = job_run_id
        # The path where the operational logs are stored.
        self.log = log
        # The job name.
        self.name = name
        # The version of Spark on which the jobs run.
        self.release_version = release_version
        # The job state.
        self.state = state
        # The reason of the job status change.
        self.state_change_reason = state_change_reason
        # The time when the job was submitted.
        self.submit_time = submit_time
        # The tags of the job.
        self.tags = tags
        # The web UI of the job.
        self.web_ui = web_ui
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.configuration_overrides:
            self.configuration_overrides.validate()
        if self.job_driver:
            self.job_driver.validate()
        if self.log:
            self.log.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_type is not None:
            result['codeType'] = self.code_type
        if self.configuration_overrides is not None:
            result['configurationOverrides'] = self.configuration_overrides.to_map()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.log is not None:
            result['log'] = self.log.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.state is not None:
            result['state'] = self.state
        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()
        if self.submit_time is not None:
            result['submitTime'] = self.submit_time
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.web_ui is not None:
            result['webUI'] = self.web_ui
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')
        if m.get('configurationOverrides') is not None:
            temp_model = ListJobRunsResponseBodyJobRunsConfigurationOverrides()
            self.configuration_overrides = temp_model.from_map(m['configurationOverrides'])
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('jobDriver') is not None:
            temp_model = JobDriver()
            self.job_driver = temp_model.from_map(m['jobDriver'])
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('log') is not None:
            temp_model = RunLog()
            self.log = temp_model.from_map(m['log'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('stateChangeReason') is not None:
            temp_model = ListJobRunsResponseBodyJobRunsStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['stateChangeReason'])
        if m.get('submitTime') is not None:
            self.submit_time = m.get('submitTime')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListJobRunsResponseBody(TeaModel):
    def __init__(
        self,
        job_runs: List[ListJobRunsResponseBodyJobRuns] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of Spark jobs.
        self.job_runs = job_runs
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.job_runs:
            for k in self.job_runs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobRuns'] = []
        if self.job_runs is not None:
            for k in self.job_runs:
                result['jobRuns'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_runs = []
        if m.get('jobRuns') is not None:
            for k in m.get('jobRuns'):
                temp_model = ListJobRunsResponseBodyJobRuns()
                self.job_runs.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListJobRunsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobRunsResponseBody = None,
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
            temp_model = ListJobRunsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReleaseVersionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        release_type: str = None,
        release_version: str = None,
        release_version_status: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The type of the version.
        # 
        # Valid values:
        # 
        # *   stable
        # *   beta
        self.release_type = release_type
        # The version of Serverless Spark.
        self.release_version = release_version
        # The status of the version. Valid values:
        # 
        # Valid values:
        # 
        # *   ONLINE
        # *   OFFLINE
        self.release_version_status = release_version_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_type is not None:
            result['releaseType'] = self.release_type
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.release_version_status is not None:
            result['releaseVersionStatus'] = self.release_version_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseType') is not None:
            self.release_type = m.get('releaseType')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('releaseVersionStatus') is not None:
            self.release_version_status = m.get('releaseVersionStatus')
        return self


class ListReleaseVersionsResponseBodyReleaseVersions(TeaModel):
    def __init__(
        self,
        community_version: str = None,
        cpu_architectures: List[str] = None,
        gmt_create: int = None,
        iaas_type: str = None,
        release_version: str = None,
        scala_version: str = None,
        state: str = None,
        type: str = None,
    ):
        # The version number of open source Spark.
        self.community_version = community_version
        # The CPU architectures.
        self.cpu_architectures = cpu_architectures
        # The creation time.
        self.gmt_create = gmt_create
        # The type of the Infrastructure as a Service (IaaS) layer.
        self.iaas_type = iaas_type
        # The version.
        self.release_version = release_version
        # The version of Scala.
        self.scala_version = scala_version
        # The status of the version.
        self.state = state
        # The type of the version.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.community_version is not None:
            result['communityVersion'] = self.community_version
        if self.cpu_architectures is not None:
            result['cpuArchitectures'] = self.cpu_architectures
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.iaas_type is not None:
            result['iaasType'] = self.iaas_type
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.scala_version is not None:
            result['scalaVersion'] = self.scala_version
        if self.state is not None:
            result['state'] = self.state
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('communityVersion') is not None:
            self.community_version = m.get('communityVersion')
        if m.get('cpuArchitectures') is not None:
            self.cpu_architectures = m.get('cpuArchitectures')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('iaasType') is not None:
            self.iaas_type = m.get('iaasType')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('scalaVersion') is not None:
            self.scala_version = m.get('scalaVersion')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListReleaseVersionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        release_versions: List[ListReleaseVersionsResponseBodyReleaseVersions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The versions.
        self.release_versions = release_versions
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.release_versions:
            for k in self.release_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['releaseVersions'] = []
        if self.release_versions is not None:
            for k in self.release_versions:
                result['releaseVersions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.release_versions = []
        if m.get('releaseVersions') is not None:
            for k in m.get('releaseVersions'):
                temp_model = ListReleaseVersionsResponseBodyReleaseVersions()
                self.release_versions.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListReleaseVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListReleaseVersionsResponseBody = None,
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
            temp_model = ListReleaseVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSessionClustersRequest(TeaModel):
    def __init__(
        self,
        kind: str = None,
        max_results: int = None,
        next_token: str = None,
        queue_name: str = None,
        region_id: str = None,
        session_cluster_id: str = None,
    ):
        self.kind = kind
        # The maximum number of entries to return.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The name of the queue.
        self.queue_name = queue_name
        # The region ID.
        self.region_id = region_id
        # The name of the job.
        self.session_cluster_id = session_cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kind is not None:
            result['kind'] = self.kind
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
        return self


class ListSessionClustersResponseBodySessionClustersApplicationConfigs(TeaModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # The name of the configuration file.
        self.config_file_name = config_file_name
        # The key of the configuration item.
        self.config_item_key = config_item_key
        # The value of the configuration item.
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')
        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')
        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')
        return self


class ListSessionClustersResponseBodySessionClustersAutoStartConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Indicates whether automatic startup is enabled.
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class ListSessionClustersResponseBodySessionClustersAutoStopConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        # Indicates whether automatic termination is enabled.
        self.enable = enable
        # The idle timeout period. The SQL Compute is automatically terminated if the idle timeout period is exceeded.
        self.idle_timeout_minutes = idle_timeout_minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.idle_timeout_minutes is not None:
            result['idleTimeoutMinutes'] = self.idle_timeout_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('idleTimeoutMinutes') is not None:
            self.idle_timeout_minutes = m.get('idleTimeoutMinutes')
        return self


class ListSessionClustersResponseBodySessionClustersStateChangeReason(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The status change code.
        self.code = code
        # The status change message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListSessionClustersResponseBodySessionClusters(TeaModel):
    def __init__(
        self,
        application_configs: List[ListSessionClustersResponseBodySessionClustersApplicationConfigs] = None,
        auto_start_configuration: ListSessionClustersResponseBodySessionClustersAutoStartConfiguration = None,
        auto_stop_configuration: ListSessionClustersResponseBodySessionClustersAutoStopConfiguration = None,
        domain: str = None,
        draft_id: str = None,
        kind: str = None,
        name: str = None,
        queue_name: str = None,
        release_version: str = None,
        session_cluster_id: str = None,
        state: str = None,
        state_change_reason: ListSessionClustersResponseBodySessionClustersStateChangeReason = None,
        user_id: str = None,
        user_name: str = None,
        web_ui: str = None,
        workspace_id: str = None,
    ):
        # The SQL Compute configurations, which are equivalent to the configurations of the Spark job.
        self.application_configs = application_configs
        # The automatic startup configurations.
        self.auto_start_configuration = auto_start_configuration
        # The automatic termination configurations.
        self.auto_stop_configuration = auto_stop_configuration
        self.domain = domain
        self.draft_id = draft_id
        self.kind = kind
        # The name of the SQL Compute.
        self.name = name
        # The name of the queue on which the SQL Compute runs.
        self.queue_name = queue_name
        self.release_version = release_version
        # The SQL Compute ID.
        self.session_cluster_id = session_cluster_id
        # The status of the SQL Compute.
        self.state = state
        # The details of the last status change of the SQL Compute.
        self.state_change_reason = state_change_reason
        # The user ID.
        self.user_id = user_id
        # The name of the user.
        self.user_name = user_name
        self.web_ui = web_ui
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.application_configs:
            for k in self.application_configs:
                if k:
                    k.validate()
        if self.auto_start_configuration:
            self.auto_start_configuration.validate()
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()
        if self.state_change_reason:
            self.state_change_reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applicationConfigs'] = []
        if self.application_configs is not None:
            for k in self.application_configs:
                result['applicationConfigs'].append(k.to_map() if k else None)
        if self.auto_start_configuration is not None:
            result['autoStartConfiguration'] = self.auto_start_configuration.to_map()
        if self.auto_stop_configuration is not None:
            result['autoStopConfiguration'] = self.auto_stop_configuration.to_map()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.draft_id is not None:
            result['draftId'] = self.draft_id
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        if self.state is not None:
            result['state'] = self.state
        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.web_ui is not None:
            result['webUI'] = self.web_ui
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('applicationConfigs') is not None:
            for k in m.get('applicationConfigs'):
                temp_model = ListSessionClustersResponseBodySessionClustersApplicationConfigs()
                self.application_configs.append(temp_model.from_map(k))
        if m.get('autoStartConfiguration') is not None:
            temp_model = ListSessionClustersResponseBodySessionClustersAutoStartConfiguration()
            self.auto_start_configuration = temp_model.from_map(m['autoStartConfiguration'])
        if m.get('autoStopConfiguration') is not None:
            temp_model = ListSessionClustersResponseBodySessionClustersAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m['autoStopConfiguration'])
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('draftId') is not None:
            self.draft_id = m.get('draftId')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('stateChangeReason') is not None:
            temp_model = ListSessionClustersResponseBodySessionClustersStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['stateChangeReason'])
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListSessionClustersResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        session_clusters: List[ListSessionClustersResponseBodySessionClusters] = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The SQL Computes.
        self.session_clusters = session_clusters
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.session_clusters:
            for k in self.session_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['sessionClusters'] = []
        if self.session_clusters is not None:
            for k in self.session_clusters:
                result['sessionClusters'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.session_clusters = []
        if m.get('sessionClusters') is not None:
            for k in m.get('sessionClusters'):
                temp_model = ListSessionClustersResponseBodySessionClusters()
                self.session_clusters.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
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


class ListWorkspaceQueuesRequest(TeaModel):
    def __init__(
        self,
        environment: str = None,
        region_id: str = None,
    ):
        # The environment type.
        # 
        # Valid values:
        # 
        # *   dev
        # *   production
        self.environment = environment
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment is not None:
            result['environment'] = self.environment
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environment') is not None:
            self.environment = m.get('environment')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListWorkspaceQueuesResponseBodyQueuesAllowActions(TeaModel):
    def __init__(
        self,
        action_arn: str = None,
        action_name: str = None,
        dependencies: List[str] = None,
        description: str = None,
        display_name: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of a behavior.
        self.action_arn = action_arn
        # The name of the permission.
        self.action_name = action_name
        # The dependencies of the operation.
        self.dependencies = dependencies
        # The description of the operation.
        self.description = description
        # The display name of the permission.
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_arn is not None:
            result['actionArn'] = self.action_arn
        if self.action_name is not None:
            result['actionName'] = self.action_name
        if self.dependencies is not None:
            result['dependencies'] = self.dependencies
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actionArn') is not None:
            self.action_arn = m.get('actionArn')
        if m.get('actionName') is not None:
            self.action_name = m.get('actionName')
        if m.get('dependencies') is not None:
            self.dependencies = m.get('dependencies')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        return self


class ListWorkspaceQueuesResponseBodyQueues(TeaModel):
    def __init__(
        self,
        allow_actions: List[ListWorkspaceQueuesResponseBodyQueuesAllowActions] = None,
        creator: str = None,
        environments: List[str] = None,
        max_resource: str = None,
        min_resource: str = None,
        properties: str = None,
        queue_name: str = None,
        queue_scope: str = None,
        queue_status: str = None,
        queue_type: str = None,
        region_id: str = None,
        used_resource: str = None,
        workspace_id: str = None,
    ):
        # The operations allowed for the queue.
        self.allow_actions = allow_actions
        # The ID of the user who created the queue.
        self.creator = creator
        # The environment types of the queue.
        self.environments = environments
        # The maximum capacity of resources that can be used in the queue.
        self.max_resource = max_resource
        # The minimum capacity of resources that can be used in the queue.
        self.min_resource = min_resource
        # The queue label.
        self.properties = properties
        # The name of the queue.
        self.queue_name = queue_name
        # The queue architecture.
        self.queue_scope = queue_scope
        # The status of the queue.
        self.queue_status = queue_status
        # The queue type.
        self.queue_type = queue_type
        # The region ID.
        self.region_id = region_id
        # The capacity of resources that are used in the queue.
        self.used_resource = used_resource
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.allow_actions:
            for k in self.allow_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['allowActions'] = []
        if self.allow_actions is not None:
            for k in self.allow_actions:
                result['allowActions'].append(k.to_map() if k else None)
        if self.creator is not None:
            result['creator'] = self.creator
        if self.environments is not None:
            result['environments'] = self.environments
        if self.max_resource is not None:
            result['maxResource'] = self.max_resource
        if self.min_resource is not None:
            result['minResource'] = self.min_resource
        if self.properties is not None:
            result['properties'] = self.properties
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.queue_scope is not None:
            result['queueScope'] = self.queue_scope
        if self.queue_status is not None:
            result['queueStatus'] = self.queue_status
        if self.queue_type is not None:
            result['queueType'] = self.queue_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.used_resource is not None:
            result['usedResource'] = self.used_resource
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.allow_actions = []
        if m.get('allowActions') is not None:
            for k in m.get('allowActions'):
                temp_model = ListWorkspaceQueuesResponseBodyQueuesAllowActions()
                self.allow_actions.append(temp_model.from_map(k))
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('environments') is not None:
            self.environments = m.get('environments')
        if m.get('maxResource') is not None:
            self.max_resource = m.get('maxResource')
        if m.get('minResource') is not None:
            self.min_resource = m.get('minResource')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('queueScope') is not None:
            self.queue_scope = m.get('queueScope')
        if m.get('queueStatus') is not None:
            self.queue_status = m.get('queueStatus')
        if m.get('queueType') is not None:
            self.queue_type = m.get('queueType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('usedResource') is not None:
            self.used_resource = m.get('usedResource')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListWorkspaceQueuesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        queues: List[ListWorkspaceQueuesResponseBodyQueues] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The list of queues.
        self.queues = queues
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.queues:
            for k in self.queues:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['queues'] = []
        if self.queues is not None:
            for k in self.queues:
                result['queues'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.queues = []
        if m.get('queues') is not None:
            for k in m.get('queues'):
                temp_model = ListWorkspaceQueuesResponseBodyQueues()
                self.queues.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListWorkspaceQueuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkspaceQueuesResponseBody = None,
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
            temp_model = ListWorkspaceQueuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspacesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        state: str = None,
    ):
        # The maximum number of entries to return.
        self.max_results = max_results
        # Fuzzy match is supported.
        self.name = name
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The workspace status.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.name is not None:
            result['name'] = self.name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListWorkspacesResponseBodyWorkspacesStateChangeReason(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code.
        self.code = code
        # The error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        auto_renew_period_unit: str = None,
        create_time: int = None,
        dlf_catalog_id: str = None,
        duration: int = None,
        end_time: int = None,
        fail_reason: str = None,
        payment_duration_unit: str = None,
        payment_status: str = None,
        payment_type: str = None,
        region_id: str = None,
        release_type: str = None,
        resource_spec: str = None,
        state_change_reason: ListWorkspacesResponseBodyWorkspacesStateChangeReason = None,
        storage: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_status: str = None,
    ):
        # Indicates whether auto-renewal is enabled. This parameter is required only if the paymentType parameter is set to Subscription.
        self.auto_renew = auto_renew
        # The auto-renewal duration. This parameter is required only if the paymentType parameter is set to Subscription.
        self.auto_renew_period = auto_renew_period
        # The unit of the auto-renewal duration. This parameter is required only if the paymentType parameter is set to Subscription.
        self.auto_renew_period_unit = auto_renew_period_unit
        # The time when the workspace was created.
        self.create_time = create_time
        # The information of the Data Lake Formation (DLF) catalog.
        self.dlf_catalog_id = dlf_catalog_id
        # The subscription period. This parameter is required only if the paymentType parameter is set to Subscription.
        self.duration = duration
        # The time when the workspace was released.
        self.end_time = end_time
        # The reason for the failure.
        self.fail_reason = fail_reason
        # The unit of the subscription duration. This parameter is required only if the paymentType parameter is set to Subscription.
        self.payment_duration_unit = payment_duration_unit
        # The status of the payment.
        self.payment_status = payment_status
        # The payment type.
        self.payment_type = payment_type
        # The region ID.
        self.region_id = region_id
        # The reason why the workspace is released.
        self.release_type = release_type
        # The resource specifications.
        self.resource_spec = resource_spec
        # The information about the workspace status change.
        self.state_change_reason = state_change_reason
        # The Object Storage Service (OSS) path.
        self.storage = storage
        # The workspace ID.
        self.workspace_id = workspace_id
        # The name of the workspace.
        self.workspace_name = workspace_name
        # The workspace status.
        self.workspace_status = workspace_status

    def validate(self):
        if self.state_change_reason:
            self.state_change_reason.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        if self.auto_renew_period_unit is not None:
            result['autoRenewPeriodUnit'] = self.auto_renew_period_unit
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.dlf_catalog_id is not None:
            result['dlfCatalogId'] = self.dlf_catalog_id
        if self.duration is not None:
            result['duration'] = self.duration
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.fail_reason is not None:
            result['failReason'] = self.fail_reason
        if self.payment_duration_unit is not None:
            result['paymentDurationUnit'] = self.payment_duration_unit
        if self.payment_status is not None:
            result['paymentStatus'] = self.payment_status
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_type is not None:
            result['releaseType'] = self.release_type
        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec
        if self.state_change_reason is not None:
            result['stateChangeReason'] = self.state_change_reason.to_map()
        if self.storage is not None:
            result['storage'] = self.storage
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        if self.workspace_status is not None:
            result['workspaceStatus'] = self.workspace_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('autoRenewPeriodUnit') is not None:
            self.auto_renew_period_unit = m.get('autoRenewPeriodUnit')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('dlfCatalogId') is not None:
            self.dlf_catalog_id = m.get('dlfCatalogId')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('failReason') is not None:
            self.fail_reason = m.get('failReason')
        if m.get('paymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('paymentDurationUnit')
        if m.get('paymentStatus') is not None:
            self.payment_status = m.get('paymentStatus')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseType') is not None:
            self.release_type = m.get('releaseType')
        if m.get('resourceSpec') is not None:
            self.resource_spec = m.get('resourceSpec')
        if m.get('stateChangeReason') is not None:
            temp_model = ListWorkspacesResponseBodyWorkspacesStateChangeReason()
            self.state_change_reason = temp_model.from_map(m['stateChangeReason'])
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        if m.get('workspaceStatus') is not None:
            self.workspace_status = m.get('workspaceStatus')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        workspaces: List[ListWorkspacesResponseBodyWorkspaces] = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The workspaces.
        self.workspaces = workspaces

    def validate(self):
        if self.workspaces:
            for k in self.workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['workspaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.workspaces = []
        if m.get('workspaces') is not None:
            for k in m.get('workspaces'):
                temp_model = ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k))
        return self


class ListWorkspacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkspacesResponseBody = None,
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobRunRequestConfigurationOverridesConfigurations(TeaModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # The configuration file of SparkConf.
        self.config_file_name = config_file_name
        # The key of SparkConf.
        self.config_item_key = config_item_key
        # The value of SparkConf.
        self.config_item_value = config_item_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_file_name is not None:
            result['configFileName'] = self.config_file_name
        if self.config_item_key is not None:
            result['configItemKey'] = self.config_item_key
        if self.config_item_value is not None:
            result['configItemValue'] = self.config_item_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configFileName') is not None:
            self.config_file_name = m.get('configFileName')
        if m.get('configItemKey') is not None:
            self.config_item_key = m.get('configItemKey')
        if m.get('configItemValue') is not None:
            self.config_item_value = m.get('configItemValue')
        return self


class StartJobRunRequestConfigurationOverrides(TeaModel):
    def __init__(
        self,
        configurations: List[StartJobRunRequestConfigurationOverridesConfigurations] = None,
    ):
        # The SparkConf objects.
        self.configurations = configurations

    def validate(self):
        if self.configurations:
            for k in self.configurations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configurations'] = []
        if self.configurations is not None:
            for k in self.configurations:
                result['configurations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configurations = []
        if m.get('configurations') is not None:
            for k in m.get('configurations'):
                temp_model = StartJobRunRequestConfigurationOverridesConfigurations()
                self.configurations.append(temp_model.from_map(k))
        return self


class StartJobRunRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        code_type: str = None,
        configuration_overrides: StartJobRunRequestConfigurationOverrides = None,
        execution_timeout_seconds: int = None,
        job_driver: JobDriver = None,
        job_id: str = None,
        name: str = None,
        release_version: str = None,
        resource_queue_id: str = None,
        tags: List[Tag] = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The code type of the job. Valid values:
        # 
        # *   SQL
        # *   JAR
        # *   PYTHON
        self.code_type = code_type
        # The advanced configurations of Spark.
        self.configuration_overrides = configuration_overrides
        # The timeout period of the job.
        self.execution_timeout_seconds = execution_timeout_seconds
        # The information about Spark Driver.
        self.job_driver = job_driver
        # The job ID.
        self.job_id = job_id
        # The job name.
        self.name = name
        # The version number of Spark.
        self.release_version = release_version
        # The name of the resource queue on which the Spark job runs.
        self.resource_queue_id = resource_queue_id
        # The tags of the job.
        self.tags = tags
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.configuration_overrides:
            self.configuration_overrides.validate()
        if self.job_driver:
            self.job_driver.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.code_type is not None:
            result['codeType'] = self.code_type
        if self.configuration_overrides is not None:
            result['configurationOverrides'] = self.configuration_overrides.to_map()
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.name is not None:
            result['name'] = self.name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('codeType') is not None:
            self.code_type = m.get('codeType')
        if m.get('configurationOverrides') is not None:
            temp_model = StartJobRunRequestConfigurationOverrides()
            self.configuration_overrides = temp_model.from_map(m['configurationOverrides'])
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('jobDriver') is not None:
            temp_model = JobDriver()
            self.job_driver = temp_model.from_map(m['jobDriver'])
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class StartJobRunResponseBody(TeaModel):
    def __init__(
        self,
        job_run_id: str = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_run_id = job_run_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StartJobRunResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartJobRunResponseBody = None,
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
            temp_model = StartJobRunResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateSqlStatementRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class TerminateSqlStatementResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class TerminateSqlStatementResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TerminateSqlStatementResponseBody = None,
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
            temp_model = TerminateSqlStatementResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


