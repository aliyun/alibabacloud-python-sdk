# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


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
        catagory_biz_id: str = None,
        creator: int = None,
        credential: Credential = None,
        full_path: List[str] = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        location: str = None,
        modifier: int = None,
        modifier_name: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        self.catagory_biz_id = catagory_biz_id
        # This parameter is required.
        self.creator = creator
        self.credential = credential
        self.full_path = full_path
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.location = location
        # This parameter is required.
        self.modifier = modifier
        self.modifier_name = modifier_name
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
        if self.catagory_biz_id is not None:
            result['catagoryBizId'] = self.catagory_biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
        if self.full_path is not None:
            result['fullPath'] = self.full_path
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.location is not None:
            result['location'] = self.location
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('catagoryBizId') is not None:
            self.catagory_biz_id = m.get('catagoryBizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('credential') is not None:
            temp_model = Credential()
            self.credential = temp_model.from_map(m['credential'])
        if m.get('fullPath') is not None:
            self.full_path = m.get('fullPath')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')
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


class KerberosConf(TeaModel):
    def __init__(
        self,
        creator: str = None,
        enabled: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        kerberos_conf_id: str = None,
        keytabs: List[str] = None,
        krb_5conf: str = None,
        name: str = None,
        network_service_id: str = None,
        workspace_id: str = None,
    ):
        self.creator = creator
        self.enabled = enabled
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.kerberos_conf_id = kerberos_conf_id
        self.keytabs = keytabs
        self.krb_5conf = krb_5conf
        self.name = name
        self.network_service_id = network_service_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.kerberos_conf_id is not None:
            result['kerberosConfId'] = self.kerberos_conf_id
        if self.keytabs is not None:
            result['keytabs'] = self.keytabs
        if self.krb_5conf is not None:
            result['krb5Conf'] = self.krb_5conf
        if self.name is not None:
            result['name'] = self.name
        if self.network_service_id is not None:
            result['networkServiceId'] = self.network_service_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('kerberosConfId') is not None:
            self.kerberos_conf_id = m.get('kerberosConfId')
        if m.get('keytabs') is not None:
            self.keytabs = m.get('keytabs')
        if m.get('krb5Conf') is not None:
            self.krb_5conf = m.get('krb5Conf')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkServiceId') is not None:
            self.network_service_id = m.get('networkServiceId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
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


class TaskCredential(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_url: str = None,
        expire: int = None,
        host: str = None,
        path: str = None,
        policy: str = None,
        security_token: str = None,
        signature: str = None,
    ):
        self.access_id = access_id
        self.access_url = access_url
        self.expire = expire
        self.host = host
        self.path = path
        self.policy = policy
        self.security_token = security_token
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
        if self.access_url is not None:
            result['accessUrl'] = self.access_url
        if self.expire is not None:
            result['expire'] = self.expire
        if self.host is not None:
            result['host'] = self.host
        if self.path is not None:
            result['path'] = self.path
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
        if m.get('accessUrl') is not None:
            self.access_url = m.get('accessUrl')
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('securityToken') is not None:
            self.security_token = m.get('securityToken')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
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
        credential: TaskCredential = None,
        default_catalog_id: str = None,
        default_database: str = None,
        default_resource_queue_id: str = None,
        default_sql_compute_id: str = None,
        deployment_id: str = None,
        environment_id: str = None,
        extra_artifact_ids: List[str] = None,
        extra_spark_submit_params: str = None,
        files: List[str] = None,
        fusion: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        has_changed: bool = None,
        has_commited: bool = None,
        is_streaming: bool = None,
        jars: List[str] = None,
        kernel_id: str = None,
        last_run_resource_queue_id: str = None,
        modifier: int = None,
        name: str = None,
        params: Dict[str, str] = None,
        py_files: List[str] = None,
        session_cluster_id: str = None,
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
        timeout: int = None,
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
        self.credential = credential
        self.default_catalog_id = default_catalog_id
        self.default_database = default_database
        self.default_resource_queue_id = default_resource_queue_id
        self.default_sql_compute_id = default_sql_compute_id
        self.deployment_id = deployment_id
        self.environment_id = environment_id
        self.extra_artifact_ids = extra_artifact_ids
        self.extra_spark_submit_params = extra_spark_submit_params
        self.files = files
        self.fusion = fusion
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        self.has_changed = has_changed
        # This parameter is required.
        self.has_commited = has_commited
        self.is_streaming = is_streaming
        self.jars = jars
        self.kernel_id = kernel_id
        self.last_run_resource_queue_id = last_run_resource_queue_id
        # This parameter is required.
        self.modifier = modifier
        # This parameter is required.
        self.name = name
        self.params = params
        self.py_files = py_files
        self.session_cluster_id = session_cluster_id
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
        self.timeout = timeout
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.credential:
            self.credential.validate()
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
        if self.credential is not None:
            result['credential'] = self.credential.to_map()
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
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.extra_artifact_ids is not None:
            result['extraArtifactIds'] = self.extra_artifact_ids
        if self.extra_spark_submit_params is not None:
            result['extraSparkSubmitParams'] = self.extra_spark_submit_params
        if self.files is not None:
            result['files'] = self.files
        if self.fusion is not None:
            result['fusion'] = self.fusion
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
        if self.kernel_id is not None:
            result['kernelId'] = self.kernel_id
        if self.last_run_resource_queue_id is not None:
            result['lastRunResourceQueueId'] = self.last_run_resource_queue_id
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
        if self.params is not None:
            result['params'] = self.params
        if self.py_files is not None:
            result['pyFiles'] = self.py_files
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
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
        if self.timeout is not None:
            result['timeout'] = self.timeout
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
        if m.get('credential') is not None:
            temp_model = TaskCredential()
            self.credential = temp_model.from_map(m['credential'])
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
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('extraArtifactIds') is not None:
            self.extra_artifact_ids = m.get('extraArtifactIds')
        if m.get('extraSparkSubmitParams') is not None:
            self.extra_spark_submit_params = m.get('extraSparkSubmitParams')
        if m.get('files') is not None:
            self.files = m.get('files')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
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
        if m.get('kernelId') is not None:
            self.kernel_id = m.get('kernelId')
        if m.get('lastRunResourceQueueId') is not None:
            self.last_run_resource_queue_id = m.get('lastRunResourceQueueId')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('pyFiles') is not None:
            self.py_files = m.get('pyFiles')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
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
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
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
        biz_id: str = None,
        creator: int = None,
        display_spark_version: str = None,
        fusion: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        is_default: bool = None,
        modifier: int = None,
        name: str = None,
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
        self.biz_id = biz_id
        # This parameter is required.
        self.creator = creator
        self.display_spark_version = display_spark_version
        self.fusion = fusion
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        self.is_default = is_default
        # This parameter is required.
        self.modifier = modifier
        self.name = name
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
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.creator is not None:
            result['creator'] = self.creator
        if self.display_spark_version is not None:
            result['displaySparkVersion'] = self.display_spark_version
        if self.fusion is not None:
            result['fusion'] = self.fusion
        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.modifier is not None:
            result['modifier'] = self.modifier
        if self.name is not None:
            result['name'] = self.name
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
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('displaySparkVersion') is not None:
            self.display_spark_version = m.get('displaySparkVersion')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')
        if m.get('name') is not None:
            self.name = m.get('name')
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


class CreateLivyComputeRequestAutoStartConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
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


class CreateLivyComputeRequestAutoStopConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        self.enable = enable
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


class CreateLivyComputeRequest(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        auto_start_configuration: CreateLivyComputeRequestAutoStartConfiguration = None,
        auto_stop_configuration: CreateLivyComputeRequestAutoStopConfiguration = None,
        cpu_limit: str = None,
        display_release_version: str = None,
        enable_public: bool = None,
        environment_id: str = None,
        fusion: bool = None,
        livy_server_conf: str = None,
        livy_version: str = None,
        memory_limit: str = None,
        name: str = None,
        network_name: str = None,
        queue_name: str = None,
        release_version: str = None,
        region_id: str = None,
    ):
        self.auth_type = auth_type
        self.auto_start_configuration = auto_start_configuration
        self.auto_stop_configuration = auto_stop_configuration
        self.cpu_limit = cpu_limit
        self.display_release_version = display_release_version
        self.enable_public = enable_public
        self.environment_id = environment_id
        self.fusion = fusion
        self.livy_server_conf = livy_server_conf
        self.livy_version = livy_version
        self.memory_limit = memory_limit
        self.name = name
        self.network_name = network_name
        self.queue_name = queue_name
        self.release_version = release_version
        self.region_id = region_id

    def validate(self):
        if self.auto_start_configuration:
            self.auto_start_configuration.validate()
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.auto_start_configuration is not None:
            result['autoStartConfiguration'] = self.auto_start_configuration.to_map()
        if self.auto_stop_configuration is not None:
            result['autoStopConfiguration'] = self.auto_stop_configuration.to_map()
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.fusion is not None:
            result['fusion'] = self.fusion
        if self.livy_server_conf is not None:
            result['livyServerConf'] = self.livy_server_conf
        if self.livy_version is not None:
            result['livyVersion'] = self.livy_version
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.name is not None:
            result['name'] = self.name
        if self.network_name is not None:
            result['networkName'] = self.network_name
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('autoStartConfiguration') is not None:
            temp_model = CreateLivyComputeRequestAutoStartConfiguration()
            self.auto_start_configuration = temp_model.from_map(m['autoStartConfiguration'])
        if m.get('autoStopConfiguration') is not None:
            temp_model = CreateLivyComputeRequestAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m['autoStopConfiguration'])
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        if m.get('livyServerConf') is not None:
            self.livy_server_conf = m.get('livyServerConf')
        if m.get('livyVersion') is not None:
            self.livy_version = m.get('livyVersion')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkName') is not None:
            self.network_name = m.get('networkName')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateLivyComputeResponseBodyData(TeaModel):
    def __init__(
        self,
        livy_compute_id: str = None,
    ):
        self.livy_compute_id = livy_compute_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.livy_compute_id is not None:
            result['livyComputeId'] = self.livy_compute_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('livyComputeId') is not None:
            self.livy_compute_id = m.get('livyComputeId')
        return self


class CreateLivyComputeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateLivyComputeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateLivyComputeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateLivyComputeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLivyComputeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLivyComputeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLivyComputeTokenRequestAutoExpireConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        expire_days: int = None,
    ):
        self.enable = enable
        self.expire_days = expire_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.expire_days is not None:
            result['expireDays'] = self.expire_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('expireDays') is not None:
            self.expire_days = m.get('expireDays')
        return self


