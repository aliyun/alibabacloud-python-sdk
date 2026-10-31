# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListBatchTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListBatchTemplatesResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The paging query result.
        self.page_result = page_result
        # Id of the request
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
            temp_model = main_models.ListBatchTemplatesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListBatchTemplatesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        template_list: List[main_models.ListBatchTemplatesResponseBodyPageResultTemplateList] = None,
        total_count: int = None,
    ):
        # The paginated template record list.
        self.template_list = template_list
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.template_list:
            for v1 in self.template_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TemplateList'] = []
        if self.template_list is not None:
            for k1 in self.template_list:
                result['TemplateList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template_list = []
        if m.get('TemplateList') is not None:
            for k1 in m.get('TemplateList'):
                temp_model = main_models.ListBatchTemplatesResponseBodyPageResultTemplateList()
                self.template_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBatchTemplatesResponseBodyPageResultTemplateList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content: str = None,
        current_version: int = None,
        data_source_config: main_models.ListBatchTemplatesResponseBodyPageResultTemplateListDataSourceConfig = None,
        description: str = None,
        dev_resource_group_id: str = None,
        dev_resource_group_name: str = None,
        engine: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        modifier: str = None,
        modifier_id: str = None,
        name: str = None,
        operator_type: int = None,
        owner: str = None,
        owner_id: str = None,
        params: List[main_models.ListBatchTemplatesResponseBodyPageResultTemplateListParams] = None,
        project_id: int = None,
        python_module_list: List[main_models.ListBatchTemplatesResponseBodyPageResultTemplateListPythonModuleList] = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        share_runtime_resource: bool = None,
        status: str = None,
    ):
        # The template submission comment.
        self.comment = comment
        # The template content.
        self.content = content
        # The latest version.
        self.current_version = current_version
        # The datasource config of the database SQL template.
        self.data_source_config = data_source_config
        # The template description.
        self.description = description
        # The ID of the resource group in the development environment.
        self.dev_resource_group_id = dev_resource_group_id
        # The name of the resource group in the development environment.
        self.dev_resource_group_name = dev_resource_group_name
        # The version of the compute engine. Valid values: Python 2.7 and Python 3.7.
        self.engine = engine
        # The time when the template was created. Format: yyyy-MM-dd HH:mm:ss.
        self.gmt_create = gmt_create
        # The time when the template was updated. Format: yyyy-MM-dd HH:mm:ss.
        self.gmt_modified = gmt_modified
        # The ID of the template. This ID is the same as the menu tree node ID.
        self.id = id
        # The user who last updated the template.
        self.modifier = modifier
        # The ID of the user who last updated the template.
        self.modifier_id = modifier_id
        # The name of the template.
        self.name = name
        # The type of the node. Valid values: 10 (Shell) and 21 (Python).
        self.operator_type = operator_type
        # The owner of the template.
        self.owner = owner
        # The ID of the template owner.
        self.owner_id = owner_id
        # The list of template parameters.
        self.params = params
        # The ID of the project.
        self.project_id = project_id
        # The list of dependent Python third-party packages.
        self.python_module_list = python_module_list
        # The ID of the resource group in the production environment.
        self.resource_group_id = resource_group_id
        # The name of the resource group in the production environment.
        self.resource_group_name = resource_group_name
        # Indicates whether runtime resources are shared.
        self.share_runtime_resource = share_runtime_resource
        # The status of the template. Valid values: 0 (draft), 2 (submitted), and 100 (in development).
        self.status = status

    def validate(self):
        if self.data_source_config:
            self.data_source_config.validate()
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()
        if self.python_module_list:
            for v1 in self.python_module_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.content is not None:
            result['Content'] = self.content

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.data_source_config is not None:
            result['DataSourceConfig'] = self.data_source_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.dev_resource_group_id is not None:
            result['DevResourceGroupId'] = self.dev_resource_group_id

        if self.dev_resource_group_name is not None:
            result['DevResourceGroupName'] = self.dev_resource_group_name

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.name is not None:
            result['Name'] = self.name

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['PythonModuleList'] = []
        if self.python_module_list is not None:
            for k1 in self.python_module_list:
                result['PythonModuleList'].append(k1.to_map() if k1 else None)

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        if self.share_runtime_resource is not None:
            result['ShareRuntimeResource'] = self.share_runtime_resource

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('DataSourceConfig') is not None:
            temp_model = main_models.ListBatchTemplatesResponseBodyPageResultTemplateListDataSourceConfig()
            self.data_source_config = temp_model.from_map(m.get('DataSourceConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevResourceGroupId') is not None:
            self.dev_resource_group_id = m.get('DevResourceGroupId')

        if m.get('DevResourceGroupName') is not None:
            self.dev_resource_group_name = m.get('DevResourceGroupName')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.ListBatchTemplatesResponseBodyPageResultTemplateListParams()
                self.params.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.python_module_list = []
        if m.get('PythonModuleList') is not None:
            for k1 in m.get('PythonModuleList'):
                temp_model = main_models.ListBatchTemplatesResponseBodyPageResultTemplateListPythonModuleList()
                self.python_module_list.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        if m.get('ShareRuntimeResource') is not None:
            self.share_runtime_resource = m.get('ShareRuntimeResource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListBatchTemplatesResponseBodyPageResultTemplateListPythonModuleList(DaraModel):
    def __init__(
        self,
        id: int = None,
        install_time: str = None,
        name: str = None,
        python_version: str = None,
        status: str = None,
        version: str = None,
    ):
        # The ID of the Python third-party package.
        self.id = id
        # The installation time.
        self.install_time = install_time
        # The name of the Python third-party package.
        self.name = name
        # The Python version. Valid values: PYTHON_2_7, PYTHON_3_7, and PYTHON_3_11.
        self.python_version = python_version
        # The status of the third-party package. Valid values: INSTALL_SUCCESS (installed successfully), INSTALL_FAILED (installation failed), INSTALLING (installing), UPGRADE_SUCCESS (upgraded successfully), UPGRADE_FAILED (upgrade failed), and UPGRADING (upgrading).
        self.status = status
        # The version of the third-party package.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.install_time is not None:
            result['InstallTime'] = self.install_time

        if self.name is not None:
            result['Name'] = self.name

        if self.python_version is not None:
            result['PythonVersion'] = self.python_version

        if self.status is not None:
            result['Status'] = self.status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstallTime') is not None:
            self.install_time = m.get('InstallTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PythonVersion') is not None:
            self.python_version = m.get('PythonVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListBatchTemplatesResponseBodyPageResultTemplateListParams(DaraModel):
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

class ListBatchTemplatesResponseBodyPageResultTemplateListDataSourceConfig(DaraModel):
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
        self.ds_id = ds_id
        # The schema of the data source for the database SQL template.
        self.schema = schema
        # The data source type of the database SQL template. Valid values: MYSQL, ORACLE, ADB_FOR_PG, OUSHUDB, PRESTO, POSTGRE_SQL, STARROCKS, CLICKHOUSE, ANALYTICDB, ADB_FOR_MYSQL_V3, GAUSSDB, SELECTDB, DORIS, SQL_SERVER, HOLOGRES, OPENGAUSS, DAMENG, OCEANBASE, TRINO, POLARDB_X2, LINDORM, EMR_SPARK_SERVERLESS, TDSQL_FOR_PG, TDSQL_FOR_MYSQL, GBASE_8A, and TDENGINE.
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

