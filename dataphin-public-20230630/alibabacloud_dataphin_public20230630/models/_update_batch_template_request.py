# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateBatchTemplateRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        project_id: int = None,
        update_command: main_models.UpdateBatchTemplateRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
        self.op_user_id = op_user_id
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The template update command.
        # 
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateBatchTemplateRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateBatchTemplateRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        content: str = None,
        data_source_config: main_models.UpdateBatchTemplateRequestUpdateCommandDataSourceConfig = None,
        description: str = None,
        dev_resource_group_id: str = None,
        directory: str = None,
        name: str = None,
        params: List[main_models.UpdateBatchTemplateRequestUpdateCommandParams] = None,
        python_module_ids: List[int] = None,
        resource_group_id: str = None,
        share_runtime_resource: bool = None,
        template_id: int = None,
    ):
        # The template content.
        # 
        # This parameter is required.
        self.content = content
        # The datasource config for database SQL templates. This parameter takes effect only for database SQL templates.
        self.data_source_config = data_source_config
        # The description of the template.
        self.description = description
        # The ID of the resource group in the development environment. By default, the default resource group of the project is used.
        self.dev_resource_group_id = dev_resource_group_id
        # The folder of the template.
        # 
        # This parameter is required.
        self.directory = directory
        # The name of the template.
        # 
        # This parameter is required.
        self.name = name
        # The list of template parameters.
        self.params = params
        # The list of IDs of dependent third-party Python packages.
        self.python_module_ids = python_module_ids
        # The ID of the resource group in the production environment. By default, the default resource group of the project is used.
        self.resource_group_id = resource_group_id
        # Specifies whether to share runtime resources.
        self.share_runtime_resource = share_runtime_resource
        # The ID of the template.
        # 
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        if self.data_source_config:
            self.data_source_config.validate()
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.data_source_config is not None:
            result['DataSourceConfig'] = self.data_source_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.dev_resource_group_id is not None:
            result['DevResourceGroupId'] = self.dev_resource_group_id

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.name is not None:
            result['Name'] = self.name

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.python_module_ids is not None:
            result['PythonModuleIds'] = self.python_module_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share_runtime_resource is not None:
            result['ShareRuntimeResource'] = self.share_runtime_resource

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataSourceConfig') is not None:
            temp_model = main_models.UpdateBatchTemplateRequestUpdateCommandDataSourceConfig()
            self.data_source_config = temp_model.from_map(m.get('DataSourceConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevResourceGroupId') is not None:
            self.dev_resource_group_id = m.get('DevResourceGroupId')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.UpdateBatchTemplateRequestUpdateCommandParams()
                self.params.append(temp_model.from_map(k1))

        if m.get('PythonModuleIds') is not None:
            self.python_module_ids = m.get('PythonModuleIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ShareRuntimeResource') is not None:
            self.share_runtime_resource = m.get('ShareRuntimeResource')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class UpdateBatchTemplateRequestUpdateCommandParams(DaraModel):
    def __init__(
        self,
        description: str = None,
        encrypt_enabled: bool = None,
        key: str = None,
        value: str = None,
    ):
        # The parameter description.
        self.description = description
        # Specifies whether encryption is enabled for the parameter.
        self.encrypt_enabled = encrypt_enabled
        # The key of the parameter.
        # 
        # This parameter is required.
        self.key = key
        # The default value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.encrypt_enabled is not None:
            result['EncryptEnabled'] = self.encrypt_enabled

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EncryptEnabled') is not None:
            self.encrypt_enabled = m.get('EncryptEnabled')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateBatchTemplateRequestUpdateCommandDataSourceConfig(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        ds_id: str = None,
        schema: str = None,
        type: str = None,
    ):
        # The catalog of the data source for the database SQL template.
        self.catalog = catalog
        # The ID of the data source for the database SQL template.
        # 
        # This parameter is required.
        self.ds_id = ds_id
        # The schema of the data source for the database SQL template.
        self.schema = schema
        # The type of the data source for the database SQL template. Valid values: MYSQL, ORACLE, ADB_FOR_PG, OUSHUDB, PRESTO, POSTGRE_SQL, STARROCKS, CLICKHOUSE, ANALYTICDB, ADB_FOR_MYSQL_V3, GAUSSDB, SELECTDB, DORIS, SQL_SERVER, HOLOGRES, OPENGAUSS, DAMENG, OCEANBASE, TRINO, POLARDB_X2, LINDORM, EMR_SPARK_SERVERLESS, TDSQL_FOR_PG, TDSQL_FOR_MYSQL, GBASE_8A, and TDENGINE.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

