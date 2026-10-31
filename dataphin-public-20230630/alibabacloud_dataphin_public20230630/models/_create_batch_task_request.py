# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateBatchTaskRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateBatchTaskRequestCreateCommand = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The create command.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator.
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
            temp_model = main_models.CreateBatchTaskRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

class CreateBatchTaskRequestCreateCommand(DaraModel):
    def __init__(
        self,
        code_template_id: str = None,
        code_template_version: int = None,
        data_source_catalog: str = None,
        data_source_id: str = None,
        data_source_schema: str = None,
        databricks_python_connect_info: main_models.CreateBatchTaskRequestCreateCommandDatabricksPythonConnectInfo = None,
        description: str = None,
        develop_owner_id_list: List[str] = None,
        directory: str = None,
        engine: str = None,
        name: str = None,
        ops_owner_id_list: List[str] = None,
        pai_config: main_models.CreateBatchTaskRequestCreateCommandPaiConfig = None,
        project_id: int = None,
        python_module_list: List[str] = None,
        schedule_type: int = None,
        spark_dynamic_resource_switch: bool = None,
        spark_resource_effect_scope: str = None,
        spark_sql_resource_config_map: str = None,
        spark_version: str = None,
        task_type: int = None,
    ):
        # The ID of the offline code template.
        self.code_template_id = code_template_id
        # The version of the offline code template.
        self.code_template_version = code_template_version
        # The catalog for database SQL tasks. This parameter takes effect only for data source types that require a catalog, such as Presto.
        self.data_source_catalog = data_source_catalog
        # The ID of the data source for database SQL tasks.
        self.data_source_id = data_source_id
        # The schema for database SQL tasks. This parameter takes effect only for data source types that require a schema, such as Oracle.
        self.data_source_schema = data_source_schema
        # The Python connection configuration.
        self.databricks_python_connect_info = databricks_python_connect_info
        # The description.
        # 
        # This parameter is required.
        self.description = description
        # The IDs of the development owners.
        self.develop_owner_id_list = develop_owner_id_list
        # The directory in the menu tree to which the task belongs.
        # 
        # This parameter is required.
        self.directory = directory
        # The task execution engine, such as Python tasks. Valid values:
        # - PYTHON2_7
        # - PYTHON3_7
        # - PYTHON3_11
        self.engine = engine
        # The name of the offline task.
        # 
        # This parameter is required.
        self.name = name
        # The IDs of the O&M owners.
        self.ops_owner_id_list = ops_owner_id_list
        # The PAI configuration.
        self.pai_config = pai_config
        # The ID of the project to which the task belongs.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The third-party Python packages that the task depends on.
        self.python_module_list = python_module_list
        # The scheduling type. Valid values: 1 (periodic task) and 3 (manual task).
        # 
        # This parameter is required.
        self.schedule_type = schedule_type
        # Specifies whether to enable dynamic resource configuration for Spark. This parameter takes effect only for Spark SQL tasks. If you do not specify this parameter, dynamic resource configuration is enabled by default for Spark SQL tasks.
        self.spark_dynamic_resource_switch = spark_dynamic_resource_switch
        # The effective scope of Spark resources. Valid values: ONLY_PROD and PROD_AND_DEV. If you do not specify this parameter, the default value ONLY_PROD is used for Spark SQL tasks.
        self.spark_resource_effect_scope = spark_resource_effect_scope
        # The resource configuration for the Spark task. The value is a JSON string, such as {"spark.executor.memory":"2g"}.
        self.spark_sql_resource_config_map = spark_sql_resource_config_map
        # The MaxCompute Spark version. Valid values: MAX_COMPUTE_23X, MAX_COMPUTE_245X, and MAX_COMPUTE_311X. For Apsara Stack, only MAX_COMPUTE_APSARA is supported. Display names such as Spark 2.3.0, Spark 2.4.5, and Spark 3.1.1 are also accepted.
        self.spark_version = spark_version
        # The task type. Valid values:
        # - 1: Hive_SQL.
        # - 101: Hive_SQL_23X.
        # - 111: HIVE_SQL_FUSION_INSIGHT_80X.
        # - 131: COMMON_HIVE_SQL.
        # - 2: HADOOP_MR.
        # - 5: MaxCompute_SQL.
        # - 6: MaxCompute_MR.
        # - 7: SPARK_SQL_ON_MAX_COMPUTE.
        # - 8: SPARK_JAR_ON_MAX_COMPUTE.
        # - 17: SPARK_SQL_ON_HIVE.
        # - 18: Spark_JAR_ON_HIVE.
        # - 10: Shell.
        # - 71: PAI_DESIGNER.
        # - 15: DataX.
        # - 16: Merge.
        # - 21: Python.
        # - 22: Python37x.
        # - 23: Perl.
        # - 24: Python311x.
        # - 25: OneService_SQL.
        # - 26: ONE_SERVICE_SQL_ADB_FOR_PG.
        # - 27: OneService_SQL_Hive11x.
        # - 29: OneService_SQL_Hive23x.
        # - 75: ONE_SERVICE_SQL_TDH_INCEPTOR.
        # - 91: ONE_SERVICE_SQL_HIVE_CDP.
        # - 92: ONE_SERVICE_SQL_HIVE_ASIA_INFO_DP_53X.
        # - 30: Dlink.
        # - 33: ONE_SERVICE_SQL_ADB_FOR_MYSQL.
        # - 31: Logical.
        # - 41: Flink_Streaming.
        # - 42: Flink_Batch.
        # - 51: ADB_FOR_PG.
        # - 100: DryRun.
        # - 902: CHECK.
        # - 999: VIRTUAL.
        # - 10000: INCEPTOR_SQL.
        # - 28: HOLOGRES_SQL.
        # - 76: ARGODB_SQL.
        # - 78: IMPALA_SQL.
        # - 79: STARROCKS_SQL.
        # - 80: SPARK_SQL.
        # - 81: GAUSS_SQL.
        # - 998: DATABASE_SQL.
        # - 997: EXTERNAL_TRIGGER.
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        if self.databricks_python_connect_info:
            self.databricks_python_connect_info.validate()
        if self.pai_config:
            self.pai_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_template_id is not None:
            result['CodeTemplateId'] = self.code_template_id

        if self.code_template_version is not None:
            result['CodeTemplateVersion'] = self.code_template_version

        if self.data_source_catalog is not None:
            result['DataSourceCatalog'] = self.data_source_catalog

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_schema is not None:
            result['DataSourceSchema'] = self.data_source_schema

        if self.databricks_python_connect_info is not None:
            result['DatabricksPythonConnectInfo'] = self.databricks_python_connect_info.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.develop_owner_id_list is not None:
            result['DevelopOwnerIdList'] = self.develop_owner_id_list

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.name is not None:
            result['Name'] = self.name

        if self.ops_owner_id_list is not None:
            result['OpsOwnerIdList'] = self.ops_owner_id_list

        if self.pai_config is not None:
            result['PaiConfig'] = self.pai_config.to_map()

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.python_module_list is not None:
            result['PythonModuleList'] = self.python_module_list

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.spark_dynamic_resource_switch is not None:
            result['SparkDynamicResourceSwitch'] = self.spark_dynamic_resource_switch

        if self.spark_resource_effect_scope is not None:
            result['SparkResourceEffectScope'] = self.spark_resource_effect_scope

        if self.spark_sql_resource_config_map is not None:
            result['SparkSqlResourceConfigMap'] = self.spark_sql_resource_config_map

        if self.spark_version is not None:
            result['SparkVersion'] = self.spark_version

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeTemplateId') is not None:
            self.code_template_id = m.get('CodeTemplateId')

        if m.get('CodeTemplateVersion') is not None:
            self.code_template_version = m.get('CodeTemplateVersion')

        if m.get('DataSourceCatalog') is not None:
            self.data_source_catalog = m.get('DataSourceCatalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')

        if m.get('DatabricksPythonConnectInfo') is not None:
            temp_model = main_models.CreateBatchTaskRequestCreateCommandDatabricksPythonConnectInfo()
            self.databricks_python_connect_info = temp_model.from_map(m.get('DatabricksPythonConnectInfo'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DevelopOwnerIdList') is not None:
            self.develop_owner_id_list = m.get('DevelopOwnerIdList')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OpsOwnerIdList') is not None:
            self.ops_owner_id_list = m.get('OpsOwnerIdList')

        if m.get('PaiConfig') is not None:
            temp_model = main_models.CreateBatchTaskRequestCreateCommandPaiConfig()
            self.pai_config = temp_model.from_map(m.get('PaiConfig'))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('PythonModuleList') is not None:
            self.python_module_list = m.get('PythonModuleList')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('SparkDynamicResourceSwitch') is not None:
            self.spark_dynamic_resource_switch = m.get('SparkDynamicResourceSwitch')

        if m.get('SparkResourceEffectScope') is not None:
            self.spark_resource_effect_scope = m.get('SparkResourceEffectScope')

        if m.get('SparkSqlResourceConfigMap') is not None:
            self.spark_sql_resource_config_map = m.get('SparkSqlResourceConfigMap')

        if m.get('SparkVersion') is not None:
            self.spark_version = m.get('SparkVersion')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class CreateBatchTaskRequestCreateCommandPaiConfig(DaraModel):
    def __init__(
        self,
        experiment_id: str = None,
        region: str = None,
        work_space_id: str = None,
    ):
        # The ID of the PAI experiment.
        self.experiment_id = experiment_id
        # The PAI region.
        self.region = region
        # The ID of the PAI workspace.
        self.work_space_id = work_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        if self.region is not None:
            result['Region'] = self.region

        if self.work_space_id is not None:
            result['WorkSpaceId'] = self.work_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('WorkSpaceId') is not None:
            self.work_space_id = m.get('WorkSpaceId')

        return self

class CreateBatchTaskRequestCreateCommandDatabricksPythonConnectInfo(DaraModel):
    def __init__(
        self,
        dev_http_path: str = None,
        enable_databricks_python_connect: bool = None,
        prod_http_path: str = None,
    ):
        # The HTTP path for the development environment.
        self.dev_http_path = dev_http_path
        # Specifies whether to enable Databricks Python connect.
        self.enable_databricks_python_connect = enable_databricks_python_connect
        # The HTTP path for the production environment.
        self.prod_http_path = prod_http_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dev_http_path is not None:
            result['DevHttpPath'] = self.dev_http_path

        if self.enable_databricks_python_connect is not None:
            result['EnableDatabricksPythonConnect'] = self.enable_databricks_python_connect

        if self.prod_http_path is not None:
            result['ProdHttpPath'] = self.prod_http_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DevHttpPath') is not None:
            self.dev_http_path = m.get('DevHttpPath')

        if m.get('EnableDatabricksPythonConnect') is not None:
            self.enable_databricks_python_connect = m.get('EnableDatabricksPythonConnect')

        if m.get('ProdHttpPath') is not None:
            self.prod_http_path = m.get('ProdHttpPath')

        return self

