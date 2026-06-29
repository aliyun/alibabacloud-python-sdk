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
    ):
        # The create command.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateBatchTaskRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateBatchTaskRequestCreateCommand(DaraModel):
    def __init__(
        self,
        data_source_catalog: str = None,
        data_source_id: str = None,
        data_source_schema: str = None,
        description: str = None,
        directory: str = None,
        engine: str = None,
        name: str = None,
        project_id: int = None,
        python_module_list: List[str] = None,
        schedule_type: int = None,
        task_type: int = None,
    ):
        # The catalog for a database SQL node. This parameter takes effect only for data source types that require a catalog, such as Presto.
        self.data_source_catalog = data_source_catalog
        # The data source ID for a database SQL node.
        self.data_source_id = data_source_id
        # The schema for a database SQL node. This parameter takes effect only for data source types that require a schema, such as Oracle.
        self.data_source_schema = data_source_schema
        # The description.
        # 
        # This parameter is required.
        self.description = description
        # The folder path in the menu tree to which the node belongs.
        # 
        # This parameter is required.
        self.directory = directory
        # The execution engine for the node, such as a Python node. Valid values:
        # - 1: PYTHON2_7
        # - 2: PYTHON3_7
        # - 3: PYTHON3_11.
        self.engine = engine
        # The name of the batch task.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the project to which the node belongs.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The list of third-party Python packages that the node depends on.
        self.python_module_list = python_module_list
        # The scheduling type. Valid values:
        # - 1: periodic node.
        # - 3: manual node.
        # 
        # This parameter is required.
        self.schedule_type = schedule_type
        # The node type. Valid values:
        # - Hive_SQL: 1
        # - Hive_SQL_23X: 101
        # - HIVE_SQL_FUSION_INSIGHT_80X: 111
        # - COMMON_HIVE_SQL: 131
        # - HADOOP_MR: 2
        # - MaxCompute_SQL: 5
        # - MaxCompute_MR: 6
        # - SPARK_SQL_ON_MAX_COMPUTE: 7
        # - SPARK_JAR_ON_MAX_COMPUTE: 8
        # - SPARK_SQL_ON_HIVE: 17
        # - Spark_JAR_ON_HIVE: 18
        # - Shell: 10
        # - PAI_DESIGNER: 71
        # - DataX: 15
        # - Merge: 16
        # - Python: 21
        # - Python37x: 22
        # - Perl: 23
        # - Python311x: 24
        # - OneService_SQL: 25
        # - ONE_SERVICE_SQL_ADB_FOR_PG: 26
        # - OneService_SQL_Hive11x: 27
        # - OneService_SQL_Hive23x: 29
        # - ONE_SERVICE_SQL_TDH_INCEPTOR: 75
        # - ONE_SERVICE_SQL_HIVE_CDP: 91
        # - ONE_SERVICE_SQL_HIVE_ASIA_INFO_DP_53X: 92
        # - Dlink: 30
        # - ONE_SERVICE_SQL_ADB_FOR_MYSQL: 33
        # - Logical: 31
        # - Flink_Streaming: 41
        # - Flink_Batch: 42
        # - ADB_FOR_PG: 51
        # - DryRun: 100
        # - CHECK: 902
        # - VIRTUAL: 999
        # - INCEPTOR_SQL: 10000
        # - HOLOGRES_SQL: 28
        # - ARGODB_SQL: 76
        # - IMPALA_SQL: 78
        # - STARROCKS_SQL: 79
        # - SPARK_SQL: 80
        # - GAUSS_SQL: 81
        # - DATABASE_SQL: 998
        # - EXTERNAL_TRIGGER: 997.
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_catalog is not None:
            result['DataSourceCatalog'] = self.data_source_catalog

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_schema is not None:
            result['DataSourceSchema'] = self.data_source_schema

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.python_module_list is not None:
            result['PythonModuleList'] = self.python_module_list

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceCatalog') is not None:
            self.data_source_catalog = m.get('DataSourceCatalog')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceSchema') is not None:
            self.data_source_schema = m.get('DataSourceSchema')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('PythonModuleList') is not None:
            self.python_module_list = m.get('PythonModuleList')

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