class CreateLivyComputeTokenRequest(TeaModel):
    def __init__(
        self,
        auto_expire_configuration: CreateLivyComputeTokenRequestAutoExpireConfiguration = None,
        name: str = None,
        token: str = None,
        region_id: str = None,
    ):
        self.auto_expire_configuration = auto_expire_configuration
        self.name = name
        self.token = token
        self.region_id = region_id

    def validate(self):
        if self.auto_expire_configuration:
            self.auto_expire_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_expire_configuration is not None:
            result['autoExpireConfiguration'] = self.auto_expire_configuration.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.token is not None:
            result['token'] = self.token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoExpireConfiguration') is not None:
            temp_model = CreateLivyComputeTokenRequestAutoExpireConfiguration()
            self.auto_expire_configuration = temp_model.from_map(m['autoExpireConfiguration'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateLivyComputeTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        token_id: str = None,
    ):
        # Token ID。
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        return self


class CreateLivyComputeTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateLivyComputeTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateLivyComputeTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateLivyComputeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLivyComputeTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLivyComputeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProcessDefinitionWithScheduleRequestGlobalParams(TeaModel):
    def __init__(
        self,
        direct: str = None,
        prop: str = None,
        type: str = None,
        value: str = None,
    ):
        self.direct = direct
        self.prop = prop
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direct is not None:
            result['direct'] = self.direct
        if self.prop is not None:
            result['prop'] = self.prop
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direct') is not None:
            self.direct = m.get('direct')
        if m.get('prop') is not None:
            self.prop = m.get('prop')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateProcessDefinitionWithScheduleRequestSchedule(TeaModel):
    def __init__(
        self,
        crontab: str = None,
        end_time: str = None,
        start_time: str = None,
        timezone_id: str = None,
    ):
        # The CRON expression that is used for scheduling.
        self.crontab = crontab
        # The end time of the scheduling.
        self.end_time = end_time
        # The start time of the scheduling.
        self.start_time = start_time
        # The ID of the time zone.
        self.timezone_id = timezone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crontab is not None:
            result['crontab'] = self.crontab
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.timezone_id is not None:
            result['timezoneId'] = self.timezone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crontab') is not None:
            self.crontab = m.get('crontab')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('timezoneId') is not None:
            self.timezone_id = m.get('timezoneId')
        return self


class CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams(TeaModel):
    def __init__(
        self,
        direct: str = None,
        prop: str = None,
        type: str = None,
        value: str = None,
    ):
        self.direct = direct
        self.prop = prop
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direct is not None:
            result['direct'] = self.direct
        if self.prop is not None:
            result['prop'] = self.prop
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direct') is not None:
            self.direct = m.get('direct')
        if m.get('prop') is not None:
            self.prop = m.get('prop')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the SparkConf object.
        self.key = key
        # The value of the SparkConf object.
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


class CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams(TeaModel):
    def __init__(
        self,
        display_spark_version: str = None,
        environment_id: str = None,
        fusion: bool = None,
        local_params: List[CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams] = None,
        resource_queue_id: str = None,
        spark_conf: List[CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf] = None,
        spark_driver_cores: int = None,
        spark_driver_memory: int = None,
        spark_executor_cores: int = None,
        spark_executor_memory: int = None,
        spark_log_level: str = None,
        spark_log_path: str = None,
        spark_version: str = None,
        task_biz_id: str = None,
        type: str = None,
        workspace_biz_id: str = None,
    ):
        # The displayed version of the Spark engine.
        self.display_spark_version = display_spark_version
        # The environment ID.
        self.environment_id = environment_id
        # Specifies whether to enable Fusion engine for acceleration.
        self.fusion = fusion
        self.local_params = local_params
        # The name of the resource queue on which the job runs.
        # 
        # This parameter is required.
        self.resource_queue_id = resource_queue_id
        # The configurations of the Spark job.
        self.spark_conf = spark_conf
        # The number of driver cores of the Spark job.
        self.spark_driver_cores = spark_driver_cores
        # The size of driver memory of the Spark job.
        self.spark_driver_memory = spark_driver_memory
        # The number of executor cores of the Spark job.
        self.spark_executor_cores = spark_executor_cores
        # The size of executor memory of the Spark job.
        self.spark_executor_memory = spark_executor_memory
        # The level of the Spark log.
        self.spark_log_level = spark_log_level
        # The path where the operational logs of the Spark job are stored.
        self.spark_log_path = spark_log_path
        # The version of the Spark engine.
        self.spark_version = spark_version
        # The ID of the data development job.
        # 
        # This parameter is required.
        self.task_biz_id = task_biz_id
        # The type of the Spark job.
        self.type = type
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_biz_id = workspace_biz_id

    def validate(self):
        if self.local_params:
            for k in self.local_params:
                if k:
                    k.validate()
        if self.spark_conf:
            for k in self.spark_conf:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_spark_version is not None:
            result['displaySparkVersion'] = self.display_spark_version
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.fusion is not None:
            result['fusion'] = self.fusion
        result['localParams'] = []
        if self.local_params is not None:
            for k in self.local_params:
                result['localParams'].append(k.to_map() if k else None)
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
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
        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id
        if self.type is not None:
            result['type'] = self.type
        if self.workspace_biz_id is not None:
            result['workspaceBizId'] = self.workspace_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displaySparkVersion') is not None:
            self.display_spark_version = m.get('displaySparkVersion')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        self.local_params = []
        if m.get('localParams') is not None:
            for k in m.get('localParams'):
                temp_model = CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams()
                self.local_params.append(temp_model.from_map(k))
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k in m.get('sparkConf'):
                temp_model = CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf()
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
        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('workspaceBizId') is not None:
            self.workspace_biz_id = m.get('workspaceBizId')
        return self


class CreateProcessDefinitionWithScheduleRequestTaskDefinitionJson(TeaModel):
    def __init__(
        self,
        alert_email_address: str = None,
        code: int = None,
        description: str = None,
        fail_alert_enable: bool = None,
        fail_retry_times: int = None,
        name: str = None,
        start_alert_enable: bool = None,
        tags: Dict[str, str] = None,
        task_params: CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams = None,
        task_type: str = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The node ID.
        # 
        # This parameter is required.
        self.code = code
        # The node description.
        self.description = description
        # Specifies whether to send alerts when the node fails.
        self.fail_alert_enable = fail_alert_enable
        # The number of retries when the node fails.
        self.fail_retry_times = fail_retry_times
        # The name of the node.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to send alerts when the node is started.
        self.start_alert_enable = start_alert_enable
        # The tags.
        self.tags = tags
        # The job parameters.
        # 
        # This parameter is required.
        self.task_params = task_params
        # The type of the node.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The timeout period of the callback. Unit: seconds.
        self.timeout = timeout

    def validate(self):
        if self.task_params:
            self.task_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.fail_alert_enable is not None:
            result['failAlertEnable'] = self.fail_alert_enable
        if self.fail_retry_times is not None:
            result['failRetryTimes'] = self.fail_retry_times
        if self.name is not None:
            result['name'] = self.name
        if self.start_alert_enable is not None:
            result['startAlertEnable'] = self.start_alert_enable
        if self.tags is not None:
            result['tags'] = self.tags
        if self.task_params is not None:
            result['taskParams'] = self.task_params.to_map()
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('failAlertEnable') is not None:
            self.fail_alert_enable = m.get('failAlertEnable')
        if m.get('failRetryTimes') is not None:
            self.fail_retry_times = m.get('failRetryTimes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('startAlertEnable') is not None:
            self.start_alert_enable = m.get('startAlertEnable')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('taskParams') is not None:
            temp_model = CreateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams()
            self.task_params = temp_model.from_map(m['taskParams'])
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateProcessDefinitionWithScheduleRequestTaskRelationJson(TeaModel):
    def __init__(
        self,
        name: str = None,
        post_task_code: int = None,
        post_task_version: int = None,
        pre_task_code: int = None,
        pre_task_version: int = None,
    ):
        # The name of the node topology. You can enter a workflow name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the downstream node.
        # 
        # This parameter is required.
        self.post_task_code = post_task_code
        # The version of the downstream node.
        # 
        # This parameter is required.
        self.post_task_version = post_task_version
        # The ID of the upstream node.
        # 
        # This parameter is required.
        self.pre_task_code = pre_task_code
        # The version of the upstream node.
        # 
        # This parameter is required.
        self.pre_task_version = pre_task_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.post_task_code is not None:
            result['postTaskCode'] = self.post_task_code
        if self.post_task_version is not None:
            result['postTaskVersion'] = self.post_task_version
        if self.pre_task_code is not None:
            result['preTaskCode'] = self.pre_task_code
        if self.pre_task_version is not None:
            result['preTaskVersion'] = self.pre_task_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('postTaskCode') is not None:
            self.post_task_code = m.get('postTaskCode')
        if m.get('postTaskVersion') is not None:
            self.post_task_version = m.get('postTaskVersion')
        if m.get('preTaskCode') is not None:
            self.pre_task_code = m.get('preTaskCode')
        if m.get('preTaskVersion') is not None:
            self.pre_task_version = m.get('preTaskVersion')
        return self


class CreateProcessDefinitionWithScheduleRequest(TeaModel):
    def __init__(
        self,
        alert_email_address: str = None,
        description: str = None,
        execution_type: str = None,
        global_params: List[CreateProcessDefinitionWithScheduleRequestGlobalParams] = None,
        name: str = None,
        product_namespace: str = None,
        publish: bool = None,
        region_id: str = None,
        resource_queue: str = None,
        retry_times: int = None,
        run_as: str = None,
        schedule: CreateProcessDefinitionWithScheduleRequestSchedule = None,
        tags: Dict[str, str] = None,
        task_definition_json: List[CreateProcessDefinitionWithScheduleRequestTaskDefinitionJson] = None,
        task_parallelism: int = None,
        task_relation_json: List[CreateProcessDefinitionWithScheduleRequestTaskRelationJson] = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The description of the workflow.
        # 
        # This parameter is required.
        self.description = description
        # The execution policy
        # 
        # This parameter is required.
        self.execution_type = execution_type
        self.global_params = global_params
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The code of the service.
        # 
        # This parameter is required.
        self.product_namespace = product_namespace
        # Specifies whether to publish the workflow.
        self.publish = publish
        # The region ID.
        self.region_id = region_id
        # The resource queue.
        self.resource_queue = resource_queue
        # The number of retries.
        self.retry_times = retry_times
        # The ID of the Alibaba Cloud account used by the user who creates the workflow.
        self.run_as = run_as
        # The scheduling settings.
        self.schedule = schedule
        # The tags.
        self.tags = tags
        # The descriptions of all nodes in the workflow.
        # 
        # This parameter is required.
        self.task_definition_json = task_definition_json
        # The node parallelism.
        self.task_parallelism = task_parallelism
        # The dependencies of all nodes in the workflow. preTaskCode specifies the ID of an upstream node, and postTaskCode specifies the ID of a downstream node. The ID of each node is unique. If a node does not have an upstream node, set preTaskCode to 0.
        # 
        # This parameter is required.
        self.task_relation_json = task_relation_json
        # The default timeout period of the workflow.
        self.timeout = timeout

    def validate(self):
        if self.global_params:
            for k in self.global_params:
                if k:
                    k.validate()
        if self.schedule:
            self.schedule.validate()
        if self.task_definition_json:
            for k in self.task_definition_json:
                if k:
                    k.validate()
        if self.task_relation_json:
            for k in self.task_relation_json:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address
        if self.description is not None:
            result['description'] = self.description
        if self.execution_type is not None:
            result['executionType'] = self.execution_type
        result['globalParams'] = []
        if self.global_params is not None:
            for k in self.global_params:
                result['globalParams'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace
        if self.publish is not None:
            result['publish'] = self.publish
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_queue is not None:
            result['resourceQueue'] = self.resource_queue
        if self.retry_times is not None:
            result['retryTimes'] = self.retry_times
        if self.run_as is not None:
            result['runAs'] = self.run_as
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        if self.tags is not None:
            result['tags'] = self.tags
        result['taskDefinitionJson'] = []
        if self.task_definition_json is not None:
            for k in self.task_definition_json:
                result['taskDefinitionJson'].append(k.to_map() if k else None)
        if self.task_parallelism is not None:
            result['taskParallelism'] = self.task_parallelism
        result['taskRelationJson'] = []
        if self.task_relation_json is not None:
            for k in self.task_relation_json:
                result['taskRelationJson'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')
        self.global_params = []
        if m.get('globalParams') is not None:
            for k in m.get('globalParams'):
                temp_model = CreateProcessDefinitionWithScheduleRequestGlobalParams()
                self.global_params.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')
        if m.get('publish') is not None:
            self.publish = m.get('publish')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceQueue') is not None:
            self.resource_queue = m.get('resourceQueue')
        if m.get('retryTimes') is not None:
            self.retry_times = m.get('retryTimes')
        if m.get('runAs') is not None:
            self.run_as = m.get('runAs')
        if m.get('schedule') is not None:
            temp_model = CreateProcessDefinitionWithScheduleRequestSchedule()
            self.schedule = temp_model.from_map(m['schedule'])
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        self.task_definition_json = []
        if m.get('taskDefinitionJson') is not None:
            for k in m.get('taskDefinitionJson'):
                temp_model = CreateProcessDefinitionWithScheduleRequestTaskDefinitionJson()
                self.task_definition_json.append(temp_model.from_map(k))
        if m.get('taskParallelism') is not None:
            self.task_parallelism = m.get('taskParallelism')
        self.task_relation_json = []
        if m.get('taskRelationJson') is not None:
            for k in m.get('taskRelationJson'):
                temp_model = CreateProcessDefinitionWithScheduleRequestTaskRelationJson()
                self.task_relation_json.append(temp_model.from_map(k))
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateProcessDefinitionWithScheduleShrinkRequest(TeaModel):
    def __init__(
        self,
        alert_email_address: str = None,
        description: str = None,
        execution_type: str = None,
        global_params_shrink: str = None,
        name: str = None,
        product_namespace: str = None,
        publish: bool = None,
        region_id: str = None,
        resource_queue: str = None,
        retry_times: int = None,
        run_as: str = None,
        schedule_shrink: str = None,
        tags_shrink: str = None,
        task_definition_json_shrink: str = None,
        task_parallelism: int = None,
        task_relation_json_shrink: str = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The description of the workflow.
        # 
        # This parameter is required.
        self.description = description
        # The execution policy
        # 
        # This parameter is required.
        self.execution_type = execution_type
        self.global_params_shrink = global_params_shrink
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The code of the service.
        # 
        # This parameter is required.
        self.product_namespace = product_namespace
        # Specifies whether to publish the workflow.
        self.publish = publish
        # The region ID.
        self.region_id = region_id
        # The resource queue.
        self.resource_queue = resource_queue
        # The number of retries.
        self.retry_times = retry_times
        # The ID of the Alibaba Cloud account used by the user who creates the workflow.
        self.run_as = run_as
        # The scheduling settings.
        self.schedule_shrink = schedule_shrink
        # The tags.
        self.tags_shrink = tags_shrink
        # The descriptions of all nodes in the workflow.
        # 
        # This parameter is required.
        self.task_definition_json_shrink = task_definition_json_shrink
        # The node parallelism.
        self.task_parallelism = task_parallelism
        # The dependencies of all nodes in the workflow. preTaskCode specifies the ID of an upstream node, and postTaskCode specifies the ID of a downstream node. The ID of each node is unique. If a node does not have an upstream node, set preTaskCode to 0.
        # 
        # This parameter is required.
        self.task_relation_json_shrink = task_relation_json_shrink
        # The default timeout period of the workflow.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address
        if self.description is not None:
            result['description'] = self.description
        if self.execution_type is not None:
            result['executionType'] = self.execution_type
        if self.global_params_shrink is not None:
            result['globalParams'] = self.global_params_shrink
        if self.name is not None:
            result['name'] = self.name
        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace
        if self.publish is not None:
            result['publish'] = self.publish
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.resource_queue is not None:
            result['resourceQueue'] = self.resource_queue
        if self.retry_times is not None:
            result['retryTimes'] = self.retry_times
        if self.run_as is not None:
            result['runAs'] = self.run_as
        if self.schedule_shrink is not None:
            result['schedule'] = self.schedule_shrink
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        if self.task_definition_json_shrink is not None:
            result['taskDefinitionJson'] = self.task_definition_json_shrink
        if self.task_parallelism is not None:
            result['taskParallelism'] = self.task_parallelism
        if self.task_relation_json_shrink is not None:
            result['taskRelationJson'] = self.task_relation_json_shrink
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')
        if m.get('globalParams') is not None:
            self.global_params_shrink = m.get('globalParams')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')
        if m.get('publish') is not None:
            self.publish = m.get('publish')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('resourceQueue') is not None:
            self.resource_queue = m.get('resourceQueue')
        if m.get('retryTimes') is not None:
            self.retry_times = m.get('retryTimes')
        if m.get('runAs') is not None:
            self.run_as = m.get('runAs')
        if m.get('schedule') is not None:
            self.schedule_shrink = m.get('schedule')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        if m.get('taskDefinitionJson') is not None:
            self.task_definition_json_shrink = m.get('taskDefinitionJson')
        if m.get('taskParallelism') is not None:
            self.task_parallelism = m.get('taskParallelism')
        if m.get('taskRelationJson') is not None:
            self.task_relation_json_shrink = m.get('taskRelationJson')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class CreateProcessDefinitionWithScheduleResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        id: int = None,
    ):
        # The workflow ID.
        self.code = code
        # The serial number of the workflow.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateProcessDefinitionWithScheduleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: CreateProcessDefinitionWithScheduleResponseBodyData = None,
        failed: str = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The code that is returned by the backend server.
        self.code = code
        # The returned data.
        self.data = data
        # Indicates whether the request failed.
        self.failed = failed
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The description of the returned code.
        self.msg = msg
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
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.failed is not None:
            result['failed'] = self.failed
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateProcessDefinitionWithScheduleResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateProcessDefinitionWithScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProcessDefinitionWithScheduleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProcessDefinitionWithScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSessionClusterRequestApplicationConfigs(TeaModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # The name of the configuration file.
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


class CreateSessionClusterRequestAutoStartConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Specifies whether to enable automatic startup.
        # 
        # *   true
        # *   false
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


class CreateSessionClusterRequestAutoStopConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        # Specifies whether to enable automatic termination.
        # 
        # *   true
        # *   false
        self.enable = enable
        # The idle timeout period. The session is automatically terminated when the idle timeout period is exceeded.
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


class CreateSessionClusterRequest(TeaModel):
    def __init__(
        self,
        application_configs: List[CreateSessionClusterRequestApplicationConfigs] = None,
        auto_start_configuration: CreateSessionClusterRequestAutoStartConfiguration = None,
        auto_stop_configuration: CreateSessionClusterRequestAutoStopConfiguration = None,
        display_release_version: str = None,
        env_id: str = None,
        fusion: bool = None,
        kind: str = None,
        name: str = None,
        public_endpoint_enabled: bool = None,
        queue_name: str = None,
        release_version: str = None,
        region_id: str = None,
    ):
        # The Spark configurations.
        self.application_configs = application_configs
        # Specifies whether to enable automatic startup.
        # 
        # *   true
        # *   false
        self.auto_start_configuration = auto_start_configuration
        # The automatic termination configuration.
        self.auto_stop_configuration = auto_stop_configuration
        # The version of the Spark engine.
        self.display_release_version = display_release_version
        # The ID of the Python environment. This parameter takes effect only for notebook sessions.
        self.env_id = env_id
        # Specifies whether to enable Fusion engine for acceleration.
        self.fusion = fusion
        # The session type.
        # 
        # *   SQL
        # *   NOTEBOOK
        self.kind = kind
        # The name of the job.
        self.name = name
        self.public_endpoint_enabled = public_endpoint_enabled
        # The queue name.
        self.queue_name = queue_name
        # The version number of Spark.
        self.release_version = release_version
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.application_configs:
            for k in self.application_configs:
                if k:
                    k.validate()
        if self.auto_start_configuration:
            self.auto_start_configuration.validate()
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()

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
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.fusion is not None:
            result['fusion'] = self.fusion
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.public_endpoint_enabled is not None:
            result['publicEndpointEnabled'] = self.public_endpoint_enabled
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_configs = []
        if m.get('applicationConfigs') is not None:
            for k in m.get('applicationConfigs'):
                temp_model = CreateSessionClusterRequestApplicationConfigs()
                self.application_configs.append(temp_model.from_map(k))
        if m.get('autoStartConfiguration') is not None:
            temp_model = CreateSessionClusterRequestAutoStartConfiguration()
            self.auto_start_configuration = temp_model.from_map(m['autoStartConfiguration'])
        if m.get('autoStopConfiguration') is not None:
            temp_model = CreateSessionClusterRequestAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m['autoStopConfiguration'])
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('publicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('publicEndpointEnabled')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_cluster_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The session ID.
        self.session_cluster_id = session_cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
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
        # The SQL session ID. You can create an SQL session in the workspace created in EMR Serverless Spark.
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
        # The interactive query ID.
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


class CreateWorkspaceRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cu: str = None,
    ):
        # The maximum resource quota for a workspace.
        self.cu = cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        return self


class CreateWorkspaceRequestTag(TeaModel):
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


class CreateWorkspaceRequest(TeaModel):
    def __init__(
        self,
        auto_renew: str = None,
        auto_renew_period: str = None,
        auto_renew_period_unit: str = None,
        auto_start_session_cluster: bool = None,
        client_token: str = None,
        dlf_catalog_id: str = None,
        dlf_type: str = None,
        duration: str = None,
        oss_bucket: str = None,
        payment_duration_unit: str = None,
        payment_type: str = None,
        ram_role_name: str = None,
        release_type: str = None,
        resource_spec: CreateWorkspaceRequestResourceSpec = None,
        tag: List[CreateWorkspaceRequestTag] = None,
        workspace_name: str = None,
        region_id: str = None,
    ):
        # Specifies whether to enable auto-renewal. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew = auto_renew
        # The auto-renewal duration. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew_period = auto_renew_period
        # The unit of the auto-renewal duration. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew_period_unit = auto_renew_period_unit
        # Specifies whether to automatically start a session.
        self.auto_start_session_cluster = auto_start_session_cluster
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The information of the Data Lake Formation (DLF) catalog.
        self.dlf_catalog_id = dlf_catalog_id
        # The version of DLF.
        self.dlf_type = dlf_type
        # The subscription period. This parameter is required only if the paymentType parameter is set to Pre.
        self.duration = duration
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_bucket = oss_bucket
        # The unit of the subscription duration.
        self.payment_duration_unit = payment_duration_unit
        # The billing method. Valid values:
        # 
        # *   PayAsYouGo
        # *   Pre
        self.payment_type = payment_type
        # The name of the role used to run Spark jobs.
        self.ram_role_name = ram_role_name
        # The type of the version.
        self.release_type = release_type
        # The resource specifications.
        self.resource_spec = resource_spec
        self.tag = tag
        # The name of the workspace.
        self.workspace_name = workspace_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

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
        if self.auto_start_session_cluster is not None:
            result['autoStartSessionCluster'] = self.auto_start_session_cluster
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.dlf_catalog_id is not None:
            result['dlfCatalogId'] = self.dlf_catalog_id
        if self.dlf_type is not None:
            result['dlfType'] = self.dlf_type
        if self.duration is not None:
            result['duration'] = self.duration
        if self.oss_bucket is not None:
            result['ossBucket'] = self.oss_bucket
        if self.payment_duration_unit is not None:
            result['paymentDurationUnit'] = self.payment_duration_unit
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.ram_role_name is not None:
            result['ramRoleName'] = self.ram_role_name
        if self.release_type is not None:
            result['releaseType'] = self.release_type
        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec.to_map()
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        if m.get('autoRenewPeriodUnit') is not None:
            self.auto_renew_period_unit = m.get('autoRenewPeriodUnit')
        if m.get('autoStartSessionCluster') is not None:
            self.auto_start_session_cluster = m.get('autoStartSessionCluster')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('dlfCatalogId') is not None:
            self.dlf_catalog_id = m.get('dlfCatalogId')
        if m.get('dlfType') is not None:
            self.dlf_type = m.get('dlfType')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('ossBucket') is not None:
            self.oss_bucket = m.get('ossBucket')
        if m.get('paymentDurationUnit') is not None:
            self.payment_duration_unit = m.get('paymentDurationUnit')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('ramRoleName') is not None:
            self.ram_role_name = m.get('ramRoleName')
        if m.get('releaseType') is not None:
            self.release_type = m.get('releaseType')
        if m.get('resourceSpec') is not None:
            temp_model = CreateWorkspaceRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['resourceSpec'])
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = CreateWorkspaceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class CreateWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        operation_id: str = None,
        request_id: str = None,
        workspace_id: str = None,
    ):
        # The operation ID.
        self.operation_id = operation_id
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operation_id is not None:
            result['operationId'] = self.operation_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWorkspaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLivyComputeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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


class DeleteLivyComputeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteLivyComputeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLivyComputeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLivyComputeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLivyComputeTokenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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


class DeleteLivyComputeTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteLivyComputeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLivyComputeTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteLivyComputeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditWorkspaceQueueRequestResourceSpec(TeaModel):
    def __init__(
        self,
        cu: int = None,
    ):
        self.cu = cu

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu is not None:
            result['cu'] = self.cu
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')
        return self


class EditWorkspaceQueueRequest(TeaModel):
    def __init__(
        self,
        environments: List[str] = None,
        resource_spec: EditWorkspaceQueueRequestResourceSpec = None,
        workspace_id: str = None,
        workspace_queue_name: str = None,
        region_id: str = None,
    ):
        self.environments = environments
        self.resource_spec = resource_spec
        self.workspace_id = workspace_id
        self.workspace_queue_name = workspace_queue_name
        self.region_id = region_id

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environments is not None:
            result['environments'] = self.environments
        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec.to_map()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        if self.workspace_queue_name is not None:
            result['workspaceQueueName'] = self.workspace_queue_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environments') is not None:
            self.environments = m.get('environments')
        if m.get('resourceSpec') is not None:
            temp_model = EditWorkspaceQueueRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m['resourceSpec'])
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        if m.get('workspaceQueueName') is not None:
            self.workspace_queue_name = m.get('workspaceQueueName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class EditWorkspaceQueueResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID。
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


class EditWorkspaceQueueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EditWorkspaceQueueResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EditWorkspaceQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCuHoursRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        # The end time of the query time range.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The start time of the query time range.
        # 
        # This parameter is required.
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


class GetCuHoursResponseBodyData(TeaModel):
    def __init__(
        self,
        cu_hours: str = None,
    ):
        # The number of CU-hours consumed by a queue during a specified cycle. The value is an estimated value. Refer to your Alibaba Cloud bill for the actual number of consumed CU-hours.
        self.cu_hours = cu_hours

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')
        return self


class GetCuHoursResponseBody(TeaModel):
    def __init__(
        self,
        data: GetCuHoursResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
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
            temp_model = GetCuHoursResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetCuHoursResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCuHoursResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCuHoursResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDoctorApplicationRequest(TeaModel):
    def __init__(
        self,
        locale: str = None,
        query_time: str = None,
        region_id: str = None,
    ):
        # The language of diagnostic information.
        self.locale = locale
        # The query time.
        self.query_time = query_time
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.locale is not None:
            result['locale'] = self.locale
        if self.query_time is not None:
            result['queryTime'] = self.query_time
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')
        if m.get('queryTime') is not None:
            self.query_time = m.get('queryTime')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class GetDoctorApplicationResponseBodyData(TeaModel):
    def __init__(
        self,
        suggestions: List[str] = None,
    ):
        # The diagnostics list.
        self.suggestions = suggestions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.suggestions is not None:
            result['suggestions'] = self.suggestions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('suggestions') is not None:
            self.suggestions = m.get('suggestions')
        return self


class GetDoctorApplicationResponseBody(TeaModel):
    def __init__(
        self,
        data: GetDoctorApplicationResponseBodyData = None,
    ):
        # The data returned.
        self.data = data

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetDoctorApplicationResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetDoctorApplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDoctorApplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDoctorApplicationResponseBody()
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
        display_release_version: str = None,
        end_time: int = None,
        environment_id: str = None,
        execution_timeout_seconds: int = None,
        fusion: bool = None,
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
        # The configurations of the Spark jobs.
        self.configuration_overrides = configuration_overrides
        # The version of the Spark engine.
        self.display_release_version = display_release_version
        # The end time of the job.
        self.end_time = end_time
        # The environment ID.
        self.environment_id = environment_id
        # The timeout period of the job.
        self.execution_timeout_seconds = execution_timeout_seconds
        # Indicates whether the Fusion engine is used for acceleration.
        self.fusion = fusion
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
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.fusion is not None:
            result['fusion'] = self.fusion
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
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
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


class GetLivyComputeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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


class GetLivyComputeResponseBodyDataAutoStopConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        self.enable = enable
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


class GetLivyComputeResponseBodyData(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        auto_stop_configuration: GetLivyComputeResponseBodyDataAutoStopConfiguration = None,
        compute_id: str = None,
        cpu_limit: str = None,
        created_by: str = None,
        display_release_version: str = None,
        enable_public: bool = None,
        endpoint: str = None,
        endpoint_inner: str = None,
        environment_id: str = None,
        fusion: bool = None,
        gmt_create: int = None,
        livy_server_conf: str = None,
        livy_version: str = None,
        memory_limit: str = None,
        name: str = None,
        network_name: str = None,
        queue_name: str = None,
        ram_user_id: str = None,
        release_version: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.auth_type = auth_type
        self.auto_stop_configuration = auto_stop_configuration
        self.compute_id = compute_id
        self.cpu_limit = cpu_limit
        self.created_by = created_by
        self.display_release_version = display_release_version
        self.enable_public = enable_public
        self.endpoint = endpoint
        self.endpoint_inner = endpoint_inner
        self.environment_id = environment_id
        self.fusion = fusion
        self.gmt_create = gmt_create
        self.livy_server_conf = livy_server_conf
        self.livy_version = livy_version
        self.memory_limit = memory_limit
        self.name = name
        self.network_name = network_name
        self.queue_name = queue_name
        self.ram_user_id = ram_user_id
        self.release_version = release_version
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.auto_stop_configuration is not None:
            result['autoStopConfiguration'] = self.auto_stop_configuration.to_map()
        if self.compute_id is not None:
            result['computeId'] = self.compute_id
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.endpoint_inner is not None:
            result['endpointInner'] = self.endpoint_inner
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.fusion is not None:
            result['fusion'] = self.fusion
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.livy_server_conf is not None:
            result['livyServerConf'] = self.livy_server_conf
        if self.livy_version is not None:
            result['livyVersion'] = self.livy_version
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.name is not None:
            result['name'] = self.name
        if self.network_name is not None:
            result['networkName'] = self.network_name
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.ram_user_id is not None:
            result['ramUserId'] = self.ram_user_id
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('autoStopConfiguration') is not None:
            temp_model = GetLivyComputeResponseBodyDataAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m['autoStopConfiguration'])
        if m.get('computeId') is not None:
            self.compute_id = m.get('computeId')
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('endpointInner') is not None:
            self.endpoint_inner = m.get('endpointInner')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('livyServerConf') is not None:
            self.livy_server_conf = m.get('livyServerConf')
        if m.get('livyVersion') is not None:
            self.livy_version = m.get('livyVersion')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkName') is not None:
            self.network_name = m.get('networkName')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('ramUserId') is not None:
            self.ram_user_id = m.get('ramUserId')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetLivyComputeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetLivyComputeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetLivyComputeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetLivyComputeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLivyComputeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLivyComputeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLivyComputeTokenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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


class GetLivyComputeTokenResponseBodyDataAutoExpireConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        expire_days: int = None,
    ):
        self.enable = enable
        self.expire_days = expire_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.expire_days is not None:
            result['expireDays'] = self.expire_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('expireDays') is not None:
            self.expire_days = m.get('expireDays')
        return self


class GetLivyComputeTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        auto_expire_configuration: GetLivyComputeTokenResponseBodyDataAutoExpireConfiguration = None,
        create_time: int = None,
        created_by: str = None,
        expire_time: int = None,
        last_used_time: int = None,
        name: str = None,
        token: str = None,
        token_id: str = None,
    ):
        self.auto_expire_configuration = auto_expire_configuration
        self.create_time = create_time
        self.created_by = created_by
        self.expire_time = expire_time
        self.last_used_time = last_used_time
        self.name = name
        self.token = token
        # Token ID。
        self.token_id = token_id

    def validate(self):
        if self.auto_expire_configuration:
            self.auto_expire_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_expire_configuration is not None:
            result['autoExpireConfiguration'] = self.auto_expire_configuration.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.last_used_time is not None:
            result['lastUsedTime'] = self.last_used_time
        if self.name is not None:
            result['name'] = self.name
        if self.token is not None:
            result['token'] = self.token
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoExpireConfiguration') is not None:
            temp_model = GetLivyComputeTokenResponseBodyDataAutoExpireConfiguration()
            self.auto_expire_configuration = temp_model.from_map(m['autoExpireConfiguration'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('lastUsedTime') is not None:
            self.last_used_time = m.get('lastUsedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        return self


class GetLivyComputeTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetLivyComputeTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetLivyComputeTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetLivyComputeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLivyComputeTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLivyComputeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSessionClusterRequest(TeaModel):
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


class GetSessionClusterResponseBodySessionClusterApplicationConfigs(TeaModel):
    def __init__(
        self,
        config_file_name: str = None,
        config_item_key: str = None,
        config_item_value: str = None,
    ):
        # The name of the configuration file.
        self.config_file_name = config_file_name
        # The key of the configuration.
        self.config_item_key = config_item_key
        # The configuration value.
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


class GetSessionClusterResponseBodySessionClusterAutoStartConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Indicates whether automatic startup is enabled.
        # 
        # *   true
        # *   false
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


class GetSessionClusterResponseBodySessionClusterAutoStopConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        # Indicates whether automatic termination is enabled.
        # 
        # *   true
        # *   false
        self.enable = enable
        # The idle timeout period. The session is automatically terminated when the idle timeout period is exceeded.
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


class GetSessionClusterResponseBodySessionClusterStateChangeReason(TeaModel):
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


class GetSessionClusterResponseBodySessionCluster(TeaModel):
    def __init__(
        self,
        application_configs: List[GetSessionClusterResponseBodySessionClusterApplicationConfigs] = None,
        auto_start_configuration: GetSessionClusterResponseBodySessionClusterAutoStartConfiguration = None,
        auto_stop_configuration: GetSessionClusterResponseBodySessionClusterAutoStopConfiguration = None,
        connection_token: str = None,
        display_release_version: str = None,
        domain: str = None,
        domain_inner: str = None,
        draft_id: str = None,
        env_id: str = None,
        extra: str = None,
        fusion: bool = None,
        gmt_create: int = None,
        kind: str = None,
        name: str = None,
        public_endpoint_enabled: bool = None,
        queue_name: str = None,
        release_version: str = None,
        session_cluster_id: str = None,
        start_time: int = None,
        state: str = None,
        state_change_reason: GetSessionClusterResponseBodySessionClusterStateChangeReason = None,
        user_id: str = None,
        user_name: str = None,
        web_ui: str = None,
        workspace_id: str = None,
    ):
        # The Spark configurations.
        self.application_configs = application_configs
        # Indicates whether automatic startup is enabled.
        self.auto_start_configuration = auto_start_configuration
        # Indicates whether automatic termination is enabled.
        self.auto_stop_configuration = auto_stop_configuration
        self.connection_token = connection_token
        # The version of the Spark engine.
        self.display_release_version = display_release_version
        # The domain name to which the Spark UI of the session belongs.
        self.domain = domain
        # The internal endpoint.
        self.domain_inner = domain_inner
        # The ID of the job that is associated with the session.
        self.draft_id = draft_id
        # The environment ID.
        self.env_id = env_id
        # The additional metadata of the session.
        self.extra = extra
        # Indicates whether the Fusion engine is used for acceleration.
        self.fusion = fusion
        # The creation time.
        self.gmt_create = gmt_create
        # The type of the job. This parameter is required and cannot be modified after the deployment is created. Valid values:
        # 
        # *   SQLSCRIPT
        # *   JAR
        # *   PYTHON
        self.kind = kind
        # The name of the session.
        self.name = name
        self.public_endpoint_enabled = public_endpoint_enabled
        # The queue name.
        self.queue_name = queue_name
        # The version of Serverless Spark.
        self.release_version = release_version
        # The session ID.
        self.session_cluster_id = session_cluster_id
        # The start time.
        self.start_time = start_time
        # The job status.
        # 
        # *   Starting
        # *   Running
        # *   Stopping
        # *   Stopped
        # *   Error
        self.state = state
        # The reason of the job status change.
        self.state_change_reason = state_change_reason
        # The user ID.
        self.user_id = user_id
        # The name of the account that is used to create the session.
        self.user_name = user_name
        # The Spark UI of the session.
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
        if self.connection_token is not None:
            result['connectionToken'] = self.connection_token
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.domain is not None:
            result['domain'] = self.domain
        if self.domain_inner is not None:
            result['domainInner'] = self.domain_inner
        if self.draft_id is not None:
            result['draftId'] = self.draft_id
        if self.env_id is not None:
            result['envId'] = self.env_id
        if self.extra is not None:
            result['extra'] = self.extra
        if self.fusion is not None:
            result['fusion'] = self.fusion
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.public_endpoint_enabled is not None:
            result['publicEndpointEnabled'] = self.public_endpoint_enabled
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
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
                temp_model = GetSessionClusterResponseBodySessionClusterApplicationConfigs()
                self.application_configs.append(temp_model.from_map(k))
        if m.get('autoStartConfiguration') is not None:
            temp_model = GetSessionClusterResponseBodySessionClusterAutoStartConfiguration()
            self.auto_start_configuration = temp_model.from_map(m['autoStartConfiguration'])
        if m.get('autoStopConfiguration') is not None:
            temp_model = GetSessionClusterResponseBodySessionClusterAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m['autoStopConfiguration'])
        if m.get('connectionToken') is not None:
            self.connection_token = m.get('connectionToken')
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('domainInner') is not None:
            self.domain_inner = m.get('domainInner')
        if m.get('draftId') is not None:
            self.draft_id = m.get('draftId')
        if m.get('envId') is not None:
            self.env_id = m.get('envId')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('publicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('publicEndpointEnabled')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('stateChangeReason') is not None:
            temp_model = GetSessionClusterResponseBodySessionClusterStateChangeReason()
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


class GetSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_cluster: GetSessionClusterResponseBodySessionCluster = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The session object.
        self.session_cluster = session_cluster

    def validate(self):
        if self.session_cluster:
            self.session_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_cluster is not None:
            result['sessionCluster'] = self.session_cluster.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionCluster') is not None:
            temp_model = GetSessionClusterResponseBodySessionCluster()
            self.session_cluster = temp_model.from_map(m['sessionCluster'])
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
        rows_file_path: str = None,
        schema: str = None,
    ):
        # The queried data, which is a string in the JSON format.
        self.rows = rows
        self.rows_file_path = rows_file_path
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
        if self.rows_file_path is not None:
            result['rowsFilePath'] = self.rows_file_path
        if self.schema is not None:
            result['schema'] = self.schema
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rows') is not None:
            self.rows = m.get('rows')
        if m.get('rowsFilePath') is not None:
            self.rows_file_path = m.get('rowsFilePath')
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
        # The response parameters.
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


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        template_biz_id: str = None,
        template_type: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        self.template_biz_id = template_biz_id
        # The template type.
        # 
        # Valid values:
        # 
        # *   TASK
        # *   SESSION
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.template_biz_id is not None:
            result['templateBizId'] = self.template_biz_id
        if self.template_type is not None:
            result['templateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('templateBizId') is not None:
            self.template_biz_id = m.get('templateBizId')
        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        data: Template = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # *   If the value of success was false, an error code was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_code = error_code
        # *   If the value of success was false, an error message was returned.
        # *   If the value of success was true, a null value was returned.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = Template()
            self.data = temp_model.from_map(m['data'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantRoleToUsersRequest(TeaModel):
    def __init__(
        self,
        role_arn: str = None,
        user_arns: List[str] = None,
        region_id: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.role_arn = role_arn
        # The user ARNs.
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
        is_workflow: str = None,
        job_run_deployment_id: str = None,
        job_run_id: str = None,
        max_results: int = None,
        min_duration: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_queue_id: str = None,
        start_time: ListJobRunsRequestStartTime = None,
        states: List[str] = None,
        tags: List[ListJobRunsRequestTags] = None,
    ):
        # The ID of the user who created the job.
        self.creator = creator
        # The range of end time.
        self.end_time = end_time
        self.is_workflow = is_workflow
        # The job run ID.
        self.job_run_deployment_id = job_run_deployment_id
        # The job ID.
        self.job_run_id = job_run_id
        # The maximum number of entries to return.
        self.max_results = max_results
        # The minimum running duration of the job. Unit: ms.
        self.min_duration = min_duration
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
        if self.is_workflow is not None:
            result['isWorkflow'] = self.is_workflow
        if self.job_run_deployment_id is not None:
            result['jobRunDeploymentId'] = self.job_run_deployment_id
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.min_duration is not None:
            result['minDuration'] = self.min_duration
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
        if m.get('isWorkflow') is not None:
            self.is_workflow = m.get('isWorkflow')
        if m.get('jobRunDeploymentId') is not None:
            self.job_run_deployment_id = m.get('jobRunDeploymentId')
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('minDuration') is not None:
            self.min_duration = m.get('minDuration')
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
        is_workflow: str = None,
        job_run_deployment_id: str = None,
        job_run_id: str = None,
        max_results: int = None,
        min_duration: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_queue_id: str = None,
        start_time_shrink: str = None,
        states_shrink: str = None,
        tags_shrink: str = None,
    ):
        # The ID of the user who created the job.
        self.creator = creator
        # The range of end time.
        self.end_time_shrink = end_time_shrink
        self.is_workflow = is_workflow
        # The job run ID.
        self.job_run_deployment_id = job_run_deployment_id
        # The job ID.
        self.job_run_id = job_run_id
        # The maximum number of entries to return.
        self.max_results = max_results
        # The minimum running duration of the job. Unit: ms.
        self.min_duration = min_duration
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
        if self.is_workflow is not None:
            result['isWorkflow'] = self.is_workflow
        if self.job_run_deployment_id is not None:
            result['jobRunDeploymentId'] = self.job_run_deployment_id
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.min_duration is not None:
            result['minDuration'] = self.min_duration
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
        if m.get('isWorkflow') is not None:
            self.is_workflow = m.get('isWorkflow')
        if m.get('jobRunDeploymentId') is not None:
            self.job_run_deployment_id = m.get('jobRunDeploymentId')
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('minDuration') is not None:
            self.min_duration = m.get('minDuration')
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
        cu_hours: float = None,
        display_release_version: str = None,
        end_time: int = None,
        execution_timeout_seconds: int = None,
        fusion: bool = None,
        job_driver: JobDriver = None,
        job_run_id: str = None,
        log: RunLog = None,
        mb_seconds: int = None,
        name: str = None,
        release_version: str = None,
        state: str = None,
        state_change_reason: ListJobRunsResponseBodyJobRunsStateChangeReason = None,
        submit_time: int = None,
        tags: List[Tag] = None,
        vcore_seconds: int = None,
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
        # The number of CUs consumed during a specified cycle of a task. The value is an estimated value. Refer to your Alibaba Cloud bill for the actual number of consumed CUs.
        self.cu_hours = cu_hours
        # The version of Spark on which the jobs run.
        self.display_release_version = display_release_version
        # The end time of the job.
        self.end_time = end_time
        # The timeout period of the job.
        self.execution_timeout_seconds = execution_timeout_seconds
        # Indicates whether the Fusion engine is used for acceleration.
        self.fusion = fusion
        # The information about Spark Driver.
        self.job_driver = job_driver
        # The job ID.
        self.job_run_id = job_run_id
        # The path where the operational logs are stored.
        self.log = log
        # The total amount of memory allocated to the job multiplied by the running duration (seconds).
        self.mb_seconds = mb_seconds
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
        # The total number of CPU cores allocated to the job multiplied by the running duration (seconds).
        self.vcore_seconds = vcore_seconds
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
        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.fusion is not None:
            result['fusion'] = self.fusion
        if self.job_driver is not None:
            result['jobDriver'] = self.job_driver.to_map()
        if self.job_run_id is not None:
            result['jobRunId'] = self.job_run_id
        if self.log is not None:
            result['log'] = self.log.to_map()
        if self.mb_seconds is not None:
            result['mbSeconds'] = self.mb_seconds
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
        if self.vcore_seconds is not None:
            result['vcoreSeconds'] = self.vcore_seconds
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
        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        if m.get('jobDriver') is not None:
            temp_model = JobDriver()
            self.job_driver = temp_model.from_map(m['jobDriver'])
        if m.get('jobRunId') is not None:
            self.job_run_id = m.get('jobRunId')
        if m.get('log') is not None:
            temp_model = RunLog()
            self.log = temp_model.from_map(m['log'])
        if m.get('mbSeconds') is not None:
            self.mb_seconds = m.get('mbSeconds')
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
        if m.get('vcoreSeconds') is not None:
            self.vcore_seconds = m.get('vcoreSeconds')
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
        # The Spark jobs.
        self.job_runs = job_runs
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token.
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


class ListKyuubiServicesResponseBodyDataKyuubiServices(TeaModel):
    def __init__(
        self,
        compute_instance: str = None,
        create_time: str = None,
        creator: str = None,
        inner_endpoint: str = None,
        kyuubi_configs: str = None,
        kyuubi_service_id: str = None,
        name: str = None,
        public_endpoint: str = None,
        queue: str = None,
        release_version: str = None,
        replica: int = None,
        spark_configs: str = None,
        start_time: str = None,
        state: str = None,
    ):
        self.compute_instance = compute_instance
        self.create_time = create_time
        self.creator = creator
        self.inner_endpoint = inner_endpoint
        self.kyuubi_configs = kyuubi_configs
        # KyuubiServer ID。
        self.kyuubi_service_id = kyuubi_service_id
        self.name = name
        self.public_endpoint = public_endpoint
        self.queue = queue
        self.release_version = release_version
        self.replica = replica
        self.spark_configs = spark_configs
        self.start_time = start_time
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_instance is not None:
            result['computeInstance'] = self.compute_instance
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.inner_endpoint is not None:
            result['innerEndpoint'] = self.inner_endpoint
        if self.kyuubi_configs is not None:
            result['kyuubiConfigs'] = self.kyuubi_configs
        if self.kyuubi_service_id is not None:
            result['kyuubiServiceId'] = self.kyuubi_service_id
        if self.name is not None:
            result['name'] = self.name
        if self.public_endpoint is not None:
            result['publicEndpoint'] = self.public_endpoint
        if self.queue is not None:
            result['queue'] = self.queue
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.replica is not None:
            result['replica'] = self.replica
        if self.spark_configs is not None:
            result['sparkConfigs'] = self.spark_configs
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeInstance') is not None:
            self.compute_instance = m.get('computeInstance')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('innerEndpoint') is not None:
            self.inner_endpoint = m.get('innerEndpoint')
        if m.get('kyuubiConfigs') is not None:
            self.kyuubi_configs = m.get('kyuubiConfigs')
        if m.get('kyuubiServiceId') is not None:
            self.kyuubi_service_id = m.get('kyuubiServiceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('publicEndpoint') is not None:
            self.public_endpoint = m.get('publicEndpoint')
        if m.get('queue') is not None:
            self.queue = m.get('queue')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('replica') is not None:
            self.replica = m.get('replica')
        if m.get('sparkConfigs') is not None:
            self.spark_configs = m.get('sparkConfigs')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class ListKyuubiServicesResponseBodyData(TeaModel):
    def __init__(
        self,
        kyuubi_services: List[ListKyuubiServicesResponseBodyDataKyuubiServices] = None,
    ):
        self.kyuubi_services = kyuubi_services

    def validate(self):
        if self.kyuubi_services:
            for k in self.kyuubi_services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['kyuubiServices'] = []
        if self.kyuubi_services is not None:
            for k in self.kyuubi_services:
                result['kyuubiServices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.kyuubi_services = []
        if m.get('kyuubiServices') is not None:
            for k in m.get('kyuubiServices'):
                temp_model = ListKyuubiServicesResponseBodyDataKyuubiServices()
                self.kyuubi_services.append(temp_model.from_map(k))
        return self


class ListKyuubiServicesResponseBody(TeaModel):
    def __init__(
        self,
        data: ListKyuubiServicesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = ListKyuubiServicesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListKyuubiServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKyuubiServicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListKyuubiServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKyuubiSparkApplicationsRequestStartTime(TeaModel):
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


class ListKyuubiSparkApplicationsRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        max_results: int = None,
        min_duration: int = None,
        next_token: str = None,
        order_by: List[str] = None,
        resource_queue_id: str = None,
        sort: str = None,
        start_time: ListKyuubiSparkApplicationsRequestStartTime = None,
    ):
        # The ID of the application that is submitted by using a Kyuubi gateway.
        self.application_id = application_id
        # The name of the Spark application that is submitted by using a Kyuubi gateway.
        self.application_name = application_name
        # The maximum number of entries to return.
        self.max_results = max_results
        self.min_duration = min_duration
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        self.order_by = order_by
        self.resource_queue_id = resource_queue_id
        self.sort = sort
        # The range of start time.
        self.start_time = start_time

    def validate(self):
        if self.start_time:
            self.start_time.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['applicationId'] = self.application_id
        if self.application_name is not None:
            result['applicationName'] = self.application_name
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.min_duration is not None:
            result['minDuration'] = self.min_duration
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.order_by is not None:
            result['orderBy'] = self.order_by
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.sort is not None:
            result['sort'] = self.sort
        if self.start_time is not None:
            result['startTime'] = self.start_time.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationId') is not None:
            self.application_id = m.get('applicationId')
        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('minDuration') is not None:
            self.min_duration = m.get('minDuration')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('startTime') is not None:
            temp_model = ListKyuubiSparkApplicationsRequestStartTime()
            self.start_time = temp_model.from_map(m['startTime'])
        return self


class ListKyuubiSparkApplicationsShrinkRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        max_results: int = None,
        min_duration: int = None,
        next_token: str = None,
        order_by_shrink: str = None,
        resource_queue_id: str = None,
        sort: str = None,
        start_time_shrink: str = None,
    ):
        # The ID of the application that is submitted by using a Kyuubi gateway.
        self.application_id = application_id
        # The name of the Spark application that is submitted by using a Kyuubi gateway.
        self.application_name = application_name
        # The maximum number of entries to return.
        self.max_results = max_results
        self.min_duration = min_duration
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        self.order_by_shrink = order_by_shrink
        self.resource_queue_id = resource_queue_id
        self.sort = sort
        # The range of start time.
        self.start_time_shrink = start_time_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['applicationId'] = self.application_id
        if self.application_name is not None:
            result['applicationName'] = self.application_name
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.min_duration is not None:
            result['minDuration'] = self.min_duration
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.order_by_shrink is not None:
            result['orderBy'] = self.order_by_shrink
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.sort is not None:
            result['sort'] = self.sort
        if self.start_time_shrink is not None:
            result['startTime'] = self.start_time_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationId') is not None:
            self.application_id = m.get('applicationId')
        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('minDuration') is not None:
            self.min_duration = m.get('minDuration')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('orderBy') is not None:
            self.order_by_shrink = m.get('orderBy')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('startTime') is not None:
            self.start_time_shrink = m.get('startTime')
        return self


class ListKyuubiSparkApplicationsResponseBodyApplications(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        cu_hours: float = None,
        end_time: str = None,
        mb_seconds: int = None,
        resource_queue_id: str = None,
        start_time: str = None,
        state: str = None,
        vcore_seconds: int = None,
        web_ui: str = None,
    ):
        # The ID of the application that is submitted by using a Kyuubi gateway.
        self.application_id = application_id
        # The name of the Spark application that is submitted by using a Kyuubi gateway.
        self.application_name = application_name
        # The number of CUs consumed during a specified cycle of a task. The value is an estimated value. Refer to your Alibaba Cloud bill for the actual number of consumed CUs.
        self.cu_hours = cu_hours
        # The time when the task ended.
        self.end_time = end_time
        # The total amount of memory allocated to the job multiplied by the running duration (seconds).
        self.mb_seconds = mb_seconds
        # The name of the resource queue on which the Spark jobs run.
        self.resource_queue_id = resource_queue_id
        # The time when the task started.
        self.start_time = start_time
        # The status of the Spark application.
        # 
        # *   STARTING
        # *   RUNNING
        # *   TERMINATED
        self.state = state
        # The total number of CPU cores allocated to the job multiplied by the running duration (seconds).
        self.vcore_seconds = vcore_seconds
        # The URL of the web UI for the Spark application.
        self.web_ui = web_ui

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_id is not None:
            result['applicationId'] = self.application_id
        if self.application_name is not None:
            result['applicationName'] = self.application_name
        if self.cu_hours is not None:
            result['cuHours'] = self.cu_hours
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.mb_seconds is not None:
            result['mbSeconds'] = self.mb_seconds
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.state is not None:
            result['state'] = self.state
        if self.vcore_seconds is not None:
            result['vcoreSeconds'] = self.vcore_seconds
        if self.web_ui is not None:
            result['webUI'] = self.web_ui
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicationId') is not None:
            self.application_id = m.get('applicationId')
        if m.get('applicationName') is not None:
            self.application_name = m.get('applicationName')
        if m.get('cuHours') is not None:
            self.cu_hours = m.get('cuHours')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('mbSeconds') is not None:
            self.mb_seconds = m.get('mbSeconds')
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('vcoreSeconds') is not None:
            self.vcore_seconds = m.get('vcoreSeconds')
        if m.get('webUI') is not None:
            self.web_ui = m.get('webUI')
        return self


class ListKyuubiSparkApplicationsResponseBody(TeaModel):
    def __init__(
        self,
        applications: List[ListKyuubiSparkApplicationsResponseBodyApplications] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details of the applications.
        self.applications = applications
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['applications'].append(k.to_map() if k else None)
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
        self.applications = []
        if m.get('applications') is not None:
            for k in m.get('applications'):
                temp_model = ListKyuubiSparkApplicationsResponseBodyApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListKyuubiSparkApplicationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKyuubiSparkApplicationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListKyuubiSparkApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListKyuubiTokenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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


class ListKyuubiTokenResponseBodyDataTokens(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        created_by: str = None,
        expire_time: int = None,
        last_used_time: int = None,
        name: str = None,
        token: str = None,
        token_id: str = None,
    ):
        self.create_time = create_time
        self.created_by = created_by
        self.expire_time = expire_time
        self.last_used_time = last_used_time
        self.name = name
        self.token = token
        # Token ID。
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.last_used_time is not None:
            result['lastUsedTime'] = self.last_used_time
        if self.name is not None:
            result['name'] = self.name
        if self.token is not None:
            result['token'] = self.token
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('lastUsedTime') is not None:
            self.last_used_time = m.get('lastUsedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        return self


class ListKyuubiTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        tokens: List[ListKyuubiTokenResponseBodyDataTokens] = None,
    ):
        self.tokens = tokens

    def validate(self):
        if self.tokens:
            for k in self.tokens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tokens'] = []
        if self.tokens is not None:
            for k in self.tokens:
                result['tokens'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tokens = []
        if m.get('tokens') is not None:
            for k in m.get('tokens'):
                temp_model = ListKyuubiTokenResponseBodyDataTokens()
                self.tokens.append(temp_model.from_map(k))
        return self


class ListKyuubiTokenResponseBody(TeaModel):
    def __init__(
        self,
        data: ListKyuubiTokenResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
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
            temp_model = ListKyuubiTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListKyuubiTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListKyuubiTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListKyuubiTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLivyComputeRequest(TeaModel):
    def __init__(
        self,
        environment_id: str = None,
        region_id: str = None,
    ):
        self.environment_id = environment_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListLivyComputeResponseBodyDataLivyComputes(TeaModel):
    def __init__(
        self,
        compute_id: str = None,
        created_by: str = None,
        endpoint: str = None,
        endpoint_inner: str = None,
        gmt_create: int = None,
        name: str = None,
        queue_name: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.compute_id = compute_id
        self.created_by = created_by
        self.endpoint = endpoint
        self.endpoint_inner = endpoint_inner
        self.gmt_create = gmt_create
        self.name = name
        self.queue_name = queue_name
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.compute_id is not None:
            result['computeId'] = self.compute_id
        if self.created_by is not None:
            result['createdBy'] = self.created_by
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.endpoint_inner is not None:
            result['endpointInner'] = self.endpoint_inner
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.name is not None:
            result['name'] = self.name
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('computeId') is not None:
            self.compute_id = m.get('computeId')
        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('endpointInner') is not None:
            self.endpoint_inner = m.get('endpointInner')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListLivyComputeResponseBodyData(TeaModel):
    def __init__(
        self,
        livy_computes: List[ListLivyComputeResponseBodyDataLivyComputes] = None,
    ):
        self.livy_computes = livy_computes

    def validate(self):
        if self.livy_computes:
            for k in self.livy_computes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['livyComputes'] = []
        if self.livy_computes is not None:
            for k in self.livy_computes:
                result['livyComputes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.livy_computes = []
        if m.get('livyComputes') is not None:
            for k in m.get('livyComputes'):
                temp_model = ListLivyComputeResponseBodyDataLivyComputes()
                self.livy_computes.append(temp_model.from_map(k))
        return self


class ListLivyComputeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListLivyComputeResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListLivyComputeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListLivyComputeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLivyComputeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLivyComputeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLivyComputeTokenRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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


class ListLivyComputeTokenResponseBodyDataTokens(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        createdby: str = None,
        expire_time: int = None,
        last_used_time: int = None,
        name: str = None,
        token: str = None,
        token_id: str = None,
    ):
        self.create_time = create_time
        self.createdby = createdby
        self.expire_time = expire_time
        self.last_used_time = last_used_time
        self.name = name
        self.token = token
        # Token ID。
        self.token_id = token_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.createdby is not None:
            result['createdby'] = self.createdby
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.last_used_time is not None:
            result['lastUsedTime'] = self.last_used_time
        if self.name is not None:
            result['name'] = self.name
        if self.token is not None:
            result['token'] = self.token
        if self.token_id is not None:
            result['tokenId'] = self.token_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createdby') is not None:
            self.createdby = m.get('createdby')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('lastUsedTime') is not None:
            self.last_used_time = m.get('lastUsedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('tokenId') is not None:
            self.token_id = m.get('tokenId')
        return self


class ListLivyComputeTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        tokens: List[ListLivyComputeTokenResponseBodyDataTokens] = None,
    ):
        self.tokens = tokens

    def validate(self):
        if self.tokens:
            for k in self.tokens:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tokens'] = []
        if self.tokens is not None:
            for k in self.tokens:
                result['tokens'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tokens = []
        if m.get('tokens') is not None:
            for k in m.get('tokens'):
                temp_model = ListLivyComputeTokenResponseBodyDataTokens()
                self.tokens.append(temp_model.from_map(k))
        return self


class ListLivyComputeTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListLivyComputeTokenResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListLivyComputeTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListLivyComputeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLivyComputeTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLivyComputeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogContentsRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        length: int = None,
        offset: int = None,
        region_id: str = None,
    ):
        # Full path of the file.
        self.file_name = file_name
        # Length of the log.
        self.length = length
        # Start line for query.
        self.offset = offset
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.length is not None:
            result['length'] = self.length
        if self.offset is not None:
            result['offset'] = self.offset
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('length') is not None:
            self.length = m.get('length')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListLogContentsResponseBodyListLogContentContents(TeaModel):
    def __init__(
        self,
        line_content: str = None,
    ):
        # Log line content.
        self.line_content = line_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line_content is not None:
            result['LineContent'] = self.line_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineContent') is not None:
            self.line_content = m.get('LineContent')
        return self


class ListLogContentsResponseBodyListLogContent(TeaModel):
    def __init__(
        self,
        contents: List[ListLogContentsResponseBodyListLogContentContents] = None,
        total_length: int = None,
    ):
        # List of log line contents.
        self.contents = contents
        # Total number of log lines.
        self.total_length = total_length

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['contents'].append(k.to_map() if k else None)
        if self.total_length is not None:
            result['totalLength'] = self.total_length
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('contents') is not None:
            for k in m.get('contents'):
                temp_model = ListLogContentsResponseBodyListLogContentContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('totalLength') is not None:
            self.total_length = m.get('totalLength')
        return self


class ListLogContentsResponseBody(TeaModel):
    def __init__(
        self,
        list_log_content: ListLogContentsResponseBodyListLogContent = None,
        request_id: str = None,
    ):
        # Log content.
        self.list_log_content = list_log_content
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.list_log_content:
            self.list_log_content.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.list_log_content is not None:
            result['listLogContent'] = self.list_log_content.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('listLogContent') is not None:
            temp_model = ListLogContentsResponseBodyListLogContent()
            self.list_log_content = temp_model.from_map(m['listLogContent'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListLogContentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLogContentsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLogContentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReleaseVersionsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        release_type: str = None,
        release_version: str = None,
        release_version_status: str = None,
        service_filter: str = None,
        workspace_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The type of the version.
        # 
        # Valid values:
        # 
        # *   stable
        # *   Beta
        self.release_type = release_type
        # The version of EMR Serverless Spark.
        self.release_version = release_version
        # The status of the version.
        # 
        # Valid values:
        # 
        # *   ONLINE
        # *   OFFLINE
        self.release_version_status = release_version_status
        self.service_filter = service_filter
        # The workspace ID.
        self.workspace_id = workspace_id

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
        if self.service_filter is not None:
            result['serviceFilter'] = self.service_filter
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
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
        if m.get('serviceFilter') is not None:
            self.service_filter = m.get('serviceFilter')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListReleaseVersionsResponseBodyReleaseVersions(TeaModel):
    def __init__(
        self,
        community_version: str = None,
        cpu_architectures: List[str] = None,
        display_release_version: str = None,
        fusion: bool = None,
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
        # The version number.
        self.display_release_version = display_release_version
        # Indicates whether the Fusion engine is used for acceleration.
        self.fusion = fusion
        # The creation time.
        self.gmt_create = gmt_create
        # The type of the Infrastructure as a Service (IaaS) layer.
        self.iaas_type = iaas_type
        # The version number.
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
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.fusion is not None:
            result['fusion'] = self.fusion
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
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
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
        # The session type.
        # 
        # Valid values:
        # 
        # *   NOTEBOOK
        # *   THRIFT
        # *   SQL
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
        # The key of the configuration.
        self.config_item_key = config_item_key
        # The configuration value.
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
        # The idle timeout period. The session is automatically terminated when the idle timeout period is exceeded.
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
        display_release_version: str = None,
        domain: str = None,
        domain_inner: str = None,
        draft_id: str = None,
        extra: str = None,
        fusion: bool = None,
        gmt_create: int = None,
        kind: str = None,
        name: str = None,
        public_endpoint_enabled: bool = None,
        queue_name: str = None,
        release_version: str = None,
        session_cluster_id: str = None,
        start_time: int = None,
        state: str = None,
        state_change_reason: ListSessionClustersResponseBodySessionClustersStateChangeReason = None,
        user_id: str = None,
        user_name: str = None,
        web_ui: str = None,
        workspace_id: str = None,
    ):
        # The session configurations, which are equivalent to the configurations of the Spark job.
        self.application_configs = application_configs
        # The automatic startup configurations.
        self.auto_start_configuration = auto_start_configuration
        # The configurations of automatic termination.
        self.auto_stop_configuration = auto_stop_configuration
        # The version of the Spark engine.
        self.display_release_version = display_release_version
        # The public endpoint of the Thrift server.
        self.domain = domain
        # The internal endpoint of the Thrift server.
        self.domain_inner = domain_inner
        # The ID of the job that is associated with the session.
        self.draft_id = draft_id
        # The additional metadata of the session.
        self.extra = extra
        # Indicates whether the Fusion engine is used for acceleration.
        self.fusion = fusion
        # The creation time.
        self.gmt_create = gmt_create
        # The session type.
        # 
        # Valid values:
        # 
        # *   NOTEBOOK
        # *   THRIFT
        # *   SQL
        self.kind = kind
        # The name of the session.
        self.name = name
        self.public_endpoint_enabled = public_endpoint_enabled
        # The name of the queue that is used to run the session.
        self.queue_name = queue_name
        # The version of EMR Serverless Spark.
        self.release_version = release_version
        # The session ID.
        self.session_cluster_id = session_cluster_id
        # The start time.
        self.start_time = start_time
        # The status of the session.
        # 
        # *   Starting
        # *   Running
        # *   Stopping
        # *   Stopped
        # *   Error
        self.state = state
        # The details of the most recent status change of the session.
        self.state_change_reason = state_change_reason
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name
        # The Spark UI of the session.
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
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.domain is not None:
            result['domain'] = self.domain
        if self.domain_inner is not None:
            result['domainInner'] = self.domain_inner
        if self.draft_id is not None:
            result['draftId'] = self.draft_id
        if self.extra is not None:
            result['extra'] = self.extra
        if self.fusion is not None:
            result['fusion'] = self.fusion
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.public_endpoint_enabled is not None:
            result['publicEndpointEnabled'] = self.public_endpoint_enabled
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
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
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('domainInner') is not None:
            self.domain_inner = m.get('domainInner')
        if m.get('draftId') is not None:
            self.draft_id = m.get('draftId')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('publicEndpointEnabled') is not None:
            self.public_endpoint_enabled = m.get('publicEndpointEnabled')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
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
        # A pagination token.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The sessions.
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
        create_time: int = None,
        creator: str = None,
        environments: List[str] = None,
        max_resource: str = None,
        min_resource: str = None,
        payment_type: str = None,
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
        # The time when the workspace was created.
        self.create_time = create_time
        # The ID of the user who created the queue.
        self.creator = creator
        # The environment types of the queue.
        self.environments = environments
        # The maximum capacity of resources that can be used in the queue.
        self.max_resource = max_resource
        # The minimum capacity of resources that can be used in the queue.
        self.min_resource = min_resource
        # The billing method. Valid values:
        # 
        # *   PayAsYouGo
        # *   Pre
        self.payment_type = payment_type
        # The queue label.
        self.properties = properties
        # The name of the queue.
        self.queue_name = queue_name
        # The queue architecture.
        self.queue_scope = queue_scope
        # The status of the queue.
        self.queue_status = queue_status
        # The type of the queue. Valid values:
        # 
        # *   instance
        # *   instanceChildren
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
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.creator is not None:
            result['creator'] = self.creator
        if self.environments is not None:
            result['environments'] = self.environments
        if self.max_resource is not None:
            result['maxResource'] = self.max_resource
        if self.min_resource is not None:
            result['minResource'] = self.min_resource
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
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
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('environments') is not None:
            self.environments = m.get('environments')
        if m.get('maxResource') is not None:
            self.max_resource = m.get('maxResource')
        if m.get('minResource') is not None:
            self.min_resource = m.get('minResource')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
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


class ListWorkspacesRequestTag(TeaModel):
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


class ListWorkspacesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        state: str = None,
        tag: List[ListWorkspacesRequestTag] = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # The name of the workspace. Fuzzy match is supported.
        self.name = name
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The state of the workspace.
        self.state = state
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

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
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
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
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListWorkspacesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListWorkspacesShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        region_id: str = None,
        state: str = None,
        tag_shrink: str = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # The name of the workspace. Fuzzy match is supported.
        self.name = name
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The state of the workspace.
        self.state = state
        self.tag_shrink = tag_shrink

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
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
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
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListWorkspacesResponseBodyWorkspacesPrePaidQuota(TeaModel):
    def __init__(
        self,
        allocated_resource: str = None,
        auto_renewal: bool = None,
        create_time: int = None,
        expire_time: int = None,
        instance_id: str = None,
        max_resource: str = None,
        order_id: str = None,
        payment_status: str = None,
        used_resource: str = None,
    ):
        # The amount of resources that are allocated by a subscription quota.
        self.allocated_resource = allocated_resource
        # Indicates whether auto-renewal is enabled for the subscription quota.
        # 
        # *   true
        # *   false
        self.auto_renewal = auto_renewal
        # The creation time of the subscription quota.
        self.create_time = create_time
        # The expiration time of the subscription quota.
        self.expire_time = expire_time
        # The ID of the instance that is generated when you purchase the subscription quota.
        self.instance_id = instance_id
        # The maximum amount of resources that can be used in a subscription quota.
        self.max_resource = max_resource
        self.order_id = order_id
        # The status of the subscription quota. Valid values:
        # 
        # *   NORMAL
        # *   WAIT_FOR_EXPIRE
        # *   EXPIRED
        self.payment_status = payment_status
        # The amount of resources that are used.
        self.used_resource = used_resource

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocated_resource is not None:
            result['allocatedResource'] = self.allocated_resource
        if self.auto_renewal is not None:
            result['autoRenewal'] = self.auto_renewal
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.max_resource is not None:
            result['maxResource'] = self.max_resource
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.payment_status is not None:
            result['paymentStatus'] = self.payment_status
        if self.used_resource is not None:
            result['usedResource'] = self.used_resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allocatedResource') is not None:
            self.allocated_resource = m.get('allocatedResource')
        if m.get('autoRenewal') is not None:
            self.auto_renewal = m.get('autoRenewal')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('maxResource') is not None:
            self.max_resource = m.get('maxResource')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('paymentStatus') is not None:
            self.payment_status = m.get('paymentStatus')
        if m.get('usedResource') is not None:
            self.used_resource = m.get('usedResource')
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


class ListWorkspacesResponseBodyWorkspacesTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        auto_renew_period_unit: str = None,
        create_time: int = None,
        dlf_catalog_id: str = None,
        dlf_type: str = None,
        duration: int = None,
        end_time: int = None,
        fail_reason: str = None,
        payment_duration_unit: str = None,
        payment_status: str = None,
        payment_type: str = None,
        pre_paid_quota: ListWorkspacesResponseBodyWorkspacesPrePaidQuota = None,
        region_id: str = None,
        release_type: str = None,
        resource_spec: str = None,
        state_change_reason: ListWorkspacesResponseBodyWorkspacesStateChangeReason = None,
        storage: str = None,
        tags: List[ListWorkspacesResponseBodyWorkspacesTags] = None,
        workspace_id: str = None,
        workspace_name: str = None,
        workspace_status: str = None,
    ):
        # Specifies whether to enable auto-renewal. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew = auto_renew
        # The auto-renewal duration. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew_period = auto_renew_period
        # The unit of the auto-renewal duration. This parameter is required only if the paymentType parameter is set to Pre.
        self.auto_renew_period_unit = auto_renew_period_unit
        # The time when the workflow was created.
        self.create_time = create_time
        # The information of the Data Lake Formation (DLF) catalog.
        self.dlf_catalog_id = dlf_catalog_id
        # The version of DLF.
        self.dlf_type = dlf_type
        # The subscription period. This parameter is required only if the paymentType parameter is set to Pre.
        self.duration = duration
        # The end of the end time range.
        self.end_time = end_time
        # The failure reason.
        self.fail_reason = fail_reason
        # The unit of the subscription duration.
        self.payment_duration_unit = payment_duration_unit
        # The status of the payment.
        self.payment_status = payment_status
        # The billing method. Valid values:
        # 
        # - PayAsYouGo
        # - Pre
        self.payment_type = payment_type
        # The information about the subscription quota.
        self.pre_paid_quota = pre_paid_quota
        # The region ID.
        self.region_id = region_id
        # The reason why the workspace is released.
        self.release_type = release_type
        # The resource specifications.
        self.resource_spec = resource_spec
        # The reason of the job status change.
        self.state_change_reason = state_change_reason
        # The OSS path.
        self.storage = storage
        self.tags = tags
        # The workspace ID.
        self.workspace_id = workspace_id
        # The name of the workspace.
        self.workspace_name = workspace_name
        # The workspace status.
        self.workspace_status = workspace_status

    def validate(self):
        if self.pre_paid_quota:
            self.pre_paid_quota.validate()
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
        if self.dlf_type is not None:
            result['dlfType'] = self.dlf_type
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
        if self.pre_paid_quota is not None:
            result['prePaidQuota'] = self.pre_paid_quota.to_map()
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
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
        if m.get('dlfType') is not None:
            self.dlf_type = m.get('dlfType')
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
        if m.get('prePaidQuota') is not None:
            temp_model = ListWorkspacesResponseBodyWorkspacesPrePaidQuota()
            self.pre_paid_quota = temp_model.from_map(m['prePaidQuota'])
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
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListWorkspacesResponseBodyWorkspacesTags()
                self.tags.append(temp_model.from_map(k))
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
        # The queried workspaces.
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


class RefreshLivyComputeTokenRequestAutoExpireConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        expire_days: int = None,
    ):
        self.enable = enable
        self.expire_days = expire_days

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['enable'] = self.enable
        if self.expire_days is not None:
            result['expireDays'] = self.expire_days
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('expireDays') is not None:
            self.expire_days = m.get('expireDays')
        return self


class RefreshLivyComputeTokenRequest(TeaModel):
    def __init__(
        self,
        auto_expire_configuration: RefreshLivyComputeTokenRequestAutoExpireConfiguration = None,
        name: str = None,
        token: str = None,
        region_id: str = None,
    ):
        self.auto_expire_configuration = auto_expire_configuration
        self.name = name
        self.token = token
        self.region_id = region_id

    def validate(self):
        if self.auto_expire_configuration:
            self.auto_expire_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_expire_configuration is not None:
            result['autoExpireConfiguration'] = self.auto_expire_configuration.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.token is not None:
            result['token'] = self.token
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoExpireConfiguration') is not None:
            temp_model = RefreshLivyComputeTokenRequestAutoExpireConfiguration()
            self.auto_expire_configuration = temp_model.from_map(m['autoExpireConfiguration'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class RefreshLivyComputeTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class RefreshLivyComputeTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshLivyComputeTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RefreshLivyComputeTokenResponseBody()
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
        display_release_version: str = None,
        execution_timeout_seconds: int = None,
        fusion: bool = None,
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
        # The version of the Spark engine.
        self.display_release_version = display_release_version
        # The timeout period of the job.
        self.execution_timeout_seconds = execution_timeout_seconds
        # Specifies whether to enable Fusion engine for acceleration.
        self.fusion = fusion
        # The information about Spark Driver.
        self.job_driver = job_driver
        # The job ID.
        self.job_id = job_id
        # The name of the job.
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
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.execution_timeout_seconds is not None:
            result['executionTimeoutSeconds'] = self.execution_timeout_seconds
        if self.fusion is not None:
            result['fusion'] = self.fusion
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
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('executionTimeoutSeconds') is not None:
            self.execution_timeout_seconds = m.get('executionTimeoutSeconds')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
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


class StartLivyComputeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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


class StartLivyComputeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StartLivyComputeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartLivyComputeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartLivyComputeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartProcessInstanceRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        comments: str = None,
        email: str = None,
        interval: str = None,
        is_prod: bool = None,
        process_definition_code: int = None,
        product_namespace: str = None,
        region_id: str = None,
        runtime_queue: str = None,
        version_hash_code: str = None,
        version_number: int = None,
    ):
        self.action = action
        self.comments = comments
        self.email = email
        self.interval = interval
        # Specifies whether to run the workflow in the production environment.
        self.is_prod = is_prod
        # The workflow ID.
        # 
        # This parameter is required.
        self.process_definition_code = process_definition_code
        # The code of the service.
        # 
        # This parameter is required.
        self.product_namespace = product_namespace
        # The region ID.
        self.region_id = region_id
        # The queue on which the workflow runs.
        self.runtime_queue = runtime_queue
        # The hash code of the version.
        self.version_hash_code = version_hash_code
        # The version number of the workflow.
        self.version_number = version_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.comments is not None:
            result['comments'] = self.comments
        if self.email is not None:
            result['email'] = self.email
        if self.interval is not None:
            result['interval'] = self.interval
        if self.is_prod is not None:
            result['isProd'] = self.is_prod
        if self.process_definition_code is not None:
            result['processDefinitionCode'] = self.process_definition_code
        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.runtime_queue is not None:
            result['runtimeQueue'] = self.runtime_queue
        if self.version_hash_code is not None:
            result['versionHashCode'] = self.version_hash_code
        if self.version_number is not None:
            result['versionNumber'] = self.version_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('comments') is not None:
            self.comments = m.get('comments')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('interval') is not None:
            self.interval = m.get('interval')
        if m.get('isProd') is not None:
            self.is_prod = m.get('isProd')
        if m.get('processDefinitionCode') is not None:
            self.process_definition_code = m.get('processDefinitionCode')
        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('runtimeQueue') is not None:
            self.runtime_queue = m.get('runtimeQueue')
        if m.get('versionHashCode') is not None:
            self.version_hash_code = m.get('versionHashCode')
        if m.get('versionNumber') is not None:
            self.version_number = m.get('versionNumber')
        return self


class StartProcessInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        failed: bool = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The code that is returned by the backend server.
        self.code = code
        # The data returned.
        self.data = data
        # Indicates whether the workflow fails to be run manually.
        self.failed = failed
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The description of the returned code.
        self.msg = msg
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
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.failed is not None:
            result['failed'] = self.failed
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class StartProcessInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartProcessInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartProcessInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartSessionClusterRequest(TeaModel):
    def __init__(
        self,
        queue_name: str = None,
        session_cluster_id: str = None,
        region_id: str = None,
    ):
        # The queue name.
        self.queue_name = queue_name
        # The session ID.
        self.session_cluster_id = session_cluster_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class StartSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_cluster_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The workspace ID.
        self.session_cluster_id = session_cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
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


class StopLivyComputeRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
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


class StopLivyComputeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StopLivyComputeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopLivyComputeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopLivyComputeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSessionClusterRequest(TeaModel):
    def __init__(
        self,
        queue_name: str = None,
        session_cluster_id: str = None,
        region_id: str = None,
    ):
        # The queue name.
        self.queue_name = queue_name
        # The session ID.
        self.session_cluster_id = session_cluster_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class StopSessionClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_cluster_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The session ID.
        self.session_cluster_id = session_cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_cluster_id is not None:
            result['sessionClusterId'] = self.session_cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('sessionClusterId') is not None:
            self.session_cluster_id = m.get('sessionClusterId')
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


class UpdateLivyComputeRequestAutoStartConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
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


class UpdateLivyComputeRequestAutoStopConfiguration(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        idle_timeout_minutes: int = None,
    ):
        self.enable = enable
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


class UpdateLivyComputeRequest(TeaModel):
    def __init__(
        self,
        auth_type: str = None,
        auto_start_configuration: UpdateLivyComputeRequestAutoStartConfiguration = None,
        auto_stop_configuration: UpdateLivyComputeRequestAutoStopConfiguration = None,
        cpu_limit: str = None,
        display_release_version: str = None,
        enable_public: bool = None,
        environment_id: str = None,
        fusion: bool = None,
        livy_server_conf: str = None,
        livy_version: str = None,
        memory_limit: str = None,
        name: str = None,
        network_name: str = None,
        queue_name: str = None,
        release_version: str = None,
        region_id: str = None,
    ):
        self.auth_type = auth_type
        self.auto_start_configuration = auto_start_configuration
        self.auto_stop_configuration = auto_stop_configuration
        self.cpu_limit = cpu_limit
        self.display_release_version = display_release_version
        self.enable_public = enable_public
        self.environment_id = environment_id
        self.fusion = fusion
        self.livy_server_conf = livy_server_conf
        self.livy_version = livy_version
        self.memory_limit = memory_limit
        self.name = name
        self.network_name = network_name
        self.queue_name = queue_name
        self.release_version = release_version
        self.region_id = region_id

    def validate(self):
        if self.auto_start_configuration:
            self.auto_start_configuration.validate()
        if self.auto_stop_configuration:
            self.auto_stop_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_type is not None:
            result['authType'] = self.auth_type
        if self.auto_start_configuration is not None:
            result['autoStartConfiguration'] = self.auto_start_configuration.to_map()
        if self.auto_stop_configuration is not None:
            result['autoStopConfiguration'] = self.auto_stop_configuration.to_map()
        if self.cpu_limit is not None:
            result['cpuLimit'] = self.cpu_limit
        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version
        if self.enable_public is not None:
            result['enablePublic'] = self.enable_public
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.fusion is not None:
            result['fusion'] = self.fusion
        if self.livy_server_conf is not None:
            result['livyServerConf'] = self.livy_server_conf
        if self.livy_version is not None:
            result['livyVersion'] = self.livy_version
        if self.memory_limit is not None:
            result['memoryLimit'] = self.memory_limit
        if self.name is not None:
            result['name'] = self.name
        if self.network_name is not None:
            result['networkName'] = self.network_name
        if self.queue_name is not None:
            result['queueName'] = self.queue_name
        if self.release_version is not None:
            result['releaseVersion'] = self.release_version
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authType') is not None:
            self.auth_type = m.get('authType')
        if m.get('autoStartConfiguration') is not None:
            temp_model = UpdateLivyComputeRequestAutoStartConfiguration()
            self.auto_start_configuration = temp_model.from_map(m['autoStartConfiguration'])
        if m.get('autoStopConfiguration') is not None:
            temp_model = UpdateLivyComputeRequestAutoStopConfiguration()
            self.auto_stop_configuration = temp_model.from_map(m['autoStopConfiguration'])
        if m.get('cpuLimit') is not None:
            self.cpu_limit = m.get('cpuLimit')
        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')
        if m.get('enablePublic') is not None:
            self.enable_public = m.get('enablePublic')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        if m.get('livyServerConf') is not None:
            self.livy_server_conf = m.get('livyServerConf')
        if m.get('livyVersion') is not None:
            self.livy_version = m.get('livyVersion')
        if m.get('memoryLimit') is not None:
            self.memory_limit = m.get('memoryLimit')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('networkName') is not None:
            self.network_name = m.get('networkName')
        if m.get('queueName') is not None:
            self.queue_name = m.get('queueName')
        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class UpdateLivyComputeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateLivyComputeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLivyComputeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLivyComputeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProcessDefinitionWithScheduleRequestGlobalParams(TeaModel):
    def __init__(
        self,
        direct: str = None,
        prop: str = None,
        type: str = None,
        value: str = None,
    ):
        self.direct = direct
        self.prop = prop
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direct is not None:
            result['direct'] = self.direct
        if self.prop is not None:
            result['prop'] = self.prop
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direct') is not None:
            self.direct = m.get('direct')
        if m.get('prop') is not None:
            self.prop = m.get('prop')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateProcessDefinitionWithScheduleRequestSchedule(TeaModel):
    def __init__(
        self,
        crontab: str = None,
        end_time: str = None,
        start_time: str = None,
        timezone_id: str = None,
    ):
        # The CRON expression that is used for scheduling.
        self.crontab = crontab
        # The end time of the scheduling.
        self.end_time = end_time
        # The start time of the scheduling.
        self.start_time = start_time
        # The ID of the time zone.
        self.timezone_id = timezone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crontab is not None:
            result['crontab'] = self.crontab
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.timezone_id is not None:
            result['timezoneId'] = self.timezone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('crontab') is not None:
            self.crontab = m.get('crontab')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('timezoneId') is not None:
            self.timezone_id = m.get('timezoneId')
        return self


class UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams(TeaModel):
    def __init__(
        self,
        direct: str = None,
        prop: str = None,
        type: str = None,
        value: str = None,
    ):
        self.direct = direct
        self.prop = prop
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direct is not None:
            result['direct'] = self.direct
        if self.prop is not None:
            result['prop'] = self.prop
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('direct') is not None:
            self.direct = m.get('direct')
        if m.get('prop') is not None:
            self.prop = m.get('prop')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the SparkConf object.
        self.key = key
        # The value of the SparkConf object.
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


class UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams(TeaModel):
    def __init__(
        self,
        display_spark_version: str = None,
        environment_id: str = None,
        fusion: bool = None,
        local_params: List[UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams] = None,
        resource_queue_id: str = None,
        spark_conf: List[UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf] = None,
        spark_driver_cores: int = None,
        spark_driver_memory: int = None,
        spark_executor_cores: int = None,
        spark_executor_memory: int = None,
        spark_log_level: str = None,
        spark_log_path: str = None,
        spark_version: str = None,
        task_biz_id: str = None,
        type: str = None,
        workspace_biz_id: str = None,
    ):
        # The displayed version of the Spark engine.
        self.display_spark_version = display_spark_version
        # The environment ID.
        self.environment_id = environment_id
        # Specifies whether to enable Fusion engine for acceleration.
        self.fusion = fusion
        self.local_params = local_params
        # The name of the queue on which the job runs.
        # 
        # This parameter is required.
        self.resource_queue_id = resource_queue_id
        # The configurations of the Spark jobs.
        self.spark_conf = spark_conf
        # The number of driver cores of the Spark job.
        self.spark_driver_cores = spark_driver_cores
        # The size of driver memory of the Spark job.
        self.spark_driver_memory = spark_driver_memory
        # The number of executor cores of the Spark job.
        self.spark_executor_cores = spark_executor_cores
        # The size of executor memory of the Spark job.
        self.spark_executor_memory = spark_executor_memory
        # The level of the Spark log.
        self.spark_log_level = spark_log_level
        # The path where the operational logs of the Spark job are stored.
        self.spark_log_path = spark_log_path
        # The version of the Spark engine.
        self.spark_version = spark_version
        # The ID of the data development job.
        # 
        # This parameter is required.
        self.task_biz_id = task_biz_id
        # The type of the Spark job.
        self.type = type
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_biz_id = workspace_biz_id

    def validate(self):
        if self.local_params:
            for k in self.local_params:
                if k:
                    k.validate()
        if self.spark_conf:
            for k in self.spark_conf:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_spark_version is not None:
            result['displaySparkVersion'] = self.display_spark_version
        if self.environment_id is not None:
            result['environmentId'] = self.environment_id
        if self.fusion is not None:
            result['fusion'] = self.fusion
        result['localParams'] = []
        if self.local_params is not None:
            for k in self.local_params:
                result['localParams'].append(k.to_map() if k else None)
        if self.resource_queue_id is not None:
            result['resourceQueueId'] = self.resource_queue_id
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
        if self.task_biz_id is not None:
            result['taskBizId'] = self.task_biz_id
        if self.type is not None:
            result['type'] = self.type
        if self.workspace_biz_id is not None:
            result['workspaceBizId'] = self.workspace_biz_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displaySparkVersion') is not None:
            self.display_spark_version = m.get('displaySparkVersion')
        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')
        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')
        self.local_params = []
        if m.get('localParams') is not None:
            for k in m.get('localParams'):
                temp_model = UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsLocalParams()
                self.local_params.append(temp_model.from_map(k))
        if m.get('resourceQueueId') is not None:
            self.resource_queue_id = m.get('resourceQueueId')
        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k in m.get('sparkConf'):
                temp_model = UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParamsSparkConf()
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
        if m.get('taskBizId') is not None:
            self.task_biz_id = m.get('taskBizId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('workspaceBizId') is not None:
            self.workspace_biz_id = m.get('workspaceBizId')
        return self


class UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJson(TeaModel):
    def __init__(
        self,
        alert_email_address: str = None,
        code: int = None,
        description: str = None,
        fail_alert_enable: bool = None,
        fail_retry_times: int = None,
        name: str = None,
        start_alert_enable: bool = None,
        tags: Dict[str, str] = None,
        task_params: UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams = None,
        task_type: str = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The node ID.
        # 
        # This parameter is required.
        self.code = code
        # The node description.
        self.description = description
        # Specifies whether to send alerts when the node fails.
        self.fail_alert_enable = fail_alert_enable
        # The number of retries when the node fails.
        self.fail_retry_times = fail_retry_times
        # The name of the job.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to send alerts when the node is started.
        self.start_alert_enable = start_alert_enable
        # The tags of the job.
        self.tags = tags
        # The job parameters.
        # 
        # This parameter is required.
        self.task_params = task_params
        # The type of the node.
        # 
        # This parameter is required.
        self.task_type = task_type
        # The default timeout period of the node.
        self.timeout = timeout

    def validate(self):
        if self.task_params:
            self.task_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.fail_alert_enable is not None:
            result['failAlertEnable'] = self.fail_alert_enable
        if self.fail_retry_times is not None:
            result['failRetryTimes'] = self.fail_retry_times
        if self.name is not None:
            result['name'] = self.name
        if self.start_alert_enable is not None:
            result['startAlertEnable'] = self.start_alert_enable
        if self.tags is not None:
            result['tags'] = self.tags
        if self.task_params is not None:
            result['taskParams'] = self.task_params.to_map()
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('failAlertEnable') is not None:
            self.fail_alert_enable = m.get('failAlertEnable')
        if m.get('failRetryTimes') is not None:
            self.fail_retry_times = m.get('failRetryTimes')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('startAlertEnable') is not None:
            self.start_alert_enable = m.get('startAlertEnable')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('taskParams') is not None:
            temp_model = UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJsonTaskParams()
            self.task_params = temp_model.from_map(m['taskParams'])
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateProcessDefinitionWithScheduleRequestTaskRelationJson(TeaModel):
    def __init__(
        self,
        name: str = None,
        post_task_code: int = None,
        post_task_version: int = None,
        pre_task_code: int = None,
        pre_task_version: int = None,
    ):
        # The name of the node topology. You can enter a workflow name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the downstream node.
        # 
        # This parameter is required.
        self.post_task_code = post_task_code
        # The version of the downstream node.
        # 
        # This parameter is required.
        self.post_task_version = post_task_version
        # The ID of the upstream node.
        # 
        # This parameter is required.
        self.pre_task_code = pre_task_code
        # The version of the upstream node.
        # 
        # This parameter is required.
        self.pre_task_version = pre_task_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.post_task_code is not None:
            result['postTaskCode'] = self.post_task_code
        if self.post_task_version is not None:
            result['postTaskVersion'] = self.post_task_version
        if self.pre_task_code is not None:
            result['preTaskCode'] = self.pre_task_code
        if self.pre_task_version is not None:
            result['preTaskVersion'] = self.pre_task_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('postTaskCode') is not None:
            self.post_task_code = m.get('postTaskCode')
        if m.get('postTaskVersion') is not None:
            self.post_task_version = m.get('postTaskVersion')
        if m.get('preTaskCode') is not None:
            self.pre_task_code = m.get('preTaskCode')
        if m.get('preTaskVersion') is not None:
            self.pre_task_version = m.get('preTaskVersion')
        return self


class UpdateProcessDefinitionWithScheduleRequest(TeaModel):
    def __init__(
        self,
        alert_email_address: str = None,
        description: str = None,
        execution_type: str = None,
        global_params: List[UpdateProcessDefinitionWithScheduleRequestGlobalParams] = None,
        name: str = None,
        product_namespace: str = None,
        publish: bool = None,
        region_id: str = None,
        release_state: str = None,
        resource_queue: str = None,
        retry_times: int = None,
        run_as: str = None,
        schedule: UpdateProcessDefinitionWithScheduleRequestSchedule = None,
        tags: Dict[str, str] = None,
        task_definition_json: List[UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJson] = None,
        task_parallelism: int = None,
        task_relation_json: List[UpdateProcessDefinitionWithScheduleRequestTaskRelationJson] = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The description of the workflow.
        self.description = description
        # The execution policy.
        # 
        # This parameter is required.
        self.execution_type = execution_type
        self.global_params = global_params
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The code of the service.
        # 
        # This parameter is required.
        self.product_namespace = product_namespace
        # Specifies whether to publish the workflow.
        self.publish = publish
        # The region ID.
        self.region_id = region_id
        # The status of the workflow.
        self.release_state = release_state
        # The resource queue.
        self.resource_queue = resource_queue
        # The number of retries.
        self.retry_times = retry_times
        # The execution user.
        self.run_as = run_as
        # The scheduling settings.
        self.schedule = schedule
        # The tags.
        self.tags = tags
        # The descriptions of all nodes in the workflow.
        # 
        # This parameter is required.
        self.task_definition_json = task_definition_json
        # The node parallelism.
        self.task_parallelism = task_parallelism
        # The dependencies of all nodes in the workflow. preTaskCode specifies the ID of an upstream node, and postTaskCode specifies the ID of a downstream node. The ID of each node is unique. If a node does not have an upstream node, set preTaskCode to 0.
        # 
        # This parameter is required.
        self.task_relation_json = task_relation_json
        # The default timeout period of the workflow.
        self.timeout = timeout

    def validate(self):
        if self.global_params:
            for k in self.global_params:
                if k:
                    k.validate()
        if self.schedule:
            self.schedule.validate()
        if self.task_definition_json:
            for k in self.task_definition_json:
                if k:
                    k.validate()
        if self.task_relation_json:
            for k in self.task_relation_json:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address
        if self.description is not None:
            result['description'] = self.description
        if self.execution_type is not None:
            result['executionType'] = self.execution_type
        result['globalParams'] = []
        if self.global_params is not None:
            for k in self.global_params:
                result['globalParams'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace
        if self.publish is not None:
            result['publish'] = self.publish
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_state is not None:
            result['releaseState'] = self.release_state
        if self.resource_queue is not None:
            result['resourceQueue'] = self.resource_queue
        if self.retry_times is not None:
            result['retryTimes'] = self.retry_times
        if self.run_as is not None:
            result['runAs'] = self.run_as
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        if self.tags is not None:
            result['tags'] = self.tags
        result['taskDefinitionJson'] = []
        if self.task_definition_json is not None:
            for k in self.task_definition_json:
                result['taskDefinitionJson'].append(k.to_map() if k else None)
        if self.task_parallelism is not None:
            result['taskParallelism'] = self.task_parallelism
        result['taskRelationJson'] = []
        if self.task_relation_json is not None:
            for k in self.task_relation_json:
                result['taskRelationJson'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')
        self.global_params = []
        if m.get('globalParams') is not None:
            for k in m.get('globalParams'):
                temp_model = UpdateProcessDefinitionWithScheduleRequestGlobalParams()
                self.global_params.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')
        if m.get('publish') is not None:
            self.publish = m.get('publish')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseState') is not None:
            self.release_state = m.get('releaseState')
        if m.get('resourceQueue') is not None:
            self.resource_queue = m.get('resourceQueue')
        if m.get('retryTimes') is not None:
            self.retry_times = m.get('retryTimes')
        if m.get('runAs') is not None:
            self.run_as = m.get('runAs')
        if m.get('schedule') is not None:
            temp_model = UpdateProcessDefinitionWithScheduleRequestSchedule()
            self.schedule = temp_model.from_map(m['schedule'])
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        self.task_definition_json = []
        if m.get('taskDefinitionJson') is not None:
            for k in m.get('taskDefinitionJson'):
                temp_model = UpdateProcessDefinitionWithScheduleRequestTaskDefinitionJson()
                self.task_definition_json.append(temp_model.from_map(k))
        if m.get('taskParallelism') is not None:
            self.task_parallelism = m.get('taskParallelism')
        self.task_relation_json = []
        if m.get('taskRelationJson') is not None:
            for k in m.get('taskRelationJson'):
                temp_model = UpdateProcessDefinitionWithScheduleRequestTaskRelationJson()
                self.task_relation_json.append(temp_model.from_map(k))
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateProcessDefinitionWithScheduleShrinkRequest(TeaModel):
    def __init__(
        self,
        alert_email_address: str = None,
        description: str = None,
        execution_type: str = None,
        global_params_shrink: str = None,
        name: str = None,
        product_namespace: str = None,
        publish: bool = None,
        region_id: str = None,
        release_state: str = None,
        resource_queue: str = None,
        retry_times: int = None,
        run_as: str = None,
        schedule_shrink: str = None,
        tags_shrink: str = None,
        task_definition_json_shrink: str = None,
        task_parallelism: int = None,
        task_relation_json_shrink: str = None,
        timeout: int = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The description of the workflow.
        self.description = description
        # The execution policy.
        # 
        # This parameter is required.
        self.execution_type = execution_type
        self.global_params_shrink = global_params_shrink
        # The name of the workflow.
        # 
        # This parameter is required.
        self.name = name
        # The code of the service.
        # 
        # This parameter is required.
        self.product_namespace = product_namespace
        # Specifies whether to publish the workflow.
        self.publish = publish
        # The region ID.
        self.region_id = region_id
        # The status of the workflow.
        self.release_state = release_state
        # The resource queue.
        self.resource_queue = resource_queue
        # The number of retries.
        self.retry_times = retry_times
        # The execution user.
        self.run_as = run_as
        # The scheduling settings.
        self.schedule_shrink = schedule_shrink
        # The tags.
        self.tags_shrink = tags_shrink
        # The descriptions of all nodes in the workflow.
        # 
        # This parameter is required.
        self.task_definition_json_shrink = task_definition_json_shrink
        # The node parallelism.
        self.task_parallelism = task_parallelism
        # The dependencies of all nodes in the workflow. preTaskCode specifies the ID of an upstream node, and postTaskCode specifies the ID of a downstream node. The ID of each node is unique. If a node does not have an upstream node, set preTaskCode to 0.
        # 
        # This parameter is required.
        self.task_relation_json_shrink = task_relation_json_shrink
        # The default timeout period of the workflow.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address
        if self.description is not None:
            result['description'] = self.description
        if self.execution_type is not None:
            result['executionType'] = self.execution_type
        if self.global_params_shrink is not None:
            result['globalParams'] = self.global_params_shrink
        if self.name is not None:
            result['name'] = self.name
        if self.product_namespace is not None:
            result['productNamespace'] = self.product_namespace
        if self.publish is not None:
            result['publish'] = self.publish
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.release_state is not None:
            result['releaseState'] = self.release_state
        if self.resource_queue is not None:
            result['resourceQueue'] = self.resource_queue
        if self.retry_times is not None:
            result['retryTimes'] = self.retry_times
        if self.run_as is not None:
            result['runAs'] = self.run_as
        if self.schedule_shrink is not None:
            result['schedule'] = self.schedule_shrink
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        if self.task_definition_json_shrink is not None:
            result['taskDefinitionJson'] = self.task_definition_json_shrink
        if self.task_parallelism is not None:
            result['taskParallelism'] = self.task_parallelism
        if self.task_relation_json_shrink is not None:
            result['taskRelationJson'] = self.task_relation_json_shrink
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')
        if m.get('globalParams') is not None:
            self.global_params_shrink = m.get('globalParams')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('productNamespace') is not None:
            self.product_namespace = m.get('productNamespace')
        if m.get('publish') is not None:
            self.publish = m.get('publish')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('releaseState') is not None:
            self.release_state = m.get('releaseState')
        if m.get('resourceQueue') is not None:
            self.resource_queue = m.get('resourceQueue')
        if m.get('retryTimes') is not None:
            self.retry_times = m.get('retryTimes')
        if m.get('runAs') is not None:
            self.run_as = m.get('runAs')
        if m.get('schedule') is not None:
            self.schedule_shrink = m.get('schedule')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        if m.get('taskDefinitionJson') is not None:
            self.task_definition_json_shrink = m.get('taskDefinitionJson')
        if m.get('taskParallelism') is not None:
            self.task_parallelism = m.get('taskParallelism')
        if m.get('taskRelationJson') is not None:
            self.task_relation_json_shrink = m.get('taskRelationJson')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class UpdateProcessDefinitionWithScheduleResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_email_address: str = None,
        biz_id: str = None,
        code: str = None,
        create_time: str = None,
        crontab: str = None,
        description: str = None,
        end_time: str = None,
        execution_type: str = None,
        id: str = None,
        name: str = None,
        project_name: str = None,
        release_state: str = None,
        start_time: str = None,
        timezone_id: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
        version: int = None,
        version_hash_code: str = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The workspace ID.
        self.biz_id = biz_id
        # The workflow ID.
        self.code = code
        # The time when the workflow was created.
        self.create_time = create_time
        # The CRON expression that is used for scheduling.
        self.crontab = crontab
        # The node description.
        self.description = description
        # The end of the end time range.
        self.end_time = end_time
        # The execution policy.
        self.execution_type = execution_type
        # The serial number of the workflow.
        self.id = id
        # The name of the workflow.
        self.name = name
        # The name of the project to which the workflow belongs.
        self.project_name = project_name
        # The status of the workflow.
        self.release_state = release_state
        # The start time of the scheduling.
        self.start_time = start_time
        # The ID of the time zone.
        self.timezone_id = timezone_id
        # The time when the workflow was updated.
        self.update_time = update_time
        # The ID of the user that is used to initiate a scheduling.
        self.user_id = user_id
        # The name of the user that is used to initiate a scheduling.
        self.user_name = user_name
        # The version number.
        self.version = version
        # The hash code of the version.
        self.version_hash_code = version_hash_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address
        if self.biz_id is not None:
            result['bizId'] = self.biz_id
        if self.code is not None:
            result['code'] = self.code
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.crontab is not None:
            result['crontab'] = self.crontab
        if self.description is not None:
            result['description'] = self.description
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.execution_type is not None:
            result['executionType'] = self.execution_type
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.project_name is not None:
            result['projectName'] = self.project_name
        if self.release_state is not None:
            result['releaseState'] = self.release_state
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.timezone_id is not None:
            result['timezoneId'] = self.timezone_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.version is not None:
            result['version'] = self.version
        if self.version_hash_code is not None:
            result['versionHashCode'] = self.version_hash_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('crontab') is not None:
            self.crontab = m.get('crontab')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('releaseState') is not None:
            self.release_state = m.get('releaseState')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('timezoneId') is not None:
            self.timezone_id = m.get('timezoneId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('versionHashCode') is not None:
            self.version_hash_code = m.get('versionHashCode')
        return self


class UpdateProcessDefinitionWithScheduleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: UpdateProcessDefinitionWithScheduleResponseBodyData = None,
        failed: str = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The code that is returned by the backend server.
        self.code = code
        # The data returned.
        self.data = data
        # Indicates whether the request failed.
        self.failed = failed
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The description of the returned code.
        self.msg = msg
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
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.failed is not None:
            result['failed'] = self.failed
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = UpdateProcessDefinitionWithScheduleResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('failed') is not None:
            self.failed = m.get('failed')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateProcessDefinitionWithScheduleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProcessDefinitionWithScheduleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProcessDefinitionWithScheduleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


